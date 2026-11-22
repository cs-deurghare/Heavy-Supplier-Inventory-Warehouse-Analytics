# W8-3 Stockout risk, reorder points and back-test for the 180 stock pairs

**Questions.** Which product-branch pairs are likely to run out, and what reorder point should each pair use? The Week 7 lead-time-aware trigger is fitted on 2019 to 2022 and judged out of sample on 2023 to 2025.
**Owner:** Ibrahim Khalil Umar · **Week 8, W8-3** · reviewer: Abdibasid Mohamed Ali · **Notebook:** `w83_stockout_reorder.ipynb` (31 of 31 checks pass)

> **Every figure below rests on one assumption: that the sales scale is the right reference for stock.** "Sales scale assumed (Q10 unresolved); results rest on this assumption." There are no holding or ordering cost data, so no policy is called cost-optimal.

## Answer

**The existing reorder levels would have left 78 of 180 pairs below a 95% fill in 2023 to 2025 (93.8% of demand met, 4.3 stockouts per pair a year). A reorder point fitted on 2019 to 2022 with the lead-time-aware formula at 95% service would have met 99.3% of demand with none of the pairs below 95% (0.5 stockouts per pair a year), for 25.6% more average stock value. The pairs that run short are predictable from the training years, but the existing reorder level alone predicts them as well as the full risk score.**

| Policy (fitted 2019-2022, tested 2023-2025) | Fill rate | 95% range over 500 paths | Pairs below 95% | Stockouts per pair a year | Avg stock value | Extra stock vs A |
|---|---:|---|---:|---:|---:|---:|
| **A existing** (`reorder_level`, `max_stock`) | 93.8% | 93.5 to 94.2 | 78 | 4.26 | ₹397.1M | |
| B 95% (mean-lead trigger) | 98.9% | 98.8 to 99.1 | 0 | 0.80 | ₹474.4M | +19.5% |
| B-LT 90% (lead-time-aware) | 98.8% | 98.6 to 98.9 | 2 | 0.92 | ₹466.7M | +17.5% |
| **B-LT 95%** (recommended default) | **99.3%** | 99.1 to 99.4 | **0** | **0.54** | ₹498.8M | **+25.6%** |
| B-LT 99% | 99.8% | 99.7 to 99.8 | 0 | 0.18 | ₹560.5M | +41.1% |

## What the tests say

| Claim | Test | Result |
|---|---|---|
| The fitted trigger beats the existing levels out of sample | Same lead-time draws for every policy; compare per path | B-LT 95% beats A in **500 of 500** paths: **+5.5 points** of fill (5.1 to 5.8) |
| The gain is not a few pairs | Bootstrap over the 180 pairs of each pair's mean fill difference (5,000 resamples, seed 42) | +5.2 points on average per pair, interval **4.4 to 6.1** |
| It does not help every pair | Pairs with higher or lower fill than A | B-LT 95%: higher for 166, lower for 9 (B-LT 99%: higher for 176, lower for 1) |
| Risk can be predicted from the training years | Score from 2019-2022 data against "fill under A below 95% in 2023-2025" | Cycle-stockout score: **AUC 0.97** (0.94 to 0.99), Spearman 0.92 with the fill shortfall (permutation p < 0.001); the 20 highest-scored pairs are all below 95% |
| The score adds nothing over simple baselines | Same outcome, three baselines | `reorder_level` alone: AUC 0.97 (0.94 to 0.99); cover ratio 0.97; training-period fill under A 0.97 (0.95 to 0.99). The intervals overlap completely |

## Reading it

- **The existing levels are not tied to demand.** Reorder levels run 24 to 119 units (median 62) and vary more across pairs (coefficient of variation 0.37) than the lead-time demand they should cover (36 to 68 units, 0.17), and are unrelated to it (Spearman 0.09, p = 0.24). The recommended points run 81 to 138 (median 106.5); the existing level is below the recommended point for 168 of 180 pairs. A low level is what makes a pair run short, which is why `reorder_level` alone ranks risk as well as the full score.
- **At-risk pairs by category.** Existing levels leave below 95% fill: Sensors 5 of 6, Seals 8 of 12, Engine 11 of 24, Hydraulic 11 of 36, Undercarriage 10 of 24, Electrical 8 of 18 (`w83_by_category.csv`). Every category has at least two pairs below 95%.
- **The training years carried over.** Median test-period demand is 97% of training demand, and 159 of 180 pairs are within 15%, so a back-test fitted on the early years is a fair test of the later ones on this data.
- **Most of the lead-time spread is which supplier fills the order.** 93% of the variance of actual lead times is between suppliers (promised leads of 10 to 28 days; every supplier supplies every pair), and within a supplier the SD is only 1.6 to 1.8 days. This confirms the Week 7 guess. If the supplier could be chosen at order time, the lead-time uncertainty the safety stock must cover would be much smaller than 6.7 days; this was not tested here and belongs with the W8-2 supplier risk work.
- **Same conclusion about cost.** The extra fill needs more stock. With no holding or ordering cost the data cannot say which level is best, only what each costs and buys.

## How the analysis was done

- **Unit:** the product-branch pair (180). Demand is the ledger `OUT` per pair per day over 2,203 days (91.1% of delivered units).
- **Split:** training 2019-01-03 to 2022-12-31 (demand mean and SD, lead-time mean and SD per pair); test 2023-01-01 to 2025-01-13 (744 days). Parameters never see the test days.
- **Reorder point:** `s` = mean lead-time demand + z × √(lead time × demand variance + demand² × lead-time variance), z = 1.28, 1.645, 2.33 (90%, 95%, 99%); `S = s + (max_stock − reorder_level)`. B (mean-lead) drops the lead-time variance.
- **Simulation:** daily review; order up to `S` when on hand plus on order is at or below `s`; lost sales; each policy starts full and runs a 60-day warm-up on late-2022 demand, then is counted over the test period. Lead times of orders are drawn from the pair's received purchase-order lines ordered in the test period; 500 paths, seed 42, common draws across policies.
- **Risk score:** the service factor the existing level implies, `z = (reorder_level − mean lead-time demand) / SD of lead-time demand`, turned into `1 − Φ(z)` (normal approximation). Outcome: back-test fill under A below 95%. AUC with a 5,000-resample bootstrap over pairs; Spearman with a 5,000-shuffle permutation test; seed 42.
- **Checks:** 31, including the vectorised simulator matched to a plain day-by-day loop on five pairs for two policies, AUC recomputed by brute force, and the supplier-date identities (`lead_time_actual_days` and `supplier_lead_days` reproduced from the dates for all 140,077 received lines). The notebook finds the merged data itself (or `CADETX_MERGED`) and asserts that every check passes.

## Data limits

- **The scale is an assumption, not a finding.** If a corrected purchase scale were confirmed, every result here would be rebuilt on it (`week-06/stock_scale_note.md`).
- **No holding cost, ordering cost or service target.** Stock value at cost is a proxy; none of these policies is called cost-optimal.
- **One demand history, lost sales, no backorders, no forecast error beyond the training split.** The back-test is one split of a short, very regular history, not a forecast; the two-year test covers one regime.
- **Lead-time draws treat orders as independent and the supplier of an order as random.** Real supplier choice may follow a rule the data does not show.
- **The risk score does not beat simple baselines.** It is reported as a ranking tool for the pairs, not as a sharper predictor.
- **Very regular data.** Demand and lead times are very regular; findings are worded to what the simulation shows.

## Recommendation

1. Use the pair table (`w83_pair_reorder_backtest.csv`) as the reorder list: 168 pairs would raise their reorder point; start with the 78 pairs that fell below 95% fill (Sensors and Seals first).
2. Quote the result as fill against stock cost under the sales-scale sentence, for example 93.8% against 99.3% for 25.6% more stock, not as a best policy.
3. Pass the supplier-mix finding to W8-1 and W8-2: lead-time spread is driven by supplier promised leads, and lateness is the same (about 15%) for every supplier.

## Files

| File | Contents |
|---|---|
| `w83_stockout_reorder.ipynb` | The analysis, with every check |
| `validation_report_week08_w83.csv` | 31 pass/fail checks |
| `w83_outputs/` | 7 tables (back-test summary, reorder points and back-test for all 180 pairs, comparison against A, risk validation, by category, train/test stability, lead time by supplier) |
| `w83_charts/` | 3 charts (risk score against back-test fill with policy fills, reorder point against existing level, fill against stock value) |
