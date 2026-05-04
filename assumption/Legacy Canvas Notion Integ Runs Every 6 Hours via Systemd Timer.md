---
based_on:
- '[[note/Canvas Autopilot Project Summary]]'
confidence: medium
created: '2026-05-04'
name: Legacy Canvas Notion Integ Runs Every 6 Hours via Systemd Timer
project:
- '[[project/Canvas Autopilot]]'
related:
- '[[assumption/Canvas Autopilot Will Replace Legacy Canvas Notion Integ System]]'
- '[[decision/Maintain Legacy Canvas Notion Integ During New System Development]]'
source: note/Canvas Autopilot Project Summary
source_date: '2026-03-13'
status: active
type: assumption
---

# Legacy Canvas Notion Integ Runs Every 6 Hours via Systemd Timer

## Claim
The legacy Canvas Notion Integ system runs continuously via a systemd timer on a 6-hour interval. Logs confirmed activity as of 2026-03-13, meaning it was still actively syncing Canvas data to Notion while Canvas Autopilot development was ongoing.

## Basis
From note/Canvas Autopilot Project Summary: "older Canvas Notion Integ continues running via systemd timer (logs show activity as of 2026-03-13)."

## Evidence Trail
- 2026-03-13: Systemd timer logs show active execution, confirming the legacy system is still running

## Impact
Canvas data is actively being synced to Notion via the legacy system even while Canvas Autopilot is being developed. If Canvas Autopilot's first sync creates duplicate Notion databases, it may conflict with or shadow existing data from the legacy timer. Transition planning should account for the running legacy system.

![[assumption.base#Depends On This]]
![[assumption.base#Related]]
