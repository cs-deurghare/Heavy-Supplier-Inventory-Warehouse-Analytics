# Week 7: Phase 3, forecasting and customer behaviour

**Status:** Phase 3 has opened. All four Week 7 items are in this package: **W7-1** forecast baseline, **W7-2** customer behaviour, **W7-3** priority pack, **W7-4** robustness of the reorder result to lead-time variation, plus the Week 7 data dictionary. Combined validation: **105 of 105** notebook checks and **8 of 8** cross-checks pass (`validation_report_week07.csv`).

## What is here

| Item | Question | Owner | Folder | Checks |
|---|---|---|---|---|
| W7-1 | How well does a plain level forecast do, and can anything beat it? | Abdibasid Mohamed Ali | `standalone_question_reports/w71_forecast_baseline/` | 27 |
| W7-2 | How do customers differ in recency, frequency and value? | Salim Bello Muhammad | `standalone_question_reports/w72_customer_behaviour/` | 22 |
| W7-3 | Which products, branches and stock pairs need attention first? | Chandrashekhar Deurghare | `standalone_question_reports/w73_priority_pack/` | 26 |
| W7-4 | Does the demand-based reorder trigger still beat the existing levels when lead times vary? | Ibrahim Khalil Umar | `standalone_question_reports/w74_lead_time_variation/` | 30 |
| Combined | Re-runs all four and cross-checks them | Everyone | `07_deep_dive_analysis.ipynb` | 8 |

Also in this folder: `week7_findings_summary.md` (findings), `sprint_notes_week07.md`, `corrections_log_week07.md` (review and what was changed), `data_dictionary_week07.md` and `.csv` (what each field is and whether it can be used), `validation_report_week07.csv` (113 rows: 105 from the notebooks and 8 cross-checks).

## How to run

Open any notebook anywhere inside the repository checkout and run all cells. Each notebook finds the corrected merged files (`week-02/reports/week_02/merged`) by searching its own folder and every parent folder; otherwise set `CADETX_MERGED` to that folder.

- **W7-3** also reads the Week 6 stock outputs (`week-06/standalone_question_reports/stock_kpis_and_q11_rerun/stock_outputs`); otherwise set `CADETX_WEEK6_STOCK` to that folder.
- **W7-2** also reads `week-02/reports/week_02/clean/customers_clean.csv` (or `CADETX_CLEAN`).
- `07_deep_dive_analysis.ipynb` runs the four standalone notebooks in turn and writes `validation_report_week07.csv`. W7-4 simulates 1,000 lead-time paths, so the full run takes about two minutes.

Each notebook writes its outputs, charts and validation report next to itself and asserts that every check passes. Seed 42, 5,000 resamples. Run time under a minute each.

## Stock label

Every stock result carries: *Sales scale assumed (Q10 unresolved); results rest on this assumption.* The sales and customer results do not depend on it.

## Status of the project

| Item | State |
|---|---|
| Phase 2 (Weeks 2 to 6) | Closed with the Week 6 package (134 of 134 checks) |
| Week 7 W7-1 to W7-4 | In this package, reviewed and corrected (see the corrections log) |
| Open from earlier weeks | Q6 margin concentration redo (Week 5), Q7 lead-time seasonality, "about 6% (10 of 180)" in the Week 4 notebook section 4.4 |
