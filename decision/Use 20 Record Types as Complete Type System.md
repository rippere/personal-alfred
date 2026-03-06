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
name: Use 20 Record Types as Complete Type System
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

# Use 20 Record Types as Complete Type System

## Context

The system needed to define a set of record types that could model all operational work. Too few types would force unnatural mappings; too many would create confusion and fragmentation.

## Options Considered

1. **Minimal types** — very few types (e.g., just Task, Project, Person, Note) with flexible subtypes
2. **20 distinct types** — a fixed set of 20 types covering operational, epistemic, and entity records
3. **Extensible type system** — user-defined types with schema validation

## Decision

The system defines exactly 20 record types as a complete, closed set: Project, Task, Session, Conversation, Input, Person, Org, Location, Account, Asset, Note, Decision, Process, Run, Event, Assumption, Constraint, Contradiction, Synthesis, and (implicitly) one more.

## Rationale

The Start Here guide lists "20 record types" and presents them as a complete taxonomy. The design appears to favor a curated, opinionated type system over user extensibility.

## Consequences

- New use cases must map onto these 20 types or the type system must be extended
- Clear mental model for users — finite set of types to learn
- May create awkward mappings for edge cases that don't fit cleanly
- Strong opinions about what constitutes a "type" vs. a "subtype"

---
![[decision.base#Based On]]

![[decision.base#Related]]
