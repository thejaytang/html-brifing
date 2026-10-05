---
name: html-brifing
description: Plan, create, revise or review evidence-led HTML project briefings and interactive presentations. Lead storytelling and coordinate Impeccable, UI UX Pro Max, ImageGen, GSAP, optional host Visualize and browser verification; preserve presenter control and verify offline delivery. Use for HTML briefing environment checks, HTML work reports, technical demos and project showcases, not production websites, ordinary text updates or native PPTX authoring.
license: MIT
---

# HTML briefing orchestration

Turn project materials into an explanation a new audience can follow: why the work matters, what was difficult, how the design works, and what the evidence supports. The displayed name is **HTML Briefing**. The existing machine-readable slug `html-brifing` is retained for compatibility with installed users.

## 1. Choose the scope and available capabilities

Read applicable project instructions and current source materials. Find the authoritative content and implementation; fix source files rather than layering patches over generated output. Preserve the user's language, brand, approved content and authorization.

- **Discussion / planning:** inspect materials and propose a narrative; do not build, install or publish.
- **Review only:** inspect and report findings; do not modify the presentation.
- **Create / revise:** implement and validate the authorized scope. A small edit does not trigger a full redesign or a new approval sequence.

Check required tools only when the task reaches them; do not start every briefing with a full setup inventory. Read [environment checks](references/setup.md) if a needed capability is missing or the user explicitly asks to check the environment. For “check environment only” or “只检查环境”, report readiness and stop. Reuse established availability for small edits.

Read [capabilities.md](references/capabilities.md) before selecting helpers. Reuse available skills by capability and user preference; read the actual chosen skill. Never assume a named skill, model or tool exists. Keep third-party installations intact. Check each capability's availability and scope, not every skill on the machine. A skill document does not grant its underlying tool or credentials.

## 2. Establish the narrative and evidence

Determine the audience's existing knowledge, desired understanding or decision, source scope, live versus asynchronous use, language and delivery environment. For new localized design, confirm the one-to-three language set and default unless the user already specified them; preserve an existing set for ordinary edits. Read [workspace controls](references/workspace-controls.md) for the implementation contract. Ask about duration only when it changes content choices. Infer what the materials already establish.

Read relevant implementation, outputs and test records, and inspect provided images. Use one real case to connect explanation and evidence. Preserve the distinction between implemented, tested, planned and another contributor's work. Do not invent screenshots, performance claims or test outcomes.

Use this argument where appropriate: context and importance → concrete problem → core design → mechanism and verification → result, value and next action. It is not a fixed slide count. Decision briefs may lead with the conclusion. Parallel projects may have separate branches; never fabricate a pipeline between independent systems.

Write a short title outline before visual work. Titles alone should reveal the argument. Keep test method, observation and supported conclusion together. Read [narrative.md](references/narrative.md) when planning or restructuring. Storytelling belongs to this lead: choose an audience takeaway, build a claim-to-evidence argument, choose a suitable narrative shape and make scene transitions explain the next question. Do not delegate this responsibility to a generic writing skill or force a fixed chapter template. Reuse existing project records rather than creating paperwork for a small edit.

## 3. Design scenes and select visual media

Each scene has a clear theme and a main explanatory visual. The default view includes the core design and conclusion; object-bound expansion reveals implementation details and evidence. Do not hide the solution itself behind a generic “learn more” control.

For each meaningful interaction, define: **audience question → action → change in the main visual → explanation gained**. A parameter must change the represented evidence, operation or output, rather than only card count or color. Use a static comparison when a meaningful transition cannot be defined.

Read [visual-interaction.md](references/visual-interaction.md) before designing or changing visual interactions. For left-to-right panes, support boundary resizing and supporting-pane collapse/restore; keep language and fullscreen/exit in the top-right toolbar. Read [workspace controls](references/workspace-controls.md) for responsive, keyboard, state and language behavior. For quantitative material, read [data-visualization.md](references/data-visualization.md). For image generation or editing, read [imagegen.md](references/imagegen.md) and use the Codex system `$imagegen` skill when available; this plugin does not bundle a duplicate personal copy. Consider imagery during scene design, not as decoration added at the end.

For a new presenter-led report, use [editorial glass page transitions](references/editorial-glass.md) by default unless the user selects another treatment. Let a translucent sheet rise over the previous page with restrained backdrop blur and slight outgoing-layer scale. Long pages finish their normal reading scroll before a fresh outward gesture turns a page. Existing work keeps its approved treatment; dense reference documents and reduced-motion viewing may use continuous or instant transitions. Verify the visible transition.

Use Impeccable for visual direction and design review; consult UI UX Pro Max for focused style, typography, palette, chart or interaction references within that direction. Keep small edits within the existing design. Use an available host Visualize skill for conversation-only mechanism exploration or interaction previews when it helps; its output does not replace the final offline artifact. Establish shared typography, spacing, colors, selected/focus states and motion timing in the project's existing style source. Use a representative scene with real content and an adjacent transition to check a new direction, then expand it without inventing approval gates.

## 4. Implement the explanation

Reuse existing components and reasonable project architecture. A new standalone briefing can start with semantic HTML, CSS, SVG and a small amount of JavaScript. Add a framework only when state or authoring needs warrant it. Keep content, language, selection state and animation control distinguishable.

Default to presenter-controlled, naturally extending scenes for live use. Asynchronous readers must understand the core argument without narration. Fixed slides, side navigation, title syntax, loops and visual style are project choices; do not impose a past project's layout. See [experience.md](references/experience.md) for reusable lessons and overridable defaults.

Use GSAP only when coordinated sequences or shared-object transitions need it. Use generated images for suitable raster subjects; precise labels, data, connections and interactive state remain editable. Write clear titles and explanations directly, preserving evidence and meaning. Ordinary writing, coding, charts and tables do not require an additional skill. Follow the host agent’s existing competence and applicable project rules.

A new standalone local briefing should open offline unless the project specifies otherwise. Choose a single HTML or an entry file with relative assets. Keep generated final assets inside that deliverable. Live-system demos have separate runtime requirements.

## 5. Verify and deliver

Read [validation-delivery.md](references/validation-delivery.md). Define necessary acceptance checks before running them. Inspect the actual final files with the host's permitted browser tools; use an available Playwright skill when appropriate. Static checks cannot prove rendering, motion, Windows behavior or offline runtime operation.

For feedback, diagnose the cause: “confusing” may mean missing context; “busy” may mean competing themes; “pointless animation” may mean no explanatory state change. Correct shared causes while preserving approved facts and design decisions.

In ChatGPT create/revise tasks, deliver a synchronized Site alongside HTML when Sites is available, following [ChatGPT Sites delivery](references/chatgpt-sites.md) and local-only/no-publish constraints. Use one canonical source and reuse the Site identity; a local preview is not a published Site.

Deliver the entry file or complete resource package, minimal operating instructions and actual validation scope. Mark untested environments and blocked checks explicitly. Do not upload, publish or include private project materials without corresponding authorization. The HTML explanation and the real application's installation are separate deliverables.

For maintenance or provenance, read [experience.md](references/experience.md) and [sources.md](references/sources.md). Ordinary presentation work does not require re-researching the skill ecosystem.

## Bundled skill resolution

This release includes [12 entries](references/bundled-skills.md): this storytelling lead, Impeccable, UI UX Pro Max, Playwright and all eight GSAP modules. Image generation uses the Codex system `$imagegen` skill; users with that system skill do not need a personal duplicate. Visualize is a supported host companion, not redistributed. Load only relevant helpers: a static chart needs neither GSAP nor image generation, and vanilla HTML needs no framework modules. Keep generic writing/coding and academic publishing suites outside the workflow. Prefer an explicitly chosen existing equivalent. Precise diagrams, charts and tables use native HTML/SVG and the data guidance. All helpers remain subordinate to user scope, evidence integrity and project rules.
