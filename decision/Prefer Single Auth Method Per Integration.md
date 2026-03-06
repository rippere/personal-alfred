---
approved_by: []
based_on:
- '[[assumption/Environment Variables Override Application Auth Config]]'
- '[[note/Environment Variable Precedence in Multi-Auth Systems]]'
challenged_by: []
confidence: medium
created: '2026-03-06'
decided_by:
- self
janitor_note: LINK001 — Base view embeds reference missing _bases/ directory. System
  must create _bases/ with base view definitions.
name: Prefer Single Auth Method Per Integration
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related:
- '[[synthesis/API Key Verification for AI Systems]]'
session: null
source: Lessons from personal-alfred auth debugging
source_date: '2026-03-06'
status: final
supports:
- '[[decision/Use OAuth for Personal Alfred Authentication]]'
tags: []
type: decision
---

# Prefer Single Auth Method Per Integration

## Context

When integrating systems that support multiple authentication methods (API keys, OAuth, session tokens, etc.), there's a risk of configuration conflicts where multiple auth mechanisms interfere with each other. The personal-alfred setup demonstrated this when an API key environment variable overrode OAuth authentication.

## Options Considered

1. **Allow multiple auth methods to coexist**
   - Pros: Flexibility, can switch between methods easily
   - Cons: Precedence conflicts, confusing failures, unclear which method is active

2. **Use a single auth method per integration point**
   - Pros: No precedence conflicts, clear which method is active, simpler debugging
   - Cons: Less flexibility, may require reconfiguration to switch methods

3. **Use explicit auth method selection**
   - Pros: User controls which method is used
   - Cons: Requires additional configuration, still vulnerable to environment variable pollution

## Decision

**Use a single auth method per integration point.** When a system supports multiple authentication methods, choose one and remove/comment out credentials for the others.

For personal-alfred and similar AI integrations:
- Use OAuth when available (preferred for interactive tools like Claude Code)
- Only use API keys for automated/CI contexts where OAuth isn't suitable
- Never have both OAuth and API key credentials active simultaneously

## Rationale

1. **Avoids precedence conflicts:** Environment variables silently override config files and application defaults, causing confusing failures

2. **Clearer debugging:** When auth fails, there's only one mechanism to check

3. **Explicit over implicit:** The configuration clearly shows which auth method is in use

4. **Separation of concerns:** Different contexts (interactive vs automated) can use appropriate auth methods without interference

## Consequences

**Immediate:**
- Document which auth method should be used for each tool/context
- Clean `.env` files of unused authentication credentials
- Add comments explaining why certain auth variables are commented out

**Long-term:**
- Include "single auth method" as a principle in system design docs
- Create setup checklists that verify only one auth method is configured
- Consider separate `.env` files for different contexts (`.env.interactive`, `.env.ci`) if multiple methods are truly needed

**Trade-offs accepted:**
- Switching auth methods requires more deliberate reconfiguration
- Less flexibility in dynamic auth selection
- May need multiple config files for different deployment contexts

![[decision.base#Based On]]
![[decision.base#Related]]

---
![[decision.base#Based On]]

![[decision.base#Related]]
