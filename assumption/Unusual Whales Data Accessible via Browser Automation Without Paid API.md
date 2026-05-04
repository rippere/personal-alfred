---
based_on: []
challenged_by: []
confidence: low
confirmed_by: []
created: '2026-05-04'
invalidated_by: []
janitor_note: ''
name: Unusual Whales Data Accessible via Browser Automation Without Paid API
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related: []
source: 1:1 meeting notes 2026-04-15
source_date: '2026-04-15'
status: active
tags: []
type: assumption
---

# Unusual Whales Data Accessible via Browser Automation Without Paid API

## Claim

Options flow data from Unusual Whales can be accessed by automating the browser interface (via Playwright or Claude Desktop's browser tool) rather than paying for the Unusual Whales API subscription.

## Basis

Mentioned in 1:1 notes (2026-04-15): "Playwright or Claude desktop to scan thru unusual whales to get around api" — an exploratory idea for accessing real-time options flow data without a paid API key.

## Evidence Trail

- **2026-04-15**: Raised during 1:1 as a potential low-cost alternative to the Unusual Whales paid API tier
- **Supporting pattern**: Claude Desktop's browser automation tool can interact with authenticated web sessions that Playwright cannot directly replicate

## Impact

- If valid: enables real-time options flow data ingestion at zero marginal cost
- If invalid: paid API subscription required for reliable, structured data access
- Risk: Unusual Whales may rate-limit, detect, or block browser automation; ToS may prohibit scraping
- Next step to validate: test Playwright against public Unusual Whales pages; check Claude Desktop browser tool against authenticated session

![[assumption.base#Depends On This]]
![[assumption.base#Related]]

---
![[assumption.base#Depends On This]]

![[assumption.base#Related]]
