# WIEC documentation

**WIEC — Wiec Inteligencji, Eksploracji i Ciekawości.**
English: **A Council of Intelligence, Exploration and Curiosity**.

This documentation describes the present prototype and a proposed development
architecture. A design document is not evidence that its components are implemented.
The only executable implementation is currently the small Python core in `src/wiec/`.

## Start here

- [Polski przewodnik i pochodzenie nazwy](START_PL.md)
- [Vision, requirements and boundaries](VISION.md)
- [Project glossary](GLOSSARY.md)
- [Architecture and implementation status](ARCHITECTURE.md)
- [Domain contracts and proposed interfaces](CONTRACTS.md)
- [Research Council protocol](RESEARCH_COUNCIL.md)
- [Agent constitution](AGENT_CONSTITUTION.md)
- [Knowledge, evidence and memory](KNOWLEDGE.md)
- [Safety architecture and threat model](SAFETY.md)
- [Runtime adapters: Google ADK, Microsoft and others](integrations/RUNTIMES.md)
- [Google ADK integration design](integrations/GOOGLE_ADK.md)
- [Microsoft Agent Framework integration design](integrations/MICROSOFT.md)
- [Quantum track: foundations, design, access and experiments](quantum/README.md)
- [Evaluation and reproducibility](EVALUATION.md)
- [Development and operations](DEVELOPMENT.md)
- [Governance and decisions](GOVERNANCE.md)
- [Delivery roadmap](ROADMAP.md)
- [Annotated research library: why each source is here](research/READING_LIST.md)
- [Scientific bibliography in BibTeX](research/references.bib)
- [Source-to-design traceability](research/TRACEABILITY.md)
- [Experiment template](templates/EXPERIMENT.md)
- [Source review template](templates/SOURCE_REVIEW.md)
- [Architecture decisions](adr/0001-core-boundaries.md)

## Status vocabulary

**Implemented** means present in source and backed by identified tests.
**Proposed** means a design to implement and evaluate, not a public API guarantee.
**Research** means an open question with a falsifiable experiment.
**Deferred** means no implementation commitment or date.

Vendor and research links were reviewed on 2026-11-25. Availability, APIs and plans
must be checked again when an adapter is implemented or a paid job is considered.
