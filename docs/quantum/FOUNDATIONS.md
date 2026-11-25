# Quantum foundations for WIEC contributors

Status: educational context; the implications for WIEC are design choices.
This is a scoped foundation for the project, not an exhaustive physics textbook.

## States, gates and measurement

A pure qubit state is `alpha|0> + beta|1>`, with complex amplitudes satisfying
`|alpha|^2 + |beta|^2 = 1`. Standard-basis measurement gives classical outcomes
with those probabilities. An n-qubit state vector has `2^n` complex entries;
this does not make all entries readable in one measurement.
[IBM: quantum information](https://quantum.cloud.ibm.com/learning/en/courses/basics-of-quantum-information/single-systems/quantum-information).

Relative phases and interference matter to computation. A classical probability
distribution over hypotheses is not interchangeable with a coherent quantum state.
In a circuit model, unitary gates transform states and measurement extracts
classical results. WIEC should record the circuit/preparation, measurement basis
and observable, rather than just a label saying “quantum answer”.

Density matrices describe mixed states and reduced subsystems, including noisy
settings. Distinguish uncertainty about evidence from physical quantum states;
the former does not require a density matrix.
[IBM: density matrices](https://quantum.cloud.ibm.com/learning/en/courses/general-formulation-of-quantum-information/density-matrices/introduction).
For general measurement effects `E_m`, outcome probability is `Tr(E_m rho)`.
[IBM: measurements](https://quantum.cloud.ibm.com/learning/en/courses/general-formulation-of-quantum-information/general-measurements/formulations-of-measurements).

## Entanglement and limits

Entangled systems have joint states that cannot be expressed as independent
subsystem states. Entanglement does not provide a channel for controllable
faster-than-light messages. Teleportation needs shared entanglement and classical
communication; it transfers quantum information, not matter or instant knowledge.
[IBM: teleportation](https://quantum.cloud.ibm.com/learning/en/courses/basics-of-quantum-information/entanglement-in-action/quantum-teleportation).

The no-cloning theorem rules out a universal operation that perfectly copies an
arbitrary unknown quantum state. It does not prevent copying a classical circuit
description or preparing a known state again. A database of articles and measured
counts is classical storage, not a backup of an arbitrary physical quantum state.
[IBM: limitations](https://quantum.cloud.ibm.com/learning/en/courses/basics-of-quantum-information/quantum-circuits/limitations-on-quantum-information).

## Algorithms and conditional benefits

Grover search provides a quadratic oracle-query improvement for unstructured
search. It does not make arbitrary document retrieval free: oracle construction,
data encoding and output costs belong in the analysis.
[Grover](https://arxiv.org/abs/quant-ph/9605043).
Shor gives polynomial-time quantum algorithms for factoring/discrete logarithms;
it is not a general-purpose reasoning acceleration result.
[Shor](https://arxiv.org/abs/quant-ph/9508027).

VQE couples quantum expectation estimation with classical parameter optimization;
QAOA is a parameterized approach to combinatorial optimization. Both are candidate
experiment families, not evidence of an advantage for WIEC.
[Peruzzo et al.](https://arxiv.org/abs/1304.3061),
[Farhi et al.](https://arxiv.org/abs/1411.4028).
Variational approaches face trainability, accuracy and efficiency challenges.
[Cerezo et al.](https://arxiv.org/abs/2012.09265).
Certain circuit families exhibit gradients that shrink exponentially with width;
this is a conditional result, not a statement about every quantum model.
[McClean et al.](https://arxiv.org/abs/1803.11173).

## Noise, sampling and resources

Keep shot noise, hardware noise, model error and optimizer variability separate.
State-vector simulation is classical computation; noisy simulation models selected
effects, not every physical imperfection. Physical and logical qubit counts mean
different resources. Error mitigation postprocessing and error-correcting encoded
computation must be reported separately; neither label guarantees a correct answer.
[IBM learning courses](https://quantum.cloud.ibm.com/learning/en/courses).

For WIEC experiments, preserve raw and processed estimates, statistical methods,
seeds, noise models, compiler settings and complete cost/latency accounting.
Do not equate a confidence interval for measurement sampling with confidence that
a real-world conclusion is true.

## Topics intentionally deferred

Quantum networking, quantum memories, fault-tolerant resource estimates, advanced
Hamiltonian simulation and quantum machine learning can be studied as separate
proposals. None is required for Research Council. Quantum consciousness, access
to “all possible knowledge” and automatic NP-hard problem solving are not project
capabilities or justified research claims.
