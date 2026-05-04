---
based_on:
- '[[session/i2p-anonymous-network—2026-04-22—initial-setup]]'
confidence: medium
created: '2026-05-04'
name: Java I2P Memory Overhead Is Acceptable for Personal Use
project:
- '[[project/I2P Anonymous Network]]'
source: Session — I2P initial setup, decision to use Java I2P over i2pd
source_date: '2026-04-22'
status: active
type: assumption
---

# Java I2P Memory Overhead Is Acceptable for Personal Use

## Claim

The higher memory usage of the official Java-based I2P router compared to i2pd (C++ native implementation) is acceptable for personal use on this system.

## Basis

When choosing between Java I2P and i2pd, the trade-off of "Java dependency and higher memory usage vs native performance" was explicitly acknowledged and the Java implementation was selected. Accepting this trade-off implies the memory overhead is not a blocker for the intended use case.

## Evidence Trail

- 2026-04-22: Java I2P v2.12.0 selected over i2pd despite explicit acknowledgment of higher memory usage; no memory concerns raised.

## Impact

If system memory becomes constrained or the router is deployed on a low-RAM environment, this assumption should be revisited and i2pd reconsidered as an alternative.

![[assumption.base#Depends On This]]
![[assumption.base#Related]]
