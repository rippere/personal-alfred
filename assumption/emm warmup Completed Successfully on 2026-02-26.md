---
confidence: high
confirmed_by:
- '[[note/Canvas Autopilot Setup on Arch Linux]]'
created: '2026-05-04'
name: emm warmup Completed Successfully on 2026-02-26
project:
- '[[project/Canvas Autopilot]]'
related:
- '[[contradiction/emm warmup Completion vs System Never Run Assumptions]]'
- '[[assumption/Canvas Autopilot Scaffolded But Never Run]]'
- '[[assumption/Canvas Autopilot Installation Never Completed After Scaffolding]]'
source: note/Canvas Autopilot Setup on Arch Linux
source_date: '2026-02-26'
status: confirmed
type: assumption
---

# emm warmup Completed Successfully on 2026-02-26

## Claim
The `emm warmup` command was run and completed successfully on 2026-02-26, predating the March 2026 re-scaffolding sessions. Canvas Duo 2FA push was completed interactively, NotebookLM Google OAuth was completed, and persistent browser sessions were saved to disk automatically on browser close.

## Basis
Documented in note/Canvas Autopilot Setup on Arch Linux (2026-02-26): "Ran `emm warmup` to establish persistent browser sessions: 1. Logged into Canvas (completed Duo 2FA push) 2. Logged into NotebookLM with Google account 3. Sessions saved automatically on browser close."

## Evidence Trail
- 2026-02-26: emm warmup confirmed completed — both Canvas and NotebookLM auth flows executed

## Impact
Directly challenges the assumptions that Canvas Autopilot was "never run" or "never executed." The warmup and authentication flows were operational as of February 2026, roughly 8 days before the March 2026 micromamba re-scaffolding sessions. The project has more operational history than the March sessions alone suggest.

![[assumption.base#Depends On This]]
![[assumption.base#Related]]
