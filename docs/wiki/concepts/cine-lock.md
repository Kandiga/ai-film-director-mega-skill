---
title: CINE-LOCK Framework
created: 2026-06-25
updated: 2026-06-25
type: concept
tags: [ai-video, direction, continuity, prompt-engineering, qa]
sources: []
confidence: high
---

# CINE-LOCK Framework

CINE-LOCK is the core pre-spend gate for AI video.

## C — Continuity bible

Define character, wardrobe, props, world, camera language, and forbidden drift. See [[blueprint-first-production]] and [[ai-film-qa-loop]].

## I — Intent

Every shot must have one reason to exist: hook, reveal, escalation, relief, reversal, payoff, insert, reaction, or transition.

## N — Narrative handoff

Choose the edit logic deliberately:

- hard cut;
- start/end frame interpolation;
- match cut;
- insert cutaway;
- reaction shot;
- last-frame continuation.

## E — Exact prompt

Prompt order:

1. camera first;
2. subject anchor;
3. scene;
4. one visible action;
5. end beat;
6. lighting/style;
7. constraints.

## LOCK — QA before spend

Before paid generation, verify keyframes, one action, camera clarity, model choice, and approval for generation count/resolution/retry budget.
