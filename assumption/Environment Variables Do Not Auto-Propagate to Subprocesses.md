---
based_on: []
challenged_by: []
confidence: high
confirmed_by:
- '[[note/Personal Alfred VAULT_PATH Environment Variable Bug Fix]]'
- '[[note/Personal Alfred Vault Path Bug Fix]]'
created: '2026-03-07'
invalidated_by: []
janitor_note: ''
name: Environment Variables Do Not Auto-Propagate to Subprocesses
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related: []
source: System behavior
source_date: '2026-02-16'
status: confirmed
tags: []
type: assumption
---

# Environment Variables Do Not Auto-Propagate to Subprocesses

## Claim

Environment variables set in a parent process do not automatically propagate to child processes unless explicitly configured during subprocess invocation.

## Basis

Standard Unix/Linux process behavior: child processes inherit environment only if explicitly passed during fork/exec. The alfred-vault → Claude Code integration bug demonstrated this — ALFRED_VAULT_PATH was set in the parent but not available in the subprocess.

## Evidence Trail

- **2026-02-16:** Confirmed via [[note/Personal Alfred VAULT_PATH Environment Variable Bug Fix]] — ALFRED_VAULT_PATH was present in parent process but missing in alfred-vault's Claude Code subprocess
- **2026-02-16:** Second confirmation via [[note/Personal Alfred Vault Path Bug Fix]] — same root cause, fixed by explicit environment variable propagation

## Impact

This affects any system using subprocess invocation patterns. Developers must explicitly pass required environment variables when spawning child processes — cannot rely on implicit inheritance.

![[assumption.base#Depends On This]]
![[assumption.base#Related]]

---
![[assumption.base#Depends On This]]

![[assumption.base#Related]]
