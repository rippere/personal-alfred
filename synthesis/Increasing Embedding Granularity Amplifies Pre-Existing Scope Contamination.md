---
type: synthesis
status: draft
confidence: high
cluster_sources:
  - "[[note/Alfred Surveyor Cluster Analysis Bug and Vault Node Audit April 21 2026]]"
project:
  - "[[project/Alfred]]"
supports: []
related:
  - "[[assumption/Surveyor Cluster Quality Will Become Meaningful After Removing inbox From Embedding Scope]]"
  - "[[_archived/constraint/Surveyor Embeds inbox/processed Files Inflating Embedding Count]]"
  - "[[decision/Fix Surveyor Embedding Contamination via ignore_dirs Config]]"
created: "2026-05-04"
tags: []
---

# Increasing Embedding Granularity Amplifies Pre-Existing Scope Contamination

## Insight

When Surveyor shifted from file-level to chunk-level embedding, a pre-existing inbox/processed contamination went from a minor nuisance to 70% of the total embedding index (1,303 of 1,863 chunks). The chunking strategy was architecturally correct but was implemented before the scope contamination was fixed — each contaminating file now contributes many chunks rather than one entry, inverting the signal-to-noise ratio.

## Evidence

- Pre-chunking: ~579 file-level embeddings; inbox contamination existed but at unknown/lower ratio
- Post-chunking: 9,319 total chunks — 1,303 of 1,863 indexed chunks (70%) from `inbox/processed/`
- Actual vault knowledge records: ~560 chunks from 455 real knowledge files
- Root cause confirmed April 21 2026 via direct Milvus query: all `unknown`-type entries traced to `inbox/processed/` raw session exports

## Implications

Data quality and scope problems must be fixed **before** implementing strategies that increase embedding granularity. A contaminating record that contributes 1 embedding at file level contributes N embeddings at chunk level — contamination scales with chunk density, not file count. Cluster quality degrades proportionally because noisy chunks dominate semantic groupings and OpenRouter labeling budget.

## Applicability

Any embedding pipeline adding chunking, sliding window, or other granularity increases. For Surveyor specifically: add `inbox` to `ignore_dirs` and do a full re-index before the chunked embedding count is considered meaningful.

![[synthesis.base#Sources]]
![[synthesis.base#Related]]
