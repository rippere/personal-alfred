---
approved_by: []
based_on:
- '[[assumption/Base Views Auto-Populate Via Dataview]]'
- '[[assumption/Wikilinks in Frontmatter Enable Auto-Discovery]]'
challenged_by: []
confidence: high
created: '2026-03-07'
decided_by: []
janitor_note: ''
name: Use Base View Embeds for Dynamic Sections
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related: []
session: null
source: Template and record design
source_date: '2026-03-06'
status: final
supports: []
tags: []
type: decision
---

# Use Base View Embeds for Dynamic Sections

## Context

The system needed a way to show related records on project, person, org, and other entity pages without manual maintenance. Options included: (1) manual lists updated by users, (2) Dataview queries embedded directly in each record, (3) Dataview queries defined once in base files and embedded via transclusion.

## Options Considered

1. **Manual curation** — Users maintain lists of related records manually
   - Simple, no technical complexity
   - High maintenance burden, prone to becoming stale

2. **Inline Dataview queries** — Each record contains its own Dataview queries
   - Full flexibility per record
   - Duplicates query logic across all records, hard to update

3. **Base view embeds** — Define queries once in `_bases/`, embed via `![[base#section]]`
   - DRY: queries defined once, used everywhere
   - Consistent: all records of same type show relationships the same way
   - Requires `_bases/` infrastructure

## Decision

Use base view embeds (`![[project.base#Assumptions]]`, etc.) for all dynamic sections showing related records.

## Rationale

- **Maintainability**: Query logic lives in one place, can be updated globally
- **Consistency**: All projects show relationships in the same format
- **Zero user friction**: Users never manually update related record sections
- **Scalability**: Works equally well for 10 records or 10,000 records

## Consequences

- Requires `_bases/` directory and base files for each record type
- System setup must initialize base views before records are useful
- Users must understand wikilink syntax in frontmatter for relationships to appear
- If base views break, all relationship visibility breaks across the entire vault

![[decision.base#Based On]]
![[decision.base#Related]]

---
![[decision.base#Based On]]

![[decision.base#Related]]
