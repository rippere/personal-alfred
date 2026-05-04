---
approved_by: []
based_on:
- '[[note/Personal Alfred API Key Bug Fix]]'
challenged_by: []
confidence: high
created: '2026-03-07'
decided_by:
- '[[person/David Szabo-Stuban]]'
janitor_note: ''
name: Comment Out Rather Than Delete Conflicting Auth Config
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related: []
session: null
source: Debugging session
source_date: '2026-02-16'
status: final
supports: []
tags: []
type: decision
---

# Comment Out Rather Than Delete Conflicting Auth Config

## Context

During the personal-alfred OAuth authentication fix, needed to resolve conflict between ANTHROPIC_API_KEY in .env and Claude Code's OAuth flow.

## Options Considered

1. **Delete the ANTHROPIC_API_KEY line** — permanently remove the conflicting configuration
2. **Comment out the ANTHROPIC_API_KEY** — preserve the configuration but disable it

## Decision

Comment out the conflicting environment variable rather than delete it.

## Rationale

- Preserves configuration knowledge for future reference
- Documents what was tried and why it didn't work
- Allows easy rollback if needed
- Serves as inline documentation of the auth method choice
- Shows evolution of configuration over time

## Consequences

The .env file becomes a historical record of configuration decisions, not just current active config. This trades file cleanliness for institutional knowledge preservation.

![[decision.base#Based On]]
![[decision.base#Related]]

---
![[decision.base#Based On]]

![[decision.base#Related]]
