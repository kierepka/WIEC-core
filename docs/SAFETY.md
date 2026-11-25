# Safety architecture and threat model

Status: proposed M2 enforcement design. Current `SafetyPolicy` is an in-process
demonstration, bypassable by code with the same privileges. It does not control
network access, credentials or resource consumption.

## Assets and trust boundaries

Protect source confidentiality, report integrity, human approval records,
provider credentials, spending limits and controlled resources. Treat models,
agent plugins, retrieved text and generated code as untrusted. The orchestrator
enforces protocol/budgets; a separately administered gateway controls effects.

The intended flow is proposal -> authenticated policy service -> narrowly scoped
grant -> validating executor -> outcome/audit event. Agents have no direct path
to tool/provider credentials. The executor, policy service, credential broker and
their deployment controls are trusted components and must be reviewed as such.

## Threats and required tests

- Source injection: a paper tells an agent to upload files. Treat it as quoted
  data; test that no policy or capability changes occur.
- Forged approval: an agent sets `approved_by_human=True`. Require an authenticated
  approval bound to the exact proposal; reject caller-supplied assertions.
- Gateway bypass: a runtime tool calls a provider directly. Remove credentials
  and network routes from the agent environment; test direct access is denied.
- Replay and argument substitution: reuse a grant for a different payload.
  Bind nonce, argument digest, actor, audience, expiry and resource; reject reuse.
- Confused deputy: a cross-project request borrows a service's permissions.
  Enforce tenant/resource identity at both policy and execution boundaries.
- Budget exhaustion: retries and parallel jobs exceed a cap. Atomically reserve
  worst-case funds before dispatch, reconcile charges, and cap attempts globally.
- Evidence laundering: several agents repeat one unsupported citation. Retain
  source lineage and dependency information; do not count repetition as replication.
- Audit tampering: delete a denied action. Store events outside agent permissions;
  test tamper detection, restricted readers and redaction procedures.
- Provider ambiguity: request times out after dispatch. Reconcile with provider
  job identifiers before retrying; mark unknown outcomes explicitly.

## Failures and stopping

Missing policy service, invalid grants, unresolved authorization, unknown tool
versions or failed mandatory audit persistence deny new external execution.
Availability failure must not silently enable a fallback executor. Cancellation
stops new submissions; an already submitted remote task may continue and incur cost.
Polling/cancellation need narrow management permissions and bounded retries too.

Physical safe states depend on the device and context; cutting power is not a
universal safe stop. Physical execution is outside the project milestones here.
Human approval cannot waive configured non-negotiable constraints.

## Quantum-specific boundaries

A cloud simulator/QPU job is a remote submission: it can reveal data and incur
charges. Require destination, artifact digest, shot count, job count, data policy
and cost reservation. Calibration metadata and result provenance must survive
postprocessing. A QPU result cannot grant permissions or override safety rules.

## Release gate

Before claiming independent enforcement, demonstrate denied direct network access,
credential isolation, expired/replayed grant rejection, cross-tenant denial,
service-outage denial, bounded concurrent spend and restart reconciliation in a
documented deployment threat model. Unit tests alone do not establish this boundary.
