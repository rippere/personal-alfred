---
based_on:
- '[[project/Personal Knowledge Management Infrastructure]]'
challenged_by: []
confidence: high
confirmed_by: []
created: '2026-03-07'
invalidated_by: []
janitor_note: ''
name: Janitor Auto-Detects Structural Issues
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related:
- '[[synthesis/Zero-Friction Capture Over User Control]]'
source: Alfred OS janitor system
source_date: '2026-03-06'
status: active
tags: []
type: assumption
---

# Janitor Auto-Detects Structural Issues

## Claim

The Alfred OS janitor system can automatically detect structural issues in vault records (such as broken base view references) and flag them by adding a `janitor_note` field to the affected record's frontmatter.

## Basis

Observed on [[project/Personal Knowledge Management Infrastructure]] record:

```yaml
janitor_note: "LINK001 — Base view embeds reference missing _bases/ directory. System must create _bases/ with base view definitions."
```

The janitor added this field autonomously to flag a structural problem (missing `_bases/` directory), using a standardized error code (LINK001) and actionable description.

## Evidence Trail

**2026-03-06:** First observed on project record. The field was not manually added — it appeared through automated janitor validation.

## Impact

- Janitor provides zero-friction validation of vault structural integrity
- Error codes (LINK001, etc.) enable consistent categorization of issues
- The `janitor_note` field pattern enables lightweight issue tracking without creating separate task/issue records
- Supports [[synthesis/Zero-Friction Capture Over User Control]] — validation happens automatically

![[assumption.base#Depends On This]]
![[assumption.base#Related]]

---
![[assumption.base#Depends On This]]

![[assumption.base#Related]]
