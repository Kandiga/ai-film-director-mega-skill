---
name: ai-film-director-mega-skill
description: Use when planning, directing, generating, QAing, or documenting AI films with cinematic continuity, frame-based reference analysis, blueprint-first production, and Netanel-style “אצבע אמצעית” workflows.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [ai-video, film-direction, continuity, reverse-prompt-engineering, seedance, kling, higgsfield, netanel]
    related_skills: [video-production-orchestrator, watch-video, ai-video-frame-extraction, ai-video-frame-grid-workflow, reference-controlled-visual-production]
---

# AI Film Director Mega Skill

## Overview

This mega skill is a complete operating system for directing AI films instead of merely generating attractive isolated clips.

It combines:

- blueprint-first production;
- continuity bibles;
- controlled short-clip generation;
- reference-controlled stills;
- Seedance/Kling/Higgsfield practical workflows;
- frame extraction and contact-sheet QA;
- reverse prompt engineering from reference films;
- Netanel’s “אצבע אמצעית” production lessons;
- wiki-backed learning loops.

The standard is real cinematic production: intent, world, shot grammar, continuity, clip QA, final assembly, and durable learning updates.

## When to use

Use when the user wants to:

- create or continue an AI short film;
- turn a reference film/video into a reusable cinematic language;
- write prompts for AI-video shots with strong camera direction;
- build a production bible or blueprint package;
- generate multi-shot scenes through Seedance, Kling, Higgsfield, Cinema Studio, or similar tools;
- continue Netanel’s “אצבע אמצעית” / alien-market / Phantom spacecraft film world;
- avoid wasted paid video generation by QAing stills, prompts, and clip outputs systematically.

Do not use for a one-off image generation unless it is part of a film pipeline.

## Operating hierarchy

### Level 1 — Poet intent

Before generating, understand the emotional and narrative reason for the scene.

Ask or reconstruct:

- What is the scene trying to make the viewer feel?
- What changes by the end of the scene?
- What visual symbol carries the idea?
- What must not be lost if the model creates something beautiful but wrong?

For “אצבע אמצעית”, the middle finger is not only a joke. It can become rebellion, freedom, cosmic insult, private sacred joke, cultural beacon, or mythic defiance. The scene must preserve the symbolic intention.

### Level 2 — Continuity bible

Create a compact bible before paid generation:

- characters and identities;
- wardrobe/silhouette anchors;
- props and symbolic objects;
- world geography and palette;
- camera language;
- sound language;
- forbidden drift.

Do not overload every prompt with the full bible. Repeat only the anchors needed for that shot.

### Level 3 — Blueprint package

For serious scenes, build three blueprint layers:

1. **Character/object blueprints:** recurring people, aliens, craft, props, statues.
2. **Environment/area blueprints:** every major spatial zone.
3. **Shot blueprints:** composition, camera, motion, action, sound/SFX, forbidden drift.

A start frame generated before blueprints may be useful as draft/reference, but it is not production-locked.

### Character lock update — gray background, not white

Frame analysis of Joey's Claude-skills workflow added a practical correction: do not default recurring characters to pure white seamless reference sheets. White can blow out facial edges, bounce light into the jaw, add glossy skin, and later make faces look pasted/plastic inside generated scenes.

For recurring characters/creatures, prefer:

- solid neutral gray background;
- soft controlled lighting, not over-bright diffuse light;
- visible natural skin/material texture;
- full-body + portrait + side/back/details;
- a six-panel/turnaround sheet for important characters;
- explicit do-not-change marks: tattoos, jewelry, scars, piercings, silhouette, finger/hand shape, alien anatomy.

Separate identity from outfit. If an outfit was generated on another generic model, use outfit-first reference order: reference 1 = outfit/garment, reference 2 = character identity, then instruct the model to transfer the outfit while preserving identity from reference 2.

### Level 4 — Keyframe / start-frame control

Generate or select still frames first. QA them before video spend.

Use still-frame QA:

- identity correct;
- gesture readable;
- world/area correct;
- no fake unreadable text;
- no wrong symbols/logos;
- correct camera angle;
- enough visual information for the video model.

For Netanel’s middle-finger shots, the gesture must be unmistakable: one central raised middle finger, index/ring/little folded, thumb locking them. No torch, no index-pointing, no open hand.

### Level 5 — Video generation

Think in 5–8 second beats. Avoid one giant prompt.

Prompt order:

1. shot/camera first;
2. subject anchor;
3. environment;
4. one visible action;
5. end state/emotional beat;
6. lighting/style;
7. constraints.

Add a tool-facing reference-order block for serious Seedance/Kling/Higgsfield shots:

```text
References to attach, in this exact order:
1. identity / character sheet
2. outfit / gesture / body-detail sheet
3. location / area blueprint
4. prop / vehicle / object reference
5. lighting / atmosphere reference
6. approved prior frame if continuity-critical
```

Use names such as Roe, Phantom, Zara, Mei, etc. for planning, but tool-facing prompts must also describe the visible identity, wardrobe, role, and continuity anchors. Do not rely on a model knowing a name.

Begin image-to-video prompts with:

```text
Use the provided image as the exact first frame.
```

Then describe only allowed motion. For rainy/smoky/energy environments, avoid freezing motion into still references: use wet surfaces, droplets, reflections, haze and glow as still evidence, then ask the video model to animate moving rain/smoke/particles/light.

Select camera operator mode deliberately: locked-off tripod, slow dolly, gimbal, handheld operator-breathing, Dutch angle, drone, surveillance, or POV. Handheld realism is subtle breathing/micro-shake, not random chaos.

### Level 6 — QA and repair

After generation:

- verify duration/resolution/audio with ffprobe;
- sample frames/contact sheet;
- inspect first/middle/last frame;
- compare to shot intent and continuity bible;
- check identity, hands, faces, text, black frames, frozen frames, and last-frame drift;
- fix in post if the core clip works;
- regenerate only if the failure is intrinsic.

## CINE-LOCK framework

### C — Continuity bible

Characters, wardrobe, props, world, camera language, forbidden drift.

### I — Intent

Every clip has one purpose: hook, reveal, escalation, relief, reversal, payoff, insert, reaction, transition.

### N — Narrative handoff

Choose the handoff deliberately:

- hard cut;
- start/end interpolation;
- match cut;
- insert cutaway;
- reaction shot;
- last-frame continuation.

Do not force start/end frames when a hard cut is more cinematic.

### E — Exact prompt

Camera first, subject anchor second, one action, end beat, constraints.

### LOCK — QA before spend

Do not submit paid video until the still/keyframe and prompt pass the checklist.

## Model routing

### Seedance 2.0

Use for stronger motion, identity-sensitive cinematic shots, genre control, and serious 4–15s clips. Prefer 720p unless 1080p is approved. Keep clips 5–8s when possible.

Risk zones:

- public-figure or celebrity resemblance;
- bodily/gross wording;
- too many actions;
- long single-generation scenes;
- expensive retries.

### Kling 3.0

Use for controlled atmospheric image-to-video, budget-sensitive shots, start/end transitions, and subtle cinematic motion.

Risk zones:

- large unrelated start/end morphs;
- many characters;
- complex action choreography;
- text/signs.

### GPT Image / Image 2 / still-generation tools

Use for blueprints, character sheets, environment sheets, and locked start frames. Treat stills as visual-only unless the tool reliably renders exact text.

## Reverse prompt engineering from reference films

When a video is provided as style reference:

1. Extract frames, not only transcript.
2. Build contact sheets with timestamps.
3. Identify clusters by visual language.
4. Extract camera grammar:
   - extreme macro;
   - overhead POV;
   - low ground angle;
   - orbital view;
   - wide symbolic tableau;
   - reflection/screen-within-screen;
   - 2x2 broadcast grid;
   - VHS/archive insert.
5. Extract light behavior:
   - blown window;
   - golden backlight;
   - low-key smoke;
   - starburst sun;
   - overexposed safe room;
   - foggy snow headlights.
6. Extract motif logic:
   - eye/mirror/window/screen;
   - sacred place + impossible animal;
   - domestic object + cosmic orbit;
   - data over nature;
   - public authority + media repetition;
   - body fragment + memory.
7. Write prompt libraries by cluster.
8. Caveat: reverse-engineered from visible frames, not original hidden prompts.

## “הנביא החשמלי” style grammar

Use this when the desired tone is prophetic, avant-garde, Jewish/sacred, fragmented, absurd, and visually poetic.

Key principles:

- Montage grammar, not one look.
- Extreme scale jumps: eye/mouth/glass/water/smoke ↔ Saturn/Earth/cloud ocean/city panorama.
- One impossible collision per shot: sacred place + animal/angel, office + floating cloud, media screen + ghost, kitchen + cosmic orbit.
- Camera language matters more than object list.
- Light is a subject.
- Avoid generic “surreal cinematic”. Anchor the exact mechanics.

Prompt skeleton:

```text
Experimental prophetic Hebrew art-house cinema, sacred absurdity mixed with domestic documentary realism, [specific subject], [camera grammar], [impossible collision], [light behavior], [material/texture], [composition], analog grain / VHS / archival texture only if motivated, fragmented montage logic, high contrast, volumetric haze, dream logic, post-traumatic spiritual realism, no generic fantasy clutter, no unreadable fake text.
```

## “אצבע אמצעית” production rules

### Active visual bible anchors

- Phantom spacecraft: mystical musical vessel, not action warship.
- Teal-gold fracture planet: mystery reveal, not generic planet.
- Crystal palace: mystical/energy encounter, not just fantasy architecture.
- Alien Liberty Statue middle-finger beacon: iconic cultural/political/comedic symbol.
- Roe alien: tonal heart / rebel / comic anchor.
- Market cultures: distinct societies, not generic crowd.

### Scene 0 / prequel guidance

A prequel should add intent, not repeat arrival.

Strong directions:

1. Mythology of the finger — a vulgar gesture becomes sacred civilization myth.
2. Cosmic broadcast — statue/finger beacon emits red-gold pulse that the Phantom hears.
3. Roe in the market — introduce emotional/comic heart before arrival.
4. Sacred joke — wordless prologue of rebellion elevated into cosmic religion.

### Public figure / satire handling

If the user explicitly wants a recognizable public figure, preserve that production intent in the bible. If a provider blocks it:

- inspect job status and JSON;
- retry transient 502/504 after delay;
- repair prompt by removing explicit name from video prompt while preserving exact first-frame identity;
- avoid direct voice cloning or deceptive impersonation;
- if necessary, rebuild as fictional non-identifying satire and report the change honestly.

## Wiki engine loop

When this skill is used in a repo with `docs/wiki`:

1. Read `docs/wiki/SCHEMA.md`.
2. Read `docs/wiki/index.md`.
3. Search relevant pages.
4. Update or create wiki pages for durable lessons.
5. Run:

```bash
python3 scripts/wiki_engine.py lint docs/wiki
python3 scripts/wiki_engine.py index docs/wiki
```

6. Commit the wiki update with the production change.

## Common pitfalls

1. Generating video before blueprints exist.
2. Treating a pretty still as production lock.
3. Using one long prompt for a whole film.
4. Changing too many variables after a failed generation.
5. Retrying paid video without checking job status/history.
6. Copying a reference film’s surface style but missing camera grammar.
7. Using transcript-only analysis when visuals carry the style.
8. Publishing extracted third-party frames in a public repo without rights.
9. Using generic cinematic adjectives instead of exact shot mechanics.
10. Ignoring user corrections about intent or identity.

## Verification checklist

- [ ] Poet intent summarized.
- [ ] Continuity bible exists.
- [ ] Character/object blueprints exist.
- [ ] Environment/area blueprints exist.
- [ ] Shot blueprints exist.
- [ ] Start frames QA’d.
- [ ] Paid generation count/model/duration approved when relevant.
- [ ] Clip prompt has one action and clear camera.
- [ ] Generated clip inspected with frames/contact sheet.
- [ ] Failures are classified as fix-in-post vs regenerate.
- [ ] Wiki/skill updated with durable lessons.
