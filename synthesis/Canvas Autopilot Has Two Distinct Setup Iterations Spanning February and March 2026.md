---
cluster_sources:
- '[[note/Canvas Autopilot Setup on Arch Linux]]'
- '[[note/Canvas Autopilot Project Scaffolding and Micromamba Setup]]'
- '[[session/Canvas Autopilot Environment Setup and Installation]]'
- '[[note/Canvas Autopilot Project Directory Structure and Setup]]'
confidence: medium
created: '2026-05-04'
name: Canvas Autopilot Has Two Distinct Setup Iterations Spanning February and March
  2026
project:
- '[[project/Canvas Autopilot]]'
related:
- '[[contradiction/emm warmup Completion vs System Never Run Assumptions]]'
- '[[assumption/Canvas Autopilot Scaffolded But Never Run]]'
- '[[assumption/Canvas Autopilot Installation Never Completed After Scaffolding]]'
status: active
supports:
- '[[assumption/emm warmup Completed Successfully on 2026-02-26]]'
- '[[assumption/emm sync Attempted on 2026-02-26 But Notion Databases Not Created]]'
type: synthesis
---

# Canvas Autopilot Has Two Distinct Setup Iterations Spanning February and March 2026

## Insight
Canvas Autopilot was set up at least twice using different approaches, which explains the conflicting records about installation method and whether the system was "ever run":

**Iteration 1 — 2026-02-26 (pipx):**
- `pipx install --editable /mnt/external/Projects/canvas-autopilot` succeeded
- Playwright/Chromium installed via the pipx venv's playwright binary
- Canvas API auth verified (returned user's name)
- `emm warmup` completed — Canvas Duo 2FA push + NotebookLM Google OAuth
- `emm sync` attempted but failed — Notion databases not created

**Iteration 2 — 2026-03-06 (micromamba):**
- Dedicated `canvas-autopilot` micromamba environment created (Python 3.11)
- All 17 source files scaffolded (or re-scaffolded)
- Dependencies installed via `micromamba run -n canvas-autopilot pip install -e .`
- Playwright Chromium installed in the micromamba env
- Configuration not completed — warmup/sync not run in this iteration

## Evidence
- note/Canvas Autopilot Setup on Arch Linux (2026-02-26): pipx install, warmup, sync attempt
- note/Canvas Autopilot Project Scaffolding and Micromamba Setup (2026-03-06): micromamba env, 17 files
- session/Canvas Autopilot Environment Setup and Installation (2026-03-06): same March session

## Implications
The March 2026 sessions may represent a fresh restart rather than continuation of the February work. The micromamba env and the pipx env are separate installations — the system may have two conflicting install paths. The "never run" assumptions apply specifically to the March micromamba installation; the February pipx installation was operational through warmup but stalled at sync.

## Applicability
Applies when resuming Canvas Autopilot setup: the correct environment to use (pipx vs micromamba) must be established before running `emm sync`. The pipx install has the most operational history (warmup completed).

![[synthesis.base#Sources]]
![[synthesis.base#Related]]
