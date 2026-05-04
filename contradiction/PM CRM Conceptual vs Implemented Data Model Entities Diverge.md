---
claim_a: 'Architecture session defined six entities: Task, Metric, Communication,
  Assignment, User, TenantConfig'
claim_b: 'Implementation created seven SQLAlchemy models: Workspace, User, Connector,
  Message, Task, MetricTemplate/TaskMetric, ClarityScore'
created: '2026-05-04'
name: PM CRM Conceptual vs Implemented Data Model Entities Diverge
project:
- '[[project/PM CRM]]'
related:
- '[[session/PM CRM Initial Architecture Planning Session]]'
- '[[note/PM CRM Week 1-4 Build Summary]]'
source_a: session/PM CRM Initial Architecture Planning Session
source_b: note/PM CRM Week 1-4 Build Summary
status: unresolved
type: contradiction
---

# PM CRM Conceptual vs Implemented Data Model Entities Diverge

## Claim A
The April 5 architecture planning session defined six core data entities: Task, Metric, Communication, Assignment, User, TenantConfig.

## Claim B
The April 7 implementation created seven SQLAlchemy models: Workspace, User, Connector, Message, Task, MetricTemplate/TaskMetric, ClarityScore. Several entities were renamed, split, or dropped: "Communication" became "Message", "TenantConfig" was absorbed into "Workspace", "Connector" replaced the implicit channel abstraction, "ClarityScore" and "MetricTemplate/TaskMetric" broke apart the single "Metric" type, and "Assignment" appears to have been folded into Task or dropped entirely.

## Analysis
The divergence likely reflects intentional refinement during implementation — the builder adapted the conceptual model to actual API contracts and storage requirements. However, no decision record documents this. The most significant gap is the absence of "Assignment" as a standalone entity: the conceptual model implied explicit assignment tracking, but the implementation may handle this through Task fields.

## Resolution
Unresolved — no record documents why entity names and count changed between the April 5 design and the April 7 build. Should be confirmed against the actual schema in migrations/001_initial.sql.

![[contradiction.base#Related]]
