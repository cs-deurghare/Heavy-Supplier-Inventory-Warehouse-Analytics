# How to run the Week 6 notebooks

Open any notebook anywhere inside the repository checkout and run all cells. Each notebook finds the corrected merged files (`week-02/reports/week_02/merged`) by searching its own folder and every parent folder. Otherwise set `CADETX_MERGED` to that folder. The Q13 notebook also reads `week-02/reports/week_02/clean/customers_clean.csv` (found the same way, or set `CADETX_CLEAN` to the `clean` folder). If the data cannot be found, the notebook stops with a message saying so.

| Notebook | Folder (inside `standalone_question_reports/`) | Checks | Run time |
|---|---|---|---|
| `q4_payment_followup.ipynb` | `q4_payment_followup/` | 43 | under 30 seconds |
| `phase2_coverage.ipynb` | `phase2_coverage/` | 43 | under 30 seconds |
| `q13_customer_master_dates.ipynb` | `q13_customer_master_dates/` | 25 | under 30 seconds |
| `stock_kpis_and_q11_rerun.ipynb` | `stock_kpis_and_q11_rerun/` | 23 | under 30 seconds |

Each notebook writes its outputs, charts and validation report next to itself and asserts that every check passes. Random seed 42, 5,000 resamples. `validation_report_week06.csv` combines the four validation reports (134 checks). `stock_scale_note.md` states the working assumption behind every stock result.
