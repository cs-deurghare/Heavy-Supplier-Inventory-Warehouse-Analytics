# Q2 Regional Concentration: Investigation

**Question:** Is revenue concentrated in a few regions, and is that a market-size effect or an under-coverage effect?
**Basis:** corrected Week 2 merged data; net revenue = `line_total` (ex-GST) of Delivered orders only; 500 customers, 20,000 orders, 130,402 sales lines.

## Answer
Revenue is concentrated because customers are concentrated. South (31.63%) and West (29.32%) hold 60.95% of delivered revenue and 61.8% of customers. A customer is worth about the same in every region.

| Region | Revenue (Rs M) | Revenue share | Customers | Customer share | Rs M per customer |
|---|---|---|---|---|---|
| South | 7,262 | 31.63% | 158 | 31.6% | 46.0 |
| West | 6,731 | 29.32% | 151 | 30.2% | 44.6 |
| East | 4,052 | 17.65% | 87 | 17.4% | 46.6 |
| North | 3,938 | 17.15% | 82 | 16.4% | 48.0 |
| Central | 502 | 2.19% | 11 | 2.2% | 45.6 |
| North East | 475 | 2.07% | 11 | 2.2% | 43.1 |

## Tests (one row per customer)
- Revenue per customer across 6 regions: Kruskal-Wallis H = 6.34, p = 0.275 (no difference).
- Delivered orders per customer: 34.5 to 36.9, H = 4.91, p = 0.427 (no difference).
- Central + North East vs other regions, revenue per customer: ratio 0.97, bootstrap 95% interval 0.88 to 1.06 (5,000 resamples, seed 42).
- Value per order: Rs 1.24M to Rs 1.30M (descriptive, not tested).

## How strong is the conclusion
- Effect sizes are negligible: epsilon-squared 0.003 for revenue per customer and 0.000 for orders per customer.
- South + West share of revenue is 60.95%, bootstrap 95% interval over customers 56.5% to 65.3%.
- No single customer drives it: the largest is 0.37% of revenue and the top 5 together are 1.68%. Without them the South + West share is 61.99%.
- Central + North East: with only 22 customers, a revenue-per-customer gap larger than about 12% is ruled out; a smaller gap cannot be excluded.

## Branch presence
Central and North East have no branch. Their 22 customers spend as much as customers elsewhere, so having no branch does not show up in how much each customer buys. Elsewhere, 73% to 88% of a region's orders are handled by a branch in the same region (customer region vs branch region: Cramér's V = 0.74).

## Limits
The data holds only customers who already buy. A small market and an unserved market cannot be told apart, so we do not claim that missing branches cause the concentration.

## Recommendation
Test customer acquisition in Central and North East before investing in branches. Add regional market-size data for the next review.

## Reproducibility
Run `q2_regional_concentration.ipynb` with the merged datasets available (env var `CADETX_MERGED` or the folder beside the repo). 16 validation checks are written to `validation_report_week04_q2.csv`; all pass. `q2_outputs/q2_robustness.csv` holds the robustness figures.
