---
type: constraint
status: active
source: "TRIBE v2 model architecture requirements — discovered during Sprint 1 setup 2026-04-09"
source_date: "2026-04-09"
authority: "TRIBE v2 model design (Meta Research)"
project: ["[[project/Persuasion Observatory]]"]
location: []
related: ["[[decision/CPU Inference for TRIBE v2 Sprint 1 Testing]]"]
created: "2026-05-04"
tags: [hardware, tribe-v2, gpu]
---

# TRIBE v2 Requires Minimum 8GB GPU VRAM for Hardware-Accelerated Inference

## Constraint

TRIBE v2 requires a minimum of 8GB GPU VRAM for hardware-accelerated inference. The development hardware (RTX 3050 Ti) has only 4GB total VRAM, with approximately 666MB free at runtime — well below the minimum.

## Source

Discovered empirically during Sprint 1 environment setup on 2026-04-09. The RTX 3050 Ti 4GB could not load the full model weights (~1GB for LLaMA 3.2-3B + V-JEPA2 + Wav2Vec-BERT) into VRAM alongside CUDA runtime overhead.

## Implications

- GPU inference is not possible on the development machine
- CPU inference is required for all local development and Sprint 1 testing
- Production deployment will require cloud GPU (RunPod or equivalent) with ≥8GB VRAM
- The architecture decision already budgets ~$500/month for cloud GPU at scale

## Expiry / Review

This constraint applies until either: (a) hardware is upgraded to a GPU with ≥8GB VRAM, or (b) the project migrates fully to cloud GPU infrastructure. Review at Sprint 5 when cloud GPU deployment is planned.

![[constraint.base#Affected Projects]]
![[constraint.base#Related]]
