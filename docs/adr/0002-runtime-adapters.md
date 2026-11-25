# ADR-0002: Keep runtimes replaceable; evaluate ADK and Microsoft first

Status: Proposed, 2026-11-25.

## Context

Research Council requires orchestration, state, bounded calls and observable events.
The user requested Google ADK, Microsoft agents and other agent ecosystems.
The domain/evidence model must remain independent of a vendor SDK.

## Proposed decision

Evaluate Google ADK and Microsoft Agent Framework with one shared recorded-output
conformance suite. Keep LangGraph as a control/fallback and document OpenAI Agents
SDK/CrewAI mappings. Select one first implementation through a follow-up ADR after
the spikes; do not install every runtime as a core dependency.

## Alternatives and consequences

A custom scheduler adds maintenance before domain behavior is validated. Coupling
directly to one vendor simplifies the first prototype but makes provenance/export
and later migration harder. Adapter boundaries cost some translation code but
preserve comparable reports and independent effect controls.

## Evidence and acceptance

See [runtime sources and mappings](../integrations/RUNTIMES.md). All proposed
adapters must preserve evidence references, dissent and partial status, enforce
bounded retries and produce replayable artifacts. No adapter is implemented yet.
