# Week 8, W8-3 (Ibrahim): stockout and reorder package

| Item | File |
|---|---|
| Stockout risk, reorder points and back-test | `standalone_question_reports/w83_stockout_reorder/` (notebook, report, outputs, charts, validation) |
| Section for the shared notebook | `section_notebook/08_deep_dive_section_w8_3_ibrahim.ipynb` (paste its cells into `08_deep_dive_analysis.ipynb`; names prefixed `w83_`) |
| Data dictionary for supplier fields | `data_dictionary_week08.md` and `data_dictionary_week08.csv` |
| Combined validation | `validation_report_week08.csv`, built by `combine_validation_week08.py` from every `validation_report_week08*.csv` in `standalone_question_reports/` |

Open the notebook anywhere inside the repository checkout and run all cells (under a minute); it finds `week-02/reports/week_02/merged` itself (or set `CADETX_MERGED`) and asserts every check passes. Seed 42, 5,000 resamples, 500 lead-time paths. After the other work items add their validation files, rerun `combine_validation_week08.py`.
