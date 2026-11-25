# Delivery roadmap

## M0 — Domain model (included)
- [x] Immutable claim/evidence/challenge contracts
- [x] Contradictions retained rather than voted away
- [x] External effects denied in reference policy
- [x] Unit tests and runnable example

## M1 — Research Council MVP
- [ ] LangGraph adapter behind runtime interface
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

No milestone is permission for uncontrolled external action.
