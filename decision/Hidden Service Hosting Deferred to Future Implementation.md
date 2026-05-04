---
confidence: high
created: '2026-05-04'
name: Hidden Service Hosting Deferred to Future Implementation
project:
- '[[project/I2P Anonymous Network]]'
session: '[[session/i2p-anonymous-network—2026-04-22—initial-setup]]'
source: I2P Usage SOP scope planning — initial setup session
source_date: '2026-04-22'
status: final
type: decision
---

# Hidden Service Hosting Deferred to Future Implementation

## Context

During creation of the I2P Usage SOP, the scope of the initial implementation needed to be defined. I2P supports both client-side usage (anonymous browsing, CLI proxying) and server-side usage (hosting hidden services — eepsites, server tunnels accessible within the I2P network).

## Options Considered

1. **Include hidden service hosting** — Cover server tunnel and eepsite setup in the initial SOP alongside client-side usage.
2. **Defer hidden service hosting** — Focus initial scope on client-side proxy usage; mark server-side hosting as future scope.

## Decision

Hidden service hosting was explicitly excluded from the initial SOP and implementation scope, deferred to a future phase.

## Rationale

The primary use case for this implementation is anonymous client-side activity: proxied browsing, CLI tool routing, and automated workflow integration via SOCKS5. Server-side hosting (eepsites, I2P server tunnels) adds significant complexity and distinct OPSEC requirements that are not needed for this use case. Getting client-side usage reliable and well-documented was the correct first milestone.

## Consequences

The existing SOP covers pre-flight checks, proxy configuration (SOCKS5 port 4447, HTTP port 4444), CLI tool integration, post-session cleanup, and emergency procedures. A future implementation phase will need to separately cover: eepsite setup, server tunnel configuration, and server-specific OPSEC.

![[decision.base#Based On]]
![[decision.base#Related]]
