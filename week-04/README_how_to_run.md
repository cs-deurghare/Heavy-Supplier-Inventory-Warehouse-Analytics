# How to run (Week 4)
Open any notebook anywhere inside the repository checkout and run all cells. It searches its own folder and every parent folder for the corrected merged files (`week-02/reports/week_02/merged`) and, for the standalone Q1, the Week 3 KPI baseline (`week-03/kpi_outputs`). Otherwise set `CADETX_MERGED` and `CADETX_KPI` to those folders. A notebook stops with a message if it cannot find the data, and stops if any validation check fails.

| Notebook | Writes | Checks |
|---|---|---|
| `04_deep_dive_analysis.ipynb` (all four questions) | `analysis_outputs/`, `analysis_charts/`, `validation_report_week04.csv` | 37 |
| `standalone_question_reports/q1_revenue_drift/04_q1_revenue_drift.ipynb` | its own `q1_outputs/`, `q1_charts/` | 26 |
| `standalone_question_reports/q2_regional_concentration/q2_regional_concentration.ipynb` | its own `q2_outputs/`, `q2_charts/` | 16 |
| `standalone_question_reports/q10_stock_scale/q10_stock_scale.ipynb` | its own `q10_outputs/`, `q10_charts/` | 19 |

Summary: `week4_findings_summary.md`. Notes: `sprint_notes_week04.md`. Corrections: `Corrections_Log.md`.
