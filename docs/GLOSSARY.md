# Project glossary

- **Agent:** a bounded computational participant with an identity, perspective,
  inputs, outputs and declared capabilities. It need not be an LLM.
- **Perspective:** a documented role, source context and method; not proof of
  statistical independence from another agent.
- **Claim:** a statement scoped to assumptions, evidence and a context.
- **Evidence:** an inspectable observation, source or result relevant to a claim;
  citation alone does not establish support.
- **Challenge:** a recorded objection or attempted falsification of a claim.
- **Contradiction:** incompatible positions under comparable scope/assumptions;
  different contexts can explain an apparent conflict.
- **Falsification:** attempting to find a counterexample or discriminating test;
  failing to refute a claim is not a proof of universal truth.
- **Council:** the bounded process that preserves and compares perspectives.
- **Integrator:** a report-assembly role with no inherent action authority.
- **World Kernel:** proposed versioned knowledge view over scoped claims, not an oracle.
- **Safety Kernel:** target independent policy/enforcement subsystem; the current
  `SafetyPolicy` is only an in-process demonstration.
- **Capability grant:** an authenticated, scoped, expiring permission for a concrete
  effect; proposed for M2 and absent in the alpha.
- **Runtime adapter:** translation between orchestration frameworks and WIEC contracts.
- **Model provider:** a service supplying model inference; separate from runtime choice.
- **QPU:** physical quantum processing hardware; using a simulator is not QPU access.
- **Shot:** one circuit execution/measurement repetition in a sampling experiment.
- **Observable:** a mathematically specified quantity estimated from measurements.
- **Simulator:** classical software modeling a quantum process under stated assumptions.
- **Quantum-assisted agent:** a classical agent using a bounded quantum computation
  as one source of evidence; proposed research, not current functionality.
- **Quantum-native agent:** deferred research involving quantum resources beyond a
  job wrapper; no implementation or demonstrated benefit is claimed.
- **Replay:** reconstructing a run from recorded artifacts without redoing external calls.
- **Replication:** repeating an experiment; stochastic outputs need not match exactly.

See [contracts](CONTRACTS.md) for the exact current Python surface and proposed extensions.
