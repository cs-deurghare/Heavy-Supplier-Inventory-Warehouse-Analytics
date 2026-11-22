# Sprint notes: Week 8

## Scope
Phase 3 (Weeks 7 to 9), middle. No Week 8 brief was available, so scope was proposed from the Phase 3 outline (supplier reliability and risk, RFM and segmentation, demand forecasting, stockout and reorder prediction) and the Week 7 open items. Owners confirmed at the check-in.

## Work done in this package
| Item | Owner | Package | Checks |
|---|---|---|---|
| W8-1 Supplier reliability | Chandrashekhar Deurghare | `w81_supplier_reliability/` | 29 |
| W8-2 Supplier risk | Abdibasid Mohamed Ali | `w82_supplier_risk/` | 38 |
| W8-3 Stockout and reorder | Ibrahim Khalil Umar | `w83_stockout_reorder/` | 31 |
| W8-4 Customer segments | Salim Bello Muhammad | `w84_customer_segments/` | 22 |
| Combined notebook | Everyone | `08_deep_dive_analysis.ipynb` | runs all four |

Combined: **120 of 120** notebook checks pass (`validation_report_week08.csv`), re-run end to end on the merged files supplied. The data dictionary for supplier fields is `data_dictionary_week08.csv` / `.md` (Ibrahim).

## Decisions and treatment
- **W8-2 reports "not firm" instead of a ranking.** The three-pillar score is built and shown, then tested by bootstrap, split-half against shuffled labels and weight sensitivity; none supports acting on the order. The Week 7 forecast benchmark recheck is part of the W8-2 notebook; the Week 7 figures were not available, so only the data reconciliation and the benchmark ordering are reported.
- **W8-3 is on the sales-scale assumption throughout.** Every table carries the label; no policy is called cost-optimal.
- **Merge fixes:** W8-4 no longer needs the clean folder; W8-3 folder names match the master (see `corrections_log_week08.md`, items 6 to 8).
- **W8-1 reports a null result honestly.** The suppliers are indistinguishable, as Weeks 3 and 4 already showed; the new work adds lead-time spread, time and criticality splits, concentration with a chance test, and intervals.
- **W8-4 tests the segments instead of assuming them.** W7-2 advised against segmenting; the segmentation Phase 3 asks for is built and then shown to be unstable, so it is delivered as a snapshot, not a driver.
- **k-means null corrected during the build.** A plain normal null suggested structure at k = 3; because skew alone raises the silhouette, the final null keeps each measure's distribution and correlation, and nothing is significant.
- **"Data owner" wording corrected.** There is no data owner to confirm the stock and purchase scale; the sales scale is the working assumption (see `corrections_log_week08.md`).

## Open items
1. **Week 7 forecast benchmark figures:** compare the W8-2 recheck (mean of previous 12 months 6.59% MAPE, last month 6.84%, same month last year 8.40%) with the Week 7 write-up and note any difference.
2. **Week 7 repository gaps:** upload the any-layout notebooks, the updated `analysis_questions_locked.md` to week-03, the corrected `week-06.zip` and the Step 1 wording zip; `week-06/stock_scale_note.md` is cited by the W8-3 report but was not in the files supplied.
3. **Q7** lead-time seasonality is still not written.
4. **Locked questions:** Week 8 questions and answers are in `analysis_questions_week08.md`; merge into `analysis_questions_locked.md`.
5. **Owner sign-off:** each owner confirms their package before it is submitted under their name; Abdibasid reviews every Week 8 notebook (W8-2 is his own, so another member should review it).
6. **Week 9:** holding and ordering cost data, if any exist, would let W8-3 compare policies on cost; price and quality data would let supplier risk mean more than timing.
