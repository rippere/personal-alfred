---
created: '2026-03-06'
description: Fixed personal-alfred integration by setting ALFRED_VAULT_PATH environment
  variable in subprocess spawned by alfred-vault for Claude Code
janitor_note: LINK001 — Base view embed reference missing _bases/ directory. System
  must create _bases/ with base view definitions.
name: Personal Alfred Vault Path Bug Fix
project: '[[project/Personal Knowledge Management Infrastructure]]'
related:
- '[[person/David]]'
- '[[note/Personal Alfred API Key Bug Fix]]'
- '[[note/Environment Variable Precedence in Multi-Auth Systems]]'
relationships: []
session: null
status: active
subtype: learning
tags: []
type: note
---

# Personal Alfred Vault Path Bug Fix

## Context

While integrating personal-alfred deployment on Arch Linux (part of the Personal Knowledge Management Infrastructure project), encountered a critical integration bug preventing Claude Code from successfully invoking the alfred-vault CLI tooling.

## Problem

The root cause was a missing `ALFRED_VAULT_PATH` environment variable in the subprocess that alfred-vault spawns for Claude Code. Without this environment variable, the subprocess couldn't locate the vault path and operations would fail.

## Solution

Set the `ALFRED_VAULT_PATH` environment variable in the subprocess environment setup. This ensures that when alfred-vault spawns Claude Code as a subprocess, it has access to the required vault path configuration.

## Key Learnings from Debugging Session

This debugging session provided valuable insights across three technical areas:

### 1. OAuth vs API Key Authentication

Understanding the distinction between OAuth flows (user-delegated, browser-based authentication) and API key authentication (direct credential passing). Different components of the system may use different authentication strategies, and these must be properly configured for each component.

### 2. Environment Variable Propagation in Subprocess Calls

**Critical insight:** When spawning subprocesses, environment variables from the parent process are not automatically inherited unless explicitly passed. This is especially important for configuration variables like paths, API endpoints, and authentication credentials.

The alfred-vault → Claude Code integration required explicit environment variable setup in the subprocess call to ensure Claude Code could locate the vault.

### 3. Importance of Subprocess Environment Setup

Subprocess environment configuration is a common source of integration bugs. When debugging subprocess failures, always verify:
- Which environment variables the subprocess expects
- Whether those variables are being propagated from the parent
- Whether subprocess initialization code sets up the required environment

## Collaborators

- **Claude Code:** AI assistant that helped diagnose the issue through systematic debugging
- **[[person/David]]:** Creator of the alfred-vault package that this infrastructure depends on

## Related Context

This bug fix complements the earlier [[note/Personal Alfred API Key Bug Fix|API key authentication issue]], which addressed OAuth vs API key conflicts. Together, these two debugging sessions established a working personal-alfred integration on Arch Linux.

## Related
![[related.base#All]]
