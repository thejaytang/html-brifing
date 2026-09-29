---
name: academic-humanizer
description: Revise or audit academic manuscripts, theses, abstracts, rebuttals, cover letters, and research proposals for clear, concise, author-consistent scholarly prose. Use when Codex should prioritize information, remove defensive or reviewer-facing framing, make minimal evidence-bound edits, restructure paragraphs, match an author's voice or target venue, calibrate claims to supplied evidence, restore section function, or independently validate a revision. Do not use for detector evasion, authorship attribution, pure translation, hiding unfavorable findings, or inventing facts and citations.
license: MIT
---

# Academic Humanizer

Improve academic prose without changing the scholarship. Optimize for clarity, precision, argument visibility, and an identifiable authorial voice. Do not optimize for an AI-detector score or claim that prose is human- or AI-authored.

## Select the mode

Infer the least invasive mode that satisfies the request:

- **Polish**: return a revised passage. This is the default when the user asks to edit, improve, humanize, or polish.
- **Audit**: diagnose paragraph-level problems without rewriting unless examples are requested.
- **Polish + audit**: revise, then run the independent validation gate below. Use for submission-facing, high-stakes, long, or heavily edited text.
- **Voice profile**: derive editing constraints from author samples before revising. Use when samples are supplied or voice matching is explicit.
- **Structural compression**: prioritize, compress, merge, move, or remove low-value material while preserving the argument. Use only when the user requests substantive polishing, restructuring, shortening, or a word-limit reduction.

Do not turn a local language edit into a substantive or structural rewrite. If the text's argument or section function is broken, distinguish the writing defect from the missing scholarly work.

## Establish the editing contract

Before editing, identify from the request and supplied files:

1. manuscript language and discipline;
2. document and section type;
3. target venue and any supplied style guide;
4. author samples, if any;
5. evidence available for checking claims;
6. requested depth: copyedit, substantive polish, or structural edit.

Ask only when a missing choice would materially change the revision. Otherwise use conservative academic prose in the source language.

Classify the evidence scope:

- **Text-only**: calibrate wording only against evidence visible in the passage. Never supply a missing number, source, result, mechanism, or citation.
- **Source-backed**: use only the manuscript, tables, figures, references, analysis outputs, and style materials the user supplied or authorized you to inspect.
- **Externally verified**: verify current venue rules or factual claims only when the user requests it or the task requires current authoritative guidance. Prefer official sources.

State unresolved evidence gaps as author queries. A fluent sentence is not a substitute for evidence.

## Prioritize information for the reader

Run this gate before sentence-level polishing for abstracts, introductions, conclusions, long sections, word-limit work, or structural compression. Identify the manuscript's central contribution and the current section's job. Then classify each sentence:

- **Essential**: directly establishes the problem, contribution, evidence, result, reasoning, or boundary needed here.
- **Supporting**: improves understanding or credibility but can be compressed.
- **Procedural**: accurate detail that may belong in methods, a note, or an appendix.
- **Redundant**: repeats information already established without adding a necessary distinction.
- **Misplaced**: useful information located in the wrong section or paragraph.

For each non-essential sentence, choose only among retain, compress, merge, move, or remove. Base the choice on reader value, section function, word budget, and whether deleting it would change the argument or its evidential boundaries.

Do not remove, relocate, or merge substantive content during ordinary copyediting or minimal polishing. In structural compression mode, make those changes reviewable and distinguish them from language edits. Never remove a limitation, qualifier, null result, counterargument, or identification assumption merely because it interrupts the narrative.

## Build a preservation ledger

Before rewriting, record protected content at the granularity needed for the task:

- numbers, signs, units, ranges, dates, sample sizes, effect directions, uncertainty intervals, and significance statements;
- equations, symbols, variable names, code-like strings, model and dataset names;
- citations, cite keys, quotations, table/figure/appendix references, footnotes, and cross-references;
- named constructs, definitions, hypotheses, research questions, causal language, scope conditions, limitations, and contribution boundaries;
- required terminology and consistent referents.

Preserve these exactly unless the user explicitly authorizes a substantive correction. Never silently reconcile contradictory values or citations. Flag the conflict.

Preserve meaning at proposition level, not merely keyword level. A revision must not change polarity, comparison group, outcome, population, timeframe, causal status, degree of certainty, or who performed an action.

## Create a voice and venue profile

When author samples are available, prefer two or more representative passages from the same genre and language. Treat them as evidence of tendencies, not a phrase bank. Extract a compact profile:

- sentence-length distribution and syntactic density;
- paragraph openings and claim placement;
- first-person, passive-voice, connective, and parenthetical habits;
- hedging strength and location;
- preferred technical verbs, terminology, spelling, punctuation, and citation integration;
- degree of compression, exposition, and explicit signposting.

Match stable tendencies without reproducing distinctive sentences or importing claims from the samples. Do not imitate errors, obsolete terminology, or one-off quirks.

For venue matching, follow a current user-supplied or official guide when available. Separate binding requirements from stylistic inference. Do not rely on stereotypes such as “Venue X always wants terse prose.” If no reliable venue evidence exists, use discipline-appropriate scholarly prose and label the venue match as provisional.

When author voice conflicts with a binding venue rule, follow the venue rule while preserving the author's remaining preferences.

## Edit in two passes

### Pass 1: Restore scholarly function

Identify each paragraph's main function and ensure its first-order content performs that function:

- **Abstract**: problem, approach, bounded main result, and implication without unsupported novelty or importance claims.
- **Introduction**: concrete problem, literature gap, research question, approach, and bounded contribution in a coherent progression.
- **Literature review**: relationships among cited works, disagreement or limitation, and the manuscript's positioning; avoid citation dumps and generic topic summaries.
- **Theory/hypotheses**: explicit constructs, mechanism, assumptions, boundary conditions, and prediction; do not convert association into causation.
- **Methods**: reproducible actors, materials/data, procedure, estimand/model, and decision rules; retain necessary passive voice and standard reporting language.
- **Results**: report estimates and uncertainty before interpretation; keep planned, exploratory, null, and robustness results distinct.
- **Discussion**: interpret rather than repeat; connect claims to results, alternatives, limitations, scope, and contribution.
- **Conclusion**: synthesize the bounded answer without introducing evidence or escalating claims.
- **Rebuttal/response letter**: acknowledge the exact concern, state the action or reasoned disagreement, and point to the changed text or evidence.
- **Cover letter**: communicate fit and contribution precisely without unsupported promotion.
- **Proposal**: connect significance to a concrete need and ambition to feasibility; preserve justified vision language while flagging unsupported promises.

If a paragraph has multiple incompatible jobs, propose a split only when local edits cannot repair it.

### Pass 2: Make the smallest effective language changes

Prioritize edits in this order:

1. correct claim-evidence mismatch;
2. expose the actor, action, comparison, mechanism, or scope;
3. remove generic framing, empty intensifiers, filler, and redundant summary;
4. repair logical connections and referents;
5. reduce avoidable nominalization and clause stacking;
6. vary rhythm only where repetition impairs reading;
7. copyedit grammar, punctuation, and consistency.

Do not replace precise scholarly prose merely to make it sound different. Passive voice, repeated technical terms, first-person plural, conventional section signposting, semicolons, cautious hedging, and long sentences may be correct. Judge their function in context.

Use the detailed diagnostics and false-positive controls in [references/rubric.md](references/rubric.md) for paragraph scoring, claim calibration, or difficult cases.

## Calibrate claims to evidence

For each material claim, record:

`claim -> evidence anchor -> inference type -> scope -> warranted verb`

Use these distinctions:

- observed/descriptive result;
- association or model-dependent estimate;
- causal estimate under stated identification assumptions;
- interpretation or mechanism;
- generalization beyond the observed sample;
- normative or practical implication;
- proposal promise supported by feasibility evidence.

An evidence pointer does not automatically justify a claim. Check whether it supports the same construct, comparison, population, timeframe, and inference type. Keep uncertainty where the design requires it. Remove vague hedging only when the evidence supports a more exact statement.

When support is missing, choose the least invasive valid action:

1. point to supplied evidence already available;
2. narrow the claim to what the evidence supports;
3. preserve the wording and add an author query if neither is justified.

Never fabricate a number, citation, analysis, mechanism, robustness result, limitation, author preference, or venue requirement.

## Remove defensive framing without weakening the evidence

Use a claim-forward, evidence-bound structure:

`positive claim -> evidence -> one material boundary`

Avoid writing as if negotiating with an imagined reviewer. For each apparent caveat, disclaimer, prebuttal, apology, or self-limitation, classify it before editing:

- **Necessary caveat**: changes validity, interpretation, scope, ethics, safety, or methodological transparency. Keep it, state it once, and place it where readers need it.
- **Defensive**: mainly anticipates criticism, repeats what the paper does not claim, excuses a result, or signals the evidence boundary without adding information. Delete or positively reframe it.
- **Mixed**: combines a real boundary with reviewer-facing rhetoric. Preserve the boundary and remove the defensive wrapper.
- **Clean**: advances the argument directly. Leave it alone.

Prefer positive scope statements. State what the study examines, estimates, observes, supports, or applies to before stating what it does not establish. A negative formulation is appropriate only when the negation itself is a result, a necessary distinction, a safety constraint, or a direct response in a rebuttal.

Keep the manuscript and the editorial channel separate:

- The revised manuscript must not say `the passage does not provide`, `the available evidence is insufficient`, `citation needed`, or similar process language unless that statement is itself part of the scholarly argument.
- Put missing-evidence notes, source-verification needs, and meaning-dependent decisions in a separate **Author queries** section.
- In **Text-only** mode, lack of a visible evidence anchor does not prove the source claim false. Preserve its substantive direction, calibrate unjustified certainty or breadth, and query the missing support separately.

Do not replace defensiveness with promotion. Do not hide or downplay unfavorable comparisons, negative or null results, contradictory evidence, rival explanations, real limitations, or failed robustness checks when they affect interpretation. Reframe authorial apology; preserve the scientific fact.

For a detailed defensive-writing taxonomy and placement rules, read [references/rubric.md](references/rubric.md).

## Independent validation gate

After revising, audit the before/after text as if reviewing someone else's edit. Do not assume the rewrite is correct.

Check:

1. **Coverage**: every original substantive proposition remains unless removal was authorized.
2. **Protected-content equality**: ledger items are unchanged or every authorized change is disclosed.
3. **Semantic fidelity**: no change to polarity, magnitude, comparison, scope, causality, certainty, or attribution.
4. **Claim-evidence fit**: every strengthened, softened, or relocated claim remains supported.
5. **Section function**: the passage performs the correct rhetorical job.
6. **Voice/venue fit**: matched features are evidence-based and binding requirements are satisfied.
7. **Naturalness**: no new formulaic transitions, synonym cycling, choppy simplification, generic evaluation, or uniform cadence.
8. **Document consistency**: terminology, abbreviations, notation, tense, person, and cross-references remain coherent.
9. **Cross-artifact consistency**: when the relevant sources are available, compare key numbers, units, sample definitions, table/figure statements, and citation identities across the abstract, main text, tables, figures, appendices, and response materials. Report what was actually checked.
10. **Anti-defensive regression**: no author query, audit note, imagined reviewer objection, repeated disclaimer, result excuse, or unnecessary self-limitation has entered the manuscript; every necessary caveat and unfavorable finding still survives.

If a check fails, repair and rerun the affected checks. If repair requires evidence or author judgment not available, do not guess; return an explicit unresolved query.

## Output

Adapt the response to the request. Do not bury the revised text under a long audit.

For ordinary polishing, return:

1. revised text;
2. a concise change note;
3. unresolved author queries in a clearly separate section, only if any;
4. preservation statement covering numbers, citations, equations, and substantive claims.

For audit mode, return a compact paragraph table with `location`, `function`, `severity`, `confidence`, `evidence`, `diagnosis`, and `minimal action`. Quote only the words needed to identify an issue.

For high-risk or extensive revisions, also report:

- substantive changes distinguished from stylistic edits;
- claim-evidence changes and their anchors;
- voice/venue profile used and its evidence basis;
- validation result: `PASS`, `PASS WITH QUERIES`, or `FAIL`.

Offer alternative phrasings only when they reflect a real scholarly choice, such as stronger compression versus fuller exposition. Do not create cosmetic variants.

## Boundaries

- Follow applicable disclosure and authorship policies. Editing does not remove disclosure obligations.
- Do not predict or optimize detector outcomes, introduce deliberate errors, or disguise provenance.
- Do not infer misconduct or AI authorship from style signals.
- Do not overwrite a source file unless the user asked for file edits. Preserve the original or make changes reviewable.
- Treat generated prose as editorial assistance requiring author approval, especially where claims, interpretations, or disciplinary conventions are involved.
