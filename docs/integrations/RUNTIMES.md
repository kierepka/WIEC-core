# Runtime and agent integration strategy

Status: native offline single-agent ADK and Microsoft hosts implemented;
other adapters and full Council orchestration remain proposed.
Documentation reviewed 2026-11-25; pin and test actual SDK releases at implementation.
See [implemented scope and pinned SDK versions](../PORTABILITY.md).

## Common requirements

A runtime provides scheduling and model/tool plumbing; WIEC owns claims, evidence,
challenges, report semantics and action-policy contracts. Every adapter must pass
the same recorded-output fixtures: three separated perspectives, bounded critique,
unknown reference rejection, partial results, cancellation, restart/replay and
denied direct effects. Compare integration effort, observability, model portability,
state semantics and costs without assuming a winner from feature lists.

## Google ADK — priority candidate

ADK documents workflow/agent composition, conversational sessions, state and memory,
plus evaluation. Proposed mapping: perspective roles to isolated invocations,
orchestrator stages to workflow steps, session events to WIEC event references.
Do not put policy secrets in shared session state. See the
[integration design](GOOGLE_ADK.md) and official
[context documentation](https://adk.dev/sessions/) and
[evaluation guide](https://adk.dev/evaluate/).

## Microsoft Agent Framework — priority candidate

Microsoft documents agents and explicit workflows with state/events and human
input. Proposed mapping: perspective executors feed a validated fan-in stage;
workflow checkpoints reference WIEC artifacts. This is the current Microsoft
candidate; Foundry hosting is an optional deployment choice, not a core dependency.
See [Microsoft design](MICROSOFT.md) and
[official overview](https://learn.microsoft.com/en-us/agent-framework/overview).

## LangGraph — explicit state/control alternative

Its graph runtime supports stateful orchestration, persistence and interrupts.
Map nodes to WIEC stages and checkpoint artifact references, preserving separate
perspective contexts. Interrupts are useful workflow controls; the executor must
still validate authorization. [Official overview](https://docs.langchain.com/oss/python/langgraph/overview).

## OpenAI Agents SDK — lightweight agent-loop alternative

Agents, tools, handoffs, sessions and tracing can host perspective calls. Prefer
bounded structured specialist outputs to an unconstrained manager rewriting all
positions. Agent input/output guardrails are not equivalent to checking every
effect; tool and handoff paths need explicit authorization at the gateway.
[Overview](https://openai.github.io/openai-agents-python/) and
[guardrail scope](https://openai.github.io/openai-agents-python/guardrails/).

## CrewAI — role/task workflow alternative

Crews and Flows offer a role-oriented way to express work. A future adapter must
retain the raw positions and WIEC IDs before synthesis and prohibit autonomous
delegation that escapes the configured budget. This mapping is a proposal, not
tested compatibility. [Official introduction](https://docs.crewai.com/en/introduction).

## AutoGen and Semantic Kernel

AutoGen's official site currently marks the project archived and directs new
users to Microsoft Agent Framework. Treat it as historical/migration material,
not the new default. [Official status](https://microsoft.github.io/autogen/stable/).
Existing Semantic Kernel or AutoGen integrations may be migration inputs; record
their exact versions and preserved behavior rather than assuming API equivalence.

## Other agents, symbolic solvers and remote protocols

Any backend may participate if its outputs satisfy WIEC contracts and its effects
pass the gateway. MCP/A2A-style tool or agent communication is transport, not
automatic trust, permission or epistemic independence. Validate remote identities,
data recipients, schema versions, deadlines and delegated resource limits.
A classical solver and a quantum solver contribute evidence under the same rules.

## Selection experiment

Build one small ADK spike and one Microsoft spike, each using recorded perspective
outputs before live calls. Run the identical conformance cases, measure code and
operational complexity, then record an ADR choosing the initial adapter. LangGraph
is a fallback/control. Avoid implementing six runtimes before one full protocol works.
