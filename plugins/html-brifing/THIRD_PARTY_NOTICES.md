# Bundled skill sources and notices

This plugin redistributes the following skill snapshots. Root MIT covers original HTML Brifing code and guidance; third-party files retain their listed licenses. Upstream names indicate provenance, not endorsement. Runtime services/libraries are separate.

| Skill | Upstream | Snapshot | License |
|---|---|---|---|
| [academic-humanizer](skills/academic-humanizer/SKILL.md) | [https://github.com/thejaytang/academic-humanizer](https://github.com/thejaytang/academic-humanizer) | author snapshot 2026-09-29 | [MIT](skills/academic-humanizer/LICENSE) |
| [academic-research-plotting](skills/academic-research-plotting/SKILL.md) | [https://github.com/thejaytang/academic-research-plotting](https://github.com/thejaytang/academic-research-plotting) | author snapshot 2026-09-29 | [MIT](skills/academic-research-plotting/LICENSE) |
| [gsap-core](skills/gsap-core/SKILL.md) | [https://github.com/greensock/gsap-skills](https://github.com/greensock/gsap-skills) | installed skill snapshot 1.0.0 | [MIT](skills/gsap-core/LICENSE) |
| [gsap-frameworks](skills/gsap-frameworks/SKILL.md) | [https://github.com/greensock/gsap-skills](https://github.com/greensock/gsap-skills) | installed skill snapshot 1.0.0 | [MIT](skills/gsap-frameworks/LICENSE) |
| [gsap-performance](skills/gsap-performance/SKILL.md) | [https://github.com/greensock/gsap-skills](https://github.com/greensock/gsap-skills) | installed skill snapshot 1.0.0 | [MIT](skills/gsap-performance/LICENSE) |
| [gsap-plugins](skills/gsap-plugins/SKILL.md) | [https://github.com/greensock/gsap-skills](https://github.com/greensock/gsap-skills) | installed skill snapshot 1.0.0 | [MIT](skills/gsap-plugins/LICENSE) |
| [gsap-react](skills/gsap-react/SKILL.md) | [https://github.com/greensock/gsap-skills](https://github.com/greensock/gsap-skills) | installed skill snapshot 1.0.0 | [MIT](skills/gsap-react/LICENSE) |
| [gsap-scrolltrigger](skills/gsap-scrolltrigger/SKILL.md) | [https://github.com/greensock/gsap-skills](https://github.com/greensock/gsap-skills) | installed skill snapshot 1.0.0 | [MIT](skills/gsap-scrolltrigger/LICENSE) |
| [gsap-timeline](skills/gsap-timeline/SKILL.md) | [https://github.com/greensock/gsap-skills](https://github.com/greensock/gsap-skills) | installed skill snapshot 1.0.0 | [MIT](skills/gsap-timeline/LICENSE) |
| [gsap-utils](skills/gsap-utils/SKILL.md) | [https://github.com/greensock/gsap-skills](https://github.com/greensock/gsap-skills) | installed skill snapshot 1.0.0 | [MIT](skills/gsap-utils/LICENSE) |
| [humanizer](skills/humanizer/SKILL.md) | [https://github.com/blader/humanizer](https://github.com/blader/humanizer) | 3.0.0 | [MIT](skills/humanizer/LICENSE) |
| [imagegen](skills/imagegen/SKILL.md) | [https://github.com/openai/skills](https://github.com/openai/skills) | local snapshot 2026-09-29 | [Apache-2.0](skills/imagegen/LICENSE.txt) |
| [impeccable](skills/impeccable/SKILL.md) | [https://github.com/pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 4.4.0; engine 0.1.6 | [Apache-2.0](skills/impeccable/LICENSE) |
| [playwright](skills/playwright/SKILL.md) | [https://github.com/openai/skills](https://github.com/openai/skills) | local snapshot 2026-09-29 | [Apache-2.0](skills/playwright/LICENSE.txt) |
| [ponytail](skills/ponytail/SKILL.md) | [https://github.com/DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | 4.10.0 | [MIT](skills/ponytail/LICENSE) |
| [research-results-tables](skills/research-results-tables/SKILL.md) | Jay Tang, bundled original | author snapshot 2026-09-29 | [MIT](skills/research-results-tables/LICENSE) |
| [ui-ux-pro-max](skills/ui-ux-pro-max/SKILL.md) | [https://github.com/nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | local snapshot 2026-09-29 | [MIT](skills/ui-ux-pro-max/LICENSE) |

## Package adaptations

Source and packaged file hashes, dates and per-skill adaptations are recorded in [bundle.json](bundle.json). Copied skills include the selected runtime references, assets, scripts and data. Personal copies are not modified. UI UX Pro Max, ImageGen and Playwright examples resolve the selected skill directory instead of assuming a global installation. UI UX Pro Max retains its long workflow in a linked reference for progressive disclosure. Ponytail metadata is normalized; its core coding workflow is included, not the separate plugin hooks, MCP service or optional audit/gain commands. GSAP includes all eight skill modules, not the GSAP JavaScript runtime.

Impeccable includes its [Apache license](skills/impeccable/LICENSE), [upstream notices](skills/impeccable/NOTICE.md) and the [MIT notice for modern-screenshot](skills/impeccable/scripts/modern-screenshot-LICENSE). The launcher and pinned engine-version file are included; engine binaries are obtained separately by the upstream launcher when used. Preserve its existing-project behavior and user/project verification requirements.

Academic Humanizer retains its [original attribution and MIT notice](skills/academic-humanizer/LICENSE), including AIScientists-Dev and Kiterlin. Author-maintained does not imply sole authorship.

## Excluded proprietary integration

Visualize is an optional OpenAI host plugin. Its installed manifest declares `Proprietary`; no public redistribution grant was established. Its source and assets are not copied. The briefing lead can use an existing host installation for conversation previews. Lack of Visualize does not prevent standalone HTML/SVG explanations.
