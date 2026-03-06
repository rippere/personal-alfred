---
based_on:
- '[[note/Personal Alfred API Key Bug Fix]]'
challenged_by:
- '[[synthesis/Debugging Misdiagnosis Pattern]]'
confidence: medium
confirmed_by: []
created: '2026-03-06'
invalidated_by: []
name: Invalid Credentials Indicate Wrong Auth Method Not Bad Keys
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related: []
source: ''
source_date: null
status: challenged
tags: []
type: assumption
---

# Invalid Credentials Indicate Wrong Auth Method Not Bad Keys

## Claim

When authentication fails with "invalid credentials," the initial diagnosis assumes the credentials themselves are wrong (outdated, malformed, expired) rather than the authentication mechanism being inappropriate for the context.

## Basis

The personal-alfred debugging session initially diagnosed the problem as "invalid API key" and attempted to fix it by replacing the key with a different one from `~/.anthropic_api_key`. This approach treats the symptom (invalid credentials) as the problem rather than investigating why API key auth was being used at all.

## Evidence Trail

**Initial approach (from [[note/Personal Alfred API Key Bug Fix]]):**
"Found the correct API key stored in `~/.anthropic_api_key` and updated the `.env` file with the valid key."

**Challenged by (from [[synthesis/Debugging Misdiagnosis Pattern]]):**
"When debugging authentication issues, fixing the symptom (invalid credentials) can mask the root cause (wrong auth mechanism)."

**Actual root cause:**
The system should have been using OAuth, not API keys. The presence of `ANTHROPIC_API_KEY` in `.env` was overriding the correct OAuth flow.

## Impact

This assumption leads to misdiagnosis during authentication debugging. Teams may waste time rotating credentials or checking key storage when the real issue is auth method mismatch (API key vs OAuth vs session token vs etc).

![[assumption.base#Depends On This]]
![[assumption.base#Related]]

---
![[assumption.base#Depends On This]]

![[assumption.base#Related]]
