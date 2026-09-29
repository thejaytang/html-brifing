# Capability selection and handoffs

This is an orchestration contract interpreted by the agent, not an automatic dependency installer or a promise of deterministic skill dispatch. Load only helpers relevant to the current step. Explicit user instructions and project constraints govern the work.

## Selection

1. Check skills and tools exposed by the host. If a local skill is relevant, read its actual entrypoint and required references. Never hardcode another user's home path.
2. Prefer the user's chosen helper, then the recommended helper below, then an available equivalent with the required inputs, outputs and evidence boundary. A matching name alone is insufficient.
3. Briefly state the helpers selected and any material gap. Do not require a routing report for a typo fix.
4. If a helper is absent, use the supported baseline below. If a required capability is absent, complete independent work and identify the minimum missing step. Do not quietly change an explicitly requested medium or claim an unperformed check.
5. Do not install, update, overwrite or remove other skills as a side effect of making a briefing. Obtain appropriate authorization for installation. Host and paid-service permissions remain in force.

| Job and trigger | Recommended available helper | Input → expected output | Baseline / boundary |
|---|---|---|---|
| New visual direction or substantial layout work | Impeccable | Audience, real scene, brand → coherent layout and reusable visual rules | Apply the bundled visual guidance with native HTML/CSS/SVG |
| Specific typography, palette or chart reference gap | UI UX Pro Max | A focused design question → reference to fit the existing direction | Do not generate a competing second design system |
| Quantitative evidence | academic-research-plotting; available data-visualization equivalent | Data, definitions, source and intended comparison → appropriate plot with units and uncertainty | Follow data-visualization.md; simple native graphics are sufficient where accurate |
| Empirical result tables | research-results-tables | Actual analysis output → reconciled, readable table with notes | A plain semantic HTML table is sufficient; do not infer missing estimates |
| Coordinated motion | GSAP core / timeline / scrolltrigger / performance as needed | Object identity and state transitions → controlled motion with stable reduced-motion state | CSS/native animation or static comparison; keep the presenter in control |
| Raster scene, illustration, cutout or image edit | imagegen | Purpose, composition, source roles and invariants → inspected final image in deliverable assets | Built-in image tool when available; no silent paid API fallback or fake screenshot |
| General prose finish | humanizer | Evidence-bound titles and explanations → natural copy with meaning preserved | Perform a concise prose check; no required diagnostic dump |
| Scholarly text | academic-humanizer or applicable equivalent | Claims, sources, author intent → faithful scholarly wording | Do not stack a second full general-humanizer workflow |
| Actual code implementation | Project's coding guidance; Ponytail when installed | Required behavior and existing architecture → smallest complete implementation | Simplicity never overrides accessibility, isolation or required tests |
| Rendered behavior and final-file QA | Host browser tools; playwright when appropriate | Final entrypoint, state sequence and viewports → observed results and evidence | If unavailable, static review only; browser acceptance remains NOT_RUN |
| Chat-only interactive explanation | visualize when available | Question or interaction idea → conversation preview | Not the final offline HTML package |

## Shared handoff contract

Keep a compact record in the existing project plan/content model when the task warrants it:

- audience, decision and narrative outline;
- claim → source location → evidence status → allowed wording;
- current visual tokens and reusable components;
- scene question, selected representation, object identity and state transitions;
- helper selected, artifact produced and unresolved limitations;
- final file boundary and acceptance checks.

One lead workflow owns integration. A helper's attractive image, passing unit test or successful export does not establish whole-briefing acceptance. Resolve conflicting recommendations in favor of user instructions, factual fidelity, required function and accessibility before stylistic preferences. A polishing budget does not waive required tests.

## Getting helpers

Recommended helpers are optional and not redistributed in this plugin. Keep existing installations. See sources.md for verified public upstreams and product documentation. Some helpers are private or user-maintained names, so treat them as capability hints rather than public download promises. There is no automatic skill dependency resolution here.

Pin a helper version in project evidence when it materially affects reproducibility; otherwise record the helper actually used. Do not claim broad compatibility from one local combination.
