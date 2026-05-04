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
name: Dotenv Files Override Application Auth Config
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related:
- '[[decision/Use OAuth for Personal Alfred Authentication]]'
- '[[decision/Comment Out Rather Than Delete Conflicting Auth Config]]'
source: Personal Alfred OAuth debugging session
source_date: 2026-03
status: confirmed
tags: []
type: assumption
---

# Dotenv Files Override Application Auth Config

## Claim

When both a `.env` file contains an authentication credential (like `ANTHROPIC_API_KEY`) AND an application has its own native authentication method (like OAuth), the environment variable from `.env` will take precedence and override the application's built-in auth mechanism.

## Basis

This assumption was confirmed during personal-alfred setup when:
- Claude Code was configured to use OAuth authentication (its native method)
- `.env` file contained `ANTHROPIC_API_KEY=invalid_key`
- The invalid API key from `.env` overrode Claude Code's OAuth flow, causing auth failures
- Commenting out the environment variable allowed OAuth to work correctly

This reveals a precedence hierarchy: environment variables > application config > application defaults.

## Evidence Trail

**Confirmed:** [[note/Personal Alfred API Key Bug Fix]] - OAuth authentication only worked after commenting out the conflicting `ANTHROPIC_API_KEY` in `.env`

## Impact

- [[decision/Use OAuth for Personal Alfred Authentication]] depends on this understanding
- [[decision/Comment Out Rather Than Delete Conflicting Auth Config]] emerged from this confirmation
- System designers must be aware that `.env` files can silently override intended auth mechanisms

![[assumption.base#Depends On This]]
![[assumption.base#Related]]

---
![[assumption.base#Depends On This]]

![[assumption.base#Related]]
