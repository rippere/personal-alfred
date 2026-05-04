---
cluster_sources:
- '[[note/Personal Alfred API Key Bug Fix]]'
- '[[note/Personal Alfred VAULT_PATH Environment Variable Bug Fix]]'
- '[[note/Personal Alfred Vault Path Bug Fix]]'
- '[[note/Environment Variable Precedence in Multi-Auth Systems]]'
confidence: high
created: '2026-03-07'
janitor_note: ''
name: Three-Stage Authentication Debugging
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related: []
status: active
supports:
- '[[decision/Use OAuth for Personal Alfred Authentication]]'
- '[[decision/Ensure Environment Variable Propagation in Alfred Vault Subprocess]]'
tags: []
type: synthesis
---

# Three-Stage Authentication Debugging

## Insight

Authentication integration failures typically manifest in three stages, each requiring different diagnostic approaches:

**Stage 1: Credential Validity**
- Symptom: "Invalid credentials" or "401 Unauthorized"
- Common response: Check if credentials are correct/current
- **Trap:** This treats the symptom, not the root cause

**Stage 2: Authentication Method**
- Question: Is the system using the right auth mechanism?
- Common issue: Environment variables override preferred auth method
- **Example:** API key in `.env` overriding OAuth flow

**Stage 3: Environment Propagation**
- Question: Are credentials reaching the subprocess that needs them?
- Common issue: Environment variables not propagated to child processes
- **Example:** `ALFRED_VAULT_PATH` missing in subprocess environment

## Evidence

The Personal Alfred debugging session demonstrated all three stages:

1. **Initial diagnosis:** "Invalid API key" → replaced with valid key
2. **Deeper understanding:** API key shouldn't be used at all → switched to OAuth
3. **Final fix:** OAuth working but subprocess missing `VAULT_PATH` → explicit propagation

## Implications

**For debugging protocol:**
1. Start with Stage 2 (auth method) before Stage 1 (credential validity)
2. After fixing auth method, verify Stage 3 (environment propagation)
3. Don't stop at the first fix that "appears to work"

**For system design:**
- Make auth method selection explicit and documented
- Provide clear precedence rules when multiple methods exist
- Log which auth method is actually being used at runtime

## Applicability

This pattern applies to any multi-component system where:
- Multiple authentication methods are supported
- Subprocesses handle authenticated operations
- Configuration comes from multiple sources (env vars, config files, defaults)

Examples: CI/CD pipelines, microservice authentication, CLI tools calling external APIs

![[synthesis.base#Sources]]
![[synthesis.base#Related]]

---
![[synthesis.base#Sources]]

![[synthesis.base#Related]]
