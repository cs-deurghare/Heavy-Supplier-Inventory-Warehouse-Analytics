# Week 4 full notebook: corrections log
Corrected copy of `04_deep_dive_analysis.ipynb`. Runs end to end with 0 errors; 37 of 37 validation checks pass (it was 22).

| # | Issue | Fix | Effect on the answer |
|---|---|---|---|
| 1 | Q8 on-time and delay were tested on purchase-order lines, but lines on one PO share the same supplier and dates, so the p-values were far too small (on-time p = 0.0001) | Tests now use the purchase order as the unit (21,630 received POs). Scorecard on-time, delay and lead time are also per PO. A comparison table (`q8_unit_of_analysis_comparison.csv`) shows both | Suppliers are not distinguishable on on-time (p = 0.97) or delay (p = 0.88), matching Week 3. Lead time stays the one real difference |
| 2 | Product mix (about 40% of the 2023 to 2024 fall) was presented as a finding without a test | New section 1.5b: permutation test on the 2023 to 2024 mix effect (5,000 shuffles), p = 0.35 | Mix is the largest component but not distinguishable from noise |
| 3 | The 2023 to 2024 fall of 3.8% was presented without a test | Bootstrap interval in 1.5b: -7.8% to +0.4% | The 2023 to 2024 step cannot be distinguished from no change |
| 4 | Cancellation rise judged only by 2024 vs the earlier pool (p = 0.031), chosen after looking | Added six-year homogeneity (p = 0.27) and trend (Cochran-Armitage p = 0.030) tests, plus a check | The rise has weak support |
| 5 | Q8 effect sizes missing for delay, cost and lead time; lead time p shown as 0 | Effect size added to every test; p shown as < 1e-300 | Lead time effect size 0.93 |
| 6 | "OEM about 25, Distributor about 15, Local Vendor about 12 days" read as if types were separate | Ranges stated: Distributor 10.5 to 18.5, Local Vendor 10.5 to 12.5, OEM 19.5 to 28.5 | Read lead time supplier by supplier |
| 7 | "Each new customer would be worth about 45 million" stated as fact | Marked as an assumption | Wording only |
| 8 | `__MACOSX` folder in the zip | Not included | Housekeeping |
| 9 | "Not distinguishable from normal year-to-year variation" described a bootstrap interval, which measures sampling uncertainty, not year-to-year variation; on-time chart title said "practically identical" | Wording now "cannot be distinguished from no change"; chart title now "not distinguishable" | Wording only |
| 10 | Q2 had no effect sizes, no uncertainty on the 60.9% and no check for dominant customers | New section 2.4 adds the Q2 robustness tests (numbers reproduce exactly): orders-per-customer test (p = 0.427), effect sizes (epsilon-squared 0.003 / 0.000), South + West share 95% interval 56.5-65.3%, largest customer 0.37% and top 5 = 1.68% of revenue, Central + North East ratio 0.97 (0.88-1.06), customer-branch region link (Cramer's V = 0.74). Q2 answer renumbered 2.5 | 37 of 37 checks pass (was 30); Q2 conclusion unchanged, but quote 60.9% as "about 61%" |

New outputs: `q1_mix_and_step_significance.csv`, `q8_unit_of_analysis_comparison.csv`. Updated: `q8_supplier_scorecard.csv` (now per PO, with `received_pos`), `q8_supplier_tests.csv`.

## Week 5 update: ledger adjustment sign (Q10 replay)

| # | Issue | Fix | Effect on the answer |
|---|---|---|---|
| 11 | The Q10 corrected-scale replay added every ledger adjustment, and Week 4 said "every ledger adjustment is positive". That is true of the `quantity` column only: `running_balance` applies 1,227 adjustments as additions and 1,227 as reductions | Replay re-run with adjustments signed from `running_balance` (`q10_stock_scale.ipynb`, Part D); Q10 report section 5 and issue UI-Q10-03 updated | At k = 18.1 the average balance is 142, not 330, with 37% of days below zero (not 28%). The headline Q10 result (the 18.1x scale gap, PO spend within 4% of cost of goods, thresholds fitting sales) is unaffected, but the replay no longer "lands near maximum stock" |
| 12 | "Only 8% of the 180 pairs between 0 and `max_stock`" could not be reproduced from the notebook (the Week 4 method gives 12 pairs, 6.7%, by end balance) | The definition is now stated (end-of-period balance) and computed: 10 of 180 (5.6%) with signed adjustments; average-balance and pair-day readings are also reported | Wording only; the conclusion that the ledger cannot test a replenishment policy stands |
| 13 | Q10 validation had a check that "average balance at k = 18.1 is within 25% of mean max stock" and "all ledger adjustments are positive" | Replaced by checks that the adjustment steps are exactly +/- quantity (1,227 each), that the signed replay average is below 60% of mean max stock, and that quantities are stored unsigned | Q10 now has 24 checks (was 19) |
