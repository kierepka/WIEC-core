# WIEC Core

**A safety-gated, evidence-first framework for collective agent reasoning.**

**WIEC — Wiec Inteligencji, Eksploracji i Ciekawości.**
English: **A Council of Intelligence, Exploration and Curiosity**.
The Polish word *wiec* evokes an assembly: many voices, shared inquiry and room
for disagreement. The acronym remains Polish in English materials.
[Name and Polish introduction](docs/START_PL.md).

> Status: experimental reference implementation, v0.1.0-alpha. Not production-safe.
> WIEC is a working name; trademark and domain clearance are not complete.

WIEC separates **reasoning** from **permission to act**. Multiple perspectives can
make claims, attach evidence, challenge one another, and retain unresolved
contradictions. Agreement is **not** proof. Proposed external actions require
authorization by a policy component outside the agent's control.

## Principles

1. **Non-harm as a governing design objective:** prioritize the welfare, dignity,
   and autonomy of others above the system's continuation or optimization.
2. **Fail closed for side effects:** no external action without an explicit grant.
3. **Epistemic humility:** provenance, uncertainty, disagreement and falsification
   are first-class data.
4. **Least privilege:** agents propose; independent policy authorizes.
5. **Safe stopping:** a stop must not itself increase harm.

**Safety caveat:** zero real-world harm cannot be guaranteed by software.
This prototype only demonstrates narrow, testable policy invariants; it does
not implement threat assessment, isolation, tamper resistance or physical safety.

## Architecture

```text
Question / Sources
       |
Perspective Agents (future adapters)
       |
Claims + Evidence + Challenges
       |
Contradiction-preserving Council
       |
ProposedAction
       |
Independent Safety Policy (prototype, in-process)
       |
Authorized tool execution (not implemented)
```

The future production architecture requires an out-of-process safety enforcement
boundary with capability tokens, sandboxing, immutable audit, human review,
and domain-specific safe states. An in-process Python class is **not** an
independent security boundary.

## Quick start

```bash
python -m pip install -e '.[dev]'
pytest
python examples/basic_council.py
```

Python 3.11+. No external model calls, network requests or credentials required.

## Documentation and research materials

Start with the [documentation index](docs/README.md),
[vision](docs/VISION.md), [architecture](docs/ARCHITECTURE.md),
[contracts](docs/CONTRACTS.md) and [Research Council protocol](docs/RESEARCH_COUNCIL.md).
The [agent constitution](docs/AGENT_CONSTITUTION.md),
[knowledge lifecycle](docs/KNOWLEDGE.md), [safety design](docs/SAFETY.md) and
[evaluation protocol](docs/EVALUATION.md) define the intended development boundaries.

Google ADK and Microsoft Agent Framework are priority runtime candidates;
LangGraph, OpenAI Agents SDK and CrewAI are documented alternatives.
See [integration strategy](docs/integrations/RUNTIMES.md).
These are integration designs, not implemented adapters.

The [quantum research track](docs/quantum/README.md) includes foundations, hybrid
architecture, simulator/QPU access options and baseline-controlled experiments.
The [annotated reading list](docs/research/READING_LIST.md) explains where each
source comes from, why it matters, how WIEC would use it and what it cannot prove.
[Traceability](docs/research/TRACEABILITY.md) connects sources to design decisions.
No quantum backend or provider account is connected, and no quantum advantage is claimed.

## Repository map

- `src/wiec/`: minimal typed domain model, council, and safety policy
- `tests/`: policy and epistemic invariants
- `examples/`: deterministic local demonstration
- `docs/ARCHITECTURE.md`: component boundaries and deployment target
- `docs/ROADMAP.md`: milestones, acceptance criteria and benchmarks
- `docs/adr/0001-core-boundaries.md`: initial architectural decision
- `SECURITY.md`: threat model and reporting guidance

## What this is / isn't

This **is** a small reference implementation to validate the vocabulary and
policy checks. It is **not** an operational multi-agent framework, independent
Safety Kernel, or a certified non-harm system. No LLM adapter, RAG, persistence,
tool execution, runtime orchestration or distributed isolation is present.

## Benchmark plan

Compare a single model, ordinary multi-agent consensus, and WIEC on:
- truth discovery (source-grounded correctness);
- false-belief resistance (misinformation and conflicting evidence);
- unsafe-action prevention (unauthorized tool invocation and prompt injection).

Publish datasets, uncertainty intervals, failure cases and ablations; never
claim superiority without reproducible evidence.

## License

Apache-2.0. See `LICENSE`. Trademark rights are not granted by the license.
