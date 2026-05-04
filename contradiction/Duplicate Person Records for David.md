---
claim_a: '[[person/David]]'
claim_b: '[[person/David Szabo-Stuban]]'
created: '2026-03-07'
janitor_note: ''
name: Duplicate Person Records for David
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related:
- '[[note/Personal Alfred API Key Bug Fix]]'
- '[[decision/Ensure Environment Variable Propagation in Alfred Vault Subprocess]]'
- '[[note/Personal Alfred VAULT_PATH Environment Variable Bug Fix]]'
- '[[note/Personal Alfred Vault Path Bug Fix]]'
- '[[synthesis/Subprocess Environment Debugging Pattern]]'
resolution: ''
resolved_date: null
source_a: Person record created 2026-03-06
source_b: Person record created 2026-03-06
status: unresolved
tags: []
type: contradiction
---

# Duplicate Person Records for David

## Claim A

[[person/David]] — "Creator of alfred-vault package, key collaborator on personal knowledge management infrastructure"

Related to:
- [[note/Personal Alfred Vault Path Bug Fix]]
- [[note/Personal Alfred API Key Bug Fix]]

## Claim B

[[person/David Szabo-Stuban]] — "Creator of alfred-vault package, collaborator on personal knowledge management infrastructure"

Related to:
- [[note/Personal Alfred VAULT_PATH Environment Variable Bug Fix]]
- [[note/Personal Alfred API Key Bug Fix]]
- [[decision/Ensure Environment Variable Propagation in Alfred Vault Subprocess]]
- [[synthesis/Subprocess Environment Debugging Pattern]]

## Analysis

These are clearly the same person (both described as "Creator of alfred-vault package"). The duplication likely occurred during early vault setup when the system auto-created person records from different sources:

- "David" might have been extracted from casual references
- "David Szabo-Stuban" might have been extracted from more formal sources or signatures

Both records share overlapping related notes ([[note/Personal Alfred API Key Bug Fix]]), confirming they refer to the same individual.

## Resolution

**Options:**

1. **Merge into canonical record:** Choose "David Szabo-Stuban" (full name) as canonical, update all links from "David" to point to "David Szabo-Stuban", add "David" as an alias
2. **Delete duplicate:** Delete "David" record and redirect all its relationships to "David Szabo-Stuban"
3. **Leave unresolved:** Accept duplication if the system can handle it (not recommended — breaks relationship queries)

**Recommended:** Option 1 — merge with alias.

![[contradiction.base#Related]]
