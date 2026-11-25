# Contributing

Open an issue describing the hypothesis, risk and acceptance test before
major changes. Changes to safety behavior require regression tests and review
by someone other than the author. Never add an external tool executor that
bypasses policy enforcement. Record architectural decisions in `docs/adr/`.

Start with the [development guide](docs/DEVELOPMENT.md) and
[governance](docs/GOVERNANCE.md). Proposed APIs and quantum/runtime integrations
must be marked as proposed until implementation and conformance checks exist.
Use the [experiment](docs/templates/EXPERIMENT.md) and
[source-review](docs/templates/SOURCE_REVIEW.md) templates for research contributions.
Link primary sources and add short original annotations; do not copy full papers
or introduce private data/credentials into public fixtures. Preserve failures and
negative results alongside successful experiments.
