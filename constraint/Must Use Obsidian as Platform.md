---
authority: System architecture
created: '2026-03-06'
janitor_note: LINK001 — Base view embeds reference missing _bases/ directory. System
  must create _bases/ with base view definitions. ORPHAN001 — Foundational constraint,
  no inbound links expected.
location: []
name: Must Use Obsidian as Platform
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related: []
source: Architectural decision
source_date: '2026-03-06'
status: active
tags: []
type: constraint
---

# Must Use Obsidian as Platform

## Constraint

Alfred OS must run on Obsidian. The system is described as "a unified operational system built on Obsidian" and relies on Obsidian-specific features (wikilinks, Dataview queries, file-based storage).

## Source

Architectural constraint from the Start Here documentation. The opening line states: "Alfred OS is a unified operational system built on Obsidian."

## Implications

- Cannot migrate to other platforms without architectural rewrite
- Inherits all limitations of Obsidian (local-first, markdown-based, single-user by default)
- Benefits from Obsidian ecosystem (plugins, mobile apps, sync)
- Performance is bounded by Obsidian's query engine capabilities
- Multi-user collaboration limited by Obsidian's collaboration model

## Expiry / Review

This is a foundational architectural constraint. No expiry date, but should be reviewed if Obsidian's capabilities plateau or if multi-user requirements become critical.

---
![[constraint.base#Affected Projects]]

![[constraint.base#Related]]
