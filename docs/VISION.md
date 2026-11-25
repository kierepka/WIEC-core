# Vision and product requirements

Status: proposed product direction, 2026-11-25.

## Problem and intended users

Researchers and developers need an inspectable path from sources to claims,
counterarguments and decisions. A fluent answer or unanimous panel is insufficient
evidence. WIEC's hypothesis is that explicit challenges and retained disagreement
can improve reasoning quality. This hypothesis has not yet been benchmarked.

WIEC is an epistemic and action-authorization layer over existing runtimes.
It does not require an agent to be an LLM: deterministic code, symbolic solvers,
ML models and future quantum-assisted components can contribute under the same
evidence obligations.

## First product: Research Council

Input: one bounded research question, a permitted source bundle, a time/cost
budget, and a policy profile. Output: a structured report with claims, source
references, challenges, unresolved contradictions, limitations and suggested
next experiments. The first milestone has no external action executor.

Required behavior:

1. Preserve each submitted position and its provenance.
2. Distinguish observation, source statement, inference and hypothesis.
3. Attempt falsification before synthesis; record unsuccessful attempts too.
4. Mark missing evidence and failed perspectives rather than silently omitting them.
5. Keep epistemic confidence separate from permission to act.
6. Enforce configured turn, token, time and spending bounds in trusted code.
7. Export a versioned report without embedding credentials or private source text.

## Acceptance and limits

M1 requires replayable recorded runs on 20 fixed questions, including conflicting
evidence, unknown references and an unavailable agent. Replay means reconstructing
from captured outputs; repeating a live model call need not produce identical text.
No fabricated citations or discarded opposing claims are allowed in these fixtures.
The 20 questions are a regression set, not proof of general reasoning superiority.

M2 introduces a separately enforced authorization gateway. M3 evaluates efficacy
with held-out data and appropriate baselines. Quantum work starts with local
simulators and explicit problem definitions; it cannot block the classical product.

Non-goals for this alpha: autonomous self-expansion, unrestricted web/tool access,
physical control, clinical or financial decision automation, consciousness claims,
universal knowledge, certified safety, and assumed quantum advantage.
