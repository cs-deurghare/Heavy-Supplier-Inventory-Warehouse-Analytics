# Week 7 review and corrections log

**Prepared for:** Abdibasid Mohamed Ali (review of Week 7 items W7-2, W7-3 and W7-4; W7-1 built) · **Date:** 16 November 2026
**Method:** each package was run in a clean folder layout (corrected merged and clean data and the Week 6 package only, environment variables unset), its outputs compared with the shipped files, and its key numbers recomputed independently from the corrected Week 2 merged datasets.

## 1. Summary

| Item | Owner | Reproducible | Checks | Verdict |
|---|---|---|---|---|
| W7-2 Customer behaviour | Salim | Yes, all 8 tables identical | 22 of 22 | **Accepted** (file names fixed) |
| W7-3 Priority pack | Chandrashekhar | **Partly**: input file chosen by file-system order; two of four tables differ between machines | 5 of 5, but the checks could not fail | **Rejected and rebuilt** (26 of 26 computed checks) |
| W7-4 Lead-time robustness | Ibrahim | Yes, 7 of 7 tables identical; independent simulation agrees | 30 of 30 | **Accepted** (four small fixes) |
| W7-1 Forecast baseline | Abdibasid | Built in this review | 27 of 27 | New |

Combined: 105 of 105 notebook checks and 8 of 8 cross-checks pass (`validation_report_week07.csv`, 113 rows).

## 2. W7-2 Customer behaviour (Salim): accepted

Recomputed independently and confirmed: median 36 orders (32 to 40, range 21 to 56), median revenue ₹45.3M, median recency 46 days (77% within 90 days, maximum 358), average gap 60 days (38 to 95), top 10% share 14.33%, top 20% 26.63%, Gini 0.1253, persistence Spearman +0.004 (p 0.93) and −0.019 (p 0.66), orders against order value −0.004, orders against recency −0.135, nine quiet customers.

| # | Issue | Fix | Status |
|---|---|---|---|
| S1 | The shipped files were named `w7_*` (outputs, charts, validation) but the notebook writes `w72_*` and `validation_report_week07_w72.csv`; a re-run produced differently named files than the ones submitted | Folder, notebook, outputs, charts, report and validation renamed to `w72_*` | Fixed |
| S2 | The upload contained a copy of the sprint plan (`sprint7.pptx`) and no folder structure | Removed; package placed as `week-07/standalone_question_reports/w72_customer_behaviour/` | Fixed |
| S3 | The README Week 7 section (his deliverable) was missing | Written in the combined `README.md` | Fixed |

No change to any number or conclusion.

## 3. W7-3 Priority pack (Chandrashekhar): rejected and rebuilt

| # | Problem | Evidence | Fix |
|---|---|---|---|
| C1 | **Margins were random numbers.** The notebook draws a cost factor with `np.random.uniform(0.75, 0.83)` and calls the result "dynamic margin" | Shipped: TB-900 23.75%, TC-45 23.75%, P021 19.14%. Real (from `unit_cost` on the order lines): TB-900 **17.19%**, TC-45 **18.34%**, P021 **22.94%**. The two products that earn the least were shown as healthy | Realised margin from the order lines for all 30 products; class A table rebuilt |
| C2 | **The "72 at-risk pairs" were not the at-risk pairs.** The notebook takes the first file whose name contains "stock" and "pair" or "kpi" and keeps its first 72 rows | In the shipped CSV they are P001 to P012 in all six branches with `current_stock` about 100,000 (the recorded-stock sensitivity file); in a clean layout the same notebook picks another file and returns different rows (P001 at CHN001 and so on) | Read `stock_kpis_by_pair.csv` by exact path and keep `health = At risk`; checked against the Week 6 category table (15 of 15) |
| C3 | Not listed by category; no category summary | Task asked for the list "by category" | Added list and category table |
| C4 | **Checks could not fail.** Revenue tolerance ₹1B, orders tolerance ±500, top-10 share "above 70", at-risk count tested on `head(72)` | `validation_report_week07.csv`: 5 PASS | 26 computed checks with exact values (revenue, gross profit, orders, class A set, 15 category counts, branch means) |
| C5 | Branch column "avg_order_interval_days" (1.2 to 1.5 days) is the gap between distinct order dates for a whole branch, which says nothing about customers or demand | `w73_branch_table.csv` | Dropped; branch names, units per order, shares and a stated interval method (bootstrap over 72 months) added |
| C6 | The notebook divides receipts by 18.1 "to apply the sales scale". The sales scale is the sales-based demand, not receipts ÷ 18.1 | Section 5 of the notebook | Removed |
| C7 | The data finder searches every parent folder for any directory called `merged` or `week-06` and takes the first | `find_dir` in cell 1 | Explicit paths with `CADETX_MERGED` and `CADETX_WEEK6_STOCK` |
| C8 | Report says "Verified & Complete" on five checks; it gives no numbers for price, margin or intervals and no list of what to review first | `w73_priority_pack_report.md` | Report rewritten with the tables and the four low-margin products, the branch intervals and the at-risk categories |
| C9 | The findings summary, sprint notes and locked-questions update (also his deliverables) were not in the upload | Sprint plan slide 4 | Findings summary, sprint notes and corrections log written; locked questions still open |

**What stayed correct:** revenue ₹22.96B and 18,033 delivered orders, class A at 81.5%, P015 at ₹4,857M, the six branch order rates (51.1, 47.4, 43.3, 37.2, 37.1, 34.4).

## 4. W7-4 Lead-time robustness and data dictionary (Ibrahim): accepted

Re-run clean (outputs removed, no environment variables): 7 of 7 tables identical, 30 of 30 checks. **Independent check** with my own simulator, own random draws and 40 lead-time paths: existing levels 93.59%, B 95% 98.76%, B-LT 95% 99.17% (his 93.6%, 98.8%, 99.2%). Also confirmed from the data: 140,077 received lines, 671 to 842 per pair, range 7 to 35 days, SD 6.67; all reorder points reproduce (B exactly; B-LT within one unit by rounding); demand total 1,124,832; 184 dictionary columns agree with the five merged files; `margin_percentage` is a markup on cost for 29 of 30 products.

| # | Issue | Fix | Status |
|---|---|---|---|
| I1 | The constant-lead rows of `lt_policy_summary.csv` and `lt_pair_results.csv` carried the assumption text "each order's lead time drawn independently", which is false for them | Constant-lead rows now say "one constant lead time per pair (the rounded mean, 17 to 19 days)"; no number changed | Fixed |
| I2 | The report and outputs did not say that policy B's reorder points are estimated from the same history they are tested on | "In-sample" added to the assumption text, the data limits and the recommendation | Fixed |
| I3 | The data dictionary said OF-90 is "inconsistent with both" margin definitions; its `margin_percentage` 37.3 matches a margin on price (37.5%), not a markup (60.0%). The purchase-order row also needed to say the value is copied from the product master | Both rows reworded | Fixed |
| I4 | His package held a section notebook that repeats the whole simulation and a script that overwrites the combined validation file | Not used: the combined notebook runs his notebook itself and builds the validation file. Folder, notebook, outputs, charts and validation renamed `w74_*` to match the other items | Fixed |

No numbers changed.

## 5. W7-1 Forecast baseline (Abdibasid): built

Built to the plan: 40 series, plain average on per-day rates with a 95% interval, rolling back-test, one challenger tested against it, a bar for "more than a level forecast" fixed in advance. The Week 6 raw-month baseline errors reproduce exactly (revenue 6.7303%, units 5.4439%, orders 6.2320%, gross profit 6.4597%). Result: 0 of 40 series justify more than a level forecast.

## 6. Cross-checks between the items

Customer revenue (W7-2) equals product revenue (W7-3) and delivered revenue, ₹22,958,987,430; customer orders equal branch orders, 18,033; W7-1 branch series means equal the W7-3 branch table (6 of 6); W7-1 product units equal the class A units; 500 customers, 6 branches, 30 products and 180 pairs everywhere; the 72 pairs where policy A fails 95% fill under constant lead times in W7-4 are exactly the 72 on the W7-3 at-risk list.

## 7. Still open (not part of this package)

Q6 redo (Week 5); Q7; the Week 4 notebook "8%" to "about 6% (10 of 180)"; the Week 6 coverage label "Q6 margin %" and the "in-sample" wording in the stock report; locked-questions update; owner sign-offs.
