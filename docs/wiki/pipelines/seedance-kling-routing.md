---
title: Seedance and Kling Routing
created: 2026-06-25
updated: 2026-06-25
type: pipeline
tags: [ai-video, seedance, kling, higgsfield, prompt-engineering, qa]
sources: []
confidence: high
---

# Seedance and Kling Routing

## Seedance 2.0

Use for:

- stronger cinematic motion;
- identity-sensitive scenes;
- 4–15 second clips;
- genre-controlled shots;
- serious film beats.

Prefer 5–8 seconds and 720p unless 1080p is approved. Related: [[ai-film-qa-loop]].

Risk zones:

- public-figure likeness;
- celebrity/deepfake concerns;
- too many actions;
- long single-shot prompts;
- expensive retry loops.

## Kling 3.0

Use for:

- atmospheric image-to-video;
- controlled start/end transitions;
- budget-sensitive clips;
- subtle motion;
- restrained camera drift.

Risk zones:

- large unrelated morphs;
- many characters;
- exact text;
- aggressive choreography.

## Failure handling

- Separate transient API failure from terminal model failure.
- Inspect job IDs and JSON before retrying.
- Change one prompt variable at a time.
- Do not silently swap models or deliver a local animatic as if it were a model render.
