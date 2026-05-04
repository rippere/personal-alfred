---
based_on:
- '[[Start Here]]'
challenged_by: []
confidence: high
confirmed_by: []
created: '2026-03-07'
invalidated_by: []
janitor_note: ''
name: Session Tracking Must Be Automatic Not Manual
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related: []
source: Start Here guide
source_date: '2026-03-06'
status: active
tags: []
type: assumption
---

# Session Tracking Must Be Automatic Not Manual

## Claim

The Alfred OS architecture assumes that session tracking MUST be fully automated. Users do not start or stop sessions manually. The session tracker worker detects bounded work periods from activity signals (chats, task completions, file changes, meetings) and creates session records automatically.

## Basis

**From [[Start Here]]:**

> "You don't manually start or stop sessions. A session tracker worker runs periodically and automatically detects bounded work periods from your activity."

This is presented as the only supported mode. No manual session commands are mentioned or offered as an alternative.

## Evidence Trail

- **2026-03-06**: Start Here guide explicitly states sessions are automatic, with no mention of manual controls

## Impact

- Session detection logic must be reliable and comprehensive - missing sessions = lost work provenance
- Users cannot override session boundaries or correct mis-detected sessions
- All activity signals (chats, file changes, meetings, task completions) must be reliably captured
- Session tracker must run frequently enough to avoid losing context

![[assumption.base#Depends On This]]
![[assumption.base#Related]]

---
![[assumption.base#Depends On This]]

![[assumption.base#Related]]
