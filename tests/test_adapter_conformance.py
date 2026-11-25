"""One suite against the local host and real optional SDKs, without model calls."""
import asyncio
from dataclasses import replace

import pytest

from wiec import Claim, Evidence
from wiec.portable import (AgentManifest, AgentOutput, AgentRequest, AgentState,
                           ContractError, EvidenceEchoBackend, JsonStateStore, PortableAgent)
from wiec.adapters.local import LocalAdapter


def host(name):
    if name == "local":
        return LocalAdapter()
    if name == "adk":
        pytest.importorskip("google.adk")
        from wiec.adapters.google_adk import GoogleAdkAdapter
        return GoogleAdkAdapter()
    pytest.importorskip("agent_framework")
    from wiec.adapters.microsoft import MicrosoftAdapter
    return MicrosoftAdapter()


@pytest.fixture(params=["local", "adk", "microsoft"])
def adapter(request):
    return host(request.param)


def make_agent(backend=None):
    return PortableAgent(AgentManifest("analyst", "v1", "evidence_echo_v1"),
                         backend or EvidenceEchoBackend())


def make_request(**changes):
    return replace(AgentRequest("conformance", "Retain competing source statements",
                               evidence=(Evidence("a", "fixture:a", "X"),
                                         Evidence("b", "fixture:b", "not X"))), **changes)


def test_retained_sources_and_identical_portable_result(adapter, tmp_path):
    portable = make_agent()
    state = portable.prepare(make_request())
    expected = asyncio.run(portable.run(state))
    store = JsonStateStore(tmp_path)
    actual = asyncio.run(adapter.run(portable, state, store=store))
    assert actual.to_json() == expected.to_json() == store.load("conformance").to_json()
    assert [claim.evidence_ids for claim in actual.output.claims] == [("a",), ("b",)]
    assert [claim.statement for claim in actual.output.claims] == ["X", "not X"]


@pytest.mark.parametrize("mode, status, error", [
    ("unknown_reference", "failed", "invalid_output"),
    ("wrong_actor", "failed", "invalid_output"),
    ("duplicate_claim", "failed", "invalid_output"),
    ("unstructured", "failed", "invalid_output"),
    ("oversized", "failed", "invalid_output"),
    ("crash", "failed", "backend_error"),
    ("timeout", "timed_out", "timeout"),
])
def test_failure_semantics_match_all_hosts(adapter, mode, status, error, tmp_path):
    class Backend(EvidenceEchoBackend):
        calls = 0

        async def run(self, manifest, request):
            self.calls += 1
            if mode == "crash":
                raise RuntimeError("SECRET must never appear in persisted errors")
            if mode == "timeout":
                await asyncio.Event().wait()
            if mode == "unstructured":
                return {"summary": "not a contract"}
            if mode == "oversized":
                return AgentOutput("x" * 1000)
            claim = Claim("c", "other" if mode == "wrong_actor" else manifest.agent_id,
                          "X", ("missing" if mode == "unknown_reference" else "a",))
            return AgentOutput("result", claims=(claim, claim) if mode == "duplicate_claim" else (claim,))

    backend = Backend()
    portable = make_agent(backend)
    state = portable.prepare(make_request(timeout_seconds=0.02, max_output_chars=500))
    store = JsonStateStore(tmp_path)
    result = asyncio.run(adapter.run(portable, state, store=store))
    assert (result.status, result.error_code) == (status, error)
    assert result.output is None
    assert "SECRET" not in result.to_json()
    assert store.load("conformance") == result
    # Terminal failures do not silently retry when transferred to a new host.
    assert asyncio.run(adapter.run(portable, result)) == result
    assert backend.calls == 1


def test_unsupported_capability_does_not_call_backend(adapter):
    class Forbidden(EvidenceEchoBackend):
        async def run(self, manifest, request):
            pytest.fail("Unsupported capability dispatched")

    portable = PortableAgent(AgentManifest("analyst", "v1", "evidence_echo_v1", ("qpu",)), Forbidden())
    with pytest.raises(ContractError):
        asyncio.run(adapter.run(portable, portable.prepare(make_request())))


@pytest.mark.parametrize("origin", ["local", "adk", "microsoft"])
@pytest.mark.parametrize("destination", ["local", "adk", "microsoft"])
def test_checkpoint_transfer_between_hosts(origin, destination, tmp_path):
    first, second = host(origin), host(destination)
    store = JsonStateStore(tmp_path)
    portable = make_agent()
    pending = portable.prepare(make_request())
    store.save(pending)
    completed = asyncio.run(first.run(portable, store.load("conformance"), store=store))

    class NeverCall(EvidenceEchoBackend):
        async def run(self, manifest, request):
            pytest.fail("Completed transfer executed the backend twice")

    fresh_agent = make_agent(NeverCall())
    loaded = JsonStateStore(tmp_path).load("conformance")
    assert asyncio.run(second.run(fresh_agent, loaded)).to_json() == completed.to_json()


def test_pending_checkpoint_can_start_on_another_host(adapter, tmp_path):
    portable = make_agent()
    store = JsonStateStore(tmp_path)
    store.save(portable.prepare(make_request()))
    result = asyncio.run(adapter.run(make_agent(), store.load("conformance")))
    assert result.status == "completed"


def test_running_checkpoint_never_automatically_retries(adapter):
    portable = make_agent()
    state = replace(portable.prepare(make_request()), status="running")
    with pytest.raises(ContractError):
        asyncio.run(adapter.run(portable, state))


def test_host_cancellation_persists_without_swallowing_cancel(adapter, tmp_path):
    async def scenario():
        entered = asyncio.Event()

        class Waiting(EvidenceEchoBackend):
            async def run(self, manifest, request):
                entered.set()
                await asyncio.Event().wait()

        portable = make_agent(Waiting())
        store = JsonStateStore(tmp_path)
        task = asyncio.create_task(adapter.run(portable, portable.prepare(make_request()), store=store))
        await asyncio.wait_for(entered.wait(), 5)
        task.cancel()
        with pytest.raises(asyncio.CancelledError):
            await task
        assert store.load("conformance").status == "cancelled"

    asyncio.run(scenario())


def test_native_hosts_reject_non_contract_messages():
    pytest.importorskip("google.adk")
    pytest.importorskip("agent_framework")
    from agent_framework import Message
    from wiec.adapters.microsoft import make_microsoft_agent
    native = make_microsoft_agent(make_agent())
    with pytest.raises(ContractError):
        asyncio.run(native.run([Message("user", ["not a portable state"])]))
    with pytest.raises(NotImplementedError):
        native.run([], stream=True)
