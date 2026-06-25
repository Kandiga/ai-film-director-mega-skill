---
title: Production Checklists
created: 2026-06-25
updated: 2026-06-25
type: checklist
tags: [qa, ai-video, direction, continuity]
sources: []
confidence: high
---

# Production Checklists

## Pre-generation

- [ ] Poet intent summarized.
- [ ] Continuity bible exists.
- [ ] Character/object blueprints exist.
- [ ] Environment/area blueprints exist.
- [ ] Shot blueprints exist.
- [ ] Start frame QA passed.
- [ ] Paid generation count/model/duration/resolution approved.
- [ ] Prompt has one action.
- [ ] Camera grammar is explicit.
- [ ] Forbidden drift is listed.

## Post-generation

- [ ] File exists and non-zero size.
- [ ] ffprobe confirms duration/resolution/streams.
- [ ] Contact sheet sampled.
- [ ] First frame matches start frame.
- [ ] Middle frame preserves identity/world.
- [ ] Last frame supports next edit.
- [ ] No black/frozen sections.
- [ ] No fake text/logos.
- [ ] Audio checked if present.
- [ ] Decision made: keep, fix in post, or regenerate.

Related pages: [[ai-film-qa-loop]], [[cine-lock]], [[blueprint-first-production]].
