---
cluster_sources:
- '[[note/Personal Alfred API Key Bug Fix]]'
- '[[note/Personal Alfred VAULT_PATH Environment Variable Bug Fix]]'
- '[[note/Personal Alfred Vault Path Bug Fix]]'
confidence: medium
created: '2026-03-06'
name: Temporal Proximity Bias in Bug Documentation
project:
- '[[project/Personal Knowledge Management Infrastructure]]'
related: []
status: active
supports: []
tags: []
type: synthesis
---

# Temporal Proximity Bias in Bug Documentation

## Insight

When documenting a debugging session, there's a tendency to emphasize the most recently discovered issue while downplaying or conflating earlier issues. This creates a documentation pattern where:

1. **Initial bug reports are incomplete** - Focus on symptoms, not root cause
2. **Follow-up bug reports expand scope** - Later notes reveal the earlier diagnosis was partial
3. **Multiple notes document the same incident** - Each revision tells a slightly different story

## Evidence

Three notes document what appears to be a single debugging session, each with different emphasis:

**[[note/Personal Alfred API Key Bug Fix]]** (First version):
- Problem: "Invalid Anthropic API key in `.env`"
- Solution: "Found correct API key in `~/.anthropic_api_key`"
- Later revision adds: "Actually OAuth conflict, not invalid key"

**[[note/Personal Alfred VAULT_PATH Environment Variable Bug Fix]]** (Second issue):
- Problem: "Missing `ALFRED_VAULT_PATH` in subprocess"
- Context: "After successfully resolving the OAuth authentication issue..."
- **Treats VAULT_PATH as separate, sequential bug**

**[[note/Personal Alfred Vault Path Bug Fix]]** (Alternative version):
- Problem: "Missing `ALFRED_VAULT_PATH` in subprocess"
- Context: Mentions both OAuth and VAULT_PATH issues
- **Treats both as part of single debugging session**

## Implications

**For debugging:**
- Root cause analysis should happen before documentation
- First diagnosis is often incomplete - expect revision

**For documentation:**
- Create a single "session note" that gets updated as understanding evolves
- Avoid creating new notes for each revelation
- Clearly mark "initial diagnosis" vs "actual root cause"

**For knowledge extraction:**
- Later notes are more reliable than earlier ones (more complete context)
- Multiple notes about same incident indicate evolving understanding
- Check for temporal sequence - notes written minutes apart may document single event

## Applicability

This pattern applies to:
- **Debugging sessions** where understanding evolves over time
- **Incident post-mortems** where initial assessment changes
- **Root cause analysis** where symptoms are discovered before causes

**Mitigation strategies:**
1. Use session-based note-taking (one note, updated over time)
2. Add "Updated YYYY-MM-DD" timestamps when revising understanding
3. Preserve initial diagnosis with strikethrough when correcting
4. Create a single comprehensive note after debugging completes

![[synthesis.base#Sources]]
![[synthesis.base#Related]]

---
![[synthesis.base#Sources]]

![[synthesis.base#Related]]
