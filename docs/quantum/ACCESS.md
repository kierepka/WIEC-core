# Access to quantum computation

Status: documented access paths checked 2026-11-25, **not verified account access**.
WIEC has no configured quantum provider, account entitlement, credit balance or
live device connection. Published availability is not a promise for this project.

## Stage 1: local simulation

Start with a bounded classical simulator. Cirq exposes circuit simulation and
sampling; PennyLane offers `default.qubit` and mixed-state simulation options.
Qiskit is another candidate ecosystem; select and pin one only in the simulator
adapter experiment. Simulating quantum circuits on a CPU/GPU is not QPU execution.
Memory/time limits depend on the circuit and simulation method, so do not advertise
a universal supported-qubit count.
[Cirq basics](https://quantumai.google/cirq/start/basics),
[PennyLane devices](https://docs.pennylane.ai/en/stable/code/qp_devices.html).

Local execution still needs bounded compute and safe code handling. The first
experiment should use trusted, reviewed circuits rather than executing arbitrary
model-generated programs.

## Stage 2: IBM Quantum Platform

IBM documents an Open Plan and paid plans. An account, appropriate instance and
credentials are needed; access and consumption depend on the selected plan.
Verify current eligibility, instance/device entitlements and usage limits in the
account before planning a run. Free access does not imply unlimited usage or no queue.
Keep credentials in the trusted provider caller and explicitly select the permitted
instance/target rather than letting an agent choose paid fallback automatically.
[Plans overview](https://quantum.cloud.ibm.com/docs/en/guides/plans-overview),
[instances](https://quantum.cloud.ibm.com/docs/en/guides/instances).

## Stage 2 alternative: Azure Quantum

Azure Quantum provides a workspace-based route to provider hardware, simulation
and resource estimation. Account/workspace setup and enabled provider plans are
separate from Microsoft Agent Framework. Workspace provider visibility can depend
on billing country/region. Check provider terms, target capabilities and charges
for the actual workspace; do not assume every advertised device is enabled.
[Service overview](https://learn.microsoft.com/en-us/azure/quantum/overview-azure-quantum),
[provider configuration](https://learn.microsoft.com/en-us/azure/quantum/how-to-add-a-provider).

Resource estimation predicts requirements under specified assumptions; it is not
execution on the hypothetical future machine. Label it as an estimate in evidence.

## Stage 2 alternative: Amazon Braket

Braket offers local/managed simulation and access to several hardware technologies.
Use an AWS account with appropriate IAM permissions, region, storage and billing
controls. Remote tasks can queue; device status and access windows vary.
Provider QPU processing can involve third-party facilities. Verify data handling,
device properties, current price and quota before submitting.
[Service overview](https://docs.aws.amazon.com/braket/latest/developerguide/),
[task flow and processing](https://docs.aws.amazon.com/braket/latest/developerguide/braket-how-it-works.html),
[availability and queues](https://docs.aws.amazon.com/braket/latest/developerguide/braket-task-when.html).

## Other providers and access modes

Direct vendor accounts, institutional allocations and research programs can be
evaluated through the same adapter contract. Do not assume a free grant or hardware
access from installing an SDK. Google ADK and Cirq do not, by themselves, establish
this project's access to a Google QPU. Agent-provider access and QPU access are
independent configuration and authorization decisions.

## Access readiness record (complete before any remote run)

Record owner/project, provider, account/workspace/instance identifier, region,
allowed target, backend mode, entitlement confirmation time, price reference,
approved currency/cost bound, quota/queue snapshot, permitted data classification,
credential location, retention policy, approval/grant ID and cancellation behavior.
Store only non-secret identifiers. Unknown entries block automated remote dispatch.

Refresh device availability at preflight; a static list in a repository will age.
If a device disappears, return an explicit unavailable result. Do not silently
purchase another plan or submit to another provider. The current alpha denies
all such external execution.
