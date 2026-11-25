# Research Council protocol

Status: proposed M1 workflow; no live agents are included in the alpha.

## Roles

The first council has three perspective agents: a source analyst examining
direct evidence, an alternative-model analyst seeking competing explanations,
and a skeptical analyst testing assumptions and counterexamples. A critic stage
then challenges the collected claims; an integrator composes the report.
Critic and integrator are logical roles and may require additional calls.
The policy authority is a service, not another agent whose opinion can be outvoted.

Different prompts do not establish statistical independence. Record shared model
families, training/provider dependencies where known, overlapping sources and
visible prior outputs. Initially isolate perspective contexts; exchange positions
only after initial submissions. Describe this as procedural separation, not proof
of independent cognition.

## Bounded state machine

`created -> sources_frozen -> perspectives_running -> claims_validated ->
challenged -> integrated -> reported`

From each active state, timeout or cancellation can produce `partial` or `failed`.
Only the orchestrator advances states after validating required artifacts.
A partial report identifies missing roles and skipped stages; it never claims
the full protocol ran. Tool/action proposals enter a separate authorization path.

1. Freeze question, inclusion/exclusion rules, source manifest and budgets.
2. Run the three perspectives without seeing each other's initial outputs.
3. Validate IDs, source locations, structured output and scope.
4. Group related claims without deleting originals; identify possible contradictions.
5. Ask the critic for the strongest falsifier of each material conclusion.
6. Allow one bounded response round; log new evidence separately.
7. Integrate with explicit unresolved disagreements and limitations.
8. Export report and event/artifact manifest. Stop at the configured limit.

An invalid output gets at most one format-repair attempt within the original
budget. It cannot trigger unlimited retries. Expensive provider calls are not
automatically retried after ambiguous submission failures.

## Worked example (illustrative, not a recorded model run)

Question: should a small MaxCut instance use a QPU in the first release?
The source analyst notes that QAOA defines a relevant optimization algorithm.
The alternative analyst proposes exhaustive search for the small instance.
The skeptic asks whether data encoding, queue delay and shots outweigh any benefit.
The critic requires an end-to-end baseline comparison, not a circuit-only timing.
The integrator recommends a simulator experiment and records that no quantum
advantage has been established. A proposed paid QPU run remains unauthorized.

## Report requirements

Include the question, scope, source manifest, each material claim and its support,
counterevidence, falsification attempts, unresolved contradictions, confidence
method (or `not_calibrated`), missing inputs, runtime/model versions, costs,
latency and recommended experiments. Report consensus separately from evidence.
Do not request or publish hidden model reasoning; use inspectable argument summaries,
tool outcomes and provenance instead.
