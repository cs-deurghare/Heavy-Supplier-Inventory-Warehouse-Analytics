# How to run the Week 5 notebooks

**Master notebook.** `05_deep_dive_analysis.ipynb` (in `week-05/`) re-runs all six question notebooks below, confirms there are no errors and that all 167 question checks pass, rebuilds `validation_report_week05.csv`, and shows each answer with its key tables and charts (25 checks of its own, in `validation_report_week05_master.csv`). It takes about 1 to 2 minutes. Set `RUN_QUESTION_NOTEBOOKS = False` in its first code cell to collect saved results without re-running.

Open any notebook anywhere inside the repository checkout and run all cells. Each notebook finds the corrected merged files (`week-02/reports/week_02/merged`) by searching its own folder and every parent folder. Otherwise set `CADETX_MERGED` to that folder. Q5 also reads `raw_data/customers.csv` (found the same way, or set `CADETX_RAW` to the `raw_data` folder). If the data cannot be found, the notebook stops with a message saying so.

| Notebook | Folder (inside `standalone_question_reports/`) | Checks | Run time |
|---|---|---|---|
| `q3_cancellation_concentration.ipynb` | `q3_cancellation_concentration/` | 27 | under 30 seconds |
| `q5_customer_lifetime_value.ipynb` | `q5_customer_lifetime_value/` | 34 | under 30 seconds |
| `q6_margin_concentration.ipynb` | `q6_margin_concentration/` | 38 | under 30 seconds |
| `q7_lead_time_seasonality.ipynb` | `q7_lead_time_seasonality/` | 34 | under 30 seconds |
| `05_q11_stock_scale_gate_and_scenario.ipynb` | `q11_stock_scale_gate/` | 16 | under 30 seconds |
| `05_q12_ledger_mismatches.ipynb` | `q12_ledger_mismatches/` | 18 | under 30 seconds |

Each notebook writes its outputs, charts and validation report next to itself and asserts that every check passes. Random seed 42, 5,000 resamples. Please keep all weekly folders lowercase (`week-01` to `week-05`).
