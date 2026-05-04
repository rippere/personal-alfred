---
based_on:
- '[[project/Personal Knowledge Management Infrastructure]]'
challenged_by: []
confidence: medium
confirmed_by: []
created: '2026-03-07'
invalidated_by: []
janitor_note: ''
name: Project Ownership Is Optional
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related: []
source: Project record schema
source_date: '2026-03-06'
status: active
tags: []
type: assumption
---

# Project Ownership Is Optional

## Claim

The Alfred OS project record schema assumes that projects can exist and be actively managed without a designated owner. The `owner` field is nullable.

## Basis

Observed on [[project/Personal Knowledge Management Infrastructure]]:

```yaml
owner: null
status: active
```

This is an active project (not abandoned or proposed) yet has no assigned owner. The system does not enforce ownership requirements or flag this as a validation error.

## Evidence Trail

**2026-03-06:** Project created with active status and null owner. No janitor errors generated.

This contrasts with other fields that ARE validated (e.g., base view embeds generate LINK001 janitor notes when broken).

## Impact

- Personal projects may not require explicit ownership tracking
- Ownership becomes meaningful primarily for delegation, accountability, and permission contexts
- System must handle queries about "who owns this" gracefully when owner is null
- Task assignment can exist independently of project ownership (tasks can have `assigned` even if project has no `owner`)

**Potential challenges:**
- Unclear who to notify for project-level issues
- Ambiguity about decision authority if ownership is undefined

![[assumption.base#Depends On This]]
![[assumption.base#Related]]

---
![[assumption.base#Depends On This]]

![[assumption.base#Related]]
