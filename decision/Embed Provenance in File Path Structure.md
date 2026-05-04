---
approved_by: []
based_on: []
challenged_by: []
confidence: high
created: '2026-03-07'
decided_by: []
janitor_note: ''
name: Embed Provenance in File Path Structure
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related: []
session: ''
source: Start Here guide
source_date: '2026-03-06'
status: final
supports: []
tags: []
type: decision
---

# Embed Provenance in File Path Structure

## Context

The system needed a way to track who created what work and when. Options included: (1) provenance only in frontmatter metadata, (2) manual tagging of authorship, (3) embedding provenance in the file path structure itself.

## Options Considered

1. **Frontmatter only** — Store authorship in `created_by:` field
2. **Manual tagging** — Users tag their own work
3. **Path structure** — Embed date and author directly in folder hierarchy

## Decision

Use path structure to embed provenance: `YYYY/MM/DD/{person}/HHMM_session-name/`. The path itself answers "who did this work and when."

## Rationale

From [[Start Here]]:

> "Provenance is built into the path — you always know who created what and when."

The file system becomes a self-documenting timeline. Human work and Alfred work are separated by folder (alice/ vs alfred/). Date hierarchy provides temporal organization. No metadata lookup required to know authorship.

## Consequences

- **Benefit**: Provenance is instantly visible from file path alone
- **Benefit**: Separates human and AI work streams for clarity
- **Benefit**: Date-based folder structure enables temporal analysis
- **Constraint**: Session folders must be created in the correct location or provenance is lost
- **Constraint**: Users cannot move session folders without breaking provenance

![[decision.base#Based On]]
![[decision.base#Related]]

---
![[decision.base#Based On]]

![[decision.base#Related]]
