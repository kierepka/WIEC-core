# Development and operations guide

## Current local development

Use Python 3.11 or newer and an isolated environment. From the repository root:

```bash
python -m venv .venv
# Activate the environment using your shell's standard activation command.
python -m pip install -e '.[dev]'
python -m pytest -q
python examples/basic_council.py
```

Current CI installs the package and runs pytest on Python 3.11. No model keys,
network requests or QPU account are needed by the example/tests. The alpha has
no server to deploy and no live Research Council command.

## Implementing the next milestone

1. Define versioned output/envelope schemas and validators from [contracts](CONTRACTS.md).
2. Add stored perspective fixtures and the bounded [Council protocol](RESEARCH_COUNCIL.md).
3. Implement artifact/event persistence and recorded replay.
4. Compare [ADK](integrations/GOOGLE_ADK.md) and [Microsoft](integrations/MICROSOFT.md)
   spikes against the same conformance cases; document the selection.
5. Introduce permitted model calls with provider/data/cost checks.
6. Keep external tool execution absent until independent enforcement is verified.

Each implementation change identifies its acceptance criteria, regression checks
and documentation updates. Do not add large SDKs as unconditional core dependencies.
Fixtures must not contain credentials, private source text or real approval tokens.

## Proposed operational controls

Track stage latency, model requests, repairs/retries, budget reserved/spent,
validation failures, missing perspectives, gateway denials and remote job states.
Logs use run/artifact IDs and redacted error categories. Raw prompts and source
content are restricted artifacts, not default telemetry. Define retention before
enabling logging in a hosted environment.

On provider outage, preserve partial artifacts and mark unavailable stages.
On suspected credential compromise, stop new dispatches, revoke affected access,
reconcile outstanding jobs/costs and document impact. On source correction,
append a correction event and identify dependent reports. Never rewrite a published
result as if it had originally used the corrected source.

## Release checklist

Run relevant tests, inspect the diff and license/attribution changes, check public
documentation links, state what is implemented versus proposed, and verify CI for
the exact published commit. Publish measured results only with artifacts and scope.
A tag/release must be created intentionally; a version string is not a GitHub Release.
