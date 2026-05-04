---
based_on:
- '[[note/Personal Alfred VAULT_PATH Environment Variable Bug Fix]]'
- '[[note/Personal Alfred Vault Path Bug Fix]]'
challenged_by: []
confidence: high
confirmed_by:
- '[[synthesis/Environment Variable Propagation in Subprocess Calls]]'
- '[[synthesis/Subprocess Environment Debugging Pattern]]'
created: '2026-03-07'
invalidated_by: []
janitor_note: ''
name: Subprocess Environment Isolation Is Default Behavior
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related:
- '[[assumption/Environment Variables Do Not Auto-Propagate to Subprocesses]]'
source: Personal Alfred vault path debugging session
source_date: '2026-03-07'
status: confirmed
tags: []
type: assumption
---

# Subprocess Environment Isolation Is Default Behavior

## Claim

When spawning subprocesses, the default behavior across most programming environments and operating systems is **environment isolation**: environment variables from the parent process are NOT automatically inherited by the child process unless explicitly configured.

## Basis

From personal-alfred integration debugging:

The alfred-vault CLI spawns Claude Code as a subprocess. The `ALFRED_VAULT_PATH` environment variable was set in the parent process but was NOT available in the subprocess, causing vault path resolution failures.

**Key insight:** The variable had to be **explicitly propagated** to the subprocess environment. It was not sufficient to have it set in the parent.

This pattern appears in:
- [[note/Personal Alfred VAULT_PATH Environment Variable Bug Fix]]
- [[note/Personal Alfred Vault Path Bug Fix]]
- [[synthesis/Environment Variable Propagation in Subprocess Calls]]

## Evidence Trail

**Confirmed by:**
- Actual bug manifestation: parent process had `ALFRED_VAULT_PATH`, subprocess did not
- Fix required explicit environment variable passing to subprocess
- [[synthesis/Subprocess Environment Debugging Pattern]] documents this as a recurring pattern

**Related existing learning:**
- [[assumption/Subprocess Environment Variables Don't Auto-Propagate]] — earlier capture of same pattern
- [[assumption/Environment Variables Do Not Auto-Propagate to Subprocesses]] — another instance

## Impact

**Design implications:**
- Any subprocess integration must explicitly configure environment variable propagation
- Cannot rely on "environment inheritance" as default behavior
- Need subprocess environment setup checklist for new integrations

**Debugging implications:**
- When subprocess fails with "path not found" or "config missing", check environment variable propagation BEFORE checking filesystem
- Parent process environment ≠ subprocess environment

![[assumption.base#Depends On This]]
![[assumption.base#Related]]

---
![[assumption.base#Depends On This]]

![[assumption.base#Related]]
