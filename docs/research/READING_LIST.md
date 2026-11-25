# Annotated source library: where, why and how

Reviewed: 2026-11-25. These are references and original short annotations, not
redistributed papers. Read the full source before implementing a technical result.
arXiv is a repository, not itself a peer-review guarantee. Record exact versions,
corrections and publication links when creating source records.
The seven algorithm/review papers also have [BibTeX entries](references.bib).

## QI-01 — Quantum states and measurements

**Origin:** [IBM Quantum Learning, quantum information](https://quantum.cloud.ibm.com/learning/en/courses/basics-of-quantum-information/single-systems/quantum-information).
**Contribution:** introduces state vectors and measurement probabilities.
**Why WIEC:** establishes that a measured classical result is not a readable list
of all amplitudes. **Use:** Q0 preparation/basis records and contributor onboarding.
**Limit:** educational theory is not evidence that WIEC has a quantum device.

## QI-02 — Limitations on quantum information

**Origin:** [IBM Quantum Learning](https://quantum.cloud.ibm.com/learning/en/courses/basics-of-quantum-information/quantum-circuits/limitations-on-quantum-information).
**Contribution:** explains no-cloning and state-discrimination limitations.
**Why WIEC:** prevents designing classical “backups” of unknown physical states.
**Use:** separate circuit descriptions, measured artifacts and physical resources.
**Limit:** does not prohibit copying classical records or re-preparing known states.

## QI-03 — Teleportation

**Origin:** [IBM Quantum Learning, teleportation](https://quantum.cloud.ibm.com/learning/en/courses/basics-of-quantum-information/entanglement-in-action/quantum-teleportation).
**Contribution:** a protocol using entanglement and classical communication.
**Why WIEC:** constrains speculative distributed quantum-agent designs.
**Use:** explain why a future quantum network would need explicit resources and
classical messaging. **Limit:** no instantaneous shared knowledge or transported matter.

## QA-01 — Grover (1996)

**Origin:** Lov K. Grover, [A fast quantum mechanical algorithm for database search](https://arxiv.org/abs/quant-ph/9605043).
**Contribution:** quadratic improvement in an unstructured oracle-search setting.
**Why WIEC:** teaches how to scope an algorithmic advantage claim.
**Use:** demand explicit oracle, data-loading and output assumptions before a search
adapter proposal. **Limit:** not an automatic acceleration of web search, RAG or LLMs.

## QA-02 — Shor (1994/1997)

**Origin:** Peter W. Shor, [Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer](https://arxiv.org/abs/quant-ph/9508027).
**Contribution:** efficient quantum algorithms for specific algebraic problems.
**Why WIEC:** separates a precise theoretical result from generic acceleration stories.
**Use:** contributor background and resource-assumption reviews.
**Limit:** no claim that these algorithms run at useful scale in this repository.

## QA-03 — VQE, Peruzzo et al. (2014)

**Origin:** [A variational eigenvalue solver on a quantum processor](https://arxiv.org/abs/1304.3061), Nature Communications 5, 4213.
**Contribution:** a hybrid eigenvalue-estimation approach with a small photonic demonstration.
**Why WIEC:** gives a concrete pattern for classical optimization plus quantum measurements.
**Use:** Q2 Hamiltonian experiment and result provenance.
**Limit:** an experimental demonstration is not general computational advantage or
validation of arbitrary chemistry applications.

## QA-04 — QAOA, Farhi, Goldstone and Gutmann (2014)

**Origin:** [A Quantum Approximate Optimization Algorithm](https://arxiv.org/abs/1411.4028).
**Contribution:** parameterized circuits for approximate combinatorial optimization.
**Why WIEC:** supplies a bounded, checkable candidate workload.
**Use:** Q1 MaxCut comparison with exact/heuristic classical methods.
**Limit:** no general promise of practical speedup; depth, optimization and sampling
are part of the experiment, not costs to hide.

## QA-05 — Variational algorithms, Cerezo et al. (2021)

**Origin:** [Variational Quantum Algorithms](https://arxiv.org/abs/2012.09265), Nature Reviews Physics 3, 625–644.
**Contribution:** surveys hybrid variational methods and trainability, accuracy and
efficiency challenges. **Why WIEC:** identifies failure modes to record rather
than treating optimization failure as an implementation detail.
**Use:** evaluation budgets, optimizer histories and uncertainty reporting.
**Limit:** a review outlines prospects; it does not establish WIEC's utility.

## QA-06 — Barren plateaus, McClean et al. (2018)

**Origin:** [Barren plateaus in quantum neural network training landscapes](https://arxiv.org/abs/1803.11173), Nature Communications 9, 4812.
**Contribution:** identifies exponentially suppressed gradients for specified
parameterized-circuit settings. **Why WIEC:** prevents assuming larger circuits
train more effectively. **Use:** ansatz/initialization review and scaling checks.
**Limit:** the result's assumptions matter; it is not a no-go theorem for all models.

## QA-07 — Quantum ML limits, Ciliberto et al. (2018)

**Origin:** [Quantum machine learning: a classical perspective](https://arxiv.org/abs/1707.08561), Proceedings of the Royal Society A.
**Contribution:** reviews quantum ML in comparison with classical methods, including
input assumptions. **Why WIEC:** evidence quality requires fair baselines and full
data costs. **Use:** reject proposals that omit classical data encoding or compare
only against a weak baseline. **Limit:** not a current hardware/provider survey.

## Runtime primary documentation

- **RT-01 Google ADK:** [workflows](https://adk.dev/workflows/),
  [sessions](https://adk.dev/sessions/), [safety](https://adk.dev/safety/),
  [evaluation](https://adk.dev/evaluate/). Use for workflow/state mapping and adapter
  tests; SDK capabilities do not establish WIEC's evidence quality or isolation.
- **RT-02 Microsoft Agent Framework:** [overview](https://learn.microsoft.com/en-us/agent-framework/overview),
  [workflows](https://learn.microsoft.com/agent-framework/concepts/workflows/).
  Use for a second conformance spike; verify version and language-specific behavior.
- **RT-03 LangGraph:** [overview](https://docs.langchain.com/oss/python/langgraph/overview).
  Use for graph/checkpoint design and a control implementation, not assumed compatibility.
- **RT-04 OpenAI Agents SDK:** [overview](https://openai.github.io/openai-agents-python/),
  [guardrails](https://openai.github.io/openai-agents-python/guardrails/).
  Use for bounded specialist calls and scope-aware effect checks.
- **RT-05 CrewAI:** [introduction](https://docs.crewai.com/en/introduction).
  Use as a role/workflow candidate; preserve original claims before synthesis.
- **RT-06 AutoGen:** [official archival notice](https://microsoft.github.io/autogen/stable/).
  Use for historical context and migration, not a new default dependency.

## Source admission policy

Prefer original papers, official vendor documentation and reproducible artifacts.
Record a specific claim, locator, version and limitations, not just a title.
Vendor documentation supports a capability description; a paper supports a scoped
scientific argument. Neither is evidence of a successful WIEC integration.
Use the [review template](../templates/SOURCE_REVIEW.md) before promoting sources
into a future knowledge corpus. No full paper downloads, embeddings or RAG index
are created by this documentation change.
