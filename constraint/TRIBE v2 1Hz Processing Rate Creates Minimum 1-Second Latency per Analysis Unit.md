---
type: constraint
status: active
source: "TRIBE v2 fMRI model design — 1Hz temporal resolution inherited from fMRI acquisition rate"
source_date: "2026-04-09"
authority: "TRIBE v2 model architecture (Meta Research)"
project: ["[[project/Persuasion Observatory]]"]
location: []
related: ["[[decision/Persuasion-Observatory-Architecture]]"]
created: "2026-05-04"
tags: [latency, tribe-v2, performance]
---

# TRIBE v2 1Hz Processing Rate Creates Minimum 1-Second Latency per Analysis Unit

## Constraint

TRIBE v2 operates at 1Hz temporal resolution (1 sample per second), inherited from the fMRI acquisition rate it was trained on. Each discrete analysis unit requires at least 1 second of processing time, independent of hardware speed.

## Source

TRIBE v2 was designed to predict fMRI brain activity, where the BOLD signal is sampled at 1Hz (one volume per second). The model architecture encodes this temporal resolution as a structural constraint, not a performance limitation.

## Implications

- Real-time, sub-second analysis of web content is not possible with TRIBE v2 as designed
- For the browser extension, this means: analysis cannot be instantaneous on page load
- The backend API approach (premium tier) can pipeline and batch analyses, partially masking latency
- The local pattern library (80–90% coverage) is latency-free and designed to handle the majority of cases precisely because of this constraint
- Streaming video analysis (YouTube) would require chunking into 1-second windows

## Expiry / Review

This constraint is structural to TRIBE v2's architecture and will not change without model replacement. Review if/when a faster brain encoding model becomes available.

![[constraint.base#Affected Projects]]
![[constraint.base#Related]]
