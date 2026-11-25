# Architecture and trust boundaries

## Bounded context

**Epistemic layer:** `AgentPerspective`, `Claim`, `Evidence`, `Challenge`,
`Contradiction` (planned explicit graph), and `Council`. It generates hypotheses
and preserves counterarguments, with source provenance and confidence metadata
to be added.

**Safety layer:** `ProposedAction` and `SafetyDecision` are contracts.
Prototype `SafetyPolicy` denies external writes and physical effects
unconditionally, even if approval flags are set. No action executor exists.

**Runtime adapter:** LangGraph is a candidate default for orchestration,
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
