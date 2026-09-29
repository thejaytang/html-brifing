---
name: html-brifing-setup
description: Check a new HTML Brifing installation and recommend the complete companion skill set. Inventory bundled and already available capabilities, preserve existing skills, link verified installation sources, and install missing items only when authorized. Use on first setup, installation questions or an explicit capability refresh.
license: MIT
---

# First-use setup

Help a new user obtain the full HTML briefing combination without replacing what they already have. This is a setup recommendation workflow, not an automatic installer. Ordinary plugin installation does not execute this skill; the first starter prompt and the briefing lead route users here.

## Inspect the available capabilities

Read the host's exposed skill/tool catalog and, when available, the installed plugin entry. Check only relevant capabilities; do not scan unrelated personal files. A skill can be installed but unavailable in the current chat; distinguish these states and suggest a new chat where appropriate. File presence does not prove its underlying tool or credentials work.

Verify five bundled skill entrypoints relative to this file's parent skills directory:

- html-brifing: narrative, visual composition and delivery coordination.
- html-brifing-setup: this configuration check.
- academic-humanizer: evidence-bound scholarly writing.
- academic-research-plotting: quantitative charts, style, audit and export helpers.
- research-results-tables: numerical reconciliation and explanatory result tables.

The user does not need separate downloads for these. Existing copies remain intact. Prefer the user's explicitly selected existing version; otherwise the bundled copy is the default for these jobs. In a host with namespaced invocation, select this plugin's skill when necessary; when names are ambiguous, inspect the chosen entrypoint rather than guessing or deleting duplicates.

## Recommend the complete companion set

Read [sources and companions](../html-brifing/references/sources.md). Recommend all eight companion groups for the full experience, including capabilities that are optional for a particular briefing:

1. Impeccable: primary visual design and visual review.
2. UI UX Pro Max: supplementary design and chart references.
3. Humanizer: ordinary-language text finishing.
4. GSAP Skills: coordinated motion; core, timeline and performance plus other modules when relevant.
5. ImageGen: raster generation/editing with its underlying tool available.
6. Playwright or the host browser equivalent: actual rendered and interactive verification.
7. Ponytail: project-respecting simple implementation.
8. Visualize: optional chat-native exploration; it does not create the final offline package.

For each group report **available**, **installed but not exposed**, **missing**, or **unknown**, along with role, source and any required execution capability. Do not label an equivalent working browser missing merely because it has no Playwright skill name. Distinguish a recommended exact skill from a satisfied capability. Do not claim GSAP skills install the JS library or ImageGen instructions grant an image service.

Return one concise table for bundled skills and one complete companion checklist. Mark what is already satisfied and recommend filling the remaining gaps. Explain that the full set is recommended, while individual tasks load only relevant helpers. Do not block independent work on optional companions.

Use verified upstream links from sources.md. For host-bundled Visualize use the host's plugin directory; no standalone public skill source has been verified. Do not invent a package URL. If installation commands are needed, consult the actual upstream/host instructions for the user's platform instead of guessing them.

## Authorization and existing installations

A request to check or recommend does not authorize installation. Only install the missing items the user authorizes. Never reinstall, upgrade, replace or remove working existing skills merely to standardize versions. Check licenses, host support and tool requirements before recommending a specific installation path. Do not request secrets in chat or silently choose a paid image-generation route.

Use the user's existing project/environment policy for runtime dependencies. Bundled Matplotlib helper scripts require Matplotlib; the plugin does not install Python packages. Reuse an appropriate isolated environment or explain what is missing.

For an authorized installation, use supported host/skill installation mechanisms, verify installed files and clearly separate installed from functionally exercised. If fresh-chat discovery is required, say so rather than claiming this chat has refreshed.

## Avoid repeat prompts

Treat setup as complete for the current session once the inventory has been reported. Reuse an existing project setup note if supplied, and refresh it only on request or a relevant environment change. Do not repeatedly ask for all companions on each scene or small edit. Do not write a global setup flag or change host configuration just to record that a recommendation was shown.

If only setup was requested, stop after the checklist or authorized installation. Do not start making a presentation. Respect explicit review-only and discussion-only scope.
