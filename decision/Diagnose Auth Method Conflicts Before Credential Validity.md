---
approved_by: []
based_on:
- '[[note/Personal Alfred API Key Bug Fix]]'
- '[[note/Environment Variable Precedence in Multi-Auth Systems]]'
challenged_by: []
confidence: high
created: '2026-03-07'
decided_by:
- '[[person/Henry Mellor]]'
janitor_note: ''
name: Diagnose Auth Method Conflicts Before Credential Validity
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related: []
session: null
source: Personal Alfred OAuth debugging session
source_date: '2026-03-07'
status: final
supports: []
tags: []
type: decision
---

# Diagnose Auth Method Conflicts Before Credential Validity

## Context

During personal-alfred deployment, encountered authentication failures with Claude Code. Initial debugging focused on credential validity (invalid API key) rather than auth method conflicts (environment variable overriding OAuth).

This led to wasted effort replacing API keys when the real issue was auth method misconfiguration.

## Options Considered

1. **Credential-first debugging:** Check if credentials are valid/expired before investigating auth method conflicts
2. **Auth-method-first debugging:** Check for conflicting auth methods (environment variables, config files) before checking credential validity

## Decision

**Adopted auth-method-first debugging for OAuth-based systems:**

When debugging OAuth authentication failures:
1. First check for conflicting environment variables or config files that might override OAuth
2. Only after ruling out auth method conflicts, check credential validity

## Rationale

- Environment variable conflicts are harder to detect (invisible to the application) while credential errors are typically logged
- Fixing invalid credentials when auth method is wrong creates false positives and wastes debugging time
- OAuth systems typically have their own credential management; environment variables presence usually indicates misconfiguration

## Consequences

- Debugging OAuth failures now follows: env vars → config files → credential validity → token refresh
- Documentation for personal-alfred setup includes explicit warning about `.env` file auth conflicts
- When creating new integrations, prefer single auth method per component

![[decision.base#Based On]]
![[decision.base#Related]]

---
![[decision.base#Based On]]

![[decision.base#Related]]
