---
based_on:
- '[[Start Here]]'
challenged_by: []
confidence: medium
confirmed_by: []
created: '2026-03-06'
invalidated_by: []
janitor_note: LINK001 — Base view embeds reference missing _bases/ directory. System
  must create _bases/ with base view definitions. ORPHAN001 — Foundational assumption,
  no inbound links expected.
name: Base Views Query Pattern Scales to Vault Size
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related: []
source: Start Here.md documentation
source_date: '2026-03-06'
status: active
tags: []
type: assumption
---

# Base Views Query Pattern Scales to Vault Size

## Claim

The base view pattern (`file.hasLink(this.file)`) assumes that live queries scanning the entire vault for wikilinks will remain performant as the vault grows to thousands or tens of thousands of records.

## Basis

The Start Here guide describes base views as "live queries" that "query the vault in real time based on what links to the current file." There is no mention of caching, indexing, or performance considerations. The pattern is presented as universally applicable.

## Evidence Trail

- No performance caveats mentioned in the documentation
- Pattern described as working the same way for all pages
- No alternative patterns for high-traffic or large-scope queries

## Impact

- If the query pattern does not scale, performance will degrade as the vault grows
- Users with large vaults may experience slow page loads or UI freezes
- May require architectural changes (caching, indexing, materialized views) if assumption is invalidated
- Currently unclear what the performance threshold is (1000 records? 10,000? 100,000?)

---
![[assumption.base#Depends On This]]

![[assumption.base#Related]]
