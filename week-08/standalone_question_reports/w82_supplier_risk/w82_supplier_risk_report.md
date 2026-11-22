# W8-2 Supplier risk: a transparent score and how firm its ranking is

**Question.** How exposed are we to each of the 8 suppliers, and is the risk ranking firm enough to act on?
**Owner:** Abdibasid Mohamed Ali · **Week 8, W8-2** · **Notebook:** `w82_supplier_risk.ipynb` (38 of 38 checks pass)

> Money figures carry: *PROCUREMENT SCALE - purchase spend is about 14x sales revenue (Q10 unresolved); money figures are descriptive.* Rates, shares and lead times do not depend on that scale.

## Answer

**A risk score can be computed and SUP0003 comes out on top, but the ranking is not firm and should not be used to pick or drop a supplier.** No pair of suppliers keeps its order in 95% of the 5,000 resamples (0 of 28 pairs); the median 95% rank interval is 7 ranks wide on a scale of 8; SUP0003 is the riskiest in only 41.5% of resamples; and rankings built on two random halves of the purchase orders do not agree. This is the same message as W8-1: the 8 suppliers are not distinguishable on late deliveries, cancellations, spend share or lead-time spread.

## The score (equal pillars, no fitted weights)

Each pillar is scaled 0 to 1 across the 8 suppliers and the three are averaged, then multiplied by 100. A min-max score always spreads 8 suppliers from 0 to 100, so the size of a score says nothing on its own; the tests below do.

| Pillar | Built from |
|---|---|
| Reliability | mean of late-delivery rate (received POs) and cancellation rate (all POs) |
| Concentration | share of received purchase spend before GST |
| Lead-time spread | standard deviation of actual lead time within the supplier (days) |

| Rank | Supplier | Late | Cancelled | Spend share | Lead SD (days) | Score | Rank 95% interval | P(riskiest) |
|---:|---|---:|---:|---:|---:|---:|---|---:|
| 1 | SUP0003 | 14.98% | 10.22% | 12.56% | 1.78 | 72.8 | 1 to 7 | 41.5% |
| 2 | SUP0008 | 15.80% | 9.57% | 12.58% | 1.72 | 58.4 | 1 to 8 | 15.3% |
| 3 | SUP0007 | 15.33% | 9.94% | 12.51% | 1.73 | 56.5 | 1 to 8 | 14.2% |
| 4 | SUP0001 | 15.08% | 9.88% | 12.64% | 1.72 | 55.6 | 1 to 8 | 14.7% |
| 5 | SUP0002 | 15.03% | 10.28% | 12.09% | 1.72 | 40.5 | 1 to 8 | 3.8% |
| 6 | SUP0006 | 14.79% | 9.41% | 12.53% | 1.72 | 38.1 | 1 to 8 | 5.8% |
| 7 | SUP0005 | 14.67% | 9.53% | 12.90% | 1.65 | 35.5 | 2 to 8 | 2.5% |
| 8 | SUP0004 | 15.17% | 10.18% | 12.19% | 1.69 | 35.4 | 2 to 8 | 2.2% |

The raw components differ by under 1.2 points of late rate, 0.9 points of cancellation, 0.8 points of spend share and 0.13 days of lead-time spread across all eight suppliers.

## How firm is the ranking?

| Test | Result |
|---|---|
| Bootstrap of POs (5,000 resamples, seed 42) | 0 of 28 pairs keep their order in 95% of resamples; mean Spearman between a resample's ranking and the base ranking 0.48 |
| Split-half against shuffled labels (5,000 splits each) | True labels: mean agreement between halves -0.31. Shuffled supplier labels: -0.03. The true-label ranking agrees *no better* than a ranking with no real supplier differences (AUC 0.28; 0.5 would be equal) |
| Weights and scaling (6 variants) | SUP0003 is riskiest in all 6, but all six use the same data and the same small gaps, so this agreement is mechanical and does not offset the bootstrap result. Rankings correlate 0.88 to 0.98 with the base |

The negative split-half agreement is expected for two disjoint halves of one fixed dataset when real differences are smaller than the sampling noise: each supplier's deviation in one half is mirrored in the other. The shuffled run has the same mirroring, so it is the fair yardstick, and the true-label run sits below it. In this data the realised between-supplier differences are, if anything, smaller than random assignment of POs would produce.

## Exposure context (not part of the score)

- **Spend concentration:** supplier HHI 0.1250, the minimum possible with 8 suppliers; shares 12.1% to 12.9%.
- **Critical products:** 93.5% to 94.1% of every supplier's spend is on High-criticality products, and each supplier carries 12.1% to 12.9% of all High-criticality spend. No product depends on one supplier.
- **Geography:** all 8 suppliers are in China: East China 62.4% of spend, South China 24.7%, North China 12.9%. A single-country exposure is the one concentration the data does show; it is not a supplier-level difference.
- **Lead time:** this is the real difference between suppliers: promised 10 to 28 days, actual about 0.5 days longer; within a supplier SD is only 1.65 to 1.78 days. Supplier choice changes how long stock is on order, not how reliably it arrives (see W8-3).

## Week 7 forecast benchmark, rechecked on the merged data

Inputs reconcile to the Week 7 basis (18,033 delivered orders, ₹22.96B before GST, 72 months from 2019-01 to 2024-12). One-step-ahead forecasts for the 24 months of 2023 and 2024:

| Benchmark | MAPE | 95% interval |
|---|---:|---|
| Mean of previous 12 months | 6.59% | 5.00 to 8.19 |
| Last month (naive) | 6.84% | 4.91 to 8.87 |
| Same month last year | 8.40% | 6.41 to 10.57 |

The two non-seasonal benchmarks are not distinguishable, and repeating last year's month is the worst, which is consistent with the no-seasonality finding of earlier weeks. **The Week 7 benchmark figures were not in the uploaded files, so this section does not claim a numerical match to Week 7; compare the ordering and the MAPEs above with the Week 7 forecast write-up and note any difference.**

## Data limits

- No price quotes, quality or defect data and no cost of a late delivery: risk means timing, cancellation, spend share and lead-time spread only.
- Equal pillar weights are a convention, not an estimate; the sensitivity run shows the top spot does not move but nothing below it is firm.
- Very regular data: identical supplier rates are rare in real purchasing data, so every statement is worded to what the data shows.

## Recommendation

1. Do not rank suppliers by this score; report it as "no supplier stands out". Re-run it when price, quality or delivery-promise data arrive.
2. If lead-time exposure matters, use supplier promised lead (10 to 28 days) as the lever, as in W8-3.
3. Treat the single-country concentration (all suppliers in China) as the exposure worth discussing.

## Files

| File | Contents |
|---|---|
| `w82_supplier_risk.ipynb` | The analysis, with every check |
| `validation_report_week08_w82.csv` | 38 pass/fail checks |
| `w82_outputs/` | 9 tables: scorecard, rank stability, pairwise order probabilities, firmness summary, split-half, sensitivity, exposure context, region exposure, forecast benchmark recheck |
| `w82_charts/` | 3 charts: rank intervals, split-half agreement, pairwise order probabilities |
