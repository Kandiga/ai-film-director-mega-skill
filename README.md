# AI Film Director Mega Skill

A public, production-oriented knowledge base and Hermes skill for directing AI-generated films with strong cinematic continuity, reference-controlled visuals, and frame-based reverse prompt engineering.

This repository was created from practical production work on Netanel’s AI-film pipeline, especially the film project **“אצבע אמצעית”**, plus broader AI-video direction lessons from Seedance, Kling, Higgsfield, GPT Image workflows, frame extraction, QA loops, and the long-form frame analysis of **“הנביא החשמלי”**.

> Important: this repo contains production knowledge, prompt frameworks, wiki pages, and reusable skill instructions. It intentionally does **not** publish raw extracted frames/contact sheets from third-party videos. Use the scripts and methods here to analyze references you have rights to inspect.

## What is inside

```text
.
├── README.md
├── skills/
│   └── ai-film-director-mega-skill/
│       ├── SKILL.md
│       └── references/
├── docs/
│   └── wiki/
│       ├── SCHEMA.md
│       ├── index.md
│       ├── log.md
│       ├── concepts/
│       ├── pipelines/
│       ├── projects/
│       ├── prompt-libraries/
│       └── checklists/
└── scripts/
    └── wiki_engine.py
```

## The central idea

AI film production should be directed like cinema, not like a single giant prompt.

The workflow is:

1. Define poetic intent.
2. Build a continuity bible.
3. Build character, object, environment, and shot blueprints.
4. Generate or choose exact start frames.
5. QA stills before video spend.
6. Generate 5–8 second controlled clips.
7. QA every clip with ffprobe + frame samples/contact sheets.
8. Repair locally when possible; regenerate only the failed unit.
9. Assemble, sound-design, and final-QA the film.
10. Feed learnings back into the wiki and skill.

## Quick start

```bash
# Validate the wiki and regenerate docs/wiki/index.md
python3 scripts/wiki_engine.py lint docs/wiki
python3 scripts/wiki_engine.py index docs/wiki

# Search the wiki
python3 scripts/wiki_engine.py search docs/wiki "Seedance"
```

## Install as a Hermes skill

Copy the skill directory into your Hermes skills folder:

```bash
mkdir -p ~/.hermes/skills/creative
cp -R skills/ai-film-director-mega-skill ~/.hermes/skills/creative/
```

Then in a new Hermes session, load:

```text
skill_view(name='ai-film-director-mega-skill')
```

## Main frameworks

### CINE-LOCK

A generation-spend gate for AI video:

- **C — Continuity bible:** character, wardrobe, props, world, camera language, forbidden drift.
- **I — Intent:** one visible purpose per shot.
- **N — Narrative handoff:** hard cut, start/end frame, match cut, insert, or reaction.
- **E — Exact prompt:** camera first, subject anchor, scene, one action, end beat, lighting, constraints.
- **LOCK — QA before spend:** keyframe match, one action, model choice, credit approval.

### Blueprint-first production

Never treat a pretty start frame as production-ready by itself. For serious scenes, prepare:

- character/object blueprints;
- environment/area blueprints;
- shot blueprints;
- locked start frames;
- contact sheet QA;
- clip-level QA.

### Claude-skills / Joey workflow update

Frame-level analysis of Joey's Claude-skills video (`4TXaAnittHs`) added these upgrades:

- lock recurring characters on solid gray reference sheets rather than white seamless backgrounds;
- split identity, outfit, location, prop, and atmosphere references into separate roles;
- generate six-panel/turnaround sheets for important characters;
- always output a `References to attach in Seedance, in this order` block for serious shots;
- use character names only as planning handles; tool-facing prompts must describe the visible identity;
- avoid frozen rain/light streaks in still references; use wet surfaces and animate rain in video;
- choose camera-operator mode deliberately: locked, gimbal, handheld breathing, Dutch angle, drone, POV;
- treat raw generations as ~70%; the jump to film quality happens in the edit bay with color, J-cuts, sound, pacing and structure.

Detailed notes live in `skills/ai-film-director-mega-skill/references/joey-claude-skills-frame-analysis-2026-06-27.md` and `docs/wiki/pipelines/claude-skills-ai-video-reference-pipeline.md`.

### Pre-prophetic reverse prompting

When analyzing a reference film visually:

- download/ingest the actual video;
- extract broad sampled frames;
- extract denser scene-change frames;
- build contact sheets with timestamps;
- analyze camera, lens, light, composition, motif, transition grammar;
- write reverse-engineered prompts with a clear caveat that they are not original hidden prompts.

## Public-figure and safety note

For satirical or public-figure-related films, keep intent legal and ethical. If a platform blocks a recognizable public figure in video generation, do not secretly change the story. Instead:

- keep the user-approved production intent in the bible;
- use non-identifying / fictional satirical visual routes when required by model policy;
- avoid voice cloning or deceptive impersonation;
- use story, costume, posture, context, crowd, and reaction shots to preserve meaning without unsafe deepfake behavior.

## License

MIT for the repo text/code. Third-party references named in the wiki remain owned by their creators. Do not redistribute extracted frames or video assets unless you have rights.
