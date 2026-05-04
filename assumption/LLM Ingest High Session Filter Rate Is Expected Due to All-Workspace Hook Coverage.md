---
type: assumption
status: active
confidence: medium
source: "note/Alfred System Status Audit April 21 2026"
source_date: "2026-04-21"
project:
  - "[[project/Alfred]]"
based_on:
  - "[[note/Alfred System Status Audit April 21 2026]]"
  - "[[assumption/claude_code_hook Fires for All Claude Code Sessions Including Home-Directory Workspaces]]"
confirmed_by: []
challenged_by: []
invalidated_by: []
related:
  - "[[assumption/Short Claude Code Sessions Are Low-Value and Safe to Skip]]"
created: "2026-05-04"
tags: []
---

# LLM Ingest High Session Filter Rate Is Expected Due to All-Workspace Hook Coverage

## Claim

The ~90% session filter rate observed in LLM Ingest (199 too-short, 22 unchanged, 0 ingested out of 221 checked sessions across Apr 20–21 timer runs) is expected and correct — not evidence of a broken or miscalibrated pipeline.

## Basis

`alfred_code_hook` fires for **all** Claude Code sessions across all workspaces on the machine, including home-directory, one-off, and trivial sessions. Most of these are naturally short (< 3 human turns). Project-focused sessions that generate meaningful knowledge are a minority of total Claude Code activity. The 3-turn minimum is therefore filtering genuine noise, not relevant signal.

## Evidence Trail

- Apr 20 20:23, Apr 20 22:23, Apr 21 14:14 timer runs each returned: `0 ingested, 22 unchanged, 199 too short`
- `assumption/claude_code_hook Fires for All Claude Code Sessions Including Home-Directory Workspaces` confirmed: hook is not project-scoped
- The Apr 20 Hyprland screenshot session (<3 human turns) is a representative example of what the filter correctly excludes

## Impact

The filter rate should not trigger alarm or prompt lowering the 3-turn threshold. Investigation is only warranted if *known* meaningful project sessions consistently fall below the threshold — not if the aggregate filter rate is high.

![[assumption.base#Depends On This]]
![[assumption.base#Related]]
