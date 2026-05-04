---
authority: alfred-vault architecture
created: '2026-03-07'
location: []
name: Alfred-Vault Subprocess Requires ALFRED_VAULT_PATH
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related:
- '[[note/Personal Alfred VAULT_PATH Environment Variable Bug Fix]]'
- '[[note/Personal Alfred Vault Path Bug Fix]]'
source: alfred-vault subprocess design
source_date: 2026-03
status: active
tags: []
type: constraint
---

# Alfred-Vault Subprocess Requires ALFRED_VAULT_PATH

## Constraint

When alfred-vault spawns a subprocess for Claude Code integration, the subprocess MUST have access to the `ALFRED_VAULT_PATH` environment variable. Without this variable, the subprocess cannot locate the vault and all vault operations will fail.

This is a hard technical constraint imposed by alfred-vault's architecture.

## Source

alfred-vault subprocess design - the subprocess environment is isolated and does not automatically inherit parent environment variables unless explicitly propagated.

## Implications

**For integration:**
- Any system invoking alfred-vault as a subprocess must ensure `ALFRED_VAULT_PATH` is set in the subprocess environment
- Cannot rely on parent process environment variable inheritance
- Must explicitly pass the variable during subprocess invocation

**For debugging:**
- Path resolution failures in alfred-vault subprocess are a primary diagnostic signal for missing `ALFRED_VAULT_PATH`
- Verify subprocess environment configuration, not just parent environment

**Workarounds:**
- Explicitly propagate `ALFRED_VAULT_PATH` when spawning subprocess
- Alternative: Hard-code vault path (not recommended - reduces portability)

## Expiry / Review

Active indefinitely unless alfred-vault architecture changes to use a different path resolution mechanism.

![[constraint.base#Affected Projects]]
![[constraint.base#Related]]

---
![[constraint.base#Affected Projects]]

![[constraint.base#Related]]
