---
type: decision
status: final
confidence: high
source: "Strategic planning session with user"
source_date: "2026-04-09"
project: ["[[project/Persuasion Observatory]]"]
decided_by: ["[[person/Ben Rippere]]"]
approved_by: []
based_on: []
supports: ["[[project/Persuasion Observatory]]"]
challenged_by: []
session:
related: []
created: "2026-04-09"
tags: [architecture, product-strategy, business-model, neuroscience]
---

# Persuasion Observatory - Core Architecture & Strategy Decisions

## Context

Building a browser extension that uses Meta's TRIBE v2 brain encoding model to detect persuasion tactics in media. The project has dual purposes: (1) educational tool for media-literate users, and (2) research platform to collect data on real-world persuasion mechanics.

Multiple strategic tensions needed resolution before implementation:
- Protection vs. paternalism
- Privacy vs. effectiveness
- Free access vs. sustainability
- Accuracy vs. explainability
- Platform cooperation vs. evasion

## Key Decisions

### 1. Core Value Proposition: Educational, Not Prescriptive

**Decision**: Frame as "transparency engine" that teaches *how* content works, not *what* to think about it.

**Options Considered**:
- "Antivirus for your brain" (technical protection) - Rejected: Too paternalistic, creates dependency
- "Media literacy teacher" (educational empowerment) - **Selected**
- "Thought police" (imposes values) - Rejected: Violates user autonomy

**Rationale**:
- Respects user autonomy while providing information
- Informational focus: show somatotopic brain activation + rhetorical tactics
- TRIBE v2 outputs are descriptive (brain regions), not causal or prescriptive
- Data is generalized across populations, not individual-specific

**Consequences**:
- UI shows "High amygdala activation" + "This pattern often indicates fear appeals"
- Explanations focus on mechanisms ("how it works") not judgments ("this is bad")
- Users decide what's acceptable persuasion vs. manipulation

---

### 2. Business Model: Freemium with Power User Tier

**Decision**: Three-tier model with data flywheel economics.

**Tiers**:
1. **Free**: Pattern library only (local), 1-month lag on updates, covers ~80% of common tactics
2. **Premium** ($7/month): TRIBE v2 backend analysis, real-time updates, historical analytics
3. **Power** ($20/month): Premium + researcher features (bulk API, pattern contribution dashboard, commercial license)

**Options Considered**:
- Donation model - Rejected: Rarely covers costs, unsustainable
- Simple freemium (Free + Premium only) - Rejected: Doesn't solve "paradox of maturity" (as library improves, premium value decreases)
- Grant-funded only - Rejected: Time-limited, bureaucratic
- **Freemium + Power tier** - Selected

**Rationale**:
- Solves freemium paradox: Power tier value shifts from "detection" to "research capabilities"
- Premium users subsidize pattern library → benefits free tier → network effects
- Data flywheel: Premium analyses → pattern extraction → free tier improves → more users → more data
- Power tier enables professional use (journalists, educators, researchers)
- Can pursue grants while maintaining sustainable revenue model

**Consequences**:
- Early adopters pay to build infrastructure that eventually benefits everyone
- Research dataset becomes valuable asset (academic publications, licensing)
- Need clear data usage transparency and user consent

---

### 3. Privacy Stance: Pragmatic Transparency

**Decision**: Hybrid architecture with local-first option and transparent backend data collection.

**Options Considered**:
- Full backend (high protection, low privacy) - Rejected: Betrays trust
- Full local (high privacy, low protection) - Rejected: Limits accuracy, hard to implement
- **Hybrid: Pattern library + selective API** - Selected
- Federated learning - Rejected: Too complex for v1

**Rationale**:
- Target audience already has data harvested by platforms "for far more malicious purposes"
- Goal is to "enable them to understand this" not to protect privacy at all costs
- Transparency > privacy maximalism: explain trade-offs clearly
- Local-first option available for privacy-conscious users
- Explicit consent for data collection, with clear value exchange

**Implementation**:
- Free tier: 100% local, zero data collection
- Premium tier: Backend analysis with consent, anonymized storage
- Users see their contribution: "Your analysis helped grow the library by 3 patterns"
- Open source extension code for verification
- Monthly transparency reports

**Consequences**:
- Some privacy advocates won't use it - acceptable trade-off
- Legal/ethical position is strong (explicit consent, clear value)
- Can still pursue academic partnerships and grants

---

### 4. Platform Strategy: Fly Under Radar

**Decision**: Avoid confrontation with social media platforms through descriptive language and technical obfuscation.

**Options Considered**:
- Open confrontation (public advocacy) - Rejected: David vs. Goliath, legal costs
- Platform cooperation - Rejected: Loss of control, mission drift
- **Stealth approach** - Selected
- Platform independence (Mastodon only) - Rejected: Limited impact

**Rationale**:
- Don't want to "deal with fighting legal teams"
- Platforms have financial incentive to block persuasion detection
- Descriptive framing reduces attack surface

**Implementation**:
- Language: "Persuasion techniques" not "manipulation"
- UI: "This content activates fear-processing regions" not "Facebook is manipulating you"
- Technical: Obfuscated class names, anti-fingerprinting, no DOM modifications
- Educational framing: "Media literacy tool" not "manipulation detector"
- Start on open platforms (YouTube, Reddit) before tackling walled gardens

**Consequences**:
- Lower profile = lower risk of platform blocking
- May need to pivot to standalone web app if platforms detect and block
- Less marketing punch (can't say "protect yourself from Facebook")

---

### 5. Technical Architecture: Local-First with Cloud Augmentation

**Decision**: Start with local TRIBE v2 deployment, migrate to cloud GPU only when paying users exist.

**Timeline**:
- Weeks 1-8: Local GPU deployment (zero marginal cost)
- Weeks 9+: Cloud GPU (RunPod) only if ≥10 paying users

**Options Considered**:
- Cloud from day 1 - Rejected: $300-500/month cost before revenue
- **Local → Cloud migration** - Selected
- Local only forever - Rejected: Limits scale

**Tech Stack**:
- Extension: Vanilla JavaScript (lightweight, no build step)
- Backend: Python 3.11+, FastAPI, PyTorch
- Database: PostgreSQL (cloud analyses), SQLite (local pattern library)
- Model: TRIBE v2 (LLaMA 3.2-3B + V-JEPA2 + Wav2Vec-BERT)
- Cloud GPU: RunPod (cheapest on-demand)

**Rationale**:
- Validate model performance before paying for cloud
- User likely has gaming GPU that can run inference
- Migration is straightforward (same API, different endpoint)
- De-risks financial commitment

**Consequences**:
- Early beta limited to users you can support locally
- Can't scale to thousands of users until cloud deployment
- Need to budget ~$500/month for GPU costs at scale

---

### 6. Platform Prioritization: YouTube First

**Decision**: Target YouTube for MVP, then expand to Twitter/X and Reddit.

**Sequence**: YouTube (Sprint 2) → Twitter/X (Sprint 4) → Reddit (Sprint 4) → Facebook (Sprint 6+)

**Options Considered**:
- Social media feeds first (Facebook/X/Instagram) - Rejected: Complex, adversarial
- **YouTube first** - Selected
- Universal extension from day 1 - Rejected: Too ambitious

**Rationale**:
- Content density: Long-form video transcripts = rich persuasion content
- Extraction reliability: YouTube captions API is stable
- User value: Educational/news YouTube has high concentration of tactics
- Technical simplicity: Single DOM structure, no rate limits
- Monetization alignment: Users already pay for YouTube Premium

**Consequences**:
- Narrow initial focus enables faster iteration
- Need to expand to other platforms for comprehensive coverage
- YouTube may still block if detected

---

### 7. Accuracy vs. Explainability: Multi-Level Explanations

**Decision**: Provide layered explanations that balance technical accuracy with user understanding.

**Approach**:
```
Level 1 (Always show): "High emotional content detected"
Level 2 (Click for details): "Amygdala: 0.78, Prefrontal Cortex: 0.42"
Level 3 (Educational): "This pattern often indicates fear appeals because..."
```

**Options Considered**:
- Raw brain data only - Rejected: No one understands it
- **Multi-level explanations** - Selected
- Specific tactic labels only - Rejected: Introduces interpretation bias

**Rationale**:
- Different users need different levels of detail
- Tech-savvy users can drill down to brain regions
- Casual users get simple summaries
- Educational layer builds media literacy over time

**Consequences**:
- More complex UI to implement
- Need to build explanation templates for each tactic
- Reduces risk of misinterpretation

---

### 8. Pattern Library: 500 Minimum, 2000 Target

**Decision**: Seed library with 500 patterns manually, grow to 2000 via user contributions.

**Coverage Goals**:
- 500 patterns = ~50% coverage (based on Zipf's law)
- 2000 patterns = ~80% coverage
- 5000 patterns = ~90% coverage (6-month goal)

**Bootstrapping Process**:
1. Manually curate 100 examples of persuasion tactics (Week 1-2)
2. Run through TRIBE v2 (one-time cost)
3. Extract patterns via clustering
4. Package as SQLite database (~50-100MB)
5. Ship with extension for local-only operation

**Rationale**:
- 500 patterns enable viable free tier from day 1
- Users won't tolerate <50% accuracy
- Manual curation ensures quality before automation
- Provides research value even if product fails

**Consequences**:
- Requires significant upfront work (Week 1-2)
- Initial library quality determines free tier adoption
- Need pattern extraction pipeline for ongoing growth

---

## Implementation Priorities

Based on these decisions, the implementation sequence is:

1. **Sprint 1 (Weeks 1-2)**: Validate TRIBE v2 accuracy on test dataset (go/no-go gate)
2. **Sprint 2 (Weeks 3-4)**: Build MVP extension (YouTube only, local backend)
3. **Sprint 3 (Weeks 5-6)**: Create pattern library (500+ patterns, local matching)
4. **Sprint 4 (Weeks 7-8)**: Multi-platform expansion (Twitter/X, Reddit)
5. **Sprint 5-6 (Weeks 9-12)**: Premium launch (cloud GPU, Stripe, auth)
6. **Sprint 7-8 (Weeks 13-16)**: Data flywheel optimization (pattern quality, updates)

---

## Open Questions

1. **Commercial licensing**: If product succeeds, will Meta grant commercial license for TRIBE v2?
2. **Pattern library update frequency**: Weekly? Monthly? User-triggered?
3. **Premium pricing**: Is $7/month optimal, or should we test $5 vs. $10?
4. **Platform blocking**: What's the fallback if YouTube blocks the extension?
5. **Grant funding**: Which organizations align with mission (Mozilla, Knight, NSF)?

---

## Review Criteria

This decision should be reviewed if:
- TRIBE v2 accuracy <60% (Week 2) - May need to pivot model
- 0 paying users after 100 signups (Week 12) - Business model invalid
- Platform blocks extension (any time) - Need stealth strategy revision
- User feedback contradicts assumptions (Week 4) - UX needs rework

![[decision.base#Based On]]
![[decision.base#Related]]
