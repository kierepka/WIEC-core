# Delivery roadmap

## M0 — Domain model (included)
- [x] Immutable claim/evidence/challenge contracts
- [x] Contradictions retained rather than voted away
- [x] External effects denied in reference policy
- [x] Unit tests and runnable example

## M1 — Research Council MVP
- [ ] Versioned schemas, validators and recorded perspective fixtures
- [ ] Compare Google ADK and Microsoft Agent Framework conformance spikes
- [ ] Select one runtime adapter by ADR; keep LangGraph as an alternative
- [ ] Three genuinely differentiated perspective agents
- [ ] Explicit contradiction graph and provenance
- [ ] Critic attempts falsification; integrator preserves uncertainty
- [ ] JSON export of evidence and decisions
**Acceptance:** deterministic replay of 20 seeded questions and no silently
discarded contradictions.

## M2 — Independent Safety Kernel
- [ ] Out-of-process policy decision and enforcement points
- [ ] Sandboxed tools and short-lived capability tokens
- [ ] Tamper-evident audit, authenticated policy updates
- [ ] Human approval workflow, domain-specific safe states
- [ ] Prompt injection and bypass red-team suite
**Acceptance:** all external effects denied when policy service is unavailable;
demonstrated inability to bypass tool gateway in defined threat model.

## M3 — Scientific evaluation
- [ ] Public benchmark with adjudicated evidence
- [ ] Baselines: single agent, consensus multi-agent, WIEC
- [ ] Metrics: truth accuracy, false-belief resistance, unsafe-action prevention
- [ ] Confidence intervals, cost, latency and failure analysis
**Acceptance:** reproducible report with negative results included.

## M4 — Optional integrations
- [ ] Persistent world knowledge, RAG and versioned provenance
- [ ] Runtime adapter evaluation
- [ ] Quantum solvers only where measurable value is demonstrated

## Documentation baseline (included; not runtime functionality)

- [x] Polish project name, English translation and rationale
- [x] Domain contracts, council protocol and agent constitution
- [x] Knowledge lifecycle, threat model and evaluation design
- [x] Google ADK, Microsoft and alternative runtime integration designs
- [x] Annotated primary-source library and source-to-experiment traceability
- [x] Quantum foundations, access paths and proposed job/result contracts

## Q track — Optional quantum research (no results yet)

- [ ] Q0 local simulation: measurement and provenance conformance
- [ ] Q1 small MaxCut with exact/heuristic classical baselines
- [ ] Q2 tiny Hamiltonian with exact diagonalization reference
- [ ] Q3 optional authorized QPU replication after M2 controls and access checks
- [ ] Q4 council ablation: no solver / classical / quantum contributor

Q0–Q2 can progress independently of a cloud provider. They must not delay the
classical council or be presented as quantum advantage. Q3 needs verified account
access, approved data/cost bounds and independently enforced dispatch controls.
Detailed acceptance is in [quantum experiments](quantum/EXPERIMENTS.md).

No milestone is permission for uncontrolled external action.
