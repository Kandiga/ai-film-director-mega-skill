---
title: AI Film QA Loop
created: 2026-06-25
updated: 2026-06-25
type: pipeline
tags: [ai-video, qa, continuity, direction]
sources: []
confidence: high
---

# AI Film QA Loop

QA is not optional. Render success is not creative success.

## Still QA

Before video:

- identity/subject correct;
- gesture readable;
- environment correct;
- no fake text;
- no unwanted symbols/logos;
- camera angle matches shot intent;
- start frame contains enough visual information.

## Clip QA

After video:

```bash
ffprobe -v error -show_streams -show_format clip.mp4
ffmpeg -i clip.mp4 -vf fps=1 contact/frame_%03d.jpg
```

Inspect:

- first/middle/last frame;
- identity drift;
- hand/face artifacts;
- text/logos;
- black frames;
- freeze frames;
- transition from previous shot;
- audio presence and clipping.

## Fix vs regenerate

Fix locally when:

- pacing/crop/color/caption/audio/CTA are wrong but core motion works.

Regenerate when:

- identity, product, gesture, physical interaction, camera path, or temporal consistency are broken.

See [[cine-lock]] and [[seedance-kling-routing]].
