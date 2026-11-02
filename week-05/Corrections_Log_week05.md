# Week 5 review and corrections log

**Prepared for:** Abdibasid Mohamed Ali (review of all Week 5 findings, sprint plan slides 8 and 12) · **Date:** 1 November 2026
**Method:** every package was unpacked, re-run in a clean folder layout (merged data only, environment variables unset), and its outputs compared byte for byte with the shipped files. Key numbers were recomputed independently from the corrected Week 2 merged datasets. The Q11 policy simulation was re-implemented independently from the report's stated assumptions and matches exactly (item 17).

## 1. Summary

| Q | Owner | Reproducible | Checks | Verdict |
|---|---|---|---|---|
| Q3 Cancellation concentration | Salim | Yes, identical outputs | 27 of 27 | Ready |
| Q5 Customer lifetime value | Salim | Yes, identical outputs | 34 of 34 | Ready (industry wording changed to "exploratory lead") |
| Q6 Margin on top products | Chandrashekhar | **First version: no** (hard-coded `D:\` path, typed-in data, what-if 10× too small). **Rebuilt version: yes**, identical outputs | rebuilt: 38 of 38 | First version not ready; **rebuilt version ready** (see 3) |
| Q7 Lead-time seasonality | Abdibasid | Yes, identical outputs | 34 of 34 | Ready |
| Q11 Gate and scenario | Ibrahim, with Abdibasid | Yes, identical outputs | 16 of 16 | Ready (revised) |
| Q12 Ledger mismatches | Ibrahim | Yes, identical outputs | 18 of 18 | Ready (revised) |

Combined: **167 of 167 checks pass** across Q3 (27), Q5 (34), Q6 rebuilt (38), Q7 (34), Q11 (16) and Q12 (18) (`validation_report_week05.csv`). The first Q6 version had no runnable checks and is not included.

## 2. Corrections log

| # | Package | Issue found | Fix | Status |
|---|---|---|---|---|
| 1 | Q12 | "Replay reproduces 180 of 180 pairs" is true by construction (sign read from `running_balance`) | Report now states this and names the real evidence (every adjustment step is exactly ±qty, every IN/OUT step matches, every opening reconciles) | Fixed |
| 2 | Q11 | "349× max_stock" mixed a median of ratios with a ratio of medians (347×) | Now "about 350×", both figures stated | Fixed |
| 3 | Q11 | 84.3 vs 95 units a month explained only as "about 91% coverage" | Bridge added: ledger holds 91.1% of delivered units and lines; 84.3 ÷ 0.911 = 92.6 = delivered-lines median 92.7; mean 94.8 | Fixed |
| 4 | Q11 | Scenario figures (for example 5.7% of demand lost) could be quoted as findings | "Do not quote outside this labelled scenario" box; assumptions listed | Fixed |
| 5 | Q12 / Week 4 | "Every adjustment is positive" is true of the quantity column only; the ledger applies 1,227 up and 1,227 down | Week 4 corrections written up (agreed by the team) (exact lines listed); no Week 1 to 4 file changed yet | Fixed (agreed by the team; applied in the Week 4 files) |
| 6 | Q3 | 2024 uptick could be read as established | Framed as singled out after looking; supports a weak trend only | Fixed |
| 7 | Q5 | Industry segment (adjusted p = 0.059) called "probable small effect" | Now "exploratory lead to re-test"; permutation p = 0.014 and split-half stability reported with the caveat that both halves use the same customers | Fixed |
| 8 | Q7 | Month labels for the minimum and maximum were one position off in a draft | Corrected; Mar (7.92) and Feb (8.20) | Fixed |
| 9 | Q7 | Customer region raw p = 0.008 | Reported as a weak lead: Holm 0.08, whole-scan permutation 0.07, ε² = 0.0006 | Fixed |
| 10 | Q10 (Week 4) | Signing adjustments from `running_balance` changes the corrected-scale replay: at k = 18.13 the average balance is 141, not 329, with 36.9% of days below zero (28.5% before). Week 4's "average balance lands near maximum stock" no longer holds | Proposed in Ibrahim's corrections note; headline 18.1× result unaffected | Fixed (agreed by the team; applied in the Week 4 files) |
| 11 | Q10 (Week 4) | "Only 8% of pairs between 0 and max_stock" does not match the end-balance count (12 of 180 = 6.7% under the Week 4 method, 10 under signed) | Agree one definition (end balance or average) and re-run before quoting | Fixed: 10 of 180 pairs (end balance, signed adjustments) |
| 12 | Q6 | Not reproducible (see 3) | Rebuilt: computed tables, real CSVs, 38 checks that can fail, mix-shift analysis added | Fixed (rebuilt version) |
| 13 | Q6 | **What-if figures were 10× too small**: +1% price on EB-600 was reported as ₹4.86M and base gross profit as ₹95.9M; correct values are ₹48.57M and ₹959.2M | Recomputed in the rebuilt version (see its price scenario with break-even volume loss) | Fixed (rebuilt version) |
| 14 | Q6 | Recommendation of "low-risk 1% to 2% price adjustments" was unsupported (no price history, no elasticity) | Replaced with the break-even volume loss and a "no pricing recommendation" statement | Fixed (rebuilt version) |
| 15 | Q6 / data | Product master `margin_percentage` is a markup on cost for 29 of 30 products, and Engine Oil Filter OF-90 is inconsistent (master 37.3%, markup 60.0%, margin 37.5%) | Reported in the rebuilt Q6; data-owner question added | New finding |
| 16 | Q6 | The 2024 EB-600 fall (₹71.3M) is the largest of 30 product changes but within chance (scan permutation p = 0.25) | Worded as not established | New finding |
| 17 | Q11 | Scenario simulation not independently confirmed | Independently re-implemented (daily review, demand then review, order-up-to level S = trigger + (max_stock − reorder_level), lead time = rounded pair mean, lost sales, opening-stock start): all four policies match exactly on fill rate (94.26%, 98.91%, 99.39%, 99.81%), average on-hand, orders placed (4,457, 4,804, 4,839, 4,872), stock value and pairs below 95% (72, 0, 0, 0). An alternative reading of Policy B (order up to `max_stock`) gives different figures (fill 98.6%, 99.1%, 99.7%; 6,311 to 10,741 orders), so the scenario is sensitive to that convention. Report wording clarified | Fixed |
| 18 | Q10 (Week 4) | Corrected-scale replay added every adjustment; "8% of pairs" not reproducible | Q10 Part D re-run with signed adjustments; one definition stated (end-of-period balance): 10 of 180 pairs (5.6%); average balance 142 vs 330; 24 checks (was 19); Week 4 report, findings summary, sprint notes and Corrections_Log updated | Fixed |
| 19 | Repository | `analysis_questions_locked.md` not updated; the repository README ended mid-sentence ("build directly on this# Heavy Supplier...") with a duplicated title | Locked-questions status updated; README restored | Fixed |
| 20 | Week 4 notebook | `week-04/04_deep_dive_analysis.ipynb` as it stands in the repository has its title and revision-note cells (cells 0 and 1) saved as code cells, so "Run all" stops at the first cell with a SyntaxError | Both cells converted to markdown; notebook re-run from a clean layout: 0 errors, 37 of 37 checks pass, all `analysis_outputs` tables identical to the repository's | Fixed (corrected notebook supplied) |

## 3. Q6 (Chandrashekhar): first version not ready (about 45/100); rebuilt version ready

**First version.** The figures for the two products' revenue, gross profit and margin were correct (EB-600 ₹4,856,985,000 and ₹959,152,500; TA-800 ₹3,387,929,000 and ₹608,610,000; the other 28 products 22.99% against 21.56%; category shares). The package failed the working rules:
1. It read from a hard-coded `D:\` path and a superseded dataset name, so it failed anywhere else.
2. Tables were typed into the notebook as dictionaries, not computed from the data.
3. The CSV output files were empty and the validation was static, so it could not fail.
4. **The price what-if was ten times too small**: +1% on EB-600 was reported as ₹4.86M when 1% of ₹4.857B is ₹48.57M, and base gross profit was shown as ₹95.9M instead of ₹959.2M.
5. The mix-shift analysis the sprint plan asks for was missing, and the 1% to 2% price recommendation was unsupported.

**Rebuilt version** (`Q6_Margin_Concentration/`): computed from the merged data with a portable data finder, 38 checks that can fail, 9 real output tables, 3 charts, identical outputs on a clean re-run. It adds the contribution-to-margin-gap view, the mix-versus-rate test (margin stable, p = 0.84), a scan test of the 2024 EB-600 fall (within chance, p = 0.25), the corrected labelled price scenario with break-even volume loss, and the master `margin_percentage` data issue. Chandrashekhar should read it, rerun it and take ownership before it goes into `week-05/`.

## 4. Decisions needed from the team
1. **Agreed by the team:** the Week 4 adjustment-sign corrections (items 5, 10, 11, 18). The corrected Week 4 files (Q10 notebook, report, findings summary, sprint notes, Corrections_Log) and the updated `analysis_questions_locked.md` are supplied in this submission, and go in one commit with the Week 5 merge. The Q10 re-run (24 checks, 10 of 180 pairs by end balance).
3. **Agreed:** Chandrashekhar reviewed and adopted the rebuilt Q6; it is the version in `week-05/`, and the old Q6 files are not merged.
4. Confirm who owns `validation_report_week05.csv`: the sprint plan lists Ibrahim (slide 11) and Abdibasid (slide 4). The combined file is provided here.

## 5. Not reviewed
`05_deep_dive_analysis.ipynb` (the shared notebook), `week5_findings_summary.md`, `sprint_notes_week05.md` and the README Week 5 section do not exist yet; they should be reviewed when Chandrashekhar compiles them.
