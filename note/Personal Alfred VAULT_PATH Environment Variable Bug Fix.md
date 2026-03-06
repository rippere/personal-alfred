---
created: '2026-03-06'
description: Resolved alfred-vault integration issue - missing ALFRED_VAULT_PATH environment
  variable in subprocess prevented Claude Code from accessing vault; fixed by ensuring
  environment variable propagation
janitor_note: LINK001 — Base view embed reference missing _bases/ directory. System
  must create _bases/ with base view definitions.
name: Personal Alfred VAULT_PATH Environment Variable Bug Fix
project: '[[project/Personal Knowledge Management Infrastructure]]'
related:
- '[[person/David Szabo-Stuban]]'
- '[[decision/Use OAuth for Personal Alfred Authentication]]'
- '[[note/Personal Alfred API Key Bug Fix]]'
relationships: []
session: null
status: active
subtype: learning
tags: []
type: note
---

# Personal Alfred VAULT_PATH Environment Variable Bug Fix

## Context

This bug occurred during the deployment of personal-alfred on Arch Linux as part of the Personal Knowledge Management Infrastructure project. After successfully resolving the OAuth authentication issue (documented in [[note/Personal Alfred API Key Bug Fix]]), encountered a new integration issue with Claude Code.

## Problem

The alfred-vault CLI was failing when invoked from within Claude Code sessions. The root cause was a missing `ALFRED_VAULT_PATH` environment variable in the subprocess that alfred-vault spawns for Claude Code operations.

While the environment variable was set in the parent process, it was not being propagated to the subprocess, causing vault operations to fail with path resolution errors.

## Solution

Fixed the subprocess environment setup to ensure `ALFRED_VAULT_PATH` is properly propagated when spawning child processes for Claude Code integration.

This required modifying the subprocess invocation code to explicitly pass the environment variable from the parent process to the child process.

## Collaborators

- **Claude Code:** AI assistant that helped with debugging and identifying the subprocess environment issue
- **[[person/David Szabo-Stuban]]:** Creator of the alfred-vault package

## Key Learnings

### 1. OAuth vs API Key Authentication

Understanding when each authentication method is appropriate:
- **OAuth:** Best for interactive applications and user-facing tools (like Claude Code)
- **API keys:** Better for server-side automation and non-interactive scripts

### 2. Environment Variable Propagation in Subprocess Calls

**Critical insight:** Environment variables set in a parent process do NOT automatically propagate to child processes unless explicitly configured.

When spawning subprocesses:
- Always verify which environment variables the child process needs
- Explicitly pass required environment variables to the subprocess
- Don't assume parent environment is inherited

**Common failure pattern:** Setting environment variables in the shell/parent process and assuming they'll be available in spawned subprocesses without explicit propagation.

### 3. Subprocess Environment Setup Importance

Proper subprocess environment configuration is critical for:
- Path resolution (like `ALFRED_VAULT_PATH`)
- Authentication credentials
- Configuration values
- Tool-specific settings

**Best practice:** When debugging subprocess failures, always check:
1. What environment variables does the subprocess expect?
2. Are those variables being explicitly passed?
3. What's the actual environment visible to the subprocess?

## Technical Impact

This fix enables seamless integration between:
- alfred-vault (vault management CLI)
- Claude Code (AI assistant interface)
- The Obsidian vault (knowledge base)

Without this fix, Claude Code could not perform vault operations despite having the correct authentication, making the entire personal-alfred system non-functional.

## Related Timeline

1. **First bug:** API key override issue (resolved by using OAuth) → [[note/Personal Alfred API Key Bug Fix]]
2. **Second bug:** Missing VAULT_PATH in subprocess (this issue)
3. **Result:** Fully functional personal-alfred deployment on Arch Linux

## Related
![[related.base#All]]
