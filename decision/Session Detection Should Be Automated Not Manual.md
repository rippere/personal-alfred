---
approved_by: []
based_on:
- '[[Start Here]]'
challenged_by: []
confidence: high
created: '2026-03-06'
decided_by: []
janitor_note: LINK001 — Base view embeds reference missing _bases/ directory. System
  must create _bases/ with base view definitions.
name: Session Detection Should Be Automated Not Manual
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related: []
session: null
source: Start Here.md documentation
source_date: '2026-03-06'
status: final
supports: []
tags: []
type: decision
---

# Session Detection Should Be Automated Not Manual

## Context

The system needed a way to capture work periods and their outputs. Manual session tracking (start/stop commands) would create friction and gaps in the record.

## Options Considered

1. **Manual session tracking** — users explicitly start and stop sessions
2. **Automated session detection** — a background worker detects bounded work periods from activity signals

## Decision

Session tracking is fully automated. A session tracker worker runs periodically and detects work periods from activity: chats, task completions, file changes, meetings. No manual start/stop required.

## Rationale

The Start Here guide explicitly states: "You don't manually start or stop sessions. A session tracker worker runs periodically and automatically detects bounded work periods from your activity." This reflects a design decision to prioritize zero-friction capture over user control.

## Consequences

- Users have no direct control over when sessions start or stop
- Session boundaries are inferred from activity patterns, which may not always align with user intent
- No context switching or interruption to the user's flow
- Complete provenance capture without requiring user discipline

---
![[decision.base#Based On]]

![[decision.base#Related]]
