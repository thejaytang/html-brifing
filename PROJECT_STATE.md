# Current state

- Released and installed: **0.1.0**, 2026-09-29. Plugin `html-brifing@html-brifing` is enabled in Codex; a new chat is required to pick up its skills.
- Release commit: `6eb3fecf0a24deaa8f52cfc5c04e56a0637077d3`, tag `v0.1.0`. [Public release](https://github.com/thejaytang/html-brifing/releases/tag/v0.1.0).
- Verification: **8/8 release acceptance groups passed**. [Full evidence and limits](project-support/evaluation.md), [artifact identity](project-support/release-verification.json).
- Scope: one orchestration entrypoint, optional installed helper reuse, ImageGen routing, evidence/narrative/interaction/data guidance and actual final-file acceptance. No automatic helper installation.
- Author's legacy entrypoint was backed up and converted to a compatibility pointer; other skills remain separate. This is a local migration, not an installation hook distributed to users.
- Entry: [English README](README.md), [中文说明](README.zh-CN.md), [skill](plugins/html-brifing/skills/html-brifing/SKILL.md), [fictional offline example](examples/offline-routing.html).
- Limits: native Windows/Linux, actual image generation and all external helper combinations are unverified. The passing scope is specified in the evidence, not inferred from installed files.
- Next: collect actual briefing feedback before extending guidance. Main contains publication evidence added after the tag; the release ZIP and installed runtime files are unchanged.
