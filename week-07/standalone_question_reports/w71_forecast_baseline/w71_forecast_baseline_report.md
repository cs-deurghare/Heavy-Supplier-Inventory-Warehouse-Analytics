# W7-1: How well does a plain level forecast do, and can anything beat it?

**Question.** How well does the plain average of per-day rates forecast the 40 monthly series, and does any series justify more than a level forecast?
**Owner:** Abdibasid Mohamed Ali (Data Scientist) · **Week 7** · **Notebook:** `w71_forecast_baseline.ipynb` (27 of 27 checks pass)

## Answer

**The plain average is enough for all 40 series. A straight-line trend challenger beats it in none of them by the bar we fixed in advance, and no series shows a trend or a seasonal pattern once months are put on a per-day basis.** The baseline misses a month by about 6% for the totals and about 13% for single products and branches, and its 95% interval holds its coverage (96% of back-test months fall inside it).

| Group | Series | Baseline error (median, % of series mean) | Trend challenger error | Trend wins by the bar | 95% interval: months inside | Typical half-width of the interval |
|---|---:|---:|---:|---:|---:|---:|
| Totals (revenue, units, orders, gross profit) | 4 | 5.9% | 5.8% | 0 | 96.9% | ±15% |
| Products (units) | 30 | 12.7% | 13.0% | 0 | 96.4% | ±35% |
| Branches (orders) | 6 | 12.9% | 13.3% | 0 | 94.4% | ±32% |

## Evidence

| Finding | Result |
|---|---|
| **Per-day rates help a little** | Against the Week 6 raw-month average, the per-day baseline lowers the error for all four totals: revenue 6.73% to 6.53%, units 5.44% to 4.95%, orders 6.23% to 5.52%, gross profit 6.46% to 6.25%. The Week 6 raw-month figures reproduce exactly (checks 12 to 15) |
| **Nothing beats the baseline** | For each series the paired error difference (trend minus baseline) has a 95% bootstrap interval and a sign-flip p-value, Holm-adjusted across 40 series. **0 of 40 pass.** The trend is better in 15 series and worse in 25 |
| **Raw p-values look like chance** | 4 of 40 series have a raw p below 0.05 (P008, P012, P016, P026), against about 2 expected by chance. Three of the four are cases where the **trend is worse**. Smallest Holm-adjusted p = 0.37 |
| **No trend** | Per-day trend p for the totals: revenue 0.09, units 0.21, orders 0.60, gross profit 0.09. Three of 40 series have a raw p below 0.05 (smallest 0.031, P028), none after Holm adjustment (smallest 1.0) |
| **Seasonality is month length** | In raw months 9 of 40 series show a seasonal pattern (p < 0.05); on per-day rates only 1 of 40 (P020, p = 0.042, Holm-adjusted 1.0) |
| **The interval holds** | 96.1% of the 960 back-test months fall inside the 95% interval; totals 96.9%, products 96.4%, branches 94.4%. Individual series range from 87.5% to 100% with only 24 months each |
| **Year-ahead level** | The 2025 level forecast for revenue is ₹3.82B, which is **3.9% above 2024** (₹3.68B): the plain average returns to the six-year mean, it does not extend the small 2024 drop. Orders 3,002, units 205,580, gross profit ₹824M. Monthly figures and intervals for all 40 series are in `w71_forecast_2025.csv` |

## What the forecast is and is not

- **It is a benchmark.** Any Phase 3 model must beat these errors in the same rolling back-test. For the totals a model has to do better than about 6% a month; for single products or branches, better than about 13%.
- **It is not a prediction that revenue recovers.** Revenue and gross profit drift down slightly (Spearman about −0.19; per-day p 0.09) but not by more than chance. A flat forecast therefore sits above the 2024 level. Test the drift again when more months are available.
- **The interval is wide for single products and branches** (about ±35% and ±32%): monthly volumes vary by about 17% around their average and the history is 72 months.

## How the analysis was done

- **Series (40):** four totals of delivered orders (revenue before GST, units, orders, gross profit = `line_total − quantity × unit_cost`); 30 product series (units); 6 branch series (orders). 72 months, Jan 2019 to Dec 2024. Product revenue moves with product units because each product has one price.
- **Baseline:** mean of all earlier per-day rates (month value ÷ days in month), times the days in the target month. **Interval:** forecast ± t(0.975) × SD of earlier per-day rates × √(1 + 1/n), applied per day.
- **Back-test:** rolling origin, 24 one-step forecasts (Jan 2023 to Dec 2024), each using only earlier months. Error is the mean absolute error as a % of the series' mean monthly value, as in Week 6.
- **Challenger (one):** straight-line trend on the earlier per-day rates, extended one month. Chosen before the run because Week 6 found it the lowest-error method on the totals by a small margin.
- **Bar for "justifies more than a level forecast" (fixed in advance):** challenger mean error lower, 95% bootstrap interval of the paired difference wholly below zero, and sign-flip p-value below 0.05 after Holm adjustment across 40 series.
- **Tests:** Spearman trend, Kruskal-Wallis seasonality (12 calendar months), bootstrap (5,000) and sign-flip (5,000) on the 24 paired errors; Holm across 40. Seed 42.
- **Checks:** 27, including a plain-loop recomputation of the baseline, a no-look-ahead test, reconciliation of totals (18,033 orders, ₹22.96B, ₹4.95B gross profit; products and branches add up to the totals), reproduction of the Week 6 baseline errors, and verdicts re-derived from the bar.
- **Reproducibility:** the notebook finds the merged data itself (or `CADETX_MERGED`) and asserts that every check passes.

## Data limits

- **Six years, 24 test months.** A small trend or seasonal effect could go undetected, and a single series' interval coverage (87.5% to 100%) is a rough estimate. The challenger tests have low power for single products.
- **Very regular data.** Product volumes lie within 8% of each other and there is no seasonality. Real demand is rarely this regular, so a level forecast winning here does not mean it would win elsewhere.
- **Forecast errors of the 24 months are not independent** (neighbouring months share a level), so the sign-flip p-values are approximate. The result does not hang on them: the challenger also fails on the bootstrap interval for every series.
- **Delivered orders only.** Cancelled orders (9.84%) are not forecast; branch series count orders, product series count units.

## Recommendation

1. Use the plain average on per-day rates with the 95% interval as the Phase 3 benchmark for all 40 series.
2. Do not use a trend, seasonal or other more complex model unless it beats this baseline by the same bar in the same back-test.
3. Quote the interval with the forecast: about ±15% for totals, ±32% to ±35% for products and branches.
4. Re-test the slight revenue and gross-profit drift when more months exist.

## Files

| File | Contents |
|---|---|
| `w71_forecast_baseline.ipynb` | The analysis, with every check |
| `validation_report_week07_w71.csv` | 27 pass/fail checks |
| `w71_outputs/` | 5 tables (series results for all 40, back-test detail for 960 forecasts, 2025 forecast for 40 series × 12 months, group summary, readiness verdicts) |
| `w71_charts/` | 3 charts (revenue back-test with interval, challenger against baseline for every series, error and interval coverage by group) |
