---
cluster_sources:
- '[[decision/Use Base View Embeds for Dynamic Sections]]'
- '[[constraint/Base Views Require _bases Directory]]'
- '[[assumption/Base Views Auto-Populate Via Dataview]]'
confidence: high
created: '2026-03-07'
janitor_note: ''
name: Base Views as Single Source of Truth for Relationship Display
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related:
- '[[decision/Use Base View Embeds for Dynamic Sections]]'
- '[[assumption/Base Views Auto-Populate Via Dataview]]'
- '[[synthesis/Competitive Advantage from Connected Records]]'
status: active
supports:
- '[[decision/Use 20 Record Types as Complete Type System]]'
tags: []
type: synthesis
---

# Base Views as Single Source of Truth for Relationship Display

## Insight

The Alfred OS architecture achieves global consistency in how relationships are displayed through a "single source of truth" pattern: all instances of a record type (projects, people, orgs, etc.) use the same base view embeds, which reference centrally-defined Dataview queries in `_bases/`. This creates a leverage point where one change propagates across all records.

## Evidence

- **Template consistency**: All 20 record type templates use base view embeds (`![[type.base#Section]]`)
- **Janitor enforcement**: System detects missing `_bases/` and flags it as LINK001 error
- **Related patterns**: Similar to [[synthesis/Competitive Advantage from Connected Records]] — value comes from connections, not individual features

## Implications

- **For maintenance**: Changing how relationships display requires editing ONE file, not hundreds of records
- **For debugging**: If relationships aren't showing, check the base file, not individual records
- **For system design**: This pattern could extend to other aspects (formatting, calculations, summaries)

## Applicability

- **Direct**: Any system using transclusion/embeds and Dataview
- **Indirect**: Any knowledge management system where relationship display logic could be centralized

![[synthesis.base#Sources]]
![[synthesis.base#Related]]

---
![[synthesis.base#Sources]]

![[synthesis.base#Related]]
