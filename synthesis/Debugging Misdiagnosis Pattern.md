---
cluster_sources:
- '[[note/Personal Alfred API Key Bug Fix]]'
- '[[note/Environment Variable Precedence in Multi-Auth Systems]]'
confidence: medium
created: '2026-03-06'
janitor_note: LINK001 — Base view embeds reference missing _bases/ directory. System
  must create _bases/ with base view definitions.
name: Debugging Misdiagnosis Pattern
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related:
- '[[synthesis/API Key Verification for AI Systems]]'
- '[[assumption/Environment Variables Override Application Auth Config]]'
status: active
supports: []
tags: []
type: synthesis
---

# Debugging Misdiagnosis Pattern

## Insight

When debugging authentication issues, fixing the symptom (invalid credentials) can mask the root cause (wrong auth mechanism). The personal-alfred debugging demonstrated a two-phase pattern:

**Phase 1 (Symptom fix):** "The API key is invalid" → Replace with correct key → Appears to work
**Phase 2 (Root cause):** "The system shouldn't be using an API key at all" → Remove API key entirely → OAuth works as designed

This pattern suggests that **auth debugging should start with "which auth method should be active?" before jumping to "are the credentials valid?"**

## Evidence

**From [[note/Personal Alfred API Key Bug Fix]]:**
- Initial diagnosis: "invalid API key in .env needs to be replaced"
- Solution attempted: Update with key from `~/.anthropic_api_key`
- Appeared to work, but wasn't addressing root cause

**From [[note/Environment Variable Precedence in Multi-Auth Systems]]:**
- Deeper analysis revealed the API key (valid or not) was overriding OAuth
- Correct solution: Comment out the API key, let OAuth function natively
- Root cause was environment variable precedence, not credential validity

## Implications

**For debugging methodology:**
1. **Start with auth method verification** — Before validating credentials, verify which auth method should be active
2. **Check for auth mechanism conflicts** — Look for environment variables or config that might override the intended auth flow
3. **Symptom fixes can hide root causes** — A "working" system after credential replacement might still be using the wrong auth mechanism

**For documentation:**
- Document the **intended** auth method for each system, not just how to fix broken credentials
- Include "verify auth method" as a pre-flight check in troubleshooting guides
- Warn about environment variable precedence in setup docs

**For system design:**
- Make auth method selection explicit and visible
- Log which auth mechanism is actually being used at runtime
- Consider validation checks that warn when multiple auth mechanisms are configured

## Applicability

This pattern applies beyond authentication:

**General debugging:**
- Configuration issues where precedence matters (env vars, config files, defaults)
- Systems with multiple modes of operation (local vs production, interactive vs batch)
- Integration issues where symptom fixes mask architectural mismatches

**Specific contexts:**
- Multi-auth systems (current context)
- Database connection pooling (connection string override issues)
- API endpoint configuration (base URL precedence)
- Feature flags (multiple flag sources conflicting)

**Broader principle:**
**"Fix the symptom vs fix the cause"** — Always ask "is this the right mechanism?" before asking "are the values correct?"

![[synthesis.base#Sources]]
![[synthesis.base#Related]]

---
![[synthesis.base#Sources]]

![[synthesis.base#Related]]
