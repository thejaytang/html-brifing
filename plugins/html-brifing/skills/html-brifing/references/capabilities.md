# Capability selection and handoffs

This is an orchestration contract interpreted by the agent, not an automatic dependency installer or a promise of deterministic skill dispatch. Load only helpers relevant to the current step. Explicit user instructions and project constraints govern the work.

## Selection

1. Check skills and tools exposed by the host. If a local skill is relevant, read its actual entrypoint and required references. Never hardcode another user's home path.
2. Prefer the user's explicitly selected existing helper; otherwise choose the real bundled entry from [the inventory](bundled-skills.md). The five helper entries in the inventory are the entire bundled set; ordinary agent capabilities need no skill wrapper. A matching name does not establish the selected version or its runtime availability.
3. Briefly state the helpers selected and any material gap. Do not require a routing report for a typo fix.
4. If a helper is absent, use the supported baseline below. If a required capability is absent, complete independent work and identify the minimum missing step. Do not quietly change an explicitly requested medium or claim an unperformed check.
5. Do not install, update, overwrite or remove other skills as a side effect of making a briefing. Obtain appropriate authorization for installation. Host and paid-service permissions remain in force.

| Job and trigger | Recommended available helper | Input → expected output | Baseline / boundary |
|---|---|---|---|
| New visual direction or substantial layout work | Impeccable | Audience, real scene, brand → coherent layout and reusable visual rules | Apply the bundled visual guidance with native HTML/CSS/SVG |
| Quantitative evidence | Native HTML/SVG or existing project chart tools | Data, definitions, source and intended comparison → appropriate plot with units and uncertainty | Follow data-visualization.md; simple native graphics are sufficient where accurate |
| Empirical result tables | Semantic HTML tables | Actual analysis output → reconciled, readable table with notes | A plain semantic HTML table is sufficient; do not infer missing estimates |
| Coordinated motion | GSAP core / timeline only when coordinated motion is needed | Object identity and state transitions → controlled motion with stable reduced-motion state | CSS/native animation or static comparison; keep the presenter in control |
| Raster scene, illustration, cutout or image edit | imagegen | Purpose, composition, source roles and invariants → inspected final image in deliverable assets | Built-in image tool when available; no silent paid API fallback or fake screenshot |
| Rendered behavior and final-file QA | Host browser tools; playwright when appropriate | Final entrypoint, state sequence and viewports → observed results and evidence | If unavailable, static review only; browser acceptance remains NOT_RUN |

## Shared handoff contract

Keep a compact record in the existing project plan/content model when the task warrants it:

- audience, decision and narrative outline;
- claim → source location → evidence status → allowed wording;
- current visual tokens and reusable components;
- scene question, selected representation, object identity and state transitions;
- helper selected, artifact produced and unresolved limitations;
- final file boundary and acceptance checks.

One lead workflow owns integration. A helper's attractive image, passing unit test or successful export does not establish whole-briefing acceptance. Resolve conflicting recommendations in favor of user instructions, factual fidelity, required function and accessibility before stylistic preferences. A polishing budget does not waive required tests.

## Bundle and runtime gaps

Read [the six-entry inventory](bundled-skills.md) only when resolving a helper or diagnosing the package. Preserve personal installations. Check tools at the point of use; read [environment checks](setup.md) for a real gap or an explicit check request. Missing skill files indicate an incomplete installation. Missing image tools, a browser or a required runtime is a separate capability gap. Do not suggest installing a general writing, coding or academic skill suite.

Sources, notices and adaptations are packaged in [THIRD_PARTY_NOTICES](../../../THIRD_PARTY_NOTICES.md). Pin runtime versions in project evidence when they materially affect reproducibility. Do not infer whole-briefing acceptance from a helper's local success.
