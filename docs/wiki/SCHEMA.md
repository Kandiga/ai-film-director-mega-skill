# Wiki Schema

## Domain

AI film direction through generative models: cinematic prompt engineering, multi-shot continuity, blueprint-first production, reference analysis, Netanel-style “אצבע אמצעית” workflows, Seedance/Kling/Higgsfield/GPT Image pipelines, QA, and wiki-backed learning loops.

## Conventions

- File names: lowercase, hyphens, no spaces.
- Every page starts with YAML frontmatter.
- Use `[[wikilinks]]` for internal links.
- Every substantial page should link to at least two other pages.
- Update `updated` when editing a page.
- Every action should be logged in `log.md`.
- Do not publish raw extracted frames from third-party videos unless rights are clear.

## Frontmatter

```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: concept | pipeline | project | prompt-library | checklist | raw-note
tags: [tag]
sources: []
confidence: high | medium | low
---
```

## Tag taxonomy

- ai-video
- direction
- continuity
- blueprint
- prompt-engineering
- reverse-prompting
- qa
- seedance
- kling
- higgsfield
- gpt-image
- netanel
- etzba-emtzaeit
- prophetic-cinema
- safety
- wiki-engine

## Page thresholds

Create a page when the concept is central, reusable, or affects generation spend/quality. Do not create pages for passing mentions.

## Update policy

When new production evidence contradicts old guidance, keep both if useful, date them, and mark the current recommendation clearly.
