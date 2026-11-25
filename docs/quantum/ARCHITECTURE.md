# Hybrid quantum/classical architecture

Status: proposed contracts, not a callable API. No quantum package is a core dependency.

## Data and control flow

A perspective proposes a precisely scoped computational question. A classical
problem compiler creates a circuit, Hamiltonian or other supported representation.
Preflight validates its size, data classification, device compatibility, execution
budget and permitted destination. A local sandbox or future remote gateway runs it.
Classical postprocessing generates an evidence record linked to the original
problem, transformation, raw results and a baseline. The council can challenge it.

An LLM may help formulate a problem; trusted code validates numeric artifacts and
provider requests. Provider credentials never enter a prompt. A compiler-generated
problem transformation must preserve constraints and objective conventions, with
small-instance checks against a trusted classical formulation.

## Proposed problem and job records

`QuantumProblem`: schema version, ID, problem family, mathematical specification,
input artifact digest, units, optimization direction, constraints, encoding,
observable definitions, baseline specification and acceptance tolerance.

`QuantumJob`: problem ID, local/simulator/QPU mode, provider/target/region,
SDK/compiler versions, compiled artifact digest, qubit mapping, circuit depth,
shot budget, total evaluation cap, deadline, cost reservation and authorization ID.
Record logical/physical qubits separately where applicable. Do not store API keys.

`QuantumResult`: job/provider IDs, backend type, submission/start/end timestamps,
raw artifact digest, counts or observable estimates, uncertainty method, requested
and actual shots, noise/calibration references where supplied, mitigation settings,
optimizer history, postprocessing version, actual/estimated charges and status.

Statuses distinguish `proposed`, `preflight_failed`, `authorized`, `submitted`,
`queued`, `running`, `completed`, `failed`, `cancel_requested`, `cancelled` and
`outcome_unknown`. A requested cancellation is not confirmation of cancellation.

## Capability negotiation

The adapter advertises supported problem/program types, observables, operations,
measurement support, parameter binding, numeric precision, size limits and
availability snapshot time. Reject unsupported circuits before dispatch. Never
silently replace a hardware target with a simulator or a different provider.
Fallback requires the original policy to permit that mode and is labeled in results.

Provider-specific code lives outside the domain core. Proposed adapters expose
`capabilities`, `estimate`, `submit`, `status`, `fetch_result` and `cancel`.
These names are WIEC design concepts, not claims about vendor method names.
Polling and cancellation must be bounded and use narrowly scoped permissions.

## Budgets, failures and verification

Cap circuit evaluations, shots, optimizer iterations, retries, concurrency and
wall time. Reserve across concurrent jobs atomically before dispatch. Cost includes
classical preprocessing, compilation, provider tasks, storage and postprocessing.
If the provider cannot offer a strict cost bound, require a conservative approved
reservation or refuse automated dispatch; do not promise an exact cap from an estimate.

Reconcile ambiguous submissions before retrying. Store raw outputs before summary
generation. Check normalization, bit ordering, units and requested-vs-actual workload;
record discarded shots and failures. Valid counts do not prove the device executed
the intended physics: verification strength depends on the experiment and threat model.

## Future quantum-native agents

An agent with persistent physical quantum memory would require state-lifetime,
measurement, transfer and ownership semantics beyond classical record persistence.
Entanglement distribution would require explicit hardware and classical channels.
These are deferred research questions, not features of a cloud QPU job wrapper.
Do not represent unknown quantum states as safely clonable JSON memory.
