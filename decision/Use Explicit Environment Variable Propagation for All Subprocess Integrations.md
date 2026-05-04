---
approved_by: []
based_on:
- '[[note/Personal Alfred VAULT_PATH Environment Variable Bug Fix]]'
- '[[assumption/Subprocess Environment Isolation Is Default Behavior]]'
challenged_by: []
confidence: high
created: '2026-03-07'
decided_by:
- '[[person/Henry Mellor]]'
janitor_note: ''
name: Use Explicit Environment Variable Propagation for All Subprocess Integrations
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related: []
session: null
source: Personal Alfred integration debugging
source_date: '2026-03-07'
status: final
supports: []
tags: []
type: decision
---

# Use Explicit Environment Variable Propagation for All Subprocess Integrations

## Context

During alfred-vault → Claude Code integration, discovered that required environment variables (`ALFRED_VAULT_PATH`) were not available in the subprocess despite being set in the parent process.

This caused silent failures where the subprocess couldn't locate required configuration.

## Options Considered

1. **Rely on automatic environment inheritance** — assume subprocess gets parent environment
2. **Explicitly propagate required variables** — configure subprocess with specific environment variables
3. **Use configuration files instead** — avoid environment variables for subprocess communication

## Decision

**Adopt explicit environment variable propagation as standard practice for all subprocess integrations.**

When spawning subprocesses:
1. Document which environment variables the subprocess requires
2. Explicitly pass those variables in the subprocess invocation
3. Do NOT assume parent environment is inherited
4. Add validation to detect missing environment variables early

## Rationale

- Environment isolation is default behavior; explicit propagation is portable and reliable
- Makes dependencies visible in code (documents what subprocess needs)
- Prevents silent failures from missing configuration
- Easier to debug (explicit variable list vs implicit inheritance)

## Consequences

**For implementation:**
- All subprocess spawn calls must include explicit environment configuration
- Code review checklist includes "Are required env vars propagated?"

**For documentation:**
- Integration guides must list required environment variables for each subprocess
- Setup scripts validate environment variables before spawning subprocesses

**For debugging:**
- When subprocess fails, check explicit propagation list BEFORE checking parent environment

![[decision.base#Based On]]
![[decision.base#Related]]

---
![[decision.base#Based On]]

![[decision.base#Related]]
