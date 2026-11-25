# Source-to-design traceability

Status: design rationale, not proof that the design has been implemented.
Source identifiers resolve in the [annotated reading list](READING_LIST.md).

- **QI-01 -> preparation/basis/shot metadata -> Q0.** Reject a result with unknown
  measurement meaning. Passing criterion: analytic expectations and artifact
  metadata survive the adapter and report export.
- **QI-02 -> physical-state/classical-record separation -> quantum contracts.**
  Review criterion: no promise of universally cloning or serializing unknown states.
- **QI-03 -> explicit classical communication -> deferred network research.**
  Review criterion: no instantaneous cross-agent information channel is assumed.
- **QA-01/QA-02 -> scoped complexity assumptions -> claim-review gate.** Require
  the precise workload and resource model rather than a blanket speedup claim.
- **QA-03 -> hybrid observable estimation -> Q2.** Compare with exact eigenvalues;
  record raw/processed estimates and reject missing units/conventions.
- **QA-04 -> MaxCut candidate -> Q1.** Check returned solutions classically and
  compare full costs under a declared budget; publish unsuccessful runs.
- **QA-05/QA-06 -> bounded optimization and trainability checks -> Q1/Q2.** Record
  restarts, gradients if measured, failures and scaling, not only the best result.
- **QA-07 -> fair input/baseline accounting -> Q4.** Include data preparation and
  compare the quantum contributor against a classical solver as well as no solver.
- **RT-01/RT-02 -> interchangeable orchestration -> M1 spikes.** Same recorded
  fixtures must produce equivalent WIEC record relationships and partial statuses.
- **RT-03/RT-04/RT-05 -> alternative runtimes -> adapter conformance.** Replace
  scheduling without changing the evidence model or bypassing the gateway.
- **RT-06 -> current Microsoft candidate -> ADR-0002.** Avoid presenting archived
  AutoGen as the actively maintained foundation for new work.

## Open hypotheses

H1: explicit falsification improves supported-answer quality at matched cost.
H2: preserved disagreement improves detection of false consensus.
H3: a separately enforced gateway reduces unauthorized effects in its threat model.
H4: some specified workload benefits from a quantum contributor after full costs.

H1/H2 need the [evaluation protocol](../EVALUATION.md). H3 needs adversarial deployment
tests, not prompt quality. H4 needs the [quantum claim gate](../quantum/EXPERIMENTS.md).
No listed source establishes any of H1–H4 for WIEC. Negative results can reject or
narrow these hypotheses and should remain in the research record.
