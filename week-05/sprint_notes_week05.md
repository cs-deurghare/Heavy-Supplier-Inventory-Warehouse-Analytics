# Sprint notes: Week 5

## Scope
Q3, Q5, Q6, Q7, Q11 (gate and labelled scenario) and Q12 (pulled forward from Week 6), as set in the Week 5 sprint plan. Q4 follow-up and Q13 stay in Week 6.

## Work done
| Q | Owner | Package | Checks |
|---|---|---|---|
| Q3 Cancellation concentration | Salim Bello Muhammad | `q3_cancellation_concentration/` | 27 |
| Q5 Customer lifetime value | Salim Bello Muhammad | `q5_customer_lifetime_value/` | 34 |
| Q6 Margin concentration | Chandrashekhar Deurghare | `q6_margin_concentration/` (rebuilt) | 38 |
| Q7 Lead-time seasonality | Abdibasid Mohamed Ali | `q7_lead_time_seasonality/` | 34 |
| Q11 Gate and scenario | Ibrahim Khalil Umar, with Abdibasid | `q11_stock_scale_gate/` | 16 |
| Q12 Ledger mismatches | Ibrahim Khalil Umar | `q12_ledger_mismatches/` | 18 |

Combined: 167 of 167 checks pass (`validation_report_week05.csv`), rebuilt by the master notebook `05_deep_dive_analysis.ipynb` (25 further checks). Review of all packages and the corrections log: `Corrections_Log_week05.md`. Findings: `week5_findings_summary.md`.

## Issues and treatment
- **Q6 first version not reproducible and what-if ten times too small.** Rebuilt with computed tables, real outputs and checks that can fail; mix-shift analysis added.
- **Q12 sign evidence:** the 180-of-180 replay is true by construction; the report now names the independent evidence.
- **Q11 wording:** 349× versus 347×, and the 84.3 versus 95 units bridge, fixed with a checked bridge table.
- **Q5 industry segment** reworded from "probable small effect" to "exploratory lead".
- **Q7 month labels** were one position off in a draft; corrected.
- **Week 4 main notebook** had two markdown cells saved as code cells and failed on "Run all"; fixed and re-verified (37 of 37 checks).
- **Failed checks not loosened:** Q3 detectable-gap threshold split into typical and smallest segment; Q5 widest-gap interval replaced by a permutation test; Q5 "all customers active every year" restated as at least 99%; Q6 master-margin check restated as 29 of 30.

## Open items
1. **Agreed by the team:** apply the Week 4 adjustment-sign corrections in one commit: the corrected `week-04` files (Q10 notebook and report, `week4_findings_summary.md`, `sprint_notes_week04.md`, `Corrections_Log.md`) and `week-03/analysis_questions_locked.md` are supplied with this submission. Q10 re-run: (24 checks; 10 of 180 pairs within bounds by end balance; average balance 142).
2. Q11 scenario was independently re-implemented and matches exactly; no action needed beyond the clarified wording of Policy B.
3. Send the data-owner pack and wait for the replies on the purchase-order scale (blocks Q10 and Q11).
4. Q6: the rebuilt package was reviewed and adopted by its owner (Chandrashekhar); the earlier Q6 files are replaced.
5. The shared notebook `05_deep_dive_analysis.ipynb` is a master notebook: each owner's question notebook stays self-contained in `standalone_question_reports/`, and the master re-runs all six, checks them, rebuilds the combined validation and shows every answer in one place.

## Working rules kept
Order, purchase order or customer as the unit (never the line by default); each claim worded to its test with effect sizes and intervals; seed 42 and 5,000 resamples; notebooks find the merged data themselves and assert that every check passes; folders lowercase.
