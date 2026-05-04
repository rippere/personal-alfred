---
based_on: []
challenged_by: []
confidence: medium
confirmed_by: []
created: '2026-03-09'
invalidated_by: []
janitor_note: ''
name: Project Related Field Captures External Context Not Internal Records
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related: []
source: Project record relationship analysis
source_date: '2026-03-09'
status: active
tags: []
type: assumption
---

# Project Related Field Captures External Context Not Internal Records

## Claim

The Alfred OS system assumes that the project `related` field is for capturing external context and meta-knowledge (synthesis records, key collaborators, architectural decisions) rather than operational records (tasks, sessions, notes). Operational records link TO projects via their own `project` field, while projects link OUT to synthesis and people via `related`.

## Basis

Observed on [[project/Personal Knowledge Management Infrastructure]]:

```yaml
related: [
  "[[synthesis/API Key Verification for AI Systems]]",
  "[[person/David]]",
  "[[person/David Szabo-Stuban]]",
  "[[synthesis/Configuration Files as Documentation]]",
  "[[synthesis/Subprocess Environment Debugging Pattern]]"
]
```

The `related` field contains:
- 3 synthesis records (meta-knowledge)
- 2 person records (key collaborators)

It does NOT contain:
- Task records (though tasks exist for this project)
- Session records (though sessions exist)
- Note records (though notes exist)

This suggests a bidirectional linking strategy:
- **Operational records → project:** Tasks, sessions, notes link to project via their `project` field
- **Project → meta-knowledge:** Projects link to synthesis, key people via `related` field

## Evidence Trail

**2026-03-09:** Project has base view embeds for operational records (Tasks, Sessions, Notes sections) but uses `related` field for synthesis and people.

## Impact

- The `related` field serves as "project intelligence" — key insights and collaborators
- Base view queries discover operational records automatically via backlinks
- This creates clean separation between "what work is happening" (discovered) and "what we learned" (curated)
- Manual curation is required for the `related` field, while operational records self-organize

![[assumption.base#Depends On This]]
![[assumption.base#Related]]

---
![[assumption.base#Depends On This]]

![[assumption.base#Related]]
