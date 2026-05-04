---
based_on:
- '[[note/Personal Alfred API Key Bug Fix]]'
challenged_by: []
confidence: medium
confirmed_by:
- '[[decision/Comment Out Conflicting Environment Variables Rather Than Delete]]'
created: '2026-03-07'
invalidated_by: []
janitor_note: ''
name: Commenting Out Config Is Better Than Deleting
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related:
- '[[synthesis/Configuration Files as Documentation]]'
source: Personal Alfred API Key Bug Fix session
source_date: '2026-03-07'
status: confirmed
tags: []
type: assumption
---

# Commenting Out Config Is Better Than Deleting

## Claim

When resolving configuration conflicts (like the `ANTHROPIC_API_KEY` in `.env`), commenting out the conflicting line is preferable to deleting it entirely.

## Basis

This reflects a general systems administration principle: preserve historical configuration for documentation and potential future reference. Commented-out config serves as inline documentation of what was tried and why it was disabled.

## Evidence Trail

**Applied (2026-03-07):** During the Personal Alfred OAuth fix, the decision was made to "comment out the `ANTHROPIC_API_KEY` in the `.env` file" rather than delete it.

This was formalized in [[decision/Comment Out Conflicting Environment Variables Rather Than Delete]].

## Impact

This principle affects:
- **Debugging:** Future debugging can see what was previously configured
- **Documentation:** Config files become self-documenting artifacts showing evolution
- **Reversibility:** Easy to re-enable if needed for different contexts

**Related assumption:** Configuration files serve dual purpose as runtime config and documentation ([[synthesis/Configuration Files as Documentation]]).

![[assumption.base#Depends On This]]
![[assumption.base#Related]]

---
![[assumption.base#Depends On This]]

![[assumption.base#Related]]
