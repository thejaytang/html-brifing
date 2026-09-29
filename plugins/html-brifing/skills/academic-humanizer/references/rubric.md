# Academic Humanizer Rubric

Read this reference when the task requires paragraph-level scoring, strong claim-evidence checking, difficult false-positive decisions, or independent validation of a substantial revision.

## Review unit

Assess a paragraph as a rhetorical unit. Record:

- section and intended function;
- core claim or task;
- evidence anchor and inference type;
- author/venue feature that matters;
- smallest edit that fixes the defect.

Do not score isolated words without context.

## Severity and confidence

| Severity | Meaning | Default action |
|---:|---|---|
| 0 | Functional, precise, and natural for its context | Leave unchanged except requested copyediting |
| 1 | One local defect with little effect on the argument | Phrase- or sentence-level edit |
| 2 | Multiple defects obscure the claim, evidence, logic, or voice | Focused paragraph revision |
| 3 | The paragraph does not perform its scholarly function or materially misstates evidence | Reconstruct the paragraph or return an author query |

Confidence reflects the evidence for the diagnosis:

- `low`: may be a field convention, required wording, translation feature, or author preference;
- `medium`: the defect is visible, but its effect or best repair depends on context;
- `high`: multiple independent signals or a direct claim-evidence/section-function mismatch establish the problem.

Severity 3 requires a functional or substantive failure, not a vocabulary match.

## Diagnostic families

### 0. Information value and placement

Before judging style, ask whether each sentence earns its location and length. Classify it as essential, supporting, procedural, redundant, or misplaced. Use retain, compress, merge, move, or remove as the available actions.

Flag:

- accurate but low-value detail crowding out the central contribution or result;
- background the intended reader already knows;
- the same claim repeated across adjacent paragraphs or sections without a new function;
- procedural detail in an abstract, introduction, results interpretation, or conclusion;
- important limitations, results, or scope conditions buried after secondary material.

Do not treat brevity as the objective. Preserve information required to understand, reproduce, qualify, or fairly evaluate the work. Only apply deletion or relocation when substantive editing is authorized.

### 1. Claim-evidence mismatch

Check whether the evidence anchor supports the claim's construct, direction, magnitude, comparator, population, timeframe, causal status, and generality.

Flag:

- `prove`, `establish`, `confirm`, `cause`, `robust`, `generalizable`, or `significant` when the supplied evidence does not warrant that meaning;
- broad claims supported only by one setting, proxy, subgroup, model specification, or citation;
- vague magnitudes where supplied results allow exact reporting;
- citations placed near a claim but not clearly supporting it;
- interpretation presented as an observed result;
- proposal ambition without supplied feasibility evidence.

Do not strengthen a claim just because the prose sounds hesitant. Do not invent the evidence needed to make a stronger sentence true.

### 2. Missing specificity

Flag prose that hides the research object behind generic nouns or evaluations. Look for missing actors, variables, methods, mechanisms, comparisons, scope conditions, or evidence anchors.

Words such as `important`, `novel`, `robust`, `comprehensive`, `complex`, `significant`, `framework`, `landscape`, and `implications` are not defects by themselves. Flag them only when they replace information the sentence needs.

### 3. Formulaic progression

Flag repeated generic openers, serial `Moreover/Furthermore/Additionally`, predictable three-part padding, empty recap sentences, and transitions that name no logical relation.

Repair by making the actual relation visible: contrast, cause, condition, evidence, consequence, concession, or sequence. Delete a connector when paragraph order already supplies the relation.

### 4. Promotional or inflated framing

Flag importance, novelty, or impact language whose object and basis are absent. Replace it with the concrete gap, consequence, result, or scope already supported by the source.

Do not flatten justified vision language in proposals, or strong conclusions directly supported by the design and results.

### 5. Abstraction and nominalization overload

Flag noun-heavy phrasing when it hides who did what, or when stacked abstractions create ambiguous relations. Restore an actor and a precise verb when the discipline permits.

Do not force an actor into procedural passive constructions where the actor is irrelevant.

### 6. Mechanical rhythm and syntax

Flag repeated sentence openings, uniform sentence lengths, serial clause stacks, excessive parenthetical interruption, or choppy simplification. Revise only when the pattern impairs emphasis or comprehension.

Sentence length is diagnostic, not a threshold. A long sentence can be correct when its hierarchy is clear.

### 7. Voice flattening

Flag edits that erase the author's interpretive move, preferred level of directness, or disciplined use of `we`; produce generic consensus language; or substitute decorative synonyms for stable terms.

Voice matching must be grounded in supplied samples. Do not infer personal traits or add humor, informality, anecdotes, opinions, or autobiographical experience.

### 8. Section-function mismatch

Examples:

- an abstract spends space on generic context but omits the bounded result;
- a literature review lists sources without explaining relationships or positioning;
- a theory paragraph states a prediction without a mechanism or boundary condition;
- methods sell importance rather than describe procedure;
- results interpret before reporting the estimate and uncertainty;
- discussion repeats results without addressing meaning, alternatives, limitations, or scope;
- a rebuttal thanks the reviewer but does not answer the concern;
- a proposal states ambition without a route, evidence, fallback, or measurable outcome.

Fix the function before surface style.

### 9. Process leakage and generic meta-language

Remove drafting residue, placeholder phrasing, unexplained meta-commentary, and text that speaks about “this response,” “the prompt,” or the writing process when it does not belong in the manuscript.

Do not remove legitimate methodological reflexivity or preregistered process descriptions.

### 10. Defensive academic writing

Classify each candidate as `NECESSARY_CAVEAT`, `DEFENSIVE`, `MIXED`, or `CLEAN`. Diagnose its rhetorical function, not the presence of a cue word.

#### Reviewer-facing prebuttal

The manuscript anticipates an objection before advancing its own claim: `one might argue`, `to avoid misunderstanding`, `we emphasize that`, or `a potential concern is`.

Default repair: state the technical fact or supported claim directly. Retain the objection only when it is an actual rival explanation or a necessary part of the argument.

#### Repeated non-claim disclaimers

The prose repeatedly explains what the paper does not claim, prove, cover, or imply.

Default repair: state the supported claim positively and express its scope once. Keep a negation when the distinction itself is substantive.

#### Caveat stacking

Several hedges, concessive clauses, and scope markers surround one claim and make the author sound unsure beyond the evidence.

Default repair: lead with the claim, keep the exact uncertainty the design requires, and retain at most one locally necessary boundary. Relocate broader limitations when appropriate.

#### Result excuses

The author calls a weak result `encouraging`, blames task difficulty without diagnostics, or explains a shortfall before reporting it.

Default repair: report the result first. Explain it only when the manuscript supplies evidence for the explanation. Never conceal the unfavorable result.

#### Omitted-experiment defense

The manuscript argues with an imagined reviewer about why a comparison or experiment was not performed.

Default repair: describe the evaluation protocol or state a material omission once as a limitation. Do not declare a missing test unnecessary without support.

#### Fairness self-defense

The text asserts that a comparison is `fair` instead of describing the controlled design.

Default repair: name the shared backbone, sample, budget, preprocessing, or evaluation rule directly.

#### Evidence-boundary over-signaling

The manuscript repeatedly says that evidence supports X but does not establish Y, even when Y is not the paper's claim.

Default repair: write the bounded positive claim, such as `In the evaluated setting, X`. Mention an untested generalization once only if it materially affects interpretation.

#### Legalistic or process-facing prose

The manuscript includes long lists of non-claims, editorial placeholders, evidence-audit commentary, or statements such as `the available passage does not provide...`.

Default repair: remove editorial process language from the manuscript. Put unresolved support in a separate author query.

#### Promotional compensation

Strong adjectives compensate for a weak or uncertain result: `compelling`, `encouraging`, `highly effective`, `robust`, or `comprehensive` without a measurement or defined property.

Default repair: report the measurement or named property. If it is unavailable, calibrate the existing proposition and query the missing anchor separately.

#### Redundant automatic summary

`Taken together`, `overall`, or `these results demonstrate` repeats the preceding result without adding a specific inference.

Default repair: delete it or state the one warranted synthesis.

#### Placement test

- Abstract and contribution statements should establish the contribution before qualifications.
- Results should report the estimate and uncertainty before explanation.
- Discussion should address supported alternatives and implications without sounding like a rebuttal.
- Limitations should contain material boundaries once, not repeat them throughout the paper.
- Conclusions should preserve a boundary only when omitting it would make the takeaway misleading.
- Rebuttals may address reviewer objections explicitly because that is their section function.

#### Integrity backstop

Anti-defensive editing fails if it deletes, obscures, or reframes away an unfavorable result, null result, contradiction, rival explanation, identification assumption, ethical limit, or limitation that changes interpretation. Remove apology and imagined-reviewer framing, not scientific information.

## False-positive controls

Preserve when functional and field-appropriate:

- evidence-calibrated hedging;
- passive voice in methods or when the actor is irrelevant;
- repeated technical terms needed for referential stability;
- conventional statistical, legal, clinical, or reporting language;
- explicit signposting in long or complex arguments;
- first-person singular or plural allowed by the discipline and venue;
- discipline-specific long sentences with clear logical hierarchy;
- reviewer-requested or venue-required wording;
- non-native language features that do not reduce clarity or precision;
- null results, limitations, and ambiguity that make the paper less rhetorically smooth but more accurate.

When uncertain, label the item `author check` rather than silently normalizing it.

## Claim-verb calibration

Choose verbs from the evidence, not from a fixed banned-word list.

| Evidence situation | Usually warranted | Usually needs stronger support |
|---|---|---|
| Direct descriptive result | `we find`, `we observe`, `the estimate is` | population-wide generalization |
| Model-dependent association | `is associated with`, `is consistent with` | `causes`, `leads to` |
| Credible causal design within scope | `increases/decreases` with design and scope stated | universal or mechanism claim |
| Mechanism not directly tested | `may reflect`, `is consistent with` | `shows the mechanism is` |
| Mixed or imprecise evidence | bounded statement with uncertainty | categorical conclusion |
| Proposal with supplied feasibility evidence | `we will test/develop/evaluate` | guaranteed outcome or impact |

`Demonstrate` can mean “show empirically” in some fields; inspect scope rather than banning the word. `Significant` must retain its statistical meaning when used that way.

## Voice profile evidence

For each inferred preference, record at least one location in the author samples. Prefer recurring features across samples. Separate:

- stable author tendency;
- genre or section convention;
- target-venue requirement;
- one-off feature not safe to generalize.

If evidence is thin, match only high-confidence features such as spelling, person, terminology, citation style, and degree of compression.

## Independent comparison checklist

Compare the original and revision directly:

- same claims and logical relations;
- same numbers, units, signs, ranges, equations, citations, and cross-references;
- same result direction, comparator, population, and timeframe;
- same epistemic status and causal scope unless a disclosed correction was made;
- no dropped limitation, qualifier, counterargument, or negative/null result;
- no new fact, explanation, mechanism, citation, or venue rule;
- no terminology drift or elegant variation that changes referents;
- no accidental duplication or paragraph loss;
- no new generic or mechanical phrasing;
- requested voice and venue features are actually evidenced.
- key numbers, units, sample definitions, result descriptions, and citation identities agree across every supplied artifact that was actually checked.
- no editorial query or evidence-audit commentary appears inside the revised manuscript.
- defensive wrappers are removed while necessary caveats, negative/null results, rival explanations, and interpretive boundaries remain intact.

Assign the final status:

- `PASS`: all checks pass and no author decision remains;
- `PASS WITH QUERIES`: stylistic revision is safe, but clearly marked evidence or author-choice queries remain;
- `FAIL`: the revision changes protected meaning/content or cannot be validated with available material.

## Audit table

Use only when an audit is requested or materially useful:

| Location | Function | Severity | Confidence | Evidence | Diagnosis | Minimal action |
|---|---|---:|---|---|---|---|

Keep evidence excerpts short. Report a paragraph-level judgment, then identify the highest-leverage local change.
