---
type: decision
status: final
confidence: high
source: "Hardware assessment during Sprint 1 environment setup"
source_date: "2026-04-09"
project: ["[[project/Persuasion Observatory]]"]
decided_by: ["[[person/Ben Rippere]]"]
approved_by: []
based_on: []
supports: []
challenged_by: []
session:
related: ["[[constraint/TRIBE v2 Requires Minimum 8GB GPU VRAM for Hardware-Accelerated Inference]]"]
created: "2026-05-04"
tags: [hardware, sprint-1, inference]
---

# CPU Inference for TRIBE v2 Sprint 1 Testing

## Context

During Sprint 1 environment setup on 2026-04-09, hardware assessment revealed the development machine has an RTX 3050 Ti with only 4GB VRAM (~666MB free at runtime). TRIBE v2 requires a minimum of 8GB GPU VRAM for hardware-accelerated inference.

## Options Considered

1. **GPU inference** — Not viable; RTX 3050 Ti has 4GB VRAM, well below the 8GB minimum
2. **CPU inference** — Slower but feasible for validation-scale testing (20-sample dataset)
3. **Cloud GPU (RunPod)** — Viable but premature before validating model accuracy

## Decision

Use CPU inference for all Sprint 1 testing. GPU or cloud deployment deferred until Sprint 1 validation confirms TRIBE v2 accuracy is acceptable (>70% target).

## Rationale

Sprint 1's sole purpose is technical validation on a small dataset (~20 samples). CPU inference is slow but sufficient at this scale. Paying for cloud GPU before confirming the model works would risk capital on an unvalidated approach. The architecture decision already established a local→cloud migration path contingent on paying users.

## Consequences

- Sprint 1 inference will be significantly slower than production targets
- If accuracy passes, the next hardware question is cloud GPU cost at scale (~$500/month)
- If CPU proves too slow even for validation, cloud GPU becomes the only path forward

![[decision.base#Based On]]
![[decision.base#Related]]
