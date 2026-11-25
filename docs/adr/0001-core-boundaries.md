# ADR-0001: Separate epistemic reasoning from action authority

Status: Accepted for prototype (2026-11-24)

## Context
Existing agent runtimes already solve orchestration and persistence. WIEC's
distinct hypothesis is that falsification and durable disagreement improve
epistemic outcomes, while independent authorization limits unsafe actions.

## Decision
Build WIEC as a small epistemic + safety contract layer, not a replacement
for general agent runtimes. Start with pure Python domain objects and
no executable external tools. All external effects remain denied until
an independently enforced authorization boundary exists.

## Consequences
+ Low initial complexity; testable invariants.
+ Easy to compare runtimes later.
- No production agent functionality in v0.1.
- Non-harm remains an objective requiring contextual hazard analysis.
