# Installation and maintenance

The repository is a small Codex marketplace containing one plugin. The requested plugin and marketplace identifiers are both html-brifing. Keep the extracted directory in place when installing from a local ZIP; a Git installation is managed by Codex.

## Update

The quick start pins v0.3.1 for reproducibility. To move to a newer published version, select that tag explicitly. Inspect `codex plugin marketplace add --help` and the configured source before changing it. When the marketplace name is already configured, remove only its source registration before adding the replacement:

```sh
codex plugin marketplace remove html-brifing
codex plugin marketplace add thejaytang/html-brifing --ref v0.3.1
codex plugin add html-brifing@html-brifing
```

Replace v0.3.1 with the published version you intend to install. This does not authorize deleting project files or other skills. Start a new chat after installation. For local development, use the host's documented plugin cachebuster/update helper; do not edit installed cache files or hand-edit marketplace configuration to force refresh.

## First use, duplicates and bundle updates

Invoke `$html-brifing` in a new chat; it checks relevant capabilities internally on first use. Say “Use $html-brifing to check my environment only” for a standalone check. The bundle contains 18 entries; the former separate setup skill is now an internal reference. Migrating from 0.3.0 removes only that redundant entrypoint, not a helper skill. Preserve personal copies and prefer the user's explicitly chosen version. Otherwise resolve the plugin's own skill path. Do not overwrite global skill folders or ask users to separately install already-included skills.

All redistributed snapshots and file hashes are in plugins/html-brifing/bundle.json; the companion THIRD_PARTY_NOTICES.md identifies upstreams, licenses and adaptations. When updating a copied skill, review its actual changes, preserve notices, update its hashes and rerun structural and behavioral checks. Do not apply the root MIT license over Apache-2.0 material. Visualize stays external until a redistribution grant is established.

Runtime tools are separate: image service, browser, Node/npx, Python packages, GSAP JS and the Impeccable engine. Setup recommends missing capabilities without installing them. Preserve project isolation and user authorization.

## Legacy personal html-briefing skill

This plugin's entrypoint is html-brifing. An older html-briefing skill can remain installed, but do not run two orchestration workflows for the same task. For a deliberate migration, back up the old directory and replace its instructions with a short pointer only after the plugin is installed and validated. Migration is a user-approved local action, not an automatic installation hook.

## Validation boundaries

`python3 scripts/check_package.py` checks packaged references, manifest paths and SVG XML. It does not execute arbitrary HTML, download helpers, inspect private source projects or establish runtime compatibility. Behavioral and browser evidence belongs in project-support/evaluation.md. Runtime image generation and native Windows acceptance require separate tests.
