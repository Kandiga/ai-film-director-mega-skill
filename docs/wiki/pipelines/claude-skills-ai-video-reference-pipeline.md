---
title: Claude Skills AI Video Reference Pipeline
created: 2026-06-27
updated: 2026-06-27
type: pipeline
tags: [ai-video, skills, reference-control, seedance, qa, prompt-engineering]
sources: [YouTube 4TXaAnittHs]
confidence: high
---

# Claude Skills AI Video Reference Pipeline

This page distills frame-level lessons from Joey's video “these new Claude skills are saving me hundreds” into the repo workflow. It supports [[blueprint-first-production]], [[ai-film-qa-loop]], [[seedance-kling-routing]], and [[etzba-emtzaeit-production-bible]].

## Core lesson

Good AI video is not a single prompt. The repeatable unit is a skill-backed production loop:

1. Lock character.
2. Lock wardrobe / outfit separately.
3. Build a scene / environment reference pack.
4. Map references in the exact order the target video model will receive them.
5. Generate short beat-based prompts.
6. Render at economical resolution first, often 720p.
7. Upscale if needed.
8. Finish the last 20–30% in the edit bay: color, J-cuts, sound, pacing, structure.
9. Update the skill with what actually worked.

## Frame-level extracted principles

### 00:00–04:45 — Skill as production system

The opening alternates talking-head explanation, AI characters placed into the creator's room, cinematic examples, subtitles, car shots, blue-screen/BTS imagery, and editing software. The visual lesson is that a “skill” should coordinate a whole production pipeline, not merely output prompts.

Reusable modules:

- project intake;
- reference analysis;
- character bible;
- shot bible;
- prompt generation;
- compositing/edit plan;
- QA and revision loop;
- final skill update.

### 05:18–06:06 — Depth / haze / atmosphere

The speaker stresses that cinema often lights the air, not only the subject. Haze, fog, practical light, atmosphere, and depth help a character feel embedded rather than pasted into a plate.

Prompt implication:

```text
Add motivated atmosphere: haze/fog/rain mist/dust in the air so light has volume. The subject must sit inside the same air as the environment, not look pasted on top.
```

### 06:06–08:38 — Character lock: gray background beats white

The strongest correction: do not default to pure white seamless backgrounds for character reference sheets. White blows out facial edges, bounces light into the jaw, creates shine, and later makes characters look plasticky or pasted into scenes. Use solid gray with soft controlled lighting.

Character-sheet rule:

- neutral solid gray background;
- soft but not over-bright light;
- visible skin texture, no glossy plastic face;
- clean face identity anchor;
- full-body and close-up variants;
- no distracting environment until identity is locked.

### 08:38–10:47 — Outfit is separate from identity

Simple outfits can be built directly on the character. More stylized outfits may be easier in a stronger fashion/cinematic model, then transferred back onto the character. For outfit swaps, reference order matters: outfit first, character second. Preserve markings, tattoos, piercings, jewelry, and signature details explicitly.

Outfit-swap rule:

```text
Reference 1 = outfit / garment design. Reference 2 = character identity. Transfer the outfit from reference 1 onto the same person from reference 2. Preserve identity, tattoos, piercings, jewelry, hairline, body proportions and face structure from reference 2.
```

### 10:47–11:20 — Six-panel character sheet

After identity/outfit/hairstyle are locked, run a six-panel character sheet: full-body, portrait, side/back/pose variants, hands, jewelry, nails, accessories. This reduces later drift and avoids manually cutting many individual references in Photoshop.

Minimum continuity pack:

1. identity portrait;
2. full-body wardrobe sheet;
3. side/back or turnaround;
4. hand/accessory detail;
5. expression/pose variant;
6. final composite model sheet.

### 11:20–13:45 — Scene reference pack without frozen rain

For the rainy Tokyo canyon/car scene, the lesson was not to bake visible rain streaks into a static reference, because Seedance may keep the rain streaks frozen. Instead use rain texture on ground, roof, glass, and environment surfaces, and let the video model animate rain/mist.

Scene-reference rule:

- avoid static rain streaks as hard lines in seed frames;
- use wet asphalt, roof droplets, reflections, mist, haze, puddles;
- let moving precipitation be generated in video, not locked as still artifacts.

### 12:13–14:31 — Names help Claude, but prompts describe the people

The creator names characters internally (Zara, Mei) to keep conversation organized, but the generated prompt describes the characters rather than relying only on names. This maps directly to Netanel's project: names like Roe are useful in planning, but prompts must repeat the visual identity and role anchors.

Prompt rule:

```text
Use names for planning, but every tool-facing prompt must include the visible identity description, wardrobe, role, and continuity anchors. Do not rely on the model knowing the name.
```

### 13:46–14:31 — Seedance reference order is part of the prompt

The prompt delivery should list the references in the exact order they must be uploaded to Seedance. The prompt may tag them as image 1, image 2, image 3, etc. The video mentions up to nine reference images.

Reference-order block:

```text
References to attach in Seedance, in this exact order:
1. character identity sheet
2. wardrobe / outfit sheet
3. scene / location plate
4. key prop / vehicle
5. lighting / atmosphere reference
6. prior approved frame if continuity-critical
```

Then use `image 1`, `image 2`, etc. consistently in the prompt.

### 14:31–15:25 — 720p + upscale, and real camera motion

He uses 720p because upscale can be clean later. The more important realism update is camera operator movement: subtle handheld breathing, non-gimbal micro-shake, and occasional Dutch angles. Realism does not mean chaotic camera movement; it means motivated human-operated camera behavior.

Camera rule:

```text
Use subtle camera-operator breathing and micro-shake unless the shot is explicitly locked-off, gimbal, tripod, drone, or surveillance. Add Dutch angle only when it serves the scene's tension.
```

### 15:36–18:00 — 70% generation, 90% film

The most important editing lesson: a pile of beautiful generations on a timeline is not a film. AI tools get the project to about 70%. The jump to 90% happens in the edit bay: color grade, J-cuts, audio, sound design, pacing, structure, cutting beautiful seconds that do not tell the story.

Netanel pipeline implication:

- do not judge the film from raw generations only;
- edit, trim, grade, and sound-design;
- cut beautiful but storyless seconds;
- use J-cuts and sound bridges for continuity;
- aim for emotionally moving, not fake-perfect.

### 17:00–18:00 — Keep the human seam

The creator explicitly rejects deceptive realism, deepfakes, fake news, and harm. AI is a brush for building worlds and emotional entertainment, not a tool to erase the human seam.

Ethical rule:

- keep satire/fiction clear;
- avoid deceptive public-figure voice/face use;
- be proud of the human edit/craft layer;
- use AI to build worlds, not to impersonate reality harmfully.

## Direct upgrade to אצבע אמצעית workflow

For the film:

1. Build all recurring characters on controlled gray-background identity sheets, not white-background glamour sheets.
2. Split identity, outfit, scene, prop, and atmosphere references into separate roles.
3. For Roe / alien market / human shaman / Phantom / statue, keep prompt names plus visual descriptions.
4. For rainy, smoky, or glowing environments, avoid frozen visual streaks; ask for surface evidence and moving atmospheric behavior in video.
5. Add a `Seedance reference order` block to every serious shot blueprint.
6. Prefer 720p generation + verified upscale for iteration-heavy passes.
7. Add intentional handheld/operator movement only where cinematic; keep sacred/statue/myth shots locked or slow-drift when needed.
8. Treat raw generated clips as 70%; the film is finished in editing: color grade, sound design, J-cuts, pacing, removal of storyless seconds.

## QA additions

Before generation:

- [ ] Character identity built on gray background, not white unless justified.
- [ ] Outfit/wardrobe separated from identity.
- [ ] Six-panel/turnaround exists for recurring characters.
- [ ] Scene reference avoids frozen rain/light streak artifacts.
- [ ] Reference order is written explicitly.
- [ ] Prompt uses both character names and visual descriptions.
- [ ] Camera operator mode selected: locked-off, gimbal, handheld, Dutch, drone, surveillance.

After generation:

- [ ] Character looks embedded in the air/light of the scene.
- [ ] No pasted/plastic face effect.
- [ ] Rain/haze/light moves naturally and is not frozen from still references.
- [ ] Clip is usable after edit, not merely pretty.
- [ ] Edit plan includes color, sound, pacing, J-cuts, trims, and story structure.
