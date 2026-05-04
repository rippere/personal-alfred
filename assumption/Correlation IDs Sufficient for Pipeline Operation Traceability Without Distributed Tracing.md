---
based_on:
- '[[task/Implement Logging and Error Handling Infrastructure]]'
confidence: medium
created: '2026-05-04'
name: Correlation IDs Sufficient for Pipeline Operation Traceability Without Distributed
  Tracing
project:
- '[[project/Sector Flow Analyzer]]'
related:
- '[[assumption/JSON Structured Logging Suitable for Production Observability]]'
- '[[decision/Structured Logging with JSON Production Format]]'
- '[[assumption/Monitoring Hooks Enable Future Observability Stack Integration Without
  Refactoring]]'
source: task/Implement Logging and Error Handling Infrastructure
source_date: '2026-04-16'
status: active
type: assumption
---

# Correlation IDs Sufficient for Pipeline Operation Traceability Without Distributed Tracing

## Claim

Adding correlation IDs to structured log entries — to link log lines from different modules belonging to the same pipeline run — provides adequate operational traceability for the Sector Flow Analyzer without requiring dedicated distributed tracing infrastructure (e.g., Jaeger, Zipkin, OpenTelemetry).

## Basis

The logging task specifies "correlation IDs for request tracking" within a data pipeline context. Distributed tracing tools are typically used in microservice environments where requests cross process and network boundaries. The Sector Flow Analyzer is a single-process pipeline running on a single Raspberry Pi, so correlation IDs threaded through structured log output should be sufficient to diagnose cross-module issues.

## Evidence Trail

- **2026-04-16**: Logging task specifies correlation IDs as the tracing mechanism, with no mention of distributed tracing tooling in requirements or technical specs.
- The Observability Stack integration is deferred to a future phase — if that stack introduces distributed tracing, this assumption may be revisited.

## Impact

If this assumption is wrong — e.g., debugging a pipeline failure requires tracing execution across async boundaries or multiple processes — the team will need to retrofit distributed tracing. The impact is bounded by the single-host deployment constraint; full distributed tracing would only become necessary if the pipeline is decomposed into separate services.

![[assumption.base#Depends On This]]
![[assumption.base#Related]]
