# Architecture and trust boundaries

Status: current core plus proposed target architecture, 2026-11-25.
See the [documentation index](README.md) for requirements and implementation gates.

## What exists today

`model.py` defines local dataclasses; `council.py` validates selected references
and retains inputs; `safety.py` denies external/physical effects in a demonstration
policy. The original eight unit tests and a deterministic example exercise this surface.
`portable.py` adds a versioned single-agent invocation/checkpoint contract,
atomic single-owner JSON persistence and a bounded local backend port. Optional
native Google ADK/Microsoft hosts run the same offline agent with shared conformance
tests. There are no live model/QPU connections, full Council runtime, storage
services, authorization server or executor. See [implemented portability](PORTABILITY.md).
The target infrastructure below remains a design, not a deployed service.

## Target components

The intake service freezes question, source permissions, budget and run identity.
The source registry and knowledge service provide versioned evidence. The runtime
adapter schedules perspective, critic and integration stages. Domain validators
admit records into the epistemic graph. Report assembly produces an inspectable
argument and unresolved questions, independent of permission to execute anything.

The independent policy/gateway path authorizes concrete effects. A credential
broker supplies scoped secrets only to the executor. The execution ledger records
decisions and outcomes; observability exports redacted metrics and trace references.
A future quantum adapter sits behind the same gateway as other remote computation.

## Ownership of state and dependencies

The WIEC event/artifact model is the portable source of run provenance. Runtime
sessions/checkpoints contain execution state and references to it, not a second
uncontrolled truth store. Separate per-perspective contexts precede the exchange
round. Resume reconstructs from stored artifacts and reconciles remote jobs;
it does not resubmit effects blindly.

Dependency direction: adapters depend on WIEC contracts; core contracts do not
depend on Google ADK, Microsoft Agent Framework, LangGraph or quantum SDKs.
SDKs belong in future optional integration packages. No SDK is added by this documentation.

## Deployment progression

1. Alpha: local pure-Python objects and deterministic tests, implemented.
2. M1: local orchestrator plus recorded or explicitly permitted model calls;
   externally effecting tools remain absent. Start by evaluating Google ADK and
   Microsoft Agent Framework against one conformance suite. Bounded single-agent
   hosts now exist; the multi-stage Council orchestrator remains future work.
3. M2: isolated agent workers, independent gateway, artifact/event store,
   authenticated approvals and secrets restricted to executors.
4. Research: a bounded simulator adapter; later, an explicitly authorized remote
   QPU adapter only after effect/budget controls pass their gates.

Do not make orchestration selection a dependency on a single cloud or QPU vendor.
See [runtime integration strategy](integrations/RUNTIMES.md).

## Bounded context

**Epistemic layer:** `AgentPerspective`, `Claim`, `Evidence`, `Challenge`,
`Contradiction` (planned explicit graph), and `Council`. It generates hypotheses
and preserves counterarguments, with source provenance and confidence metadata
to be added.

**Safety layer:** `ProposedAction` and `SafetyDecision` are contracts.
Prototype `SafetyPolicy` denies external writes and physical effects
unconditionally, even if approval flags are set. No action executor exists.

**Runtime adapter:** Google ADK and Microsoft Agent Framework are priority candidates;
LangGraph remains an alternative for orchestration,
not a dependency of the epistemic or safety models. Microsoft Agent Framework
and Google ADK may be evaluated as adapters. This is a design choice, not a
claim of compatibility already implemented.

## Intended production trust boundary

```text
Untrusted agent process
  -> typed proposal API
  -> separate policy/enforcement service
  -> scoped, short-lived capability grant
  -> sandboxed executor
  -> tamper-evident audit + outcome monitor
```

The executor must reject requests without valid capabilities. Agent code must
not possess direct network, filesystem, cloud or physical-device credentials
outside its declared sandbox. Policy changes require separate authorization.

## Safety model

Non-harm is the highest **normative objective**. Absolute real-world safety is
not provable for unrestricted environments. Use threat models, domain-specific
hazard analysis, least privilege, fail-closed enforcement and independent
testing. `SAFE_STOP` must be defined per resource; cutting power can itself be
dangerous in medical or physical systems.

Human oversight cannot waive non-negotiable hard constraints. Safety
assessment should include harms from **inaction**, not only harms from action.

## Out of scope for v0.1

Production isolation, cryptographic capabilities, remote attestation,
tamper-evident storage, LLM integrations, retrieval, persistent knowledge,
benchmark claims, physical execution and quantum backends.
