# Bundled skill sources and notices

This plugin redistributes the following skill snapshots. Root MIT covers original HTML Brifing code and guidance; third-party files retain their listed licenses. Upstream names indicate provenance, not endorsement. Runtime services/libraries are separate.

| Skill | Upstream | Snapshot | License |
|---|---|---|---|
| [gsap-core](skills/gsap-core/SKILL.md) | [https://github.com/greensock/gsap-skills](https://github.com/greensock/gsap-skills) | installed skill snapshot 1.0.0 | [MIT](skills/gsap-core/LICENSE) |
| [gsap-timeline](skills/gsap-timeline/SKILL.md) | [https://github.com/greensock/gsap-skills](https://github.com/greensock/gsap-skills) | installed skill snapshot 1.0.0 | [MIT](skills/gsap-timeline/LICENSE) |
| [imagegen](skills/imagegen/SKILL.md) | [https://github.com/openai/skills](https://github.com/openai/skills) | local snapshot 2026-09-29 | [Apache-2.0](skills/imagegen/LICENSE.txt) |
| [impeccable](skills/impeccable/SKILL.md) | [https://github.com/pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 4.4.0; engine 0.1.6 | [Apache-2.0](skills/impeccable/LICENSE) |
| [playwright](skills/playwright/SKILL.md) | [https://github.com/openai/skills](https://github.com/openai/skills) | local snapshot 2026-09-29 | [Apache-2.0](skills/playwright/LICENSE.txt) |

## Package adaptations

Source and packaged file hashes, dates and adaptations are recorded in [bundle.json](bundle.json). ImageGen and Playwright examples resolve the selected skill directory. GSAP includes core and timeline guidance only; the core handoff note makes this scope explicit. Other upstream modules are not dependencies of this package. Runtime libraries/services are not redistributed here.

Impeccable includes its [Apache license](skills/impeccable/LICENSE), [upstream notices](skills/impeccable/NOTICE.md) and [modern-screenshot MIT notice](skills/impeccable/scripts/modern-screenshot-LICENSE). The launcher and pinned engine version are included; engine binaries remain separate.

Previously bundled helpers removed in 0.4.0 retain their attribution in prior tagged releases. This release does not ship their files or require their installation. Visualize is neither bundled nor required; its installed original manifest declares Proprietary.
