# Week 6 review and corrections log

**Prepared for:** Abdibasid Mohamed Ali (review of Week 6 findings) · **Date:** 9 November 2026
**Method:** every package was run in a clean folder layout (merged and clean data only, environment variables unset), and its outputs compared byte for byte with the shipped files. Key numbers were recomputed independently from the corrected Week 2 merged datasets.

## 1. Summary

| Q | Owner | Reproducible | Checks | Verdict |
|---|---|---|---|---|
| Q4 follow-up | Salim | Yes, identical outputs | 43 of 43 | Ready (title and wording changed, see 2) |
| Phase 2 coverage | Abdibasid | Yes, identical outputs (21 files) | 43 of 43 | Ready |
| Q13 Customer master dates | Chandrashekhar | Yes, identical outputs | 25 of 25 | Ready (rebuilt version) |
| Stock KPIs and Q11 rerun | Ibrahim, with Abdibasid | Yes, identical outputs | 23 of 23 | Ready (labelled working result) |

Combined: **134 of 134 checks pass** across Q4 (43), coverage (43), Q13 (25) and stock (23) (`validation_report_week06.csv`). Sign-off by the owners and by Abdibasid as reviewer is still to be recorded.

## 2. Corrections log

| # | Package | Issue found | Fix | Status |
|---|---|---|---|---|
| 1 | Q4 | Title, question and notebook introduction promised to say whether the money is collectable; the data has no collection or write-off records | Reworded: the question is why the money is old; collectability is not tested | Fixed |
| 2 | Q4 | Check 8 description gave wrong counts for invoices off by 0.01 | Now 75 overpaid and 92 short by exactly 0.01, both rounding differences | Fixed |
| 3 | Q4 | Exposure range could be read as a collectability claim | Labelled as a scenario (25% to 100% of past-75-day balances never collected), kept separate from any claim | Fixed |
| 4 | Weeks 3 to 5 | Reports referred to a "data owner" for a dataset supplied with the programme | Headings now "Open data limits"; Q11 pack marked not applicable for sending | Fixed (files supplied) |
| 5 | Coverage | Integrity check assumed ₹28.60B for all delivered orders | Reconciles to the invoice file (₹29.25B on 18,033) and the reliable base (₹28.60B on 17,640) | Fixed |
| 6 | Coverage | Interval rule alone labels one product Fast and one Slow | No labels when the overall tests are not significant (p = 0.62 and 0.45); rank-based split kept and labelled as ranks only | Fixed |
| 7 | Coverage | "Seasonality" in raw monthly totals | Disappears on per-day rates (p 0.42 to 0.75): month length, not demand | Fixed |
| 8 | Q13 | First version not accepted as ready | Rebuilt: verdict bar fixed in advance, group tests with Holm adjustment, 25 checks | Fixed (rebuilt version) |
| 9 | Q13 | A check on the number of result tables expected seven; there are six | Corrected to six | Fixed |
| 10 | Q13 / coverage | Chart labels overlapped bars or captions | Axis headroom and layout fixed | Fixed |
| 11 | Stock | Week 5 Q11 was a labelled scenario with no stock KPIs | Rerun on the agreed sales scale with turnover, cover and health added; reproduces Week 5 for all four policies (fill rate, orders, pairs below 95%); a plain re-implementation matches on five pairs | Fixed |
| 12 | Stock | Recorded `current_stock` could be mistaken for a usable level | Shown only as a sensitivity: median 38,272 days of cover; every pair above `max_stock` | Fixed |
| 13 | Stock | Chart of recorded against working cover was a meaningless scatter | Replaced by a two-bar comparison on a log scale | Fixed |
