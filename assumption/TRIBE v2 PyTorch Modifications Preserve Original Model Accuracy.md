---
type: assumption
status: active
confidence: medium
source: "Sprint 1 decision to fork TRIBE v2 for PyTorch 2.11.0 compatibility"
source_date: "2026-04-09"
project: ["[[project/Persuasion Observatory]]"]
based_on: ["[[decision/TRIBE v2 Forked and Modified for PyTorch 2.11.0 Compatibility]]"]
confirmed_by: []
challenged_by: []
invalidated_by: []
related: []
created: "2026-05-04"
tags: [tribe-v2, pytorch, accuracy, validation]
---

# TRIBE v2 PyTorch Modifications Preserve Original Model Accuracy

## Claim

The changes made to TRIBE v2 source code for PyTorch 2.11.0 compatibility did not alter model behaviour or degrade accuracy relative to the canonical release. The patched model produces functionally equivalent outputs.

## Basis

The modifications were limited to compatibility shims (API changes between PyTorch versions, not architectural changes). PyTorch version-to-version API changes for inference typically do not alter numerical outputs for the same model weights.

## Evidence Trail

- 2026-04-09: Fork created, modifications applied, model loaded successfully
- Accuracy not yet validated — Sprint 1 Week 2 human evaluation will provide the first empirical data point
- No diff review against canonical TRIBE v2 outputs documented yet

## Impact

Sprint 1 accuracy results are the primary evidence for whether this assumption holds. If accuracy is unexpectedly low, it may be impossible to distinguish between: (a) domain mismatch (fMRI stimuli → web content), (b) patch-induced model degradation, or (c) inherently low model accuracy on this task. This assumption must be confirmed before attributing any accuracy failure to domain mismatch alone.

![[assumption.base#Depends On This]]
![[assumption.base#Related]]
