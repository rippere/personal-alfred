---
approved_by: []
based_on:
- '[[synthesis/Multi-Auth Systems Create Hidden Configuration State]]'
- '[[note/Environment Variable Precedence in Multi-Auth Systems]]'
challenged_by: []
confidence: medium
created: '2026-03-24'
decided_by: []
name: Prefer Explicit Auth Method Declaration Over Implicit Precedence
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related: []
session: null
source: Lessons from OAuth vs API key confusion
source_date: '2026-03-24'
status: draft
supports: []
tags: []
type: decision
---

# Prefer Explicit Auth Method Declaration Over Implicit Precedence

## Context

Multi-authentication systems (supporting API keys, OAuth, tokens, etc.) traditionally use implicit precedence rules to select which method to use. This creates hidden state where the operator doesn't know which method is active until a failure occurs.

From personal-alfred debugging: Claude Code was configured for OAuth, but an environment variable `ANTHROPIC_API_KEY` silently overrode that choice, causing authentication failures.

## Options Considered

1. **Implicit precedence (current approach)** — System silently chooses auth method based on which credentials are present, following hardcoded precedence rules
2. **Explicit declaration** — Require operators to explicitly declare which auth method to use (via flag, config, or env var like `AUTH_METHOD=oauth`)
3. **Validation with warnings** — Keep implicit precedence but detect and warn when multiple auth methods are configured
4. **Fail on ambiguity** — Refuse to start if multiple auth methods are detected

## Decision

**Prefer explicit auth method declaration with validation warnings.**

For systems that support multiple auth methods:
- Provide an explicit `AUTH_METHOD` configuration option
- When auth method is not explicitly set, validate that only ONE method's credentials are present
- If multiple methods are detected, log a warning showing which method was selected and why
- Consider making explicit declaration mandatory in future versions

## Rationale

**Explicit is better than implicit:** Following the Zen of Python principle, explicit auth method selection eliminates hidden state and makes system behavior predictable.

**Fails fast:** When misconfigured, the system can detect and report the issue at startup rather than during operation.

**Debuggability:** Operators can see in logs exactly which auth method is active.

**Backward compatibility:** Option 3 allows existing implicit behavior while moving toward explicit declaration.

## Consequences

**For alfred-vault / personal-alfred:**
- Add auth method logging at startup
- Consider adding `ALFRED_AUTH_METHOD` environment variable
- Detect and warn when both OAuth tokens and API keys are present

**For future integrations:**
- Standard pattern for auth method selection
- Explicit documentation of precedence rules when implicit mode is used

---
![[decision.base#Based On]]

![[decision.base#Related]]
