# Installation and maintenance

The repository is a small Codex marketplace containing one plugin. The requested plugin and marketplace identifiers are both html-brifing. Keep the extracted directory in place when installing from a local ZIP; a Git installation is managed by Codex.

## Update

The quick start pins v0.1.0 for reproducibility. To move to a newer published version, select that tag explicitly. Inspect `codex plugin marketplace add --help` and the configured source before changing it. When the marketplace name is already configured, remove only its source registration before adding the replacement:

```sh
codex plugin marketplace remove html-brifing
codex plugin marketplace add thejaytang/html-brifing --ref v0.1.0
codex plugin add html-brifing@html-brifing
```

Replace v0.1.0 with the published version you intend to install. This does not authorize deleting project files or other skills. Start a new chat after installation. For local development, use the host's documented plugin cachebuster/update helper; do not edit installed cache files or hand-edit marketplace configuration to force refresh.

## Optional helpers

Keep your own skills. Select equivalents by inputs, output, tool availability and evidence boundaries using the bundled capability map. Third-party licenses and update schedules remain separate. If a recommended helper is unavailable, baseline guidance covers ordinary scenes and diagrams. Required ImageGen or browser work stays unverified until the necessary tool is available.

## Legacy personal html-briefing skill

This plugin's entrypoint is html-brifing. An older html-briefing skill can remain installed, but do not run two orchestration workflows for the same task. For a deliberate migration, back up the old directory and replace its instructions with a short pointer only after the plugin is installed and validated. Migration is a user-approved local action, not an automatic installation hook.

## Validation boundaries

`python3 scripts/check_package.py` checks packaged references, manifest paths and SVG XML. It does not execute arbitrary HTML, download helpers, inspect private source projects or establish runtime compatibility. Behavioral and browser evidence belongs in project-support/evaluation.md. Runtime image generation and native Windows acceptance require separate tests.
