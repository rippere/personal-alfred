---
based_on:
- '[[note/Executive Digital Twin Pilot Executive Onboarding Questionnaire]]'
- '[[task/Build Call Ingestion Pipeline for Executive Digital Twin]]'
confidence: high
created: '2026-05-04'
name: Call Transcription Requires Explicit Exec Consent and Per-Service Opt-In
project:
- '[[project/Executive Digital Twin]]'
source: note/Executive Digital Twin Pilot Executive Onboarding Questionnaire
source_date: '2026-03-28'
status: active
type: assumption
---

# Call Transcription Requires Explicit Exec Consent and Per-Service Opt-In

## Claim
The call ingestion pipeline must not activate for any call service (Zoom, Google Meet, phone) without explicit exec consent. Consent is granted per service type, not as a blanket on/off permission. The exec can additionally exclude individual call categories even within a permitted service. The default state must be off until the exec explicitly opts in.

## Basis
The onboarding questionnaire explicitly asks: "Are you open to transcribing your calls so the system can draft follow-ups and learn how you speak? If yes — Zoom, Google Meet, phone, or all three? Are there call types you'd want excluded?" The build task confirms: "Coverage scope confirmed by exec questionnaire: Zoom, Google Meet, and phone calls, with exclusions to be specified by exec." The same privacy-first exclusion model used for email applies to calls.

## Evidence Trail
Consent model defined in questionnaire design. Actual scope will be determined when exec returns answers. Call pipeline implementation must implement per-service enable/disable configuration before ingestion begins.

## Impact
The call ingestion pipeline cannot be stood up with blanket access. Engineering must implement per-service configuration flags with safe-off defaults. This mirrors the email ingestion exclusion model — any future expansion to additional call services requires questionnaire update and explicit consent.

![[assumption.base#Depends On This]]
![[assumption.base#Related]]
