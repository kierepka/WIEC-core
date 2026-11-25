# ADR-0004: Implement a bounded portable agent and native offline hosts

Status: Accepted for the portability foundation, 2026-11-25.

## Decision

Keep manifests, requests, outputs, execution semantics and JSON checkpoint validation
in an SDK-free module. Separate computation (`AgentBackend`) from hosting (`AgentHost`).
Use native custom-agent paths for Google ADK and Microsoft Agent Framework, with
fresh host sessions and explicit WIEC state. Pin optional SDK dependencies to the
tested releases. The first backend is deterministic local evidence echo.

## Alternatives and consequences

Keeping state only in vendor sessions makes transfer platform-dependent. Translating
arbitrary running agents would require semantics this alpha does not implement.
A bounded invocation with portable pending/terminal checkpoints is implementable
and testable now, while retaining future extension points. It cannot resume an
interrupted algorithm halfway or promise exactly-once remote effects.

## Validation and relationship to ADR-0002

One suite exercises the local and real SDK hosts and transfers recorded results
between every host pair. SDK installs are optional; no live provider or QPU is used.
See [implemented scope](../PORTABILITY.md). ADR-0002's full Research Council runtime
selection remains proposed: these small hosts establish a shared contract without
choosing one framework as the mandatory orchestrator.
