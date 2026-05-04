---
approved_by: []
based_on:
- '[[assumption/Subprocess Environment Variables Don''t Auto-Propagate]]'
challenged_by: []
confidence: high
created: '2026-03-07'
decided_by:
- '[[person/David Szabo-Stuban]]'
janitor_note: ''
name: Explicitly Propagate Environment Variables to Subprocesses
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related: []
session: ''
source: Personal Alfred VAULT_PATH bug fix
source_date: '2026-03-07'
status: final
supports: []
tags: []
type: decision
---

# Explicitly Propagate Environment Variables to Subprocesses

## Context

During integration of alfred-vault with Claude Code, discovered that the subprocess spawned for Claude Code operations did not have access to `ALFRED_VAULT_PATH`, even though it was set in the parent process environment.

## Options Considered

1. **Rely on automatic environment inheritance** — Assume subprocess inherits parent environment (REJECTED — doesn't work)
2. **Explicitly pass required environment variables** — Modify subprocess spawn to explicitly propagate needed variables (SELECTED)
3. **Use configuration files instead** — Store paths in config files rather than environment variables (REJECTED — adds complexity)

## Decision

Modified the subprocess invocation code to explicitly pass `ALFRED_VAULT_PATH` and other required environment variables from parent to child process.

## Rationale

- Environment variable inheritance is not guaranteed across subprocess boundaries
- Explicit propagation makes dependencies visible in code
- Low-cost fix with high reliability

## Consequences

- All future subprocess integrations must explicitly verify which environment variables are needed
- Configuration becomes more explicit and self-documenting
- Reduces risk of environment-related integration bugs

![[decision.base#Based On]]
![[decision.base#Related]]

---
![[decision.base#Based On]]

![[decision.base#Related]]
