# Quantum experiments and claim gates

Status: proposed studies. **No results, hardware runs or advantage claims yet.**
Use the [experiment template](../templates/EXPERIMENT.md) and preserve failures.

## Q0 — Measurement and provenance on a local simulator

Question: can a future adapter preserve preparation, basis, bit ordering and
sampling metadata? Use a two-qubit Bell-state circuit; compare Z-basis sampling
against the ideal distribution and test additional bases before making a claim
about coherence/entanglement. Z-basis 00/11 correlation alone can also arise from
a classical mixture and is not an entanglement witness.

Fix circuit, simulator version and seeds; use repeated preparations and a stated
shot budget, such as 4096 per basis. Predeclare a statistical test and tolerance;
compare analytic expectations with noisy and ideal simulation separately.
Acceptance is provenance/adapter correctness, not quantum advantage or hardware access.
Include deliberately swapped bit ordering and missing metadata as rejection cases.

## Q1 — Small MaxCut: QAOA versus classical methods

Question: can the system compare methods without overstating a small demonstration?
Version a graph generator and instances of 4–10 vertices. Compute exact optimum
by enumeration as the reference, and include a suitable heuristic baseline.
Run a bounded QAOA simulation over multiple seeds and optimizer restarts, with
declared depth, total shots, evaluations and time budget. Check every returned
bitstring using the same classical objective function.

Report approximation quality, optimum-hit rate, variability and total runtime/cost.
Count encoding, compilation, optimization and postprocessing. Do not exclude
failed restarts. The instances are intentionally classically tractable; success
validates the integration, not a useful computational advantage.
[Algorithm source](https://arxiv.org/abs/1411.4028).

## Q2 — Tiny Hamiltonian: VQE versus exact diagonalization

Use an explicitly recorded two-to-four-qubit Hamiltonian with coefficient units,
known classical eigenvalues and a reproducible ansatz. Compare noiseless estimates,
shot-limited estimates and a named noise model. Predeclare absolute energy-error
tolerance and total optimizer/measurement budget. Record optimizer variability
separately from sampling uncertainty. Do not equate a toy Hamiltonian with a
validated chemistry result. [VQE source](https://arxiv.org/abs/1304.3061).

## Q3 — Optional hardware replication

Only after the gateway, cost controls and an access-readiness record exist, repeat
a preregistered Q0/Q1 experiment on an allowed QPU. Preserve target/compiler mapping,
calibration snapshot if available, queue delay, raw/mitigated results and actual
cost. Reproduce the analysis from artifacts even if the device cannot be replayed.
Hardware sampling is not expected to reproduce identical counts.

## Q4 — Does a quantum contributor help the council?

Compare the same council with no solver, a classical solver and a quantum/simulated
solver under matched resource budgets. Evaluate report correctness, unsupported
claims, handling of uncertainty and whether negative results survive synthesis.
Keep backend labels hidden from adjudicators where feasible. A more accurate
report because any solver was added is not evidence of a specifically quantum benefit.

## Gate for a quantum-advantage statement

Specify workload distribution, best defensible classical baseline, hardware and
software versions, equal accuracy/success criteria, full resource accounting and
independent replication conditions. Distinguish oracle-query, asymptotic,
simulation, hardware-performance and application-level claims. Publish sensitivity
analysis and negative cases. An experiment on a simulator cannot establish
hardware quantum speedup. No generic “quantum agents are smarter” claim is permitted.
