# Sprint notes: Week 7

## Scope
Phase 3 opening: forecast baseline (W7-1), customer behaviour (W7-2) and priority pack (W7-3), as set in the Week 7 sprint plan. Includes **W7-4** (robustness, Ibrahim) and the Week 7 data dictionary.

## Work done
| Item | Owner | Package | Checks |
|---|---|---|---|
| W7-1 Forecast baseline | Abdibasid Mohamed Ali | `w71_forecast_baseline/` | 27 |
| W7-2 Customer behaviour | Salim Bello Muhammad | `w72_customer_behaviour/` | 22 |
| W7-3 Priority pack | Chandrashekhar Deurghare | `w73_priority_pack/` (rebuilt) | 26 |
| W7-4 Lead-time robustness | Ibrahim Khalil Umar | `w74_lead_time_variation/` (folder and files renamed to match the others) | 30 |
| Combined notebook | Everyone | `07_deep_dive_analysis.ipynb` | 8 cross-checks |

Combined: 105 of 105 notebook checks and 8 of 8 cross-checks pass (`validation_report_week07.csv`, 113 rows). Findings: `week7_findings_summary.md`. Review log: `corrections_log_week07.md`.

## Issues and treatment
- **W7-3 rebuilt.** The first version used random numbers for margins, listed 72 arbitrary rows as the "at-risk pairs", had checks that could not fail and a notebook that chose its input file by file-system order. See the corrections log.
- **W7-2 accepted.** Reproduces exactly and every headline number was recomputed independently. Files renamed so the shipped names match what the notebook writes.
- **W7-4 accepted.** Reproduces exactly (7 of 7 tables identical, 30 of 30 checks) and my own simulation (own random draws) agrees: A 93.6%, B 95% 98.8%, B-LT 95% 99.2%. Four small fixes made, none changing a number.
- **W7-1 built** to the plan: 40 series, per-day plain average, rolling back-test as the benchmark, one challenger, a bar fixed in advance.

## Open items
1. **Q6 margin-concentration redo** (Week 5): W7-3 now carries the correct class A and 30-product margin table, which Q6 can reuse.
2. **Q7** lead-time seasonality is still not written.
3. **Week 4 notebook** section 4.4: "8%" to read "about 6% (10 of 180)".
4. **Week 6 coverage package:** rename "Q6 margin %" to "master margin %"; add "in-sample" next to the Policy B fill rates in the stock report.
5. **Locked questions** (`analysis_questions_locked.md`) not updated for Week 7.
6. **Owner sign-off:** each owner confirms their package before it is submitted under their name.

## Working rules kept
Order, invoice or customer as the unit (never the line by default); each claim worded to its test with effect sizes and intervals; seed 42 and 5,000 resamples; notebooks find the merged data themselves and assert that every check passes; failed checks not loosened; stock results always carry the sales-scale label.
