---
based_on:
- '[[decision/Comment Out Rather Than Delete Conflicting Auth Config]]'
- '[[note/Environment Variable Precedence in Multi-Auth Systems]]'
challenged_by: []
confidence: medium
confirmed_by: []
created: '2026-03-07'
invalidated_by: []
name: Commented Config Serves as Historical Documentation
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related:
- '[[synthesis/Configuration Files as Documentation]]'
source: Personal Alfred debugging session
source_date: 2026-03
status: active
tags: []
type: assumption
---

# Commented Config Serves as Historical Documentation

## Claim

Commenting out configuration lines (rather than deleting them) serves a dual purpose: (1) disabling the config, and (2) preserving a visible record of what was tried, why it didn't work, and what the correct approach is.

This assumes that configuration files function as inline operational documentation, not just runtime settings.

## Basis

During personal-alfred OAuth debugging:
- The conflicting `ANTHROPIC_API_KEY` was commented out rather than deleted
- The comment preserved evidence of the misconfiguration for future troubleshooting
- Future developers can see what was attempted and why it was wrong

This pattern treats `.env` and similar config files as living documentation of system evolution.

## Evidence Trail

**Based on:** [[decision/Comment Out Rather Than Delete Conflicting Auth Config]] - Explicitly chose commenting over deletion

**Supports:** [[synthesis/Configuration Files as Documentation]] - Part of the broader pattern

## Impact

- Debugging sessions benefit from seeing historical config attempts
- New team members can understand why certain approaches were rejected
- Configuration files become a knowledge layer, not just a runtime layer

![[assumption.base#Depends On This]]
![[assumption.base#Related]]

---
![[assumption.base#Depends On This]]

![[assumption.base#Related]]
