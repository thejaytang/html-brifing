---
name: research-results-tables
description: Create and audit publication-ready empirical research tables from analysis outputs. Use when producing or reviewing descriptive-statistics, correlation, balance, main-regression, robustness, heterogeneity, mechanism, and appendix tables for economics, management, or social-science manuscripts; when reconciling tables with code and estimates; or when formatting tables for Word, LaTeX, HTML, or journal submission.
license: MIT
---

# Research Results Tables

## Workflow

1. Inspect the analysis output and model definitions. Treat tables as reports of estimates, not as sources of truth.
2. Define the table purpose and comparison before selecting columns or specifications.
3. Construct the smallest table that answers the research question. Place model progression and sample changes where readers can see them.
4. Include required metadata in notes: outcome, estimator, fixed effects, controls, weights, standard-error or confidence-interval method, clustering, observations, units, and significance notation if used.
5. Reconcile every displayed estimate, sample count, and fit statistic with the source output. Render and inspect the final target format.

## Table Rules

- Keep the dependent variable, sample, and coefficient scale explicit.
- Do not use significance stars as the only uncertainty display when confidence intervals or standard errors are needed for interpretation.
- Separate main specifications, robustness checks, and exploratory analyses unless the distinction is immaterial.
- Mark omitted categories, reference groups, transformations, winsorization, and sample restrictions in notes.
- Do not hide a change in sample, outcome, or inference method between columns.

## Audit Output

Return a concise table manifest, a discrepancy list, and corrected footnotes. Mark unverified values rather than estimating them from screenshots or prose.
