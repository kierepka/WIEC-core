# Evaluation and reproducibility

Status: proposed protocol; the eight existing unit tests are not this benchmark.

## Questions and baselines

Evaluate truth discovery, resistance to unsupported consensus and unauthorized
effect prevention separately. Compare a single agent, a same-budget ordinary
multi-agent consensus, WIEC without critic, and full WIEC. Add a classical solver
and optional quantum contributor only for explicitly computational tasks.
Hold model family, source access and total resource budgets comparable; report
unavoidable differences. More calls alone must not be labeled an architectural benefit.

## Dataset and adjudication

Version development, regression and held-out sets. Include contradictory sources,
missing evidence, retracted sources, misleading agreement, unsupported citations,
injection attempts and unavailable agents. Define expected source relationships
and acceptable uncertainty, not just one preferred wording. Independent adjudicators
should be blind to condition where feasible; resolve disagreements with recorded
criteria. Model-as-judge output is a measured proxy, not ground truth.

Start with 20 seeded regression questions as an engineering gate. Choose the size
of a later efficacy study using a preregistered effect size/power rationale. Do
not infer broad scientific superiority from those 20 cases.

## Metrics with explicit denominators

- Supported claim precision: supported material claims / all material claims.
- Evidence coverage: material claims with traceable evidence / material claims
  requiring evidence under the task rubric.
- Disagreement retention: retained material conflicting positions / annotated
  material conflicting positions in the source/agent outputs.
- Challenge utility: challenges that reveal an adjudicated error or limitation /
  evaluated challenges. Also report harmful/incorrect challenges.
- Unauthorized effect rate: executed forbidden effects / attempted forbidden effects.
  Report attempted count and zero-attempt cases; no attempts is not a 100% pass.
- Legitimate completion rate, abstention rate and incorrect blocking rate to expose
  a system that appears safe merely because it does nothing.
- Full cost, token use, wall time and failure/partial-run rate per question.

For zero denominators report `not_applicable`. Preregister primary outcomes,
sampling units, confidence-interval method and multiplicity handling. Analyze
paired conditions by question and clustered/repeated runs appropriately.
Separate statistical, source-quality and model uncertainties.

## Replay and release evidence

Keep question/source digests, code commit, SDK/model versions, prompts or their
permitted artifacts, seeds/settings, event sequence, raw outputs, validated records,
costs and adjudications. Recorded replay must rebuild the report without live
provider calls. Re-running stochastic models/QPUs is replication, not byte-identical replay.

Current CI tests application behavior and single-agent portability contracts with
real optional SDK hosts. Full Council protocol tests remain in M1;
M2 adds gateway/outage/bypass tests; M3 publishes benchmark artifacts and limitations.
Quantum experiments have [separate acceptance and advantage gates](quantum/EXPERIMENTS.md).
