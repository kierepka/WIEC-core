# Domain contracts and proposed interfaces

Status: current Python objects plus a proposed transport design. Proposed fields
below do not exist in the current package unless explicitly identified.

## Implemented Python surface

`Evidence(id, source, description)` records a reference, without retrieving or
verifying it. `Claim(id, agent_id, statement, evidence_ids)` associates claims
with evidence. `Challenge(id, claim_id, challenger_id, reason)` contests a claim.
`Council.synthesize(claims, challenges, evidence)` rejects duplicate claim/evidence
IDs and unknown claim/evidence references, and returns tuples in a `CouncilResult`.
It does not detect contradictions semantically, assess source reliability or prove truth.
`disagreements_preserved` always returns `True`; it is not a contradiction detector.

`ProposedAction(id, agent_id, kind, description, risk_reviewed, approved_by_human)`
uses `READ_ONLY`, `EXTERNAL_WRITE` or `PHYSICAL`. `SafetyPolicy.evaluate` permits
an action declared `READ_ONLY`, denies `None` and all external/physical actions.
Caller-supplied flags and kinds are not authenticated authorization.
`SafetyDecision(verdict, reason)` includes the enum values `ALLOW`, `DENY`,
`SAFE_STOP`; the current policy never emits `SAFE_STOP`.
Frozen dataclasses do not provide runtime validation of field types or recursively
freeze arbitrary values a caller passes. Treat them as local application objects.

## Proposed envelope v1

Each persisted event has `schema_version`, `event_id`, `run_id`, `sequence`,
`occurred_at` (UTC), `actor_id`, `event_type`, `payload`, `payload_digest` and
`parent_event_ids`. The store assigns sequence numbers; agent timestamps cannot
establish ordering. All IDs are bounded strings scoped by tenant and run.
Payload digests identify artifacts, not factual correctness or source authenticity.

The ingestion boundary rejects unknown versions, duplicate conflicting IDs,
oversized payloads, non-finite numbers and invalid references. Repeated identical
event IDs are idempotent. Reject malformed events without promoting their content.
Schema migration creates a new representation with a link to the original.

## Proposed additional records

- `AgentPerspective`: identity, role, backend/model version, prompt digest,
  context/source manifest, declared dependencies, budget and output schema.
- `EvidenceRecord`: source URI/identifier, author, retrieved and published dates,
  content digest, locator, access/license restrictions and observation method.
- `ClaimRecord`: statement, evidence relationships, assumptions, domain, units,
  scope, validity interval, status and uncertainty method where meaningful.
- `Contradiction`: linked claims, disputed proposition, scope compatibility,
  supporting challenge IDs, resolution status and resolution rationale.
- `ChallengeRecord`: target, proposed falsifier, method, result and limitations.
- `Report`: all accepted record IDs, unresolved issues, missing perspectives,
  synthesis, reproducibility manifest and proposed next steps.

Proposed claim statuses: `proposed`, `supported_in_scope`, `contested`,
`refuted_in_scope`, `withdrawn`, `superseded`. None means globally verified truth.
Retractions append new events; published history is not rewritten silently.

## Proposed adapter boundaries

`PerspectiveAdapter.run(question, source_manifest, budget) -> PerspectiveOutput`
returns structured claims and references, with raw-output artifact pointers.
`RuntimeAdapter.start/resume/cancel` drives the protocol and emits normalized
events. `KnowledgeStore.append/get/query` enforces tenant and source permissions.
`PolicyClient.evaluate(proposal) -> decision` calls an independent authority.
`Executor.execute(proposal, grant)` is a separate trusted boundary, unavailable in alpha.

Adapters translate vendor objects at the edge; domain code must not import vendor
SDKs. Contract tests must cover partial results, cancellation, event ordering,
schema errors, timeouts, authorization failure and replay after restart.

## Proposed action grant

An authenticated proposal binds actor, tenant, tool/version, exact argument
digest, resource, data classification, cost cap, expiry and idempotency key.
A grant binds the same values plus issuer, policy version, audience and nonce.
The executor validates signature, expiry, revocation and single-use constraints
at execution time. Changing arguments requires a fresh decision. A human approval
record binds a concrete proposal; an agent cannot assert its own approval.

Remote model requests and remote QPU submissions are both external effects.
They need explicit data and cost permission even if the mathematical task is
described as read-only. Never encode paid computation as an unrestricted local read.
