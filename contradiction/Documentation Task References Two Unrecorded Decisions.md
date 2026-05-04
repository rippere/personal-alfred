---
claim_a: task/Document Phase 1 Architecture plans to link [[decision/Implemented Dash
  Over Custom Frontend for Sector Flow Analyzer]] and [[decision/Used Network Visualization
  for Sector Flow Directionality]] in the projects DECISIONS.md
claim_b: Neither decision record exists in the vault — only assumption/Dash Framework
  Sufficient for Interactive Financial Dashboards and decision/Selected networkx for
  Network Graph Modeling exist, which capture different scopes (adequacy vs. choice;
  library vs. visual strategy)
created: '2026-05-04'
name: Documentation Task References Two Unrecorded Decisions
project:
- '[[project/Sector Flow Analyzer]]'
related:
- '[[assumption/Dash Framework Sufficient for Interactive Financial Dashboards]]'
- '[[decision/Selected networkx for Network Graph Modeling]]'
source_a: task/Document Phase 1 Architecture and Create Technical Design Doc
source_b: Vault learning record index
status: unresolved
type: contradiction
---

# Documentation Task References Two Unrecorded Decisions

## Claim A

The Phase 1 documentation task (`[[task/Document Phase 1 Architecture and Create Technical Design Doc]]`) explicitly plans to include in the project's `DECISIONS.md`:
- `[[decision/Implemented Dash Over Custom Frontend for Sector Flow Analyzer]]`
- `[[decision/Used Network Visualization for Sector Flow Directionality]]`

Both are referenced by wikilink as if they are existing vault records.

## Claim B

Neither record exists in the vault. The closest existing records are:
- `[[assumption/Dash Framework Sufficient for Interactive Financial Dashboards]]` — captures *adequacy belief*, not the choice between alternatives
- `[[decision/Selected networkx for Network Graph Modeling]]` — captures *library selection*, not the visual strategy of using network graphs to represent flow directionality

## Analysis

The documentation task was authored with the assumption that formal decision records for both choices would exist by documentation time. Two interpretations:

1. **Decisions made, not captured**: The Dash and network-viz choices were made during planning but only assumption records were created in the vault rather than decision records, leaving the vault underpopulated relative to what the doc task expected.
2. **Anticipated future decisions**: The documentation task was written prospectively and the wikilinks point to records that were planned but not yet created.

The distinction between an assumption ("Dash will be sufficient") and a decision ("we evaluated Dash vs. custom frontend and chose Dash") is meaningful — assumptions can be invalidated, decisions require reversal. The vault has the former but not the latter for both topics.

## Resolution

<!-- Resolve by either: (a) creating the two missing decision records capturing the actual evaluation and choice, or (b) updating the doc task to reference the existing assumption records instead -->

![[contradiction.base#Related]]
