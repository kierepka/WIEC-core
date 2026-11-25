# Knowledge, evidence and memory

Status: proposed design; the alpha stores only in-memory objects supplied by callers.

## Three stores with different authority

The source registry tracks documents, datasets and experimental artifacts.
The epistemic graph tracks claims, support, challenges and contradictions.
The execution ledger tracks proposals, policy decisions, costs and outcomes.
A conversation summary or vector search hit cannot substitute for any of these.
The future world model (sometimes called World Kernel) is a versioned view over
scoped claims, not a central oracle or a source of action permissions.

## Ingestion and retrieval

Record origin, source version, retrieval time, content digest, license, permitted
audience, language and exact locator. Retain excerpts only when permissions allow;
an open-access paper is not automatically permission to redistribute its full text.
Keep source text separate from agent instructions. Redact secrets before indexing.

Chunking and embeddings are replaceable indexes over permitted source records.
Retrieval returns record IDs, locators and scores, followed by access checks.
A similarity score is not evidence quality. Deduplicate shared sources so three
agents citing the same paper do not appear to provide three independent results.

## Evidence lifecycle

`registered -> reviewed -> cited`; later `corrected`, `superseded` or `retracted`
events preserve the earlier context. Each derived claim records the exact source
version. A correction flags downstream claims for re-evaluation; it does not
silently rewrite an existing report. Keep observation time distinct from retrieval time.

Use supported/refuted *in a defined scope*. For an empirical claim, specify
population, measurement procedure and uncertainty. For a theorem, specify
assumptions and reference. For a simulation, specify model, seed and numerical
settings. Avoid a universal 0-to-1 truth score without a calibration protocol.

## Quantum knowledge and artifacts

Distinguish a paper about quantum theory, a classical simulation of a circuit,
a hardware measurement, a resource estimate and a research hypothesis. These are
different evidence types. Store experiment and backend metadata alongside
counts, observables, statistical intervals and baseline results.
Classical knowledge storage does not preserve an unknown physical quantum state.
See [quantum foundations](quantum/FOUNDATIONS.md) and
[quantum contracts](quantum/ARCHITECTURE.md).

## Retention and privacy

Partition by project/tenant; apply access checks before retrieval and export.
Do not share private source bundles across providers by default. Separate public
artifact hashes from restricted content. Define retention and deletion before
collecting personal data. Auditability must allow redaction/tombstones where
required; never promise both unconditional deletion and permanently readable logs.
