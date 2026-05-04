---
based_on:
- '[[project/Personal Knowledge Management Infrastructure]]'
challenged_by: []
confidence: high
confirmed_by: []
created: '2026-03-07'
invalidated_by: []
janitor_note: ''
name: Projects Use Template Structure Until Customized
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related:
- '[[synthesis/Zero-Friction Capture Over User Control]]'
source: Project template usage pattern
source_date: '2026-03-06'
status: active
tags: []
type: assumption
---

# Projects Use Template Structure Until Customized

## Claim

Alfred OS project records are created from templates with standardized base view embeds. Projects begin with template structure intact and are customized progressively as work begins.

## Basis

Observed on [[project/Personal Knowledge Management Infrastructure]] — the entire body consists of base view embeds with no custom content:

```markdown
# Personal Knowledge Management Infrastructure

Brief description of the project's purpose and goal.

---

## Assumptions
![[project.base#Assumptions]]

## Decisions
![[project.base#Decisions]]
...
```

The placeholder text ("Brief description of the project's purpose and goal") remains, indicating this is a freshly created project that hasn't been customized yet.

## Evidence Trail

**2026-03-06:** Project created with template structure, status set to `active`, but body content remains at template defaults.

This pattern supports lazy initialization — projects can be created and linked immediately, with details filled in as needed.

## Impact

- Projects can exist as "stubs" with minimal information
- Template structure ensures consistency across all projects
- Base view embeds provide dynamic content even before manual customization
- Users can create project records quickly without front-loading documentation work

**Aligns with:** [[synthesis/Zero-Friction Capture Over User Control]] — favor immediate capture over complete documentation

**Potential issue:** Template placeholder text might not be obvious to users, leading to confusion about whether a project is "real" or just a stub

![[assumption.base#Depends On This]]
![[assumption.base#Related]]

---
![[assumption.base#Depends On This]]

![[assumption.base#Related]]
