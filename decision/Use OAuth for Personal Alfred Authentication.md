---
approved_by: []
based_on:
- '[[note/Personal Alfred API Key Bug Fix]]'
- '[[note/Environment Variable Precedence in Multi-Auth Systems]]'
challenged_by: []
confidence: high
created: '2026-03-06'
decided_by:
- self
janitor_note: LINK001 — Base view embeds reference missing _bases/ directory. System
  must create _bases/ with base view definitions.
name: Use OAuth for Personal Alfred Authentication
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related:
- '[[note/Personal Alfred API Key Bug Fix]]'
- '[[synthesis/API Key Verification for AI Systems]]'
- '[[person/David Szabo-Stuban]]'
session: null
source: Debugging session - discovered API key override issue
source_date: '2026-03-06'
status: final
supports:
- '[[synthesis/API Key Verification for AI Systems]]'
tags: []
type: decision
---

# Use OAuth for Personal Alfred Authentication

## Context

The personal-alfred system integrates with Claude Code, which supports both API key authentication and OAuth. Initial setup attempted to use API keys via environment variables, which caused authentication conflicts.

## Options Considered

1. **API Key Authentication (via .env)**
   - Pros: Simple, explicit credential management
   - Cons: Requires manual key management, overrides built-in OAuth, creates precedence conflicts

2. **OAuth Authentication (Claude Code default)**
   - Pros: Integrated with Claude Code, no manual key management, more secure token handling
   - Cons: Requires initial OAuth setup

## Decision

**Use OAuth authentication by allowing Claude Code's built-in OAuth mechanism to function.** Remove or comment out `ANTHROPIC_API_KEY` from `.env` files to prevent environment variable override.

## Rationale

1. **Avoids precedence conflicts:** Environment variables override application-level auth configuration, causing failures when the API key is invalid or outdated

2. **Aligns with intended design:** Claude Code is designed to use OAuth; using API keys fights against the grain

3. **Better security:** OAuth tokens are managed by the application and can be refreshed automatically

4. **Simpler maintenance:** No need to manually manage API keys across multiple configuration files

## Consequences

**Immediate:**
- Remove `ANTHROPIC_API_KEY` from `.env` files in personal-alfred setup
- Document that OAuth is the preferred authentication method

**Long-term:**
- Future integrations should default to OAuth when available
- Environment variables should be reserved for configuration that doesn't conflict with built-in auth mechanisms
- If API keys are needed for other services, use namespaced variable names (e.g., `OPENAI_API_KEY` not `API_KEY`)

![[decision.base#Based On]]
![[decision.base#Related]]

---
![[decision.base#Based On]]

![[decision.base#Related]]
