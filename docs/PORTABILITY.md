# Portable agents: implemented contract and hosting adapters

Status: implemented local portability foundation. The native SDK hosts were
tested with Google ADK **2.15.1** and Microsoft Agent Framework Core **1.26.0** on
Python 3.11. The domain module uses only Python's standard library and the WIEC core.

## What is portable

`AgentManifest` identifies agent, revision, backend and required capabilities.
`AgentRequest` contains a run ID, question, source records, context, cooperative
timeout and output-size bound. `AgentOutput` returns summary, claims, challenges
and limitations. `AgentState` binds these to schema version 1 and an execution status.
All concrete fields are defined in `src/wiec/portable.py`; JSON round trips reject
unknown fields/versions, duplicate keys, invalid types and inconsistent references.

`AgentBackend.run(manifest, request)` is the independent computation port. The
included `EvidenceEchoBackend` copies supplied source statements with their IDs
and a limitation notice. It is deterministic and offline; it does not infer truth
or make model calls. Other reviewed local algorithms can implement the same port.
Backend ID/revision must change when its behavior changes.

`AgentHost.run(agent, state, store=...)` is the minimal runtime port. `LocalAdapter`,
`GoogleAdkAdapter` and `MicrosoftAdapter` implement it. The agent implementation and
source/result format stay unchanged when the host changes.

## Native SDK paths

ADK uses a custom `BaseAgent`, a real `Runner`, native user/content/event objects
and a fresh in-memory session for each invocation. `make_adk_agent` exposes that
native agent for composition. Microsoft uses a custom SDK `BaseAgent` returning
an SDK `AgentResponse`; `make_microsoft_agent` exposes it. Its supported mode is
one non-streaming user message containing a checkpoint, with no provider/tool args.

Both hosts invoke the same `PortableAgent`. They do not translate arbitrary vendor
agents into WIEC, inherit vendor conversation memory, call an LLM, register remote
tools or claim to implement all SDK middleware/streaming features. Test coverage
establishes this bounded custom-agent path, not arbitrary platform compatibility.

## Install and run

The core remains dependency-free. Install only the host extras you need:

```bash
python -m pip install -e '.[dev]'
python examples/portable_agent.py --platform local

# Optional SDKs pinned to tested releases:
python -m pip install -e '.[dev,adk,microsoft]'
python examples/portable_agent.py --platform adk --run-id adk-demo
python examples/portable_agent.py --platform microsoft --run-id ms-demo

# Transfer an ADK checkpoint to Microsoft without calling the backend again:
python examples/portable_agent.py --platform microsoft --run-id adk-demo --resume
python -m pytest -q
```

These examples need no credentials or remote provider access. SDK package
installation needs network access; the demonstrated agent invocation does not.
The default local checkpoint directory `.wiec-state/` is ignored by Git.

## Portable checkpoints and recovery

`JsonStateStore.save/load` writes canonical JSON by atomic file replacement.
The host does not own this format. A pending snapshot can start on another host;
a completed snapshot returns its validated recorded result without backend dispatch.
The single-owner file store rejects conflicting run identities and stale writes
that would replace a terminal checkpoint with pending/running state.
Failed, timed-out and cancelled snapshots are terminal too: retry requires a new
run ID, not an implicit loop. A saved `running` snapshot is ambiguous after a crash
and is rejected until an operator reconciles it. There is no automatic exactly-once
execution claim for stale pending snapshots or independently created agent instances.

Only one owner may operate a checkpoint directory/run ID at a time. One live
`PortableAgent` rejects concurrent invocations of the same run; this is not a
distributed lock. The example refuses overwriting an existing run without `--resume`.
Atomic replacement prevents partial JSON visibility but is not a transactional job
scheduler or a guarantee against every OS/power-loss scenario. Keep this local
store out of untrusted write access and apply appropriate retention/permissions.

Input context is explicitly part of the envelope. An algorithm that needs earlier
results must receive them in permitted context or use a future versioned memory
port; it cannot rely on hidden vendor session history. This change does not provide
mid-algorithm checkpointing or migrate a live model's internal state.

## Failure and resource behavior

The engine saves `running` before dispatch; failed persistence prevents execution.
It saves either validated output or a redacted error code afterward. If the final
save fails, the stored running record stays ambiguous; reconcile before retrying.
Malformed outputs, actor mismatch, missing evidence, duplicate claims and excess
output are rejected. Errors do not persist arbitrary exception strings, which may
contain secrets. Cancellation is recorded and propagated to the caller.

Timeout/cancellation is cooperative asyncio behavior. A backend blocking the event
loop or suppressing cancellation is not forcibly stopped. Output is bounded when
returned/serialized; this is not a process-memory limit. Local reviewed code is
trusted, not sandboxed, and can bypass an in-process policy if malicious.

Only `local_reasoning` capability is supported. Remote model, external write,
physical and QPU capabilities are rejected; a declared capability is not a grant.
No executor, cloud spending or independent gateway is introduced by these hosts.

## Conformance and remaining scope

The same pytest cases run on all three hosts with real installed SDKs: equivalent
output, retained opposing sources, malformed results, unknown references, actor
mismatch, output bound, timeout, cancellation, unsupported capabilities and terminal
replay. Transfer tests cover every local/ADK/Microsoft host pair. Core-only installs
skip SDK cases; the dedicated CI job installs both extras and runs the full suite.

Remaining work includes full Council orchestration, event/provenance stores,
authenticated checkpoints, distributed coordination, model/tool gateways and
live-provider validation. Generic SDK-free contracts are an extension point for
other runtimes; no LangGraph/CrewAI/OpenAI/QPU adapter is claimed implemented.
