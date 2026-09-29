---
name: html-brifing-setup
description: Check the complete HTML Brifing bundle on first use. Verify its 19 included skills, preserve the user's existing versions, and identify missing host tools or runtimes. Use for first setup, installation questions or an explicit capability refresh; do not install anything merely because setup was requested.
license: MIT
---

# First-use check

The plugin contains 19 real skill entrypoints. Read [the bundled inventory](../html-brifing/references/bundled-skills.md) and verify their paths. Users do not need separate skill downloads for those entries. Installation itself does not execute this workflow; the setup starter and lead skill route first-time users here.

## Inventory and duplicates

Inspect the exposed skill/tool catalog and the plugin entry when available. Distinguish file-present, exposed in this chat, and functionally exercised. A same-name personal copy may coexist: preserve it, use the user's selected copy, otherwise use this plugin's bundled copy. Resolve the selected entrypoint and its resources from its actual directory. Do not guess which duplicate was loaded, delete a copy or upgrade an existing installation to standardize versions.

If the package lacks one of its 19 bundled entries, report an incomplete package and recommend reinstalling/updating HTML Brifing through the documented source; do not instruct users to assemble 17 separate downloads. A stale current chat may need a new chat before discovery updates.

## Runtime readiness

Return a compact inventory grouped by role and a readiness table. Check only capabilities needed for this work; distinguish available, missing, unknown and installed-but-not-exposed. Recommend completing relevant missing runtimes, with the following boundaries:

- Impeccable: instructions, playbooks and launcher are bundled. Its separate platform engine may be present, or the upstream launcher may download its pinned version on first use. Preserve host permissions; do not enable hooks as a setup side effect. If engine execution is unavailable, follow the skill's documented direct-context fallback.
- UI UX Pro Max: all local search data/scripts are bundled; Python is required to execute the search.
- ImageGen: instructions, references and fallback scripts are bundled; the actual host image-generation tool must be available. Skill installation grants no service access. No paid API fallback without explicit user choice, and no secrets in chat.
- Playwright: instructions and wrapper are bundled; a working host browser may satisfy QA instead. The wrapper needs Node/npx and can resolve the Playwright CLI on use. Check project/runtime permissions; do not install global tools automatically.
- GSAP: all eight guidance modules are bundled. Add the GSAP library to the target project's isolated dependencies only when motion is needed and implementation is authorized; package runtime assets locally for offline delivery.
- Academic plotting: scripts and presets are bundled; Matplotlib and any chart-specific libraries belong to the target project's isolated environment.
- Humanizer, Academic Humanizer, Results Tables and Ponytail: instructions work without a separate service. Only load the workflows relevant to the current step. Ponytail cannot override the user's completeness, validation, communication or project rules.
- Visualize: the sole external companion in this workflow. Its original plugin is proprietary and is not redistributed here. If available in the host, use it for chat previews. Otherwise recommend the host plugin directory without inventing a public repository or blocking standalone HTML work.

A setup recommendation does not authorize installing or updating runtimes, modifying host configuration or using paid services. For authorized installations use supported mechanisms, verify the result and distinguish installed from actually exercised.

## One check, then work

Once the inventory is reported, reuse it for the current session or supplied project setup note. Refresh only on request or a relevant environment change. Do not re-run the complete checklist for a title edit or every scene. Do not create a global setup flag. If only setup was requested, finish with the checklist; do not create a presentation.
