---
cluster_sources:
- '[[project/Personal Knowledge Management Infrastructure]]'
- '[[assumption/Project Ownership Is Optional]]'
- '[[synthesis/Janitor Enables Self-Validating Knowledge Graph]]'
- '[[constraint/Base Views Require _bases Directory]]'
confidence: high
created: '2026-03-09'
janitor_note: ''
name: Janitor Validates Structure Not Completeness
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related: []
status: active
supports: []
tags: []
type: synthesis
---

# Janitor Validates Structure Not Completeness

## Insight

The Alfred OS janitor system validates **structural integrity** (broken references, missing infrastructure) but does NOT validate **semantic completeness** (missing owners, placeholder text, empty relationship fields). 

From [[project/Personal Knowledge Management Infrastructure]]:

**Janitor flagged:**
- `LINK001` — Missing `_bases/` directory for base view embeds (structural issue)

**Janitor did NOT flag:**
- `owner: null` — No designated project owner
- Placeholder body text — "Brief description of the project's purpose and goal"
- Empty dependency arrays — `approved_by`, `based_on`, `depends_on`, `supports` all empty
- Generic frontmatter description

This reveals the janitor's design philosophy:

**Validates:**
- Broken wikilinks
- Missing infrastructure files
- Structural dependencies that would cause system failure

**Does NOT validate:**
- Data completeness
- Semantic richness
- Business process compliance (e.g., "projects must have owners")

## Evidence

Comparison of what generates janitor notes vs what doesn't:
- Missing `_bases/` directory → **Janitor note generated**
- Null owner field → **No janitor note**
- Placeholder content → **No janitor note**

This is consistent with [[synthesis/Janitor Enables Self-Validating Knowledge Graph]] — the janitor ensures the graph is *structurally valid*, not *semantically complete*.

## Implications

- The janitor prevents system breakage, not incomplete documentation
- "Valid" record ≠ "complete" record — records can be structurally sound but semantically sparse
- Additional validation layers would be needed for completeness checks
- This design allows rapid capture (create sparse records) followed by gradual enrichment

## Applicability

Any Alfred OS vault. Users can create minimal records without triggering validation errors, as long as structural integrity is maintained. This enables "capture first, enrich later" workflows.

![[synthesis.base#Sources]]
![[synthesis.base#Related]]

---
![[synthesis.base#Sources]]

![[synthesis.base#Related]]
