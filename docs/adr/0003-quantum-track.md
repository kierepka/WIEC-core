# ADR-0003: Quantum as an optional, evidence-producing research track

Status: Proposed, 2026-11-25.

## Context

The project should include quantum knowledge and a path to future quantum-assisted
computation without implying current hardware access or unmeasured benefits.

## Proposed decision

Keep quantum foundations and annotated primary sources in the repository. Define
provider-neutral problem/job/result records. Start with trusted local simulation,
then baseline comparisons; remote jobs require independent data/cost authorization.
Defer quantum-native memory/network agents until explicit resource semantics exist.

## Alternatives and consequences

Excluding quantum loses a legitimate research direction. Requiring a QPU in the
core prevents offline development and creates unjustified operational dependencies.
An optional track keeps the classical product usable while allowing falsifiable
experiments, at the cost of separate adapter and provenance work.

## Validation gate

Use [Q0–Q4](../quantum/EXPERIMENTS.md). No hardware or quantum-advantage claim before
artifacts, baselines, full costs and review meet the relevant gate. A QPU result
has no special authorization authority. No provider is connected by this ADR.
