# 0.2.0 release acceptance

Date: 2026-09-29. This update corrects the incomplete one-skill bundle in 0.1.0. The acceptance unit is one of the eight groups below; individual checks within a group are not added to that denominator.

| Group | Final status | Evidence |
|---|---|---|
| Five skill entrypoints and package resources | PASS | Official plugin validator; official skill validator on all five; eight package regression tests including missing bundled entry, preset and upstream notice |
| Bundled plotting execution | PASS | Four runtime tests for presets, PNG/SVG exports, label-audit detection and rejected export formats; installed copy produced inspected PNG/SVG with zero audit notes |
| First-use and scoped routing | PASS | Independent manual skill-following simulations A/B/C: five bundled + eight companions, preserve existing skills/unknown status, no automatic installation, no repeated setup for small edits, non-causal scholarly prose/table preserve numbers |
| Source integrity and attribution | PASS | All original author-local source hashes unchanged; unadapted bundled copies match snapshot; original licenses retained; table metadata/license adaptations recorded in bundled-sources.json; no personal paths or business materials detected in distributable files |
| Bilingual documentation rendering | PASS | English/Chinese at 1280 and 390 widths, no document overflow; language navigation both ways; four SVG assets loaded; nine browser checks with screenshots inspected |
| Clean local installation | PASS | Supported CLI installs 0.2.0 in isolated test home; five actual SKILL.md files discovered; plot scripts executed from installed copy |
| Public release reproducibility | PASS | Downloaded assets match SHA256; all 58 archive files match tag d77d07e; 12 tests pass from the extracted archive; clean archive installation succeeds |
| Production installation and visible count | INCOMPLETE | Supported CLI confirms enabled 0.2.0, five skill entrypoints and all 34 installed files byte-equal to the release. UI inspection is blocked because the computer-use tool prohibits access to the Codex application; the visible count has not been observed |

These checks do not establish deterministic host routing. The independent evaluation manually followed the actual instructions with fictional fixtures, not a fresh-chat automatic routing harness. ImageGen execution, every external helper combination and native Windows/Linux acceptance remain unverified. Existing 0.1.0 offline-example browser results are historical; the example is unchanged in this release.

Full tests use the isolated project environment described by requirements-dev.lock (Python 3.12 on macOS). The package checker itself uses only the standard library. No external companion was installed or upgraded during this update.

Final overall acceptance: **FAIL (verification incomplete), 7/8 groups passed**. No executed functional check failed. The remaining step is to reopen the plugin detail page and observe five skills and version 0.2.0. The GitHub Chinese README was refreshed in the user browser and visibly contained the new five-skill table, eight-companion list and version 0.2.0.

Original plotting snapshot files retain their source EOF whitespace intentionally; this produced whitespace warnings during staging, not a runtime failure or modified source hash. Release archives are immutable; main adds this post-publication evidence.
