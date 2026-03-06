---
approved_by: []
based_on:
- '[[Start Here]]'
challenged_by: []
confidence: high
created: '2026-03-06'
decided_by: []
janitor_note: LINK001 — Base view embeds reference missing _bases/ directory. System
  must create _bases/ with base view definitions. ORPHAN001 — Foundational decision,
  no inbound links expected.
name: Separate Human and Alfred Work into Different Folders
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

# Separate Human and Alfred Work into Different Folders

## Context

Session outputs need to be organized by date and by who performed the work. The system needed a folder structure that preserves provenance.

## Options Considered

1. **Single session folder per day** — all work in one folder regardless of who did it
2. **Per-person folders under date** — separate folders for each person (including Alfred) under each date
3. **Per-person folders at root** — organize by person first, then by date

## Decision

Sessions are organized as `YYYY/MM/DD/{person}/HHMM_session-name/`. Human work goes in the person's folder, Alfred work goes in `alfred/`. This is shown in the file structure: "Human work goes in the person's folder, Alfred work goes in Alfred's folder."

## Rationale

The guide states: "Provenance is built into the path — you always know who created what and when." Separating human and Alfred work at the folder level makes attribution explicit and immutable.

## Consequences

- Clear separation between human-authored and AI-authored work
- Folder path encodes both temporal and attribution metadata
- Easy to filter or search by who did the work
- Cannot easily show "all work on a project today" without traversing multiple folders

---
![[decision.base#Based On]]

![[decision.base#Related]]
