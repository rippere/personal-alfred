---
cluster_sources:
- '[[assumption/Janitor Auto-Detects Structural Issues]]'
- '[[constraint/Base Views Require _bases Directory]]'
- '[[synthesis/Zero-Friction Capture Over User Control]]'
- '[[project/Personal Knowledge Management Infrastructure]]'
confidence: medium
created: '2026-03-07'
janitor_note: ''
name: Janitor Enables Self-Validating Knowledge Graph
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related:
- '[[assumption/Janitor Auto-Detects Structural Issues]]'
- '[[constraint/Base Views Require _bases Directory]]'
- '[[synthesis/Zero-Friction Capture Over User Control]]'
status: active
supports: []
tags: []
type: synthesis
---

# Janitor Enables Self-Validating Knowledge Graph

## Insight

The Alfred OS janitor system turns the vault into a self-validating knowledge graph by automatically detecting structural issues (broken links, missing dependencies, schema violations) and flagging them directly on affected records. This combines zero-friction capture with automated quality assurance.

## Evidence

**Pattern observed across multiple records:**

1. **Auto-detection:** [[assumption/Janitor Auto-Detects Structural Issues]] — janitor adds `janitor_note` fields to records with structural problems
2. **Standardized error codes:** LINK001 for broken base view references (see [[constraint/Base Views Require _bases Directory]])
3. **Zero user friction:** Validation happens automatically, no manual checks required (aligns with [[synthesis/Zero-Friction Capture Over User Control]])
4. **Actionable guidance:** Janitor notes include both error code and remediation guidance ("System must create _bases/ with base view definitions")

**Example from [[project/Personal Knowledge Management Infrastructure]]:**
```yaml
janitor_note: "LINK001 — Base view embeds reference missing _bases/ directory. System must create _bases/ with base view definitions."
```

## Implications

- **Data quality without process overhead:** The vault self-reports quality issues without requiring manual validation workflows
- **Progressive improvement:** Users can capture knowledge immediately; janitor flags cleanup work asynchronously
- **Standardized diagnostics:** Error codes enable tooling to auto-fix common issues
- **Discovery through use:** Structural problems surface when records are accessed, not through separate validation passes

**Competitive advantage:** Most knowledge management systems require manual link checking or break silently. Alfred OS makes the knowledge graph self-aware.

## Applicability

This pattern applies to:
- Any system with structured data and relationships (wikis, CRMs, task managers)
- Development environments with complex dependencies
- Documentation systems where link rot is common

The janitor pattern could be extracted as a standalone tool for other Obsidian vaults or knowledge management platforms.

![[synthesis.base#Sources]]
![[synthesis.base#Related]]

---
![[synthesis.base#Sources]]

![[synthesis.base#Related]]
