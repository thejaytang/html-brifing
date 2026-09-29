# Environment checks when needed

Normal use starts with the briefing task, not a full inventory. Check the tool needed for the current step. Read this reference for an actual capability gap or an explicit environment-check request; report only relevant available, missing or unknown capabilities.

- Design: Impeccable guidance and launcher are included. Its platform engine is separate; use its documented direct-context fallback if unavailable. Do not enable hooks or install an engine as a check side effect.
- Images: ImageGen instructions are included, but the host image-generation tool/service must be available. No silent paid API fallback or credentials in chat.
- Browser verification: use a permitted host browser tool; the bundled Playwright wrapper is an alternative requiring Node/npx and a browser. Do not install global tools as a check side effect.
- Motion: GSAP core/timeline guidance is included. Only when the scene benefits from coordinated motion, add the JS runtime within the authorized project's isolated dependencies and package it locally for offline use. Simple transitions need no GSAP.

Writing, coding, charts and tables use the agent's normal abilities and project tools. Do not recommend a supplementary skill suite. Other upstream GSAP modules and Visualize are not required.

For an explicit package check, verify [the six bundled entries](bundled-skills.md). Missing packaged files call for repair/reinstallation of this plugin, not separate helper downloads. Distinguish file presence, exposure in the current chat and actual exercised functionality. A new chat may be needed after an update.

Preserve existing personal skills. Prefer an explicitly selected existing equivalent; otherwise use the bundled copy, resolved from its actual directory. Do not overwrite or standardize other installs.

Reuse checks until relevant conditions change. Environment-only requests finish with the result; they do not start a presentation or install anything. Do not create a global setup flag.
