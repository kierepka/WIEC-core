# Microsoft agent ecosystem integration design

Status: a native offline `BaseAgent` host returning SDK `AgentResponse` is implemented
and tested with `agent-framework-core` 1.26.0. No hosted model, cloud deployment,
streaming or full Council workflow is implemented.
See [installation, runnable example and boundaries](../PORTABILITY.md).
Sources reviewed 2026-11-25.

## Agent Framework

Microsoft Agent Framework supplies agents and workflow APIs. The documented graph
model can coordinate typed executors, state, events and human input. WIEC's proposed
mapping is intake -> perspective fan-out -> validation fan-in -> critic -> integrator
-> report export. WIEC owns evidence semantics and policy invariants.
[Overview](https://learn.microsoft.com/en-us/agent-framework/overview) and
[workflow concepts](https://learn.microsoft.com/agent-framework/concepts/workflows/).

Checkpoint progress with WIEC artifact IDs and remote job references. A restart
must not duplicate a model request or paid computation after an ambiguous response.
Keep operational workflow state separate from the versioned epistemic graph.
Use middleware for instrumentation and validation; independently restrict executor
credentials and outbound access in the future M2 deployment.

## Foundry, hosting and identity

Hosted model/agent services are optional provider adapters. Before implementation,
verify the selected service's SDK version, identity, region, data handling, model
availability, pricing and deployment limits. Do not require Azure infrastructure
to import or test the WIEC core. Secrets belong in deployment secret stores and
trusted caller/executor processes, never claims, prompts or report artifacts.

## AutoGen and Semantic Kernel lineage

The Agent Framework overview describes bringing together AutoGen agent concepts
and Semantic Kernel enterprise features. This does not make older APIs drop-in
compatible. AutoGen's official site reports archival and recommends Agent Framework.
Use historical AutoGen material for migration and design context only.
[AutoGen official status](https://microsoft.github.io/autogen/stable/).

## Azure Quantum is a separate integration

An agent runtime and a quantum provider service solve different problems.
Agent Framework does not by itself give this project QPU access. A future Azure
Quantum adapter needs its own configured workspace/provider, credentials, budget
and execution gateway. See [access options](../quantum/ACCESS.md).

## Spike acceptance

Use the same fixtures as ADK: isolated perspectives, retained dissent, invalid
reference rejection, missing-role report, bounded retries, cancellation and replay.
Record SDK/language versions, event mappings and effect paths. Choose .NET or
Python based on measured project needs; keep the core Python domain portable.
No vendor-specific workflow checkpoint format becomes the public WIEC report format.
