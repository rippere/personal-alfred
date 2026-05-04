---
approved_by: []
based_on:
- '[[assumption/Test Infrastructure Requires Minimal Valid Input]]'
- '[[note/Vault Curation Test Note]]'
challenged_by:
- '[[contradiction/Minimal Test Input vs Comprehensive Curation Output]]'
confidence: medium
created: '2026-03-07'
decided_by:
- '[[person/Henry Mellor]]'
janitor_note: ''
name: Preserve Test Minimalism Despite Curation Comprehensiveness
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related:
- '[[contradiction/Minimal Input vs Comprehensive Output in Test Design]]'
session: null
source: Vault curation test design
source_date: 2026-03
status: draft
supports: []
tags: []
type: decision
---

# Preserve Test Minimalism Despite Curation Comprehensiveness

## Context

The vault curation system needed test cases to verify end-to-end functionality. A design question arose: Should test inputs be minimal (to reduce complexity) or comprehensive (to match expected output richness)?

## Options Considered

1. **Minimal test input** — Simple one-line messages, no metadata, no relationships
   - Pro: Isolates system behavior, easier to debug, reduces test complexity
   - Con: Creates asymmetry with expected comprehensive output
   
2. **Comprehensive test input** — Full structured content matching expected output
   - Pro: Input/output symmetry, realistic test cases
   - Con: Hard to isolate bugs, complex test setup, couples test to output format

## Decision

**Use minimal test input, expect comprehensive output.**

Test cases like [[note/Vault Curation Test Note]] use deliberately simple input (single-line messages) but verify that the curator produces rich, properly structured output.

## Rationale

**Test goal:** Verify that the curator can handle ANY input and produce vault-quality output. Using minimal input is a **stress test** of the curator's ability to:
- Add proper structure where none exists
- Infer relationships and context
- Apply vault quality standards uniformly

If the curator can handle minimal input well, it can handle comprehensive input even better.

**Debugging benefit:** When tests fail, minimal input makes it easier to isolate whether the issue is in parsing, structure generation, or relationship inference.

## Consequences

**Positive:**
- Tests demonstrate curator robustness
- Simple test cases are easy to maintain
- Clear signal when curator fails to enrich minimal input

**Negative:**
- Creates asymmetry that may confuse new developers (why is output so much richer than input?)
- May create unrealistic expectations about curator capabilities (can it really synthesize this much from so little?)

**Open question:** [[contradiction/Minimal Test Input vs Comprehensive Curation Output]] - Is the curator over-engineering output, or correctly applying vault standards?

![[decision.base#Based On]]
![[decision.base#Related]]

---
![[decision.base#Based On]]

![[decision.base#Related]]
