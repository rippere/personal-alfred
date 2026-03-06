---
approved_by: []
based_on:
- '[[assumption/Environment Variables Override Application Auth Config]]'
- '[[decision/Use OAuth for Personal Alfred Authentication]]'
challenged_by: []
confidence: high
created: '2026-03-06'
decided_by:
- '[[person/Henry Mellor]]'
name: Comment Out Conflicting Environment Variables Rather Than Delete
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related: []
session: null
source: personal-alfred OAuth authentication fix
source_date: '2026-03-06'
status: final
supports: []
tags: []
type: decision
---

# Comment Out Conflicting Environment Variables Rather Than Delete

## Context

During the personal-alfred OAuth authentication fix, discovered that `ANTHROPIC_API_KEY` in `.env` was overriding Claude Code's OAuth flow. Needed to disable the environment variable without losing the information.

## Options Considered

1. **Delete the line** — Remove `ANTHROPIC_API_KEY=...` entirely from `.env`
2. **Comment out the line** — Prefix with `#` to disable: `# ANTHROPIC_API_KEY=...`

## Decision

Comment out the conflicting environment variable rather than deleting it.

## Rationale

Commenting preserves:
- **Historical context:** Shows what was tried and why it didn't work
- **Reversibility:** Easy to re-enable if circumstances change
- **Documentation:** Serves as inline documentation about auth method precedence
- **API key value:** Keeps the key available for reference without having to retrieve it from another source

Deletion would lose all of this context. Anyone encountering the `.env` file later wouldn't know that API key auth was tried and rejected.

## Consequences

**Benefits:**
- Preserves institutional knowledge in the config file itself
- Makes it obvious that API key auth is intentionally disabled (vs accidentally missing)
- Future debugging can reference the commented-out approach

**Trade-offs:**
- Slightly clutters the config file
- Risk that someone might uncomment it without understanding the context

**Mitigation:**
Add an inline comment explaining *why* it's commented out:
```
# ANTHROPIC_API_KEY disabled - conflicts with Claude Code OAuth
# ANTHROPIC_API_KEY=sk-ant-...
```

![[decision.base#Based On]]
![[decision.base#Related]]

---
![[decision.base#Based On]]

![[decision.base#Related]]
