# Before and after examples

These examples demonstrate the editing decisions, not a promise that every passage should be made shorter or more assertive. Each revision is constrained by the evidence shown in the example.

## 1. Abstract: calibrate without writing the audit into the manuscript

### Before

> In recent years, algorithmic decision-making has attracted increasing attention and has become a crucial component of the rapidly evolving digital landscape. Our comprehensive analysis clearly demonstrates that the proposed intervention is highly effective and has broad implications for organizations.

### After

> This study examines an intervention for organizational algorithmic decision-making. Our analysis suggests that the intervention is effective and may have implications for organizational practice.

### Why

- The first sentence names the research setting instead of praising its importance.
- The second sentence preserves the original result direction while calibrating certainty and breadth.
- No audit commentary or evidence-gap language is inserted into the manuscript.

**Author query, separate from the manuscript:** Add the primary outcome, evaluation context, and effect estimate if available. Without these details, the effectiveness and organizational-implication claims remain underspecified.

Validation: `PASS WITH QUERIES`, because the author must supply the relevant results before a stronger abstract claim is warranted.

## 2. Defensive result framing: report the result before the boundary

### Before

> Although the gain is only 0.8 percentage points, the result remains encouraging given the challenging distribution-shift setting, and we emphasize that we do not claim universal robustness.

### After

> Accuracy increases by 0.8 percentage points under the evaluated distribution shift.

### Why

- Removes apology-like framing, promotional compensation, and an uninvited universal claim.
- Keeps the observed magnitude and evaluation condition.
- Does not rename the local result as general robustness.

If the untested generalization materially affects interpretation, state it once in the Limitations section rather than attaching it to every result.

Validation: `PASS` when the original result source confirms the magnitude and setting.

## 3. Results: preserve every quantitative invariant

### Before

> The treatment group achieved a substantially better conversion rate than the control group. Conversion increased from 12.4% to 15.1% (difference = 2.7 percentage points, 95% CI [0.8, 4.6], p = .006), clearly proving that the intervention works across customer segments.

### After

> Conversion was 15.1% in the treatment group and 12.4% in the control group, a difference of 2.7 percentage points (95% CI [0.8, 4.6], p = .006). This estimate supports an effect in the analyzed sample; the passage does not provide subgroup results that would establish consistency across customer segments.

### Preserved ledger

- Treatment: `15.1%`
- Control: `12.4%`
- Difference: `2.7 percentage points`
- Confidence interval: `95% CI [0.8, 4.6]`
- Significance statement: `p = .006`

The revision removes `proving` and the unsupported subgroup generalization without weakening the observed result.

Validation: `PASS WITH QUERIES`, because the cross-segment claim requires subgroup evidence.

## 4. Literature review: replace citation dumping with relationships

### Before

> Prior research has extensively examined trust in automated systems [3, 5, 8, 11]. Moreover, several studies have investigated explanations [12, 14, 17]. However, the literature remains complex and multifaceted.

### After, with no source details supplied

> Prior research examines trust in automated systems [3, 5, 8, 11] and the role of explanations [12, 14, 17]. The available passage does not specify how these studies relate or which unresolved question motivates the present study.

### Why

The revision improves cohesion without pretending to know what the cited studies found. A source-backed pass could replace the second sentence with an actual synthesis after the references are inspected.

Validation: `PASS WITH QUERIES`.

## 5. Methods: keep functional passive voice

### Before

> Samples were normalized to total protein before fluorescence was measured at 485/520 nm.

### After

> Samples were normalized to total protein before fluorescence was measured at 485/520 nm.

### Why

No edit is warranted. The passive construction keeps attention on the procedure, and the measurement details are precise. A humanizer that changes every passive sentence would damage this passage.

Validation: `PASS`.

## 6. Structural compression: remove low-value repetition, not boundaries

### Before

> The study has three limitations. First, the sample was drawn from one national market. This single-market sample limits geographical generalization. Second, outcomes were observed for four weeks, which means that longer-term persistence remains unknown. Finally, the observational measure of engagement may not capture all dimensions of product use. These limitations are important and should be considered when interpreting the findings.

### After

> The study draws on one national market, observes outcomes for four weeks, and measures engagement observationally. The findings therefore do not establish geographical generalizability, longer-term persistence, or all dimensions of product use.

### Why

The revision merges repeated framing while preserving all three limitations and their interpretive consequences.

Validation: `PASS`.
