---
based_on:
- '[[session/PM CRM Initial Architecture Planning Session]]'
confidence: medium
created: '2026-05-04'
name: PM CRM Positions Leadership as Intelligence Consumer and PMs as Communication
  Data Source
project:
- '[[project/PM CRM]]'
source: PM CRM Initial Architecture Planning Session
source_date: '2026-04-05'
status: active
type: assumption
---

# PM CRM Positions Leadership as Intelligence Consumer and PMs as Communication Data Source

## Claim
PM CRM is designed so that leadership (VPs, COOs, CFOs) consumes AI-surfaced insights about their teams, while project managers are the source of the communications data being analysed. PMs do not primarily interact with the dashboard — they are the signal, not the audience.

## Basis
The architecture session framed the system as surfacing "insights to leadership." The pitch deck targets VP of Operations, Engineering Managers, and COO/CFO. The dashboard displays clarity scores and task metrics — metrics that make sense to leaders evaluating team performance, not to individual contributors managing their own work.

## Evidence Trail
- 2026-04-05: Architecture session explicitly frames output as "insights to leadership"
- 2026-04-05: Pitch deck visualization prompt targets non-technical executive buyers
- 2026-04-07: Dashboard built with status counts, task table, clarity scores — aggregate views suited to leadership

## Impact
If this assumption holds, the product's UX must prioritise aggregated team-level views over individual task management. Adding PM-facing features (personal task views, input forms, notification flows) would be scope creep. If wrong — if PMs are also primary users — the UX and feature set need to expand significantly, as there is currently no PM-facing input surface.

![[assumption.base#Depends On This]]
![[assumption.base#Related]]
