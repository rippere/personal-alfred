---
based_on:
- '[[note/Personal Alfred VAULT_PATH Environment Variable Bug Fix]]'
- '[[note/Personal Alfred Vault Path Bug Fix]]'
challenged_by: []
confidence: medium
confirmed_by: []
created: '2026-03-07'
invalidated_by: []
janitor_note: ''
name: OAuth Is Preferred for Interactive Tools API Keys for Automation
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related: []
source: Debugging session insights
source_date: '2026-02-16'
status: active
tags: []
type: assumption
---

# OAuth Is Preferred for Interactive Tools API Keys for Automation

## Claim

The personal-alfred architecture assumes:
- **OAuth authentication** is the correct choice for interactive, user-facing tools (like Claude Code)
- **API key authentication** is better suited for server-side automation and non-interactive scripts

## Basis

Emerged from debugging sessions where mixing auth methods caused conflicts. The system architecture implicitly separates concerns:
- Human interaction layer → OAuth (delegated user authorization, browser-based)
- Automation layer → API keys (direct credential passing, programmatic)

## Evidence Trail

- **2026-02-16:** [[note/Personal Alfred VAULT_PATH Environment Variable Bug Fix]] explicitly documents "OAuth vs API Key Authentication" learning
- **2026-02-16:** [[note/Personal Alfred Vault Path Bug Fix]] reinforces the same distinction

This assumption guides integration decisions but hasn't been explicitly validated against all use cases.

## Impact

Affects how new integrations are designed:
- Interactive components (UI, CLI with user prompts) → plan for OAuth
- Background workers (cron jobs, event processors) → plan for API keys
- Hybrid tools need to support both and document which is preferred for which context

![[assumption.base#Depends On This]]
![[assumption.base#Related]]

---
![[assumption.base#Depends On This]]

![[assumption.base#Related]]
