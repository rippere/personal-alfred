---
type: project
status: active
name: Persuasion Observatory
description: Browser extension and research platform using TRIBE v2 to detect and explain persuasion tactics in media
client:
parent:
owner: "[[person/Ben Rippere]]"
location:
related: []
relationships: []
supports: ["[[Media literacy education]]", "[[Neuroscience research on persuasion]]"]
based_on: ["[[decision/Persuasion-Observatory-Architecture]]"]
depends_on: []
blocked_by: []
approved_by: []
created: "2026-04-09"
tags: [neuroscience, browser-extension, media-literacy, machine-learning, persuasion]
---

# Persuasion Observatory

A dual-purpose platform that combines a **media literacy browser extension** with a **persuasion research system**. Uses Meta's TRIBE v2 brain encoding model to detect and explain rhetorical manipulation tactics in real-time across social media, video, and web content.

## Purpose

**Primary Goal**: Build a research platform to understand persuasion mechanics at scale through real-world data collection.

**Secondary Goal**: Provide an educational tool for media-conscious users to understand how content is engineered to influence them.

**Target Audience**: Tech-savvy, media-literate users who are already somewhat skeptical and want to "see the matrix" of persuasion tactics.

---

## Project Objectives

1. **Technical Validation** (Weeks 1-2): Prove TRIBE v2 can accurately detect and explain persuasion tactics
2. **MVP Extension** (Weeks 3-4): Build basic browser extension with YouTube support
3. **Pattern Library** (Weeks 5-6): Create local database of 500+ persuasion signatures for fast matching
4. **Multi-Platform** (Weeks 7-8): Expand to Twitter/X and Reddit
5. **Premium Launch** (Weeks 9-12): Deploy cloud backend, implement freemium model
6. **Data Flywheel** (Weeks 13-16): Optimize pattern library growth from user contributions

---

## Business Model

**Freemium with research value exchange:**

- **Free Tier**: Local pattern library only (1-month lag on updates), covers ~80% of common tactics
- **Premium Tier** ($7/month): TRIBE v2 backend analysis for novel content, real-time pattern updates, historical analytics
- **Power Tier** ($20/month): Premium + researcher features (bulk API, pattern contribution dashboard, commercial license)

**Data Flywheel**: Premium users' analyses feed pattern library → improves free tier → attracts more users → more data → better patterns

---

## Technical Architecture

### Core Components

1. **Browser Extension** (Chrome/Firefox Manifest V3)
   - Content script: Extracts text/video/audio from web pages
   - Background worker: Orchestrates analysis (local vs. backend)
   - Popup UI: Displays detected tactics with explanations

2. **Local Pattern Library** (SQLite, ~50-100MB)
   - Pre-computed persuasion signatures
   - Fast fuzzy matching
   - Offline-first capability

3. **Backend API** (FastAPI + PostgreSQL)
   - TRIBE v2 model serving (GPU required)
   - User authentication (Firebase/Supabase)
   - Analysis storage and pattern extraction
   - Stripe subscription management

4. **Pattern Extraction Pipeline**
   - Batch processing of user-submitted analyses
   - Clustering and de-duplication
   - Weekly pattern library updates

### Technology Stack

- **Extension**: Vanilla JavaScript (lightweight, no build step)
- **Backend**: Python 3.11+, FastAPI, PyTorch
- **Database**: PostgreSQL (analyses, patterns), SQLite (local library)
- **ML Model**: Meta TRIBE v2 (LLaMA 3.2 + V-JEPA2 + Wav2Vec-BERT)
- **Deployment**: RunPod/Lambda Labs (GPU), Docker containers
- **Payments**: Stripe

---

## Key Constraints

1. **License**: TRIBE v2 is CC-BY-NC-4.0 (non-commercial only) - must remain free/non-profit or obtain commercial license
2. **Privacy**: Pragmatic transparency - explicit consent for data collection, local-first option available
3. **Platform Relations**: Must fly under radar - descriptive language, no page modifications, avoid legal fights
4. **Accuracy vs. Explainability**: Optimize for both - show brain regions + translate to understandable tactics
5. **GPU Costs**: Backend inference expensive - start local, migrate to cloud only with paying users

---

## Success Metrics

### Phase 1 (Weeks 1-2)
- TRIBE v2 accuracy >70% on test dataset
- Explanations rated 4/5+ for clarity

### Phase 2 (Weeks 3-4)
- 3/5 beta users say "would use daily"
- 90%+ analysis success rate

### Phase 3 (Weeks 5-6)
- Pattern library achieves 50%+ of TRIBE v2 accuracy at 10x speed
- 500+ unique patterns

### Phase 4-5 (Weeks 7-12)
- Multi-platform support (YouTube, Twitter, Reddit)
- 10 paying users, $70 MRR
- 80% retention month 1

### Phase 6 (Weeks 13-16)
- Pattern library growth +20%/month
- Free tier accuracy improves measurably

### North Star (6 months)
- 10,000 DAU
- 5% free → premium conversion
- 5,000+ pattern library
- 70% pattern matching accuracy

---

## Risk Mitigation

### High-Priority Risks

1. **TRIBE v2 Underperforms** (40% likelihood)
   - Mitigation: Validate in Week 2, fallback to fine-tuned DistilBERT

2. **GPU Cost Overruns** (60% likelihood)
   - Mitigation: Start local, strict rate limits, spot instances, $500/month budget cap

3. **Low Adoption** (50% likelihood)
   - Mitigation: Heavy beta testing Week 4, pivot to B2B/grants if needed

4. **Platform Blocking** (30-40% likelihood)
   - Mitigation: Descriptive language, no DOM modifications, fallback to standalone web app

### Stop Criteria

- Week 2: TRIBE v2 accuracy <60%
- Week 12: 0-2 paying users after 100 signups
- Week 16: Costs exceed revenue with no path to profitability

---

## Assumptions
![[project.base#Assumptions]]

## Decisions
![[project.base#Decisions]]

## Constraints
![[project.base#Constraints]]

## Contradictions
![[project.base#Contradictions]]

## Dependencies
![[project.base#Dependencies]]

## Tasks
![[project.base#Tasks]]

## Sub-projects
![[project.base#Sub-projects]]

## Sessions
![[project.base#Sessions]]

## Learnings
![[project.base#Learnings]]

## Conversations
![[project.base#Conversations]]

## Inputs
![[project.base#Inputs]]

## Notes
![[project.base#Notes]]
