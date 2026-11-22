# Week 8: Phase 3, supplier reliability, supplier risk, stockout prediction and customer segments

**Status:** all four Week 8 work items are complete. Combined validation: **120 of 120** notebook checks pass (`validation_report_week08.csv`), re-run end to end on the merged datasets.

## What is here

| Item | Question | Owner | Folder | Checks |
|---|---|---|---|---|
| W8-1 | Which suppliers deliver late or vary most, and how concentrated is purchasing? | Chandrashekhar Deurghare | `standalone_question_reports/w81_supplier_reliability/` | 29 |
| W8-2 | How exposed are we to each supplier, and how firm is the ranking? | Abdibasid Mohamed Ali | `standalone_question_reports/w82_supplier_risk/` | 38 |
| W8-3 | Which stock pairs are likely to run out, and when should they reorder? | Ibrahim Khalil Umar | `standalone_question_reports/w83_stockout_reorder/` | 31 |
| W8-4 | Do customers fall into stable, meaningful segments? | Salim Bello Muhammad | `standalone_question_reports/w84_customer_segments/` | 22 |
| Combined | Re-runs every Week 8 notebook | Everyone | `08_deep_dive_analysis.ipynb` | 120 |

Also in this folder: `week8_findings_summary.md`, `sprint_notes_week08.md`, `corrections_log_week08.md` with `corrections/` (two corrected week-03 files), `analysis_questions_week08.md` (to merge into the locked questions), `data_dictionary_week08.csv` / `.md` (supplier fields), `combine_validation_week08.py`, `README_w8_3_ibrahim.md`, `section_notebook/` (W8-3 section for pasting into the shared notebook) and `validation_report_week08.csv`.

## Headlines

- **W8-1:** the 8 suppliers cannot be told apart (on time 84.2% to 85.3%, cancelled 9.4% to 10.3%, spend share 12.1% to 12.9%; all Holm-adjusted p = 1.0). Lead time differs by contract (10 to 28 days) but varies about 1.7 days within a supplier.
- **W8-2:** a transparent risk score puts SUP0003 first, but the ranking is not firm (0 of 28 pairs keep their order in 95% of resamples; split-half agreement no better than shuffled labels). All suppliers are in China.
- **W8-3:** existing reorder levels leave 78 of 180 pairs below 95% fill (93.8%); a lead-time-aware reorder point at 95% service meets 99.3% for 25.6% more stock value. Sales scale assumed (Q10 unresolved).
- **W8-4:** five RFM segments exist as labels but are not stable (adjusted Rand index 0.005), do not predict later revenue and do not differ by region, type or industry after adjustment. Snapshot list only; no churn or tenure claim.

## How to run

Keep the `merged/` data folder next to `week-08/` (or anywhere inside the repository checkout, for example `week-02/reports/week_02/merged`), open any notebook and run all cells. Each notebook finds the merged files by searching its own folder and every parent folder; otherwise set `CADETX_MERGED` to that folder. No clean folder is needed: W8-4 takes customer region, type and industry from the merged sales file. `08_deep_dive_analysis.ipynb` runs the four notebooks in turn and writes `validation_report_week08.csv`; the full run takes about five minutes. `combine_validation_week08.py` rebuilds the combined validation from the four per-question files. Each notebook writes its outputs, charts and validation report next to itself and asserts that every check passes. Seed 42, 5,000 resamples.

## Labels

Procurement money figures carry: *Procurement scale: purchase spend is about 14x sales revenue (Q10 unresolved); money figures are descriptive.* Stock results carry: *Sales scale assumed (Q10 unresolved); results rest on this assumption.* Rates, shares and lead times do not depend on either.

## Open items

See `sprint_notes_week08.md`: Week 7 benchmark figures to compare with the W8-2 recheck, Week 7 repository gaps, Q7, locked-question merge, owner sign-off.
