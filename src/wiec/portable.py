"""Versioned, SDK-free contracts for one bounded agent invocation.

Checkpoints are local application data, not authenticated approvals or a sandbox.
"""
from __future__ import annotations

import asyncio
from dataclasses import asdict, dataclass, replace
import json
import math
from pathlib import Path
import os
import re
import tempfile
from typing import Protocol

from .council import Council
from .model import Challenge, Claim, Evidence

SCHEMA_VERSION = 1
MAX_WIRE_CHARS = 1_000_000
LOCAL_CAPABILITY = "local_reasoning"


class ContractError(ValueError):
    """An invalid or unsupported portable contract."""


def _text(value: object, name: str, limit: int = 64_000) -> None:
    if type(value) is not str or not value.strip() or len(value) > limit:
        raise ContractError(f"Invalid {name}")


def _id(value: object, name: str) -> None:
    if type(value) is not str or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,127}", value):
        raise ContractError(f"Invalid {name}")


def _tuple(value: object, name: str) -> None:
    if type(value) is not tuple or len(value) > 1000:
        raise ContractError(f"Invalid {name}")


@dataclass(frozen=True)
class AgentManifest:
    agent_id: str
    revision: str
    backend_id: str
    required_capabilities: tuple[str, ...] = (LOCAL_CAPABILITY,)

    def __post_init__(self) -> None:
        for name in ("agent_id", "revision", "backend_id"):
            _id(getattr(self, name), name)
        _tuple(self.required_capabilities, "capabilities")
        for item in self.required_capabilities:
            _id(item, "capability")
        if len(set(self.required_capabilities)) != len(self.required_capabilities):
            raise ContractError("Duplicate capabilities")


@dataclass(frozen=True)
class AgentRequest:
    run_id: str
    question: str
    evidence: tuple[Evidence, ...] = ()
    context: str = ""
    timeout_seconds: float = 30.0
    max_output_chars: int = 64_000

    def __post_init__(self) -> None:
        _id(self.run_id, "run_id")
        _text(self.question, "question")
        if type(self.context) is not str or len(self.context) > 64_000:
            raise ContractError("Invalid context")
        if (type(self.timeout_seconds) not in (int, float)
                or not 0 < self.timeout_seconds <= 3600
                or not math.isfinite(self.timeout_seconds)):
            raise ContractError("Invalid timeout")
        if type(self.max_output_chars) is not int or not 1 <= self.max_output_chars <= 256_000:
            raise ContractError("Invalid output limit")
        _tuple(self.evidence, "evidence")
        ids = set()
        for item in self.evidence:
            if type(item) is not Evidence:
                raise ContractError("Invalid evidence record")
            _id(item.id, "evidence id")
            _text(item.source, "evidence source")
            _text(item.description, "evidence description")
            if item.id in ids:
                raise ContractError("Duplicate evidence id")
            ids.add(item.id)


@dataclass(frozen=True)
class AgentOutput:
    summary: str
    claims: tuple[Claim, ...] = ()
    challenges: tuple[Challenge, ...] = ()
    limitations: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        _text(self.summary, "summary", 256_000)
        for name in ("claims", "challenges", "limitations"):
            _tuple(getattr(self, name), name)
        for item in self.limitations:
            _text(item, "limitation")
        for claim in self.claims:
            if type(claim) is not Claim:
                raise ContractError("Invalid claim")
            _id(claim.id, "claim id")
            _id(claim.agent_id, "claim actor")
            _text(claim.statement, "claim statement")
            _tuple(claim.evidence_ids, "evidence references")
            for reference in claim.evidence_ids:
                _id(reference, "evidence reference")
        ids = set()
        for challenge in self.challenges:
            if type(challenge) is not Challenge:
                raise ContractError("Invalid challenge")
            for name in ("id", "claim_id", "challenger_id"):
                _id(getattr(challenge, name), f"challenge {name}")
            _text(challenge.reason, "challenge reason")
            if challenge.id in ids:
                raise ContractError("Duplicate challenge id")
            ids.add(challenge.id)


def _validate_output(manifest: AgentManifest, request: AgentRequest, output: AgentOutput) -> None:
    if type(output) is not AgentOutput:
        raise ContractError("Backend must return AgentOutput")
    if any(c.agent_id != manifest.agent_id for c in output.claims):
        raise ContractError("Claim actor mismatch")
    if any(c.challenger_id != manifest.agent_id for c in output.challenges):
        raise ContractError("Challenge actor mismatch")
    try:
        Council().synthesize(list(output.claims), list(output.challenges), list(request.evidence))
    except ValueError as exc:
        raise ContractError(str(exc)) from exc
    if len(_encode(asdict(output))) > request.max_output_chars:
        raise ContractError("Output budget exceeded")


@dataclass(frozen=True)
class AgentState:
    manifest: AgentManifest
    request: AgentRequest
    status: str = "pending"
    output: AgentOutput | None = None
    error_code: str | None = None
    schema_version: int = SCHEMA_VERSION

    def __post_init__(self) -> None:
        if type(self.schema_version) is not int or self.schema_version != SCHEMA_VERSION:
            raise ContractError("Unsupported schema version")
        if type(self.manifest) is not AgentManifest or type(self.request) is not AgentRequest:
            raise ContractError("Invalid manifest/request")
        if self.status not in ("pending", "running", "completed", "failed", "timed_out", "cancelled"):
            raise ContractError("Invalid status")
        if self.status == "completed":
            _validate_output(self.manifest, self.request, self.output)
        elif self.output is not None:
            raise ContractError("Only completed states may contain output")
        expected_errors = {"failed": ("backend_error", "invalid_output"),
                           "timed_out": ("timeout",), "cancelled": ("cancelled",)}
        if self.status in expected_errors:
            if self.error_code not in expected_errors[self.status]:
                raise ContractError("Invalid error code for status")
        elif self.error_code is not None:
            raise ContractError("Unexpected error code")

    def to_json(self) -> str:
        return _encode(asdict(self))

    @classmethod
    def from_json(cls, raw: str) -> AgentState:
        try:
            obj = _decode(raw)
            _keys(obj, {"manifest", "request", "status", "output", "error_code", "schema_version"})
            manifest = _record(obj["manifest"], AgentManifest, {"required_capabilities"})
            request_data = obj["request"]
            _keys(request_data, {"run_id", "question", "evidence", "context", "timeout_seconds", "max_output_chars"})
            request_data = dict(request_data)
            request_data["evidence"] = tuple(_record(e, Evidence) for e in _list(request_data["evidence"]))
            request = AgentRequest(**request_data)
            output = None
            if obj["output"] is not None:
                _keys(obj["output"], {"summary", "claims", "challenges", "limitations"})
                data = dict(obj["output"])
                data["claims"] = tuple(_record(c, Claim, {"evidence_ids"}) for c in _list(data["claims"]))
                data["challenges"] = tuple(_record(c, Challenge) for c in _list(data["challenges"]))
                data["limitations"] = tuple(_list(data["limitations"]))
                output = AgentOutput(**data)
            return cls(manifest, request, obj["status"], output, obj["error_code"], obj["schema_version"])
        except (TypeError, KeyError, RecursionError, ValueError) as exc:
            raise ContractError("Invalid portable state") from exc


def _encode(data: object) -> str:
    raw = json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)
    try:
        raw.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise ContractError("Invalid Unicode in wire payload") from exc
    if len(raw) > MAX_WIRE_CHARS:
        raise ContractError("Wire payload too large")
    return raw


def _keys(value: object, keys: set[str]) -> None:
    if type(value) is not dict or set(value) != keys:
        raise ContractError("Unexpected/missing fields")


def _list(value: object) -> list:
    if type(value) is not list or len(value) > 1000:
        raise ContractError("Expected bounded array")
    return value


def _record(value: object, record_type: type, tuples: set[str] = frozenset()):
    from dataclasses import fields
    _keys(value, {f.name for f in fields(record_type)})
    data = dict(value)
    for key in tuples:
        data[key] = tuple(_list(data[key]))
    return record_type(**data)


def _decode(raw: str):
    if type(raw) is not str or len(raw) > MAX_WIRE_CHARS:
        raise ContractError("Invalid wire payload")

    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ContractError("Duplicate JSON field")
            result[key] = value
        return result

    def reject_constant(value):
        raise ContractError(f"Non-finite JSON number: {value}")

    return json.loads(raw, object_pairs_hook=pairs, parse_constant=reject_constant)


class AgentBackend(Protocol):
    """An interchangeable computation backend; implementations are trusted code."""
    backend_id: str

    async def run(self, manifest: AgentManifest, request: AgentRequest) -> AgentOutput: ...


class StateStore(Protocol):
    def save(self, state: AgentState) -> None: ...


class AgentHost(Protocol):
    """Minimal host contract implemented by local, ADK and Microsoft adapters."""
    async def run(self, agent: PortableAgent, state: AgentState,
                  *, store: StateStore | None = None) -> AgentState: ...


class JsonStateStore:
    """Atomic single-owner local checkpoints. Not a multi-process scheduler."""
    def __init__(self, directory: str | Path):
        self.directory = Path(directory)

    def save(self, state: AgentState) -> None:
        raw = state.to_json()
        self.directory.mkdir(parents=True, exist_ok=True)
        destination = self.directory / f"{state.request.run_id}.json"
        if destination.exists():
            previous = self.load(state.request.run_id)
            if previous.manifest != state.manifest or previous.request != state.request:
                raise ContractError("Run ID already belongs to a different invocation")
            if previous != state:
                allowed = (previous.status == "pending" and state.status == "running") or (
                    previous.status == "running" and state.status in (
                        "completed", "failed", "timed_out", "cancelled"
                    )
                )
                if not allowed:
                    raise ContractError("Checkpoint transition would overwrite execution history")
            elif state.status == "running":
                raise ContractError("Run already dispatched; reconciliation required")
        fd, temporary = tempfile.mkstemp(prefix=".wiec-", dir=self.directory)
        try:
            with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as stream:
                stream.write(raw)
                stream.flush()
                os.fsync(stream.fileno())
            os.replace(temporary, destination)
        finally:
            if os.path.exists(temporary):
                os.unlink(temporary)

    def load(self, run_id: str) -> AgentState:
        _id(run_id, "run_id")
        with (self.directory / f"{run_id}.json").open(encoding="utf-8") as stream:
            state = AgentState.from_json(stream.read(MAX_WIRE_CHARS + 1))
        if state.request.run_id != run_id:
            raise ContractError("Checkpoint identity mismatch")
        return state


class PortableAgent:
    """Bounded local invocation, shared by all hosting adapters.

    Capability negotiation is not OS isolation. Only reviewed local backends are
    supported. External calls/tools require a future independently enforced gateway.
    """
    def __init__(self, manifest: AgentManifest, backend: AgentBackend):
        if manifest.backend_id != backend.backend_id:
            raise ContractError("Backend identity mismatch")
        self.manifest = manifest
        self.backend = backend
        self._active: set[str] = set()

    def prepare(self, request: AgentRequest) -> AgentState:
        state = AgentState(self.manifest, request)
        state.to_json()  # Enforce the total input envelope limit before dispatch.
        return state

    async def run(self, state: AgentState, *, store: StateStore | None = None) -> AgentState:
        if state.manifest != self.manifest:
            raise ContractError("Agent identity/revision/backend mismatch")
        if set(self.manifest.required_capabilities) - {LOCAL_CAPABILITY}:
            raise ContractError("Unsupported capability; external execution is unavailable")
        # Revalidate incoming snapshots even for a terminal replay.
        state = AgentState.from_json(state.to_json())
        if state.status == "running":
            raise ContractError("Ambiguous running checkpoint requires reconciliation; not retried")
        if state.status != "pending":
            if store is not None:
                store.save(state)
            return state
        run_id = state.request.run_id
        if run_id in self._active:
            raise ContractError("Run is already active in this agent instance")
        self._active.add(run_id)
        try:
            return await self._run_pending(state, store)
        finally:
            self._active.remove(run_id)

    async def _run_pending(self, state: AgentState, store: StateStore | None) -> AgentState:
        running = replace(state, status="running")
        if store is not None:
            store.save(running)  # Failure here prevents backend dispatch.
        try:
            output = await asyncio.wait_for(
                self.backend.run(self.manifest, state.request), state.request.timeout_seconds
            )
            result = replace(state, status="completed", output=output)
            result.to_json()
        except asyncio.CancelledError:
            if store is not None:
                store.save(replace(state, status="cancelled", error_code="cancelled"))
            raise
        except TimeoutError:
            result = replace(state, status="timed_out", error_code="timeout")
        except ContractError:
            result = replace(state, status="failed", error_code="invalid_output")
        except Exception:
            # Provider exceptions may contain secrets; do not persist their text.
            result = replace(state, status="failed", error_code="backend_error")
        if store is not None:
            store.save(result)
        return result


class EvidenceEchoBackend:
    """Deterministic offline reference backend, not an LLM or truth verifier."""
    backend_id = "evidence_echo_v1"

    async def run(self, manifest: AgentManifest, request: AgentRequest) -> AgentOutput:
        claims = tuple(Claim(f"claim_{i}", manifest.agent_id, evidence.description, (evidence.id,))
                       for i, evidence in enumerate(request.evidence))
        return AgentOutput(
            summary=f"Retained {len(claims)} source statements for: {request.question}",
            claims=claims,
            limitations=("Statements are copied from supplied evidence, not independently verified.",),
        )
