# Joey Claude Skills Frame Analysis — AI-video workflow upgrade (2026-06-27)

Source: YouTube `4TXaAnittHs`, “these new Claude skills are saving me hundreds (skills and prompts in description)” by JOEY, 19:03.

This reference is distilled from a full `watch-video` pass: 80 sampled frames at 768px plus captions. Contact sheets were inspected visually. Because the source is a third-party video, do not publish raw frames/contact sheets in public repos; keep only textual observations and reusable workflow lessons.

## Coverage

- Full video downloaded locally.
- 80 sampled frames across 00:00–18:49.
- Four 20-frame contact sheets inspected.
- Captions parsed and cross-checked.
- Source frames kept locally under `/home/kandiga/video_analysis_4TXaAnittHs/` for this session.

## What the video teaches

The video is not just about “prompts.” It is about turning AI-video production into reusable Claude skills. The central process is:

1. define a repeatable workflow;
2. build identity/wardrobe/environment references;
3. use Claude to convert references into structured prompts;
4. order references exactly for Seedance / video tools;
5. render short controlled clips;
6. upscale and edit;
7. feed practical discoveries back into the skill.

## Frame-by-frame cluster notes

### Frames 01–09 / 00:00–01:56 — Hook and AI characters in creator room

Visible: presenter in red-lit studio; humorous overlays; AI female character appears as if inside the same room; portrait close-up.

Lessons:

- AI characters can be integrated into a live presenter/studio format if the frame is locked and references include the real plate + character sheet.
- The workflow starts with a controlled frame of the real host that leaves room for the generated character.
- Claude receives both the host frame and character references, plus the script and camera angle constraints.

### Frames 10–14 / 02:10–03:08 — Example outputs and BTS language

Visible: red sci-fi scene, Japanese title/subtitle, dark car shot, blue-screen production image, night car set with crane.

Lessons:

- Skills can cover scene generation, subtitle/dialogue planning, vehicle shots, chroma/compositing ideas, and production-style shot references.
- A video skill should understand both cinematic outputs and BTS/production references.
- This reinforces that prompts need camera/lighting/composition language, not only subjects.

### Frames 16–20 / 03:37–04:35 — Character sheet and edit UI

Visible: multi-view female character sheet; editing/color software with scopes and timeline; generated character integrated beside presenter.

Lessons:

- Character sheets are operational assets, not decoration.
- Post-production is part of the pipeline; color scopes and timeline matter.
- The assistant should be able to generate edit notes, color-match notes, compositing constraints and pickup-shot prompts.

### Frames 21–30 / 04:49–07:00 — Why depth matters

Visible: presenter explaining; dark industrial/cinematic reference; cartoon reference; props.

Caption evidence:

- “Deakins doesn’t light a room, he lights the air in the room.”
- Atmosphere/haze lets light “grab onto the air.”
- Depth does emotional work.

Lessons:

- Add atmosphere as a first-class layer: haze, fog, mist, dust, smoke, volumetric light.
- Avoid pasted-on faces by designing the air/light of the scene.
- Prompt for characters embedded in the same atmosphere as the environment.

### Frames 31–38 / 07:14–08:55 — Character lock and gray background

Visible: portrait reference, dark generation interface, multiple character/outfit references.

Caption evidence:

- The creator used to build characters on white seamless backgrounds, then says that was wrong.
- Pure white blows out face edges and bounces light up into the jaw.
- Solid gray background gives better skin, less shine, less plastic look.

Lessons:

- Replace default white-background reference sheets with solid gray-background sheets.
- Ask for soft controlled lighting but not glossy overlit skin.
- Use full-body + portrait + outfit references.

### Frames 41–47 / 09:39–11:05 — Outfit swap and six-panel sheet

Visible: full-body cream outfit references, board of character/outfit/car references, full six-panel red/black character turnaround.

Caption evidence:

- Simple outfits: Nano Banana Pro can build them on the character.
- More stylized outfits may need Soul Cinema, then an outfit swap.
- For outfit swaps, image order matters: outfit first, character second.
- Tattoos, piercings, markings must be mentioned explicitly.
- Six-panel sheet includes full body and detail shots for nails, necklaces, jewelry, rings.

Lessons:

- Separate identity from outfit.
- Use reference order in the prompt.
- Build a six-panel sheet for recurring characters.
- Preserve signature marks explicitly.

### Frames 49–56 / 11:34–13:16 — Scene construction and rain/still pitfalls

Visible: reference board with car/landscape/character assets; black sports car rainy city still; interior car shot.

Caption evidence:

- He avoids visible rain streaks in still images because Seedance may keep those streaks frozen.
- Instead, use rain texture on ground, roof, droplets, reflections.
- Character names help Claude track who is who, but tool-facing prompts still describe the characters instead of only using names.
- Scene reference can guide Seedance without necessarily being used as the exact starting image.

Lessons:

- Avoid freezing motion artifacts into still references.
- Use surface evidence of rain, not static rain lines.
- Names are planning handles; prompts need visual identity.
- Scene references and start frames are different roles.

### Frame 60 / 14:13 — Prompt delivery format and Seedance reference order

Visible text: “One 5s prompt, all four beats… three-part delivery… update the skill… References to attach in Seedance in order: 1. Mei…”

Caption evidence:

- After references are uploaded into Claude and the scene is described, Claude gives the prompt plus the reference-sheet order for Seedance.
- It tags references as image 1, image 2, etc.
- Up to nine reference images can be uploaded.

Lessons:

- Every serious video prompt should include a reference-order block.
- The prompt should explicitly map `image 1`, `image 2`, etc. to identity, outfit, location, prop, style.
- The output should include scene title and runtime.

### Frames 61–66 / 14:28–15:40 — 720p, camera-operator movement, output examples

Visible: AI generation UI, rendered car-interior shot of woman with phone.

Caption evidence:

- He uses 720p because Topaz can upscale cleanly.
- Camera movement makes videos feel real.
- Updated skills include camera-operator shakiness.
- Non-gimbal handheld should include breathing/micro-movement; Dutch angles can add tension.

Lessons:

- 720p-first is a practical iteration strategy.
- Camera movement must be mode-selected: locked/tripod/gimbal/handheld/Dutch/drone/surveillance.
- Handheld realism is subtle operator breathing, not random shake.

### Frames 70–80 / 16:38–19:03 — Editing is the final craft

Visible: editing timeline with multiple tracks; presenter closing; end card.

Caption evidence:

- “A pile of beautiful generations sitting on a timeline is not a film.”
- Tools get you to ~70%; the jump to ~90% happens in the edit bay.
- Color grade, same roll of film, J-cuts, audio, sound effects, pacing, structure.
- Cut out four beautiful seconds if they do not tell the story.
- He rejects harmful deepfakes/fake news and says AI is a brush for building worlds.

Lessons:

- Raw generations are not deliverables.
- The production skill must include edit-bay responsibilities.
- Sound design and pacing are part of story, not optional polish.
- Preserve a human seam and ethical clarity.

## Patterns to copy into Netanel's film workflow

### Character/creature sheets

For every recurring person/alien/creature:

- gray-background identity sheet;
- six-panel sheet;
- full-body / close-up / side/back / details;
- separate outfit sheet if clothing matters;
- explicit do-not-change list.

### Reference order block

Every Seedance/Kling/Cinema prompt should include:

```text
References to attach, in order:
1. identity sheet / recurring character
2. wardrobe or body/gesture sheet
3. location/area blueprint
4. prop/vehicle/object reference
5. lighting/atmosphere reference
6. approved previous frame if continuity-critical
```

### Rain / smoke / energy rule

For moving atmosphere:

- still reference = surface evidence and lighting behavior;
- video prompt = actual moving rain/smoke/energy;
- avoid frozen streaks, frozen particles, or locked motion trails.

### Edit-bay rule

For every delivered scene package, include:

- raw render status;
- selected takes;
- cut plan;
- color-grade direction;
- sound/J-cut plan;
- trims/removals for story;
- QA notes.

## Integration checklist

- [ ] Update main skill to mention gray-background character lock.
- [ ] Add outfit-swap reference-order rule.
- [ ] Add Seedance reference-order block to shot blueprint format.
- [ ] Add atmosphere/depth rule.
- [ ] Add 720p + upscale + edit-bay rule.
- [ ] Add “70% generation / 90% film” to final delivery standard.
