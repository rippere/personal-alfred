---
based_on:
- '[[note/Canvas Autopilot Setup on Arch Linux]]'
confidence: high
created: '2026-05-04'
name: emm sync Attempted on 2026-02-26 But Notion Databases Not Created
project:
- '[[project/Canvas Autopilot]]'
related:
- '[[assumption/emm warmup Completed Successfully on 2026-02-26]]'
- '[[assumption/Canvas Autopilot Scaffolded But Never Run]]'
- '[[assumption/Canvas Autopilot Installation Never Completed After Scaffolding]]'
source: note/Canvas Autopilot Setup on Arch Linux
source_date: '2026-02-26'
status: active
type: assumption
---

# emm sync Attempted on 2026-02-26 But Notion Databases Not Created

## Claim
The `emm sync` command was attempted on 2026-02-26 following a successful `emm warmup` run, but it did not complete successfully. Specifically, the Notion databases (Assignments, Exams, Course Materials) were never created within the Canvas Calendar parent page.

## Basis
Documented in note/Canvas Autopilot Setup on Arch Linux: "The Notion databases (Assignments, Exams, Course Materials) were **not yet created** within the parent page at session end. The `emm sync` command had not completed successfully."

## Evidence Trail
- 2026-02-26: emm warmup succeeded; emm sync attempted; Notion database creation failed
- Canvas API auth was verified working (returned user's name), so the failure was in the Notion sync layer, not Canvas auth

## Impact
The system's first sync attempt failed at the Notion database creation step. The Canvas API token was valid. The root failure was in the Notion integration layer — either Notion token permissions, parent page ID, or database schema creation logic. This is the last known state of the system before the March 2026 re-scaffolding sessions.

![[assumption.base#Depends On This]]
![[assumption.base#Related]]
