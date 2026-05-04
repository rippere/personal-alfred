---
type: constraint
status: active
source: "TRIBE v2 model architecture (LLaMA 3.2-3B + V-JEPA2 + Wav2Vec-BERT) — Sprint 1 gTTS/WhisperX installation"
source_date: "2026-04-09"
authority: "TRIBE v2 model design — Wav2Vec-BERT component requires audio input"
project: ["[[project/Persuasion Observatory]]"]
location: []
related: ["[[assumption/Synthetic Audio from Web Text Retains Persuasion-Relevant Signal for Wav2Vec-BERT]]", "[[decision/Persuasion-Observatory-Architecture]]"]
created: "2026-05-04"
tags: [tribe-v2, multimodal, audio, pipeline]
---

# TRIBE v2 Multimodal Architecture Requires Audio Synthesis Step for Web Text Analysis

## Constraint

TRIBE v2 is a trimodal model: LLaMA 3.2-3B (text), V-JEPA2 (video/visual), and Wav2Vec-BERT (audio). Web content is primarily text and static images. The Wav2Vec-BERT component requires an audio waveform input; there is no native text-only operating mode.

To feed web text content into the full TRIBE v2 pipeline, the text must be converted to synthetic speech via text-to-speech (gTTS was installed during Sprint 1 setup), then processed through Wav2Vec-BERT as if it were spoken audio.

## Source

Inferred from: (1) TRIBE v2 model architecture documentation confirming three input modalities, (2) Sprint 1 dependency installation including gTTS (Google Text-to-Speech) and WhisperX for audio processing — these libraries have no other purpose in the current pipeline.

## Implications

- Every web content analysis requires a text→audio synthesis step, adding latency and a dependency on gTTS
- The synthesized audio is artificial — it was never "spoken" and may carry different prosodic features than the original content
- This adds an unvalidated assumption: that synthetic speech retains the persuasion-relevant acoustic features TRIBE v2's audio encoder was trained to detect
- Web pages with embedded video/audio could bypass this by extracting the native audio track (WhisperX may serve this purpose)
- The audio synthesis step adds ~100-500ms latency per analysis unit on top of the 1Hz base constraint

## Expiry / Review

This constraint applies as long as TRIBE v2 is used in its full trimodal form. It could be partially waived if the model is modified to run in text-only mode (using only the LLaMA 3.2-3B component), but this would require validating that the text encoder alone achieves acceptable accuracy.

![[constraint.base#Affected Projects]]
![[constraint.base#Related]]
