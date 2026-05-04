---
authority: Obsidian architecture
created: '2026-03-07'
janitor_note: ''
location: []
name: Base Views Require _bases Directory
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related: []
source: System janitor note on project record
source_date: '2026-03-06'
status: active
tags: []
type: constraint
---

# Base Views Require _bases Directory

## Constraint

The Alfred OS base view system requires a `_bases/` directory containing base view definitions. Without this directory, base view embeds (`![[project.base#Assumptions]]`) will fail to resolve.

## Source

Discovered via janitor note LINK001 on the Personal Knowledge Management Infrastructure project record: "Base view embeds reference missing _bases/ directory. System must create _bases/ with base view definitions."

## Implications

- All vault instances must have `_bases/` directory initialized before base views work
- Missing `_bases/` causes broken links in all record templates that use base view embeds
- System setup/bootstrap processes must ensure `_bases/` exists and is populated

## Expiry / Review

This constraint is architectural and permanent unless the base view system is redesigned.

![[constraint.base#Affected Projects]]
![[constraint.base#Related]]

---
![[constraint.base#Affected Projects]]

![[constraint.base#Related]]
