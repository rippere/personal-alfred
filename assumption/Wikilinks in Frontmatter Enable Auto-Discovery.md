---
based_on:
- '[[Start Here]]'
challenged_by: []
confidence: high
confirmed_by: []
created: '2026-03-06'
invalidated_by: []
janitor_note: LINK001 — Base view embeds reference missing _bases/ directory. ORPHAN001
  — Foundational assumption, no inbound links expected at this stage.
name: Wikilinks in Frontmatter Enable Auto-Discovery
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related: []
source: Start Here.md documentation
source_date: '2026-03-06'
status: active
tags: []
type: assumption
---

# Wikilinks in Frontmatter Enable Auto-Discovery

## Claim

The Alfred OS system assumes that all record relationships can be discovered automatically through wikilinks in frontmatter fields. This is the foundation for the "pages build themselves" pattern where base views use `file.hasLink(this.file)` to show connected records.

## Basis

The Start Here guide states: "Records link to each other via [[wikilinks]] in frontmatter. The graph connects everything." and "The filter is simple: *show me everything that links to this file.*" This reveals a core assumption that wikilink-based discovery is sufficient for all relationship modeling.

## Evidence Trail

- Start Here.md explicitly describes the pattern: create a task, link it to a project → it appears in the table automatically
- All base views rely on this pattern
- The system does not appear to use explicit relationship tables or foreign keys

## Impact

- All features that depend on showing "related records" rely on this assumption
- If wikilinks in frontmatter are insufficient (e.g., for many-to-many relationships, for computed relationships), the base view pattern breaks
- The `relationships:[]` field exists in templates but its purpose and relationship to wikilinks is unclear

---
![[assumption.base#Depends On This]]

![[assumption.base#Related]]
