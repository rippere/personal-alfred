---
based_on:
- '[[note/PM CRM Week 1-4 Build Summary]]'
confidence: high
created: '2026-05-04'
name: PM CRM Celery Workers Are Event-Triggered on Message Ingest Not Scheduled Polling
project:
- '[[project/PM CRM]]'
session: '[[session/PM CRM Development Session Apr 7]]'
source: PM CRM Week 1-4 Build Summary
source_date: '2026-04-07'
status: final
type: decision
---

# PM CRM Celery Workers Are Event-Triggered on Message Ingest Not Scheduled Polling

## Context
PM CRM uses Celery + Redis for async processing of incoming messages through the LLM extraction pipeline. A design choice was needed on whether workers should poll for new messages on a schedule or react to events when messages arrive at the ingest endpoint.

## Options Considered
1. **Scheduled polling** — worker runs on a timer, checks for unprocessed messages, processes them. Simple to implement but adds latency proportional to poll interval and wastes cycles when no messages are present.
2. **Event-triggered** — message ingest endpoint queues a Celery task immediately on receipt; worker processes as soon as capacity is free. Lower latency, no wasted cycles, natural fit for event-driven async architecture.

## Decision
Event-triggered: the Celery async worker is queued directly at the message ingest endpoint, not via a polling scheduler.

## Rationale
Real-time responsiveness matters for a CRM that surfaces task and metric insights. Polling would add unnecessary latency between message arrival and insight extraction. FastAPI's asyncio-native design pairs naturally with event-driven Celery dispatch via Redis. This approach also avoids a separate polling process, reducing operational complexity.

## Consequences
Worker availability becomes critical under load — if all workers are busy, messages queue in Redis. Queue depth monitoring is important for operational health. Under high-volume ingest, Redis becomes a key failure point and must be treated as infrastructure rather than ephemeral cache.

![[decision.base#Based On]]
![[decision.base#Related]]
