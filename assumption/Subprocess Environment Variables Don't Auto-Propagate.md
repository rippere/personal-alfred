---
based_on:
- '[[note/Personal Alfred VAULT_PATH Environment Variable Bug Fix]]'
challenged_by: []
confidence: high
confirmed_by:
- '[[note/Personal Alfred VAULT_PATH Environment Variable Bug Fix]]'
- '[[note/Personal Alfred Vault Path Bug Fix]]'
created: '2026-03-07'
invalidated_by: []
name: Subprocess Environment Variables Don't Auto-Propagate
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related: []
source: Personal Alfred VAULT_PATH debugging session
source_date: '2026-03-07'
status: confirmed
tags: []
type: assumption
---

# Subprocess Environment Variables Don't Auto-Propagate

## Claim

When spawning subprocesses in most programming environments, environment variables from the parent process are NOT automatically inherited by the child process unless explicitly configured to propagate.

## Basis

This assumption was operating implicitly in the alfred-vault → Claude Code integration design. The initial implementation assumed that setting `ALFRED_VAULT_PATH` in the parent process would be sufficient for the subprocess to access it.

## Evidence Trail

**Invalidated (2026-03-07):** Personal Alfred VAULT_PATH bug revealed that the subprocess did not inherit the environment variable, causing vault operations to fail with path resolution errors.

**Fix applied:** Explicitly propagated `ALFRED_VAULT_PATH` to subprocess environment during spawn.

## Impact

This affects all subprocess integrations in the personal-alfred system. Any future subprocess calls must explicitly verify and propagate required environment variables rather than assuming inheritance.

![[assumption.base#Depends On This]]
![[assumption.base#Related]]

---
![[assumption.base#Depends On This]]

![[assumption.base#Related]]
