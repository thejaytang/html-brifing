# 0.3.1 verification

Date: 2026-09-29. Scope: merge setup into the lead skill; preserve all 17 imported helper snapshots. Prior broader runtime evidence remains in [0.3.0](evaluation-0.3.0.md).

Necessary acceptance groups for this change:
1. Package integrity and automated regression checks: PASS. All 20 unit tests passed, including a mutation that reintroduces a setup entry. All 17 imported helpers retain their recorded hashes; original source snapshots are unchanged.
2. Skill/plugin schemas and manual instruction-path review: PASS. Official lead-skill/plugin validators and marketplace identifier validation passed. Reviewed first-use briefing (internal reference, no separate invocation), environment-only request (report then stop) and a small edit after a completed check (reuse inventory, no repeated setup). Manual review does not prove automatic host routing.
3. Clean installation and exact resource comparison: PASS. Isolated installation resolves version 0.3.1 with 18 skills and validates every recorded imported resource.
4. Bilingual documentation rendering/navigation and public release reproducibility: pending publication. Local rendered docs pass nine checks: both languages at 1280/390px, bidirectional language navigation and four existing assets; inspected the updated narrow Chinese rendering.
5. Production installation and file equality: pending.
6. Native Codex detail page shows a single briefing coordinator and no setup skill: blocked. The computer-use tool explicitly prohibits access to Codex; do not bypass this restriction. File inventory is separate evidence from a refreshed UI.

Overall: verification incomplete. No live image generation, native Windows/Linux or full helper requalification is claimed for this scoped change.
