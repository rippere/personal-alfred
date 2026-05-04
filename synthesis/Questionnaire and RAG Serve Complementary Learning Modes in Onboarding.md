---
cluster_sources:
- '[[note/Executive Digital Twin Pilot Executive Onboarding Questionnaire]]'
- '[[note/Executive Digital Twin Style Fingerprinting Architecture]]'
- '[[session/Executive Digital Twin Planning and Architecture Session]]'
confidence: high
created: '2026-05-04'
name: Questionnaire and RAG Serve Complementary Learning Modes in Onboarding
project:
- '[[project/Executive Digital Twin]]'
status: active
supports:
- '[[assumption/Six to Twelve Months Email History Sufficient for Style Fingerprinting]]'
- '[[synthesis/RAG on Email History Supersedes Explicit Style Questionnaires]]'
type: synthesis
---

# Questionnaire and RAG Serve Complementary Learning Modes in Onboarding

## Insight
The onboarding system is not a choice between questionnaire and RAG — they serve structurally different learning functions. RAG learns empirically from behavioral data (writing style, vocabulary, email rhythm, response patterns). The questionnaire captures what RAG cannot infer by design: consent boundaries, trust calibration thresholds, and explicit configuration preferences. The two modes are not alternatives but complements, each covering what the other cannot reach.

## Evidence
The 46-question questionnaire was reduced to 15 after recognizing that "Parts 1–2 of the original questionnaire (writing style, email rhythm) are better learned empirically." The remaining 15 questions cover exactly three categories: consent & hard limits, trust calibration, and goals & feedback preferences — all require explicit human declaration rather than behavioral inference. The synthesis `RAG on Email History Supersedes Explicit Style Questionnaires` is now superseded precisely because the questionnaire was not eliminated, only pruned to its structurally irreplaceable questions.

## Implications
Future questionnaire design should apply a single test before adding any question: "Could RAG learn this from behavioral data?" If yes, remove the question and let the model learn it. If no, keep it. This prevents questionnaire bloat while ensuring the system captures everything only the exec can provide. The same division applies to any future exec expansion — the RAG/questionnaire boundary is the correct default onboarding model for this product class.

## Applicability
Applies to Executive Digital Twin onboarding design and to any future multi-exec expansion. The principle generalizes: in any system that ingests behavioral data, explicit questionnaires should cover consent, trust, and configuration only — never style or pattern learning.

![[synthesis.base#Sources]]
![[synthesis.base#Related]]
