---
claim_a: API key was invalid and needed replacement
claim_b: API key should not have been used at all; OAuth was the correct method
created: '2026-03-07'
janitor_note: ''
name: Environment Variable Fix Narrative vs Temporal Reality
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related:
- '[[note/Personal Alfred API Key Bug Fix]]'
- '[[note/Personal Alfred API Key Bug Fix]]'
resolution: Documentation updated to reflect that API key fix was attempted first,
  then OAuth understanding developed, finally VAULT_PATH fix completed the solution
resolved_date: '2026-03-07'
source_a: note/Personal Alfred API Key Bug Fix (initial version)
source_b: note/Personal Alfred API Key Bug Fix (corrected version) and note/Environment
  Variable Precedence in Multi-Auth Systems
status: resolved
tags: []
type: contradiction
---

# Environment Variable Fix Narrative vs Temporal Reality

## Claim A

**From:** Initial version of [[note/Personal Alfred API Key Bug Fix]]

"The `.env` file contained an invalid Anthropic API key, preventing the system from functioning correctly. Found the correct API key stored in `~/.anthropic_api_key` and updated the `.env` file with the valid key. System now functions correctly."

This suggests the fix was straightforward: replace invalid key with valid key.

## Claim B

**From:** Corrected version of [[note/Personal Alfred API Key Bug Fix]] and [[note/Environment Variable Precedence in Multi-Auth Systems]]

"The `.env` file contained an `ANTHROPIC_API_KEY` environment variable that was overriding the OAuth authentication used by Claude Code... Initially thought the issue was an invalid API key that needed to be replaced... While this temporarily appeared to work, it wasn't addressing the root cause."

This reveals the API key fix was a **misdiagnosis** — the real issue was using API key auth instead of OAuth.

## Analysis

**Why the contradiction exists:**

The notes were written at different stages of understanding. The first version captured the immediate action taken (replace the key), while the second version captured the deeper understanding gained through continued investigation.

This is a classic debugging narrative arc:
1. **Symptom:** Invalid credentials
2. **First fix:** Replace credentials (treats symptom)
3. **Deeper understanding:** Wrong auth mechanism (treats root cause)
4. **Complete fix:** Remove API key, use OAuth + ensure VAULT_PATH propagates

## Resolution

**How it was resolved:**

The note was updated with a section titled "Initial Misdiagnosis" that explicitly acknowledges the evolution of understanding. The corrected version preserves both the initial response and the final understanding, making the learning journey visible.

**Key learning:** Authentication debugging should start with "which auth method should be used?" before jumping to "are the credentials valid?"

![[contradiction.base#Related]]
