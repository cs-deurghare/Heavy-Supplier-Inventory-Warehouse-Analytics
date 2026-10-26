# Sprint Notes: Week 04
## Overview
Week 4 deep dive on Q1, Q2, Q8 and Q10, built on the corrected Week 2 merged datasets (`week-02/reports/week_02/merged`) and checked against the Week 3 KPI baseline.

## Work completed
| Question | Owner | Where | Checks |
|---|---|---|---|
| Q1 Revenue drift | Salim Bello Muhammad | `04_deep_dive_analysis.ipynb` and `standalone_question_reports/q1_revenue_drift/` | 37 (notebook), 26 (standalone) |
| Q2 Regional concentration | Chandrashekhar Deurghare | notebook and `standalone_question_reports/q2_regional_concentration/` | 37 (notebook), 16 (standalone) |
| Q8 Supplier differentiation | Abdibasid Mohamed Ali | `04_deep_dive_analysis.ipynb` | 37 (notebook) |
| Q10 Stock scale | Ibrahim Khalil Umar | notebook and `standalone_question_reports/q10_stock_scale/` | 37 (notebook), 19 (standalone) |

The full notebook covers all four questions (37 of 37 checks). The standalone folders hold one question each, with their own notebook, outputs, charts and validation report. Figures agree; see the method note in `week4_findings_summary.md`.

## Issues found and how they were treated
| Issue | Treatment |
|---|---|
| Cancelled orders counted as revenue in one version (South + West 61.18%) | Delivered orders only (60.95%), matching Week 3 |
| Order lines treated as independent in supplier tests | Tested per purchase order (Q8) |
| Claims stronger than the tests supported (price, demand, cancellation, under-coverage) | Reworded to the evidence; stated as limits |
| Hard-coded computer path (`/Users/...`) in the full notebook | Notebooks search the repository for the data; tested from a clean repository layout |
| Single price list; no cancellation reason; cancelled orders carry a delivery date; PO quantities on a larger scale than sales; every ledger adjustment positive | Recorded as caveats; questions for the data owner |

## Open items
- Data owner: price history, meaning of the Cancelled status, how PO quantities were set, why ledger adjustments are all positive.
- Week 5: cancellation analysis (Q3) builds on the Q1 cancellation finding.
