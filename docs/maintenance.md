# Installation and maintenance

The repository is a small Codex marketplace containing one plugin. The requested plugin and marketplace identifiers are both html-brifing. Keep the extracted directory in place when installing from a local ZIP; a Git installation is managed by Codex.

## Update

The quick start pins v0.5.0 for reproducibility. To move to a newer published version, select that tag explicitly. Inspect `codex plugin marketplace add --help` and the configured source before changing it. When the marketplace name is already configured, remove only its source registration before adding the replacement:

```sh
codex plugin marketplace remove html-brifing
codex plugin marketplace add thejaytang/html-brifing --ref v0.6.0
codex plugin add html-brifing@html-brifing
```

Replace v0.5.0 with the published version you intend to install. This does not authorize deleting project files or other skills. Start a new chat after installation. For local development, use the host's documented plugin cachebuster/update helper; do not edit installed cache files or hand-edit marketplace configuration to force refresh.

## First use, duplicates and bundle updates

Invoke `$html-brifing` directly. Storytelling stays in the lead. The bundle includes 12 entries: the lead, Impeccable, UI UX Pro Max, Playwright and eight GSAP modules. Use Codex system `$imagegen`; a separate personal copy is unnecessary when the system skill is present. Select by need; no full-suite execution or mandatory setup inventory. Visualize is an optional host companion for chat previews, not redistributed source. Preserve existing personal copies. Generic writing/coding and academic suites remain outside the plugin.

All redistributed snapshots and file hashes are in plugins/html-brifing/bundle.json; the companion THIRD_PARTY_NOTICES.md identifies upstreams, licenses and adaptations. When updating a copied skill, review its actual changes, preserve notices, update its hashes and rerun structural and behavioral checks. Do not apply the root MIT license over Apache-2.0 material. Visualize stays external until a redistribution grant is established.

Runtime tools are separate: image service, browser, Node/npx, GSAP JS and the Impeccable engine. Check missing capabilities only when needed, without installing them as a check side effect. Preserve project isolation and user authorization.

## Legacy personal html-briefing skill

This plugin's entrypoint is html-brifing. An older html-briefing skill can remain installed, but do not run two orchestration workflows for the same task. For a deliberate migration, back up the old directory and replace its instructions with a short pointer only after the plugin is installed and validated. Migration is a user-approved local action, not an automatic installation hook.

## Validation boundaries

`python3 scripts/check_package.py` checks packaged references, manifest paths and SVG XML. It does not execute arbitrary HTML, download helpers, inspect private source projects or establish runtime compatibility. Behavioral and browser evidence belongs in project-support/evaluation.md. Runtime image generation and native Windows acceptance require separate tests.
