---
based_on:
- '[[note/Environment Variable Precedence in Multi-Auth Systems]]'
- '[[note/Personal Alfred API Key Bug Fix]]'
challenged_by: []
confidence: high
confirmed_by:
- '[[note/Environment Variable Precedence in Multi-Auth Systems]]'
created: '2026-03-06'
invalidated_by: []
janitor_note: LINK001 — Base view embeds reference missing _bases/ directory. System
  must create _bases/ with base view definitions.
name: Environment Variables Override Application Auth Config
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related:
- '[[decision/Use OAuth for Personal Alfred Authentication]]'
- '[[synthesis/API Key Verification for AI Systems]]'
source: Debug experience with personal-alfred OAuth/API key conflict
source_date: '2026-03-06'
status: confirmed
tags: []
type: assumption
---

# Environment Variables Override Application Auth Config

## Claim

In most systems, environment variables have higher precedence than configuration files or application-default authentication mechanisms. This means an environment variable can silently override a preferred auth method (like OAuth) even when the application is designed to use a different authentication flow.

## Basis

**Observed in personal-alfred setup:**
- Claude Code uses OAuth authentication by default
- An `ANTHROPIC_API_KEY` environment variable in `.env` overrode the OAuth flow
- The system attempted to use the API key instead of OAuth, causing authentication failure
- Commenting out the environment variable allowed OAuth to function as designed

**Standard system behavior:**
Most application frameworks and CLI tools follow this precedence order:
1. Environment variables (highest)
2. Configuration files (`.env`, config.json, etc.)
3. Application defaults (lowest)

This is documented behavior in many frameworks (Twelve-Factor App methodology, dotenv libraries, etc.).

## Evidence Trail

**Confirmed by:**
- [[note/Personal Alfred API Key Bug Fix]] — Direct observation of environment variable overriding OAuth
- [[note/Environment Variable Precedence in Multi-Auth Systems]] — Generalized principle extracted from debugging

**Initial misdiagnosis:**
First thought the API key just needed to be corrected. Only after deeper investigation discovered that the presence of the variable itself was the problem, not its value.

## Impact

**Decisions depending on this:**
- [[decision/Use OAuth for Personal Alfred Authentication]] — Decided to remove API key from `.env` based on this precedence behavior

**Systems affected:**
- Any multi-auth integration (personal-alfred, other AI tools)
- CI/CD pipelines with mixed credential types
- Containerized applications with multiple secret sources

**Best practices emerging:**
- Check for environment variable pollution when debugging auth issues
- Remove unused auth credentials from `.env` files
- Document which auth method should be active for each integration point
- Use namespaced environment variable names to avoid conflicts

![[assumption.base#Depends On This]]
![[assumption.base#Related]]

---
![[assumption.base#Depends On This]]

![[assumption.base#Related]]
