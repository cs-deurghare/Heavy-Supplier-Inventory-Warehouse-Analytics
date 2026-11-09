# Sprint notes: Week 6

## Scope
Q4 follow-up (payments and ageing), the Phase 2 coverage items (ABC, movers, branch throughput, forecast readiness) and Q13 (customer master dates), and the stock KPIs with the Q11 rerun on the agreed sales scale, as set in the Week 6 sprint plan.

## Work done
| Q | Owner | Package | Checks |
|---|---|---|---|
| Q4 follow-up Payments and ageing | Salim Bello Muhammad | `q4_payment_followup/` | 43 |
| Phase 2 coverage (ABC, movers, branches, forecast readiness) | Abdibasid Mohamed Ali | `phase2_coverage/` | 43 |
| Q13 Customer master dates | Chandrashekhar Deurghare | `q13_customer_master_dates/` | 25 |
| Stock KPIs and Q11 rerun on the working scale | Ibrahim Khalil Umar, with Abdibasid Mohamed Ali | `stock_kpis_and_q11_rerun/` | 23 |

Stock-scale note: `stock_scale_note.md`. Combined: 134 of 134 checks pass (`validation_report_week06.csv`). Findings: `week6_findings_summary.md`. Review log: `corrections_log_week06.md`.

## Issues and treatment
- **Q4 promised more than the data can answer:** title and question reworded; collectability is not tested and the exposure range is a labelled scenario.
- **Q4 check 8 counts** corrected to 75 overpaid and 92 short by exactly 0.01.
- **Coverage integrity check** assumed the Week 3 total for all delivered orders; it now reconciles to the invoice file (₹29.25B) and to the reliable base (₹28.60B).
- **Movers label** produced by chance suppressed when the overall tests are not significant.
- **Q13 first version** replaced by a rebuilt package with fixed verdict bar and a clean-layout rerun.
- **Chart label overlaps** fixed in the coverage and Q13 charts.
- **Stock KPIs:** the Week 5 labelled scenario was promoted to the agreed working result with turnover, cover and health added; it reproduces the Week 5 figures exactly and shows the unscaled case as a sensitivity only.

## Open items
1. **Review and sign-off:** Abdibasid to review the Week 6 notebooks; each owner to confirm their package (Chandrashekhar Q13, Abdibasid coverage, Ibrahim stock) before it is submitted under their name.
2. **Stock results stay labelled** as resting on the sales-scale assumption (`stock_scale_note.md`) until a corrected purchase scale exists, if ever; then they are rebuilt first.
3. **Ask the business** whether reorder levels are meant to follow demand and lead time (stock report, recommendation 3).
4. Re-test the Q5 industry-segment lead and the Q3 2024 cancellation uptick when more data is available.
5. Keep `validation_report_week05_ibrahim.csv` out of the Week 6 commit.

## Working rules kept
Order, invoice or customer as the unit (never the line by default); each claim worded to its test with effect sizes and intervals; seed 42 and 5,000 resamples; notebooks find the merged data themselves and assert that every check passes; failed checks not loosened.
