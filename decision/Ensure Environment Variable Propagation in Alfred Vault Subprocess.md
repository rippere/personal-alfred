---
approved_by: []
based_on: []
challenged_by: []
confidence: high
created: '2026-03-06'
decided_by:
- '[[person/David Szabo-Stuban]]'
janitor_note: LINK001 — Base view embeds reference missing _bases/ directory. System
  must create _bases/ with base view definitions.
name: Ensure Environment Variable Propagation in Alfred Vault Subprocess
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related:
- '[[note/Personal Alfred VAULT_PATH Environment Variable Bug Fix]]'
session: null
source: Debugging session with Claude Code - March 6, 2026
source_date: '2026-03-06'
status: final
supports: []
tags: []
type: decision
---

# Ensure Environment Variable Propagation in Alfred Vault Subprocess

## Context

During deployment of personal-alfred on Arch Linux, discovered that the alfred-vault subprocess spawned for Claude Code operations did not have access to the `ALFRED_VAULT_PATH` environment variable, despite it being set in the parent process.

This caused vault operations to fail because the subprocess couldn't locate the vault directory.

## Options Considered

1. **Option A: Hardcode vault path in subprocess** — Eliminate dependency on environment variable by hardcoding the path
   - ❌ Not portable across different installations
   - ❌ Requires code changes for each deployment
   
2. **Option B: Explicitly propagate environment variables to subprocess** — Modify subprocess invocation to pass required environment variables
   - ✅ Portable and configurable
   - ✅ Follows standard environment variable patterns
   - ✅ Minimal code changes

## Decision

**Use Option B:** Explicitly propagate `ALFRED_VAULT_PATH` (and other required environment variables) when spawning subprocesses for Claude Code integration.

Modify the subprocess invocation code to ensure the child process environment includes all necessary configuration from the parent process.

## Rationale

1. **Portability:** Environment variable approach works across different systems and installations
2. **Standard practice:** Explicit environment propagation is a well-established pattern in subprocess management
3. **Flexibility:** Users can configure vault location without code changes
4. **Debugging clarity:** Makes environment dependencies explicit and visible

## Consequences

### Positive
- alfred-vault works correctly with Claude Code
- Vault location remains configurable via environment variable
- Pattern can be reused for other environment-dependent configuration

### Negative
- Requires explicit environment setup in subprocess invocation code
- Adds complexity to subprocess management
- Future environment variables must be explicitly propagated

### Follow-up Actions
- Document required environment variables for alfred-vault subprocess
- Add error messages when required environment variables are missing
- Consider creating a helper function for environment-aware subprocess invocation

![[decision.base#Based On]]
![[decision.base#Related]]

---
![[decision.base#Based On]]

![[decision.base#Related]]
