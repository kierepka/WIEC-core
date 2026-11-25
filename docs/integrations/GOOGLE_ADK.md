# Google ADK integration design

Status: proposed; no runnable ADK adapter exists. Use a version-pinned spike before
publishing SDK-specific examples. Reviewed official documentation on 2026-11-25.

## Mapping

WIEC run identity maps to a runtime session reference. Each initial perspective
gets an isolated input context and allowed source manifest. Stage outputs go
through the WIEC validator before exchange. Workflow composition handles initial
perspectives, bounded criticism and integration; the WIEC state machine determines
which stages are required and when a partial result is reported.

ADK distinguishes Session, State and searchable Memory. Store transient progress
in runtime state, but persist evidence and final report manifests in the WIEC
store. Do not promote cross-session memory into an authoritative citation without
rechecking its source, version and permissions.
[Official context model](https://adk.dev/sessions/).

## Tools and security

Expose only bounded local analysis and proposal creation in the first spike.
ADK safety documentation discusses callbacks and runner-wide plugins for policies.
Use such hooks for validation and telemetry, while a future independent gateway
holds executor credentials and authorizes actual remote effects. A callback cannot
protect credentials available to malicious code in the same process.
[Official safety guide](https://adk.dev/safety/).

The model caller also sends data and incurs cost. The trusted caller must check
the chosen provider, source classification, run budget and permitted model before
dispatch. Provider access is not inferred from an agent's text or a session flag.

## Spike checklist and acceptance

1. Pin Python and ADK version; document provider configuration with no embedded keys.
2. Implement recorded-output perspectives and event conversion without live tools.
3. Run three isolated initial contexts; store outputs before critique can see them.
4. Validate evidence IDs and source locators; reject malformed responses.
5. Test one bounded repair, timeout, missing perspective, cancellation and restart.
6. Export a WIEC report, keeping all material claims and challenge relationships.
7. Add explicitly permitted model calls only after data/cost controls are tested.

Use ADK evaluations for runtime behavior, and WIEC's separate evidence/disagreement
metrics for epistemic behavior. Passing one is not passing the other.
[Official evaluation guide](https://adk.dev/evaluate/).
