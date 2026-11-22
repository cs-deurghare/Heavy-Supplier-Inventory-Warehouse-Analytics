# Week 8 Findings Summary
**CadetX Heavy Supplier, Inventory & Warehouse Analytics: Phase 3 (middle)**

**Items answered in this package:** all four: W8-1 (supplier reliability), W8-2 (supplier risk), W8-3 (stockout and reorder prediction) and W8-4 (customer segments).
**Source:** `08_deep_dive_analysis.ipynb` and the folders in `standalone_question_reports/`, on the corrected Week 2 merged datasets. 120 of 120 notebook checks pass (29 for W8-1, 38 for W8-2, 31 for W8-3, 22 for W8-4), re-run end to end on the merged files supplied.
**Basis:** purchase orders 24,000 (21,630 received, ₹312.03B before GST, procurement scale unresolved); delivered orders 18,033, 500 customers, net revenue ₹22.96B.

## At a glance

| Item | Finding in one line | Confidence |
|---|---|---|
| **W8-1** | The 8 suppliers cannot be told apart: on time 84.2% to 85.3%, cancelled 9.4% to 10.3%, spend share 12.1% to 12.9%, all Holm-adjusted p = 1.0. Lead time differs by contract (10 to 28 days) but varies only about 1.7 days within a supplier. No product depends on one supplier; all suppliers are in China (East China 62% of spend). | Strong on the comparison; money figures descriptive (procurement scale) |
| **W8-2** | A transparent risk score (reliability, spend concentration, lead-time spread) ranks SUP0003 first, but the ranking is not firm: 0 of 28 pairs keep their order in 95% of 5,000 resamples, SUP0003 is riskiest in only 41.5% of them, and halves of the data do not reproduce the ranking. The suppliers cannot be separated on risk; the exposure that exists is single-country (all in China). | Strong on "not firm"; money figures descriptive |
| **W8-3** | Existing reorder levels would have left 78 of 180 pairs below 95% fill in 2023 to 2025 (93.8% of demand met). A lead-time-aware reorder point at 95% service meets 99.3% with no pair below 95%, for 25.6% more average stock value. Every number rests on the sales-scale assumption. | Moderate: one regular history, one split, sales scale assumed |
| **W8-4** | Five RFM segments exist as labels but are not stable (adjusted Rand index 0.005), do not predict later revenue (p = 0.61), show no structure beyond chance in k-means and do not differ by region, type or industry after adjustment. | Strong (consistent with W7-2) |

## W8-1: Which suppliers deliver late or vary most, and how concentrated is purchasing?

- **Delivery:** 84.9% of received POs arrive on or before the expected date, 15.1% late (1 to 7 days), 4.5% early. Supplier range 84.2% to 85.3%, intervals about ±1.4 points and overlapping.
- **Cancellation:** 9.4% to 10.3% of POs.
- **No difference beyond chance:** five tests (on-time, cancellation, delay, lead time minus contract, spread), all Holm-adjusted p = 1.0; effect sizes 0.00 to 0.02.
- **Lead time:** mean 10.5 to 28.5 days by supplier, always about 0.5 days over contract; within-supplier SD 1.65 to 1.78 days. Between-supplier spread is more than five times the within-supplier SD.
- **Stable and uniform:** on-time by order year 84.5% to 85.2% (p = 0.95), no monthly trend (p = 0.83), critical-product POs 84.9% against 85.5% (p = 0.52).
- **Reliability score:** does not track observed on-time rate (Spearman -0.44, p = 0.30, 8 suppliers); not a usable proxy.
- **Concentration:** supplier HHI 0.1250 (minimum 0.125); every product is bought from all 8 suppliers (largest share averages 13.3%, maximum 13.9%); none more concentrated than chance after adjustment. Geographic exposure: all suppliers in China, East China 62.4%, South China 24.7%, North China 12.9%.

## W8-2: How exposed are we to each supplier, and how firm is the ranking?

- **Score:** three equal pillars scaled 0 to 1 across suppliers: reliability (mean of late rate and cancellation rate), concentration (spend share) and lead-time spread (within-supplier SD). Ranking, riskiest first: SUP0003 (72.8), SUP0008 (58.4), SUP0007 (56.5), SUP0001 (55.6), SUP0002 (40.5), SUP0006 (38.1), SUP0005 (35.5), SUP0004 (35.4).
- **The raw gaps are tiny:** across the 8 suppliers late rate differs by 1.1 points, cancellation by 0.9 points, spend share by 0.8 points and lead-time SD by 0.13 days. Min-max scaling stretches these to 0 to 100.
- **Not firm:** 0 of 28 pairs keep their order in 95% of 5,000 resamples; median 95% rank interval 7 ranks wide; SUP0003 riskiest in 41.5% of resamples; mean Spearman of resample rankings with the base ranking 0.48.
- **Not repeatable:** rankings from two random halves of the POs agree at -0.31 (true labels) against -0.03 (shuffled labels); the ranking is no better than one with no real supplier differences (AUC 0.28).
- **Sensitivity:** SUP0003 stays riskiest under 6 weightings and scalings, but they share the same data, so this does not make the ranking firm.
- **Exposure:** supplier HHI 0.1250 (the minimum for 8); 93.5% to 94.1% of each supplier's spend is on High-criticality products; all suppliers are in China (East 62.4%, South 24.7%, North 12.9% of spend).
- **Week 7 forecast benchmark recheck:** inputs reconcile (18,033 delivered orders, ₹22.96B, 72 months). Mean of previous 12 months 6.59% MAPE, last month 6.84%, same month last year 8.40% on the 24 months of 2023-2024; the first two are not distinguishable. The Week 7 benchmark figures were not in the files supplied, so a numerical match to Week 7 is not claimed.

## W8-3: Which stock pairs are likely to run out, and when should they reorder? (sales scale assumed, Q10 unresolved)

- **Existing levels:** 78 of 180 pairs fall below 95% fill in the 2023-2025 back-test; overall fill 93.8% (95% range 93.5 to 94.2), 4.3 stockouts per pair a year.
- **Lead-time-aware reorder point at 95% service (fitted 2019-2022):** fill 99.3% (99.1 to 99.4), no pair below 95%, 0.5 stockouts per pair a year, for 25.6% more average stock value; it beats the existing levels in 500 of 500 simulated paths (+5.5 points of fill, 5.1 to 5.8) and is higher for 166 pairs, lower for 9.
- **Risk can be ranked from the training years** (AUC 0.97, 0.94 to 0.99) but `reorder_level` alone does as well (AUC 0.97): the existing levels are not tied to demand (Spearman 0.09 with lead-time demand, p = 0.24).
- **Lead-time spread is a supplier effect:** 93% of lead-time variance is between suppliers (promised 10 to 28 days); within a supplier SD is 1.6 to 1.8 days.
- **No policy is called cost-optimal:** holding and ordering costs are not in the data. The pair-level reorder list is `w83_pair_reorder_backtest.csv`.

## W8-4: Do the customers fall into stable, meaningful segments?

- **Segments (end of 2024):** Champions 70, Loyal 86, Recent 130, Slipping 69, Quiet 145 customers; revenue shares 17.6%, 21.2%, 23.0%, 12.4%, 25.7% (intervals in the report).
- **Stability:** segments from 2019-2021 and 2022-2024 agree no better than chance (adjusted Rand index 0.005, p = 0.09; 20.4% stayed against 21.8% expected).
- **Prediction:** 2019-2021 segments do not differ in 2022-2024 orders (Holm-adjusted p = 0.15) or revenue (p = 0.61).
- **Structure:** k-means for k = 2 to 6 finds no more than a structureless cloud with the same distributions and correlations (smallest Holm-adjusted p = 0.88).
- **Profile:** no difference by region (Holm p = 0.19), customer type (0.56) or industry segment (0.105; raw 0.035, the same weak lead as W7-2).
- **No churn, tenure or lifetime claim:** every customer ordered in 2019 and 2024.

## What this means for Phase 3 (Week 9)

- Supplier choice cannot be justified on reliability or on a risk score; the lever is promised lead time (and, if data arrive, price and quality). Single-country sourcing is the one exposure the data shows.
- Stock results are reorder-list suggestions on the sales-scale assumption; Week 9 should add holding and ordering cost data if any can be found, otherwise keep quoting fill against stock cost, not a best policy.
- Customer segments are a snapshot list, not a treatment plan.

## Carried-forward limits

- **Stock and procurement scale unresolved (Q10):** receipts are about 18 times sales and purchase spend about 14 times sales revenue. There is no data owner to ask, so the sales scale is the working assumption for stock results and procurement money figures are descriptive. Rates and shares are unaffected.
- **No cost, quality or price-quote data:** nothing is called cost-optimal or best-value.
- **Very regular data across weeks:** identical supplier rates, near-identical customers and no seasonality are rarely seen in real data; every finding is worded to what the data shows.
