import asyncio
from dataclasses import replace
import json
import subprocess
import sys

import pytest

from wiec import Evidence
from wiec.portable import (
    AgentManifest, AgentOutput, AgentRequest, AgentState, ContractError,
    EvidenceEchoBackend, JsonStateStore, PortableAgent,
)


def agent():
    return PortableAgent(AgentManifest("analyst", "v1", "evidence_echo_v1"), EvidenceEchoBackend())


def request(**changes):
    return replace(AgentRequest("run1", "Assess both positions", evidence=(
        Evidence("e1", "fixture:a", "X"), Evidence("e2", "fixture:b", "not X"),
    )), **changes)


def test_core_import_does_not_load_vendor_sdks():
    subprocess.run([sys.executable, "-c", "import sys, wiec.portable, wiec.adapters; "
                    "assert 'google.adk' not in sys.modules; "
                    "assert 'agent_framework' not in sys.modules"], check=True)


def test_round_trip_and_replay_do_not_invoke_backend(tmp_path):
    class Counting(EvidenceEchoBackend):
        calls = 0

        async def run(self, manifest, task):
            self.calls += 1
            return await super().run(manifest, task)

    backend = Counting()
    portable = PortableAgent(agent().manifest, backend)
    store = JsonStateStore(tmp_path)
    result = asyncio.run(portable.run(portable.prepare(request()), store=store))
    assert result.status == "completed"
    assert [c.statement for c in result.output.claims] == ["X", "not X"]
    saved = store.load("run1")
    assert saved == AgentState.from_json(result.to_json()) == result
    assert asyncio.run(portable.run(saved)) == result
    assert backend.calls == 1
    assert not list(tmp_path.glob(".wiec-*"))


@pytest.mark.parametrize("mutate", [
    lambda x: x.update(schema_version=2),
    lambda x: x.update(schema_version=True),
    lambda x: x.update(extra="field"),
    lambda x: x.update(status="unknown"),
    lambda x: x.update(output={}),
    lambda x: x["manifest"].update(extra="field"),
    lambda x: x["request"].update(timeout_seconds=True),
    lambda x: x["request"].update(timeout_seconds=-1),
    lambda x: x["request"].update(timeout_seconds=10**1000),
    lambda x: x["request"].update(max_output_chars=True),
    lambda x: x["request"].update(evidence="bad"),
    lambda x: x["request"]["evidence"][0].update(source=123),
])
def test_reject_invalid_wire_contract(mutate):
    data = json.loads(agent().prepare(request()).to_json())
    mutate(data)
    with pytest.raises(ContractError):
        AgentState.from_json(json.dumps(data))


@pytest.mark.parametrize("raw", ['{"status":"pending","status":"completed"}',
                                  '{"x":NaN}', '{"x":Infinity}', "[]", "not json"])
def test_reject_duplicate_nonfinite_and_malformed_json(raw):
    with pytest.raises(ContractError):
        AgentState.from_json(raw)


@pytest.mark.parametrize("changes", [
    {"question": ""}, {"run_id": "../escape"}, {"context": None},
    {"evidence": (Evidence("x", "fixture", "X"), Evidence("x", "fixture", "Y"))},
])
def test_direct_constructors_validate(changes):
    with pytest.raises(ContractError):
        request(**changes)


def test_identity_capability_and_running_checkpoint_rejected():
    portable = agent()
    state = portable.prepare(request())
    for bad in (replace(state, manifest=replace(state.manifest, revision="v2")),
                replace(state, status="running")):
        with pytest.raises(ContractError):
            asyncio.run(portable.run(bad))
    remote = PortableAgent(replace(portable.manifest, required_capabilities=("external_write",)),
                           EvidenceEchoBackend())
    with pytest.raises(ContractError):
        asyncio.run(remote.run(remote.prepare(request())))


def test_store_failure_prevents_dispatch(tmp_path):
    class BrokenStore:
        def save(self, state):
            raise OSError("disk unavailable")

    class ForbiddenBackend(EvidenceEchoBackend):
        async def run(self, manifest, task):
            pytest.fail("Backend dispatched after failed checkpoint")

    portable = PortableAgent(agent().manifest, ForbiddenBackend())
    with pytest.raises(OSError):
        asyncio.run(portable.run(portable.prepare(request()), store=BrokenStore()))
    store = JsonStateStore(tmp_path)
    with pytest.raises(ContractError):
        store.load("../escape")
    (tmp_path / "other.json").write_text(portable.prepare(request()).to_json())
    with pytest.raises(ContractError):
        store.load("other")


def test_cooperative_cancel_persists_and_propagates(tmp_path):
    async def scenario():
        started = asyncio.Event()

        class Waiting(EvidenceEchoBackend):
            async def run(self, manifest, task):
                started.set()
                await asyncio.Event().wait()

        portable = PortableAgent(agent().manifest, Waiting())
        store = JsonStateStore(tmp_path)
        task = asyncio.create_task(portable.run(portable.prepare(request()), store=store))
        await started.wait()
        assert store.load("run1").status == "running"
        with pytest.raises(ContractError):
            await portable.run(portable.prepare(request()))
        task.cancel()
        with pytest.raises(asyncio.CancelledError):
            await task
        assert store.load("run1").status == "cancelled"

    asyncio.run(scenario())


def test_reject_corrupt_completed_checkpoint():
    result = asyncio.run(agent().run(agent().prepare(request())))
    data = json.loads(result.to_json())
    data["output"]["claims"][0]["evidence_ids"] = ["missing"]
    with pytest.raises(ContractError):
        AgentState.from_json(json.dumps(data))


def test_store_rejects_stale_pending_and_different_invocation(tmp_path):
    store = JsonStateStore(tmp_path)
    portable = agent()
    pending = portable.prepare(request())
    completed = asyncio.run(portable.run(pending, store=store))
    with pytest.raises(ContractError):
        asyncio.run(agent().run(pending, store=store))
    with pytest.raises(ContractError):
        store.save(agent().prepare(request(question="Different task")))
    assert store.load("run1") == completed


def test_output_must_be_json_object_not_array_of_pairs():
    result = asyncio.run(agent().run(agent().prepare(request())))
    data = json.loads(result.to_json())
    data["output"] = list(data["output"].items())
    with pytest.raises(ContractError):
        AgentState.from_json(json.dumps(data))


def test_invalid_unicode_is_rejected_before_dispatch():
    with pytest.raises(ContractError):
        agent().prepare(request(question="invalid\ud800"))
