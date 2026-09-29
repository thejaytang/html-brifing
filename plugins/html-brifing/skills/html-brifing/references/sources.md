# Sources, roles and licensing

## Bundled skills

Five actual skill entrypoints ship inside the plugin. The first two are original coordination guidance by Jay Tang. The three author-maintained skills retain their runtime resources and notices; upstream projects remain independently maintained.

| Skill | Maintainer/source | Redistribution |
|---|---|---|
| HTML Brifing | Jay Tang; this repository | MIT |
| HTML Brifing Setup | Jay Tang; this repository | MIT |
| [Academic Humanizer](https://github.com/thejaytang/academic-humanizer) | thejaytang, incorporating credited upstream work | MIT; preserve the bundled [license and provenance](../../academic-humanizer/LICENSE), including AIScientists-Dev and Kiterlin notices |
| [Academic Research Plotting](https://github.com/thejaytang/academic-research-plotting) | thejaytang / Academic Research Plotting contributors | Preserve the bundled [MIT license](../../academic-research-plotting/LICENSE) |
| [Research Results Tables](../../research-results-tables/SKILL.md) | Jay Tang; first bundled public snapshot | [MIT](../../research-results-tables/LICENSE) |

The source snapshot record is in the repository's project-support/bundled-sources.json. No private business documents or source-project screenshots are bundled. Author-maintained does not mean all underlying work was solely authored by the maintainer.

## Recommended external companion set

These eight companion groups are recommended at first use. They are not bundled or installed automatically. Keep working existing copies. Names describe integrations, not endorsement. Follow each upstream's installation instructions and terms; skill instructions alone do not supply runtimes or service access.

| Companion | Author/provider and actual source | Role and boundary |
|---|---|---|
| Impeccable | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | Primary design and visual review; external Apache-2.0 project |
| UI UX Pro Max | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Supplementary typography, palettes and chart references |
| Humanizer | [blader/humanizer](https://github.com/blader/humanizer) | General prose; distinct from the bundled scholarly workflow |
| GSAP Skills | [GreenSock/gsap-skills](https://github.com/greensock/gsap-skills) | Core, timeline, performance and relevant modules; JS library installation and terms remain separate |
| ImageGen | [OpenAI imagegen skill](https://github.com/openai/skills/blob/main/skills/.system/imagegen/SKILL.md) | Image generation/editing; verify the host image tool. No credentials or silent paid API fallback supplied |
| Playwright / equivalent browser | [OpenAI Playwright skill](https://github.com/openai/skills/blob/main/skills/.curated/playwright/SKILL.md), [Playwright project](https://playwright.dev/) | Rendered QA; a working host browser can satisfy this capability |
| Ponytail | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | Simple complete implementation subject to user/project rules |
| Visualize | OpenAI host-provided plugin, through the host's plugin directory | Chat-native exploration; no verified standalone public repository is asserted, and it does not replace the final offline artifact |

## Earlier workflow influences

The author's earlier skill recorded these influences. Their scope is retained here as provenance, not a fresh audit of current upstream behavior. No source code, templates or artwork from these projects are included in the briefing lead.

- [Anthropic internal-comms](https://github.com/anthropics/skills/tree/main/skills/internal-comms): audience and scope awareness; no mandatory weekly-report format.
- [onepage](https://github.com/wjhuang88/onepage-skill): selecting a report form and main visual; no mandatory dense grid.
- [frontend-slides](https://github.com/zarazhangrui/frontend-slides): representative visual preview and overflow inspection; no mandatory fixed canvas or remote fonts.
- [interactive-slides](https://github.com/sylvial928/interactive-slides): scene outline and audience-sensitive density; no mandatory scroll snapping or repeated approval gates.
- [html-artifacts](https://github.com/joshuadavidthomas/agent-skills/tree/main/html-artifacts): evidence, explanatory interaction and offline boundaries; no required component system.

## Host and format references

- [OpenAI: build skills](https://developers.openai.com/plugins/build/skills): related skills, resources and behavior evaluation.
- [OpenAI: package plugins](https://developers.openai.com/plugins/build/plugins): this release uses .codex-plugin/plugin.json and a repository marketplace.
- [Agent Skills specification](https://agentskills.io/specification): format compliance is not proof of runtime portability.

The repository's MIT license covers its original guidance, assets and checker. Bundled derived work retains its own notices. External libraries, generated assets and host services retain their respective terms.
