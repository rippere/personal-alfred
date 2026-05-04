---
based_on:
- '[[constraint/Base Views Require _bases Directory]]'
challenged_by: []
confidence: high
confirmed_by: []
created: '2026-03-07'
invalidated_by: []
janitor_note: ''
name: Base Views Auto-Populate Via Dataview
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related:
- '[[assumption/Wikilinks in Frontmatter Enable Auto-Discovery]]'
source: Project record structure
source_date: '2026-03-06'
status: active
tags: []
type: assumption
---

# Base Views Auto-Populate Via Dataview

## Claim

The system assumes that base view embeds (e.g., `![[project.base#Assumptions]]`) will automatically discover and display related records through Dataview queries embedded in the base files, without requiring manual curation or explicit linking.

## Basis

All project templates include base view embeds for standard sections (Assumptions, Decisions, Constraints, Tasks, etc.). This pattern implies the system expects these sections to populate automatically based on record relationships.

## Evidence Trail

- **2026-03-06**: Project record structure uses base view embeds throughout
- **Related**: [[assumption/Wikilinks in Frontmatter Enable Auto-Discovery]] explains the discovery mechanism

## Impact

- Users can create records and link them via frontmatter without manually updating project pages
- The system depends on correct wikilink syntax in frontmatter for auto-discovery to work
- If base views fail, all record relationships become invisible to users browsing project pages

![[assumption.base#Depends On This]]
![[assumption.base#Related]]

---
![[assumption.base#Depends On This]]

![[assumption.base#Related]]
