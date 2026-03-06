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
name: Three Primitives Are Sufficient for All Vault Interactions
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related: []
source: Start Here.md documentation
source_date: '2026-03-06'
status: active
tags: []
type: assumption
---

# Three Primitives Are Sufficient for All Vault Interactions

## Claim

The Alfred OS architecture assumes that all vault functionality can be built from three primitives: (1) Structured Base Views, (2) Alfred Dynamic Sections, and (3) Alfred Instructions. No other interaction patterns are needed.

## Basis

Start Here states: "Everything in this vault is built from combinations of three primitives" and describes these as the complete set of building blocks. The guide presents this as a complete, closed system.

## Evidence Trail

- The guide lists exactly three primitives
- States "Any page can combine all three" (implying these are the only options)
- No mention of other interaction patterns or extension points

## Impact

- If new interaction patterns are needed (e.g., real-time collaboration, bidirectional sync, webhook triggers), they must be mapped onto these three primitives or the architecture must change
- The assumption constrains the design space for new features
- May prevent certain kinds of functionality that don't fit the pattern

---
![[assumption.base#Depends On This]]

![[assumption.base#Related]]
