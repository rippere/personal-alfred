---
type: decision
status: final
confidence: high
source: "Sprint 1 environment setup — dependency compatibility failure"
source_date: "2026-04-09"
project: ["[[project/Persuasion Observatory]]"]
decided_by: ["[[person/Ben Rippere]]"]
approved_by: []
based_on: []
supports: []
challenged_by: []
session:
related: ["[[assumption/TRIBE v2 PyTorch Modifications Preserve Original Model Accuracy]]"]
created: "2026-05-04"
tags: [sprint-1, pytorch, compatibility, tribe-v2]
---

# TRIBE v2 Forked and Modified for PyTorch 2.11.0 Compatibility

## Context

TRIBE v2 as released did not run against PyTorch 2.11.0 (required by the Python 3.14.3 environment). Compatibility failures surfaced during Sprint 1 setup on 2026-04-09.

## Options Considered

1. **Downgrade PyTorch** — Would require matching the exact Python + CUDA version TRIBE v2 was tested on; high environment complexity
2. **Fork and patch TRIBE v2** — Modify the TRIBE v2 source to run under PyTorch 2.11.0; preserves current environment
3. **Wait for upstream fix** — No upstream fix timeline available; blocks sprint

## Decision

Fork TRIBE v2 and apply modifications necessary for PyTorch 2.11.0 compatibility. Run against the patched version for all Sprint 1 testing.

## Rationale

The project already runs PyTorch 2.11.0 + CUDA 13.0 as part of a working environment. Downgrading to match TRIBE v2's original requirements would create a more fragile setup and conflict with other dependencies.

## Consequences

- Sprint 1 accuracy results are measured against the patched model, not the canonical release
- Any divergence between patched and canonical behaviour is undetected until validated against ground truth
- The fork creates a maintenance burden: upstream TRIBE v2 updates require re-applying patches
- If the model later fails accuracy targets, a confound exists: domain mismatch vs. patch degradation

![[decision.base#Based On]]
![[decision.base#Related]]
