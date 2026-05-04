---
based_on:
- '[[note/Personal Alfred API Key Bug Fix]]'
- '[[note/Environment Variable Precedence in Multi-Auth Systems]]'
challenged_by: []
confidence: high
confirmed_by:
- '[[note/Personal Alfred API Key Bug Fix]]'
created: '2026-03-07'
invalidated_by: []
janitor_note: ''
name: OAuth Authentication Failures Mask Misconfiguration Not Invalid Credentials
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related: []
source: Personal Alfred debugging session
source_date: '2026-03-07'
status: confirmed
tags: []
type: assumption
---

# OAuth Authentication Failures Mask Misconfiguration Not Invalid Credentials

## Claim

When OAuth-based systems fail with "authentication error" messages, the root cause is often auth method misconfiguration (e.g., environment variables overriding OAuth flows) rather than invalid credentials or expired tokens.

## Basis

From the personal-alfred debugging session: Initial diagnosis focused on "invalid API key" and attempted to replace it with a correct key from `~/.anthropic_api_key`. This appeared to work temporarily but masked the real issue: the presence of ANY `ANTHROPIC_API_KEY` environment variable was overriding Claude Code's OAuth authentication mechanism.

The correct fix was removing/commenting out the environment variable entirely, not replacing it with a valid key.

## Evidence Trail

**Confirmed by:**
- [[note/Personal Alfred API Key Bug Fix]] — Documents the misdiagnosis pattern where fixing the symptom (invalid key) masked the root cause (wrong auth mechanism)
- [[note/Environment Variable Precedence in Multi-Auth Systems]] — Explains how environment variables override application-native auth methods

**Pattern:** "Invalid credentials" error → assumed bad key → replaced key → temporary success → actual issue was auth method conflict

## Impact

This assumption affects debugging strategy for OAuth integrations:
- When OAuth systems report auth failures, check for conflicting environment variables BEFORE checking credential validity
- "Invalid credentials" may mean "wrong auth method being used" not "credentials are bad"
- Fixing credentials without addressing auth method conflicts creates false positives in debugging

![[assumption.base#Depends On This]]
![[assumption.base#Related]]

---
![[assumption.base#Depends On This]]

![[assumption.base#Related]]
