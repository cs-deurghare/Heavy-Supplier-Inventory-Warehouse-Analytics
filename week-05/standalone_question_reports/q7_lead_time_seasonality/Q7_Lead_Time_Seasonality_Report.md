# Q7: Is lead time seasonal?

**Question.** Delivery lead time averages 8.06 days and is uniform by region. Is there a seasonal pattern by month or year, and is there enough structure to forecast?
**Owner:** Abdibasid Mohamed Ali (Data Scientist) · **Week 5** · **Notebook:** `q7_lead_time_seasonality.ipynb` (34 of 34 checks pass)

## Answer

**No. Lead time is not seasonal, and a month-of-year index does not improve a forecast.** Lead time here is delivery date minus order date on the 18,033 Delivered orders. It is a flat spread of 1 to 15 days that barely responds to anything in the data.

| Finding | Evidence |
|---|---|
| Distribution | Mean 8.06 days, median 8, range 0 to 15. Each value from 1 to 15 holds 6.3% to 7.1% of orders; an even spread is not rejected (chi-square p = 0.125). 26.9% of orders take 12 days or more |
| Month of the year | Monthly means run 7.92 (Mar) to 8.20 (Feb) days, a spread of 0.28 days. Kruskal-Wallis p = 0.85, effect size ε² = 0.000. No pair of months differs after adjusting for 66 pairs (smallest adjusted p = 1.0). Spread within months also does not change (Levene p = 0.99) |
| Yearly wave | A fitted yearly wave has amplitude 0.03 days (0.3% of the mean), p = 0.83. Correlation with the month 12 steps earlier is −0.02 |
| Sampling noise | The 72 monthly means vary by sd 0.256, against 0.272 expected from sampling noise alone (p = 0.79) |
| Year | 8.00 to 8.09 days across 2019 to 2024 (p = 0.96); no trend (Spearman ρ = −0.11, p = 0.35) |
| Strength of the "no" | A typical month would show a gap of about 0.32 days at 80% power; the smallest month (Feb, 1,358 orders) 0.34 days. Gaps of that size or larger are ruled out |
| Order volume and revenue | Monthly order counts follow month length (chi-square against days in the month, p = 0.37). No yearly wave in orders (p = 0.068, amplitude 2.9%) or revenue (p = 0.12, amplitude 2.8%). The raw monthly tests (p = 0.02 and 0.04) come mostly from short February |
| Forecast readiness | On a 2024 hold-out (2019 to 2023 training), the month index is no better than the plain mean for lead time (error 2.38% vs 2.16%), orders (6.88% vs 6.83%) or revenue (8.24% vs 7.49%). Same-month-last-year is worse for all three |

## Other cuts, and one weak lead

Ten cuts were scanned together (month, year, customer region, branch region, channel, category, customer type, industry, payment terms, warehouse type), plus order weekday and order value. Everything is flat except customer region, which has the smallest raw p-value (0.008). Central (7.56 days, 406 orders) and North East (7.72, 380 orders) customers are about 0.3 to 0.5 days quicker than the 8.06 average. This is **a weak lead, not a finding**: after Holm adjustment over the ten cuts it is p = 0.08, the whole-scan permutation test gives p = 0.07 (5,000 shuffles), and the effect size is ε² = 0.0006. The two regions are small, and the effect is not seasonal. It does not contradict "uniform by region" in any practical sense (the widest regional gap is 0.6 days), but it should be re-tested if more data arrives.

## What this does and does not support

- **Supports:** quoting lead time as a single figure with its range (8.06 days, 1 to 15) for all months, and not building a seasonal staffing or stock plan on it.
- **Does not support:** any claim about *real* delivery performance. A lead time that is evenly spread, ignores month, product, channel, order size and weekday, and is the same for cancelled orders (8.05 days) looks generated or planned rather than measured. Whether `delivery_date` is an actual or a promised date is the key question.
- **Forecasting:** the data has no reliable seasonal structure, for lead time or for volume and revenue, so a seasonal index is not worth using. Orders carry a possible ~3% wave (p = 0.07) that is too weak to help on the hold-out.
- **Not the same as supplier lead time.** Customer delivery lead time (0 to 15 days) and supplier lead time (10.5 to 28.5 days, Q8) are separate fields and are never mixed.

## Questions for the data owner

1. Is `delivery_date` the actual delivery date or a planned date? Real delivery times usually respond to season, product, distance or stock.
2. Why is every lead time between 0 and 15 days with an even spread, including for cancelled orders?
3. Is a dispatch date, carrier or delay reason recorded anywhere, so delivery performance can be measured against a promise?

## Recommendation

Report lead time as a stable company-wide figure (about 8 days, 1 to 15), do not plan around a seasonal lead-time pattern, and ask the data owner what the delivery date represents before drawing any operational conclusion.

## Notes on method

- **Unit of analysis:** the Delivered order (18,033 rows). Lead time is identical on every line of an order, so a line-level test would count each order about 6.5 times. Cancelled orders are excluded because they carry a delivery date (found in Q3).
- **Tests:** Kruskal-Wallis with ε² (negative values are reported as 0), one-way ANOVA, Levene, 66 Mann-Whitney pairs with Holm adjustment, a fitted yearly sine and cosine wave (F test), and a chi-square of the 72 monthly means against sampling noise. All ten cuts are adjusted together (Holm) and also scanned by permutation (5,000 shuffles, seed 42). Monthly intervals are bootstrap (5,000 resamples).
- **Volume and revenue:** orders by order month; revenue is the net `line_total` of Delivered orders (₹22.96B, reconciled).
- **Hold-out:** 2024 is scored by mean absolute percentage error against forecasts built from 2019 to 2023. This shows a month index adds nothing here; it is not a forecast of 2025.
- **Wording check:** the first draft labelled the minimum and maximum months one position off; the labels were corrected and the figures above (Mar and Feb) come from the corrected run.

## Files

| Item | Location |
|---|---|
| Notebook | `q7_lead_time_seasonality.ipynb` |
| Validation | `validation_report_week05_q7.csv` (34 checks) |
| Charts | `q7_charts/` (distribution, by month with intervals, month-of-year index for lead time, orders and revenue) |
| Outputs | `q7_outputs/` (distribution, by month, pairwise months, month tests, by year, monthly series, series tests, all cuts, by customer region, seasonal index, volume and revenue seasonality, 2024 hold-out) |

The notebook finds the merged data itself (any folder inside the repository), or set `CADETX_MERGED`.
