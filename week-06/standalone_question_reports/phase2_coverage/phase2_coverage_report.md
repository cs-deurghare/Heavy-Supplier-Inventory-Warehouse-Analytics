# Phase 2 coverage: ABC classes, movers, branch throughput and forecast readiness

**Questions.** Which products matter most (ABC)? Which move fast or slow? How busy is each branch? Which monthly series are ready to forecast in Phase 3? These are the Phase 2 coverage items the team confirmed for Week 6, answered from sales and branch data only.
**Owner:** Abdibasid Mohamed Ali (Data Scientist) · **Week 6** · **Notebook:** `phase2_coverage.ipynb` (43 of 43 checks pass)

## Answer

**Ten products make 81.5% of revenue, but they are the lowest-margin products and not the busiest. No product moves faster or slower than another. Branches differ clearly in how many orders they handle, and every monthly series is ready for a simple level forecast, not a more complex one.**

| Item | Finding | Evidence |
|---|---|---|
| ABC by revenue | **A: 10 products (81.5%), B: 7 (14.1%), C: 13 (4.4%)** | The top 3 products make 44.3% of revenue and the top 6 make 65.1% (Gini 0.63) |
| ABC by gross profit | A: 12 products (82.7%), B: 6 (12.6%), C: 12 (4.6%) | The two views give the same class for 27 of 30 products (kappa 0.85); P009 and P023 move from B to A, P025 from C to B |
| What drives the classes | Price, not volume | Revenue rank follows unit price (Spearman +1.00) and hardly follows units sold (+0.17) |
| A-class margins | Lowest | Gross margin is 20.3% in A, 25.5% in B and 31.8% in C; revenue against margin % across products gives Spearman −0.91 |
| Stability | Classes do not move | All 30 products keep their revenue class between 2019–2021 and 2022–2024 (kappa 1.00) |
| Movers | **No product is fast or slow** | Product volumes run from 548 to 593 units a month, only 8.1% apart. Kruskal–Wallis p = 0.62; chance-label test p = 0.45; the product ranking in 2019–2021 against 2022–2024 has Spearman −0.09 |
| Branch throughput | Branches differ in orders, not in order size | Orders a month: Chennai 51.1, Kolkata 47.4, Ahmedabad 43.3, Delhi 37.2, Pune 37.1, Hyderabad 34.4. Kruskal–Wallis effect size 0.44. Units per order are the same everywhere (67.6 to 69.1, p = 0.57) |
| Branch trends | None | No branch trends up or down (largest \|Spearman\| 0.13, all Holm-adjusted p = 1.0) |
| Forecast readiness | **All 40 series: level forecast** | No trend after Holm adjustment, no seasonality once months are put on a per-day basis, and no method beats the plain average of earlier months |

## ABC classes

Convention (set before looking at the results): rank by the measure, add up the shares, and call a product **A** if the share before it is under 80%, **B** if under 95%, otherwise **C**. Delivered orders only; revenue is before GST.

- **Class A by revenue** is P015 Engine Block, P014 Transmission Assembly, P021 Boom Cylinder, P019 Swing Motor, P004 Track Chain, P010 Turbocharger, P011 Hydraulic Cylinder, P001 Hydraulic Pump, P030 Fuel Pump and P022 Control Valve. By category, Engine makes 33.0% of revenue, Hydraulic 28.4% and Transmission 14.8%.
- **The classes depend on price.** These products each sell about the same units as everything else, so a higher price puts them in class A. Class A holds 33.5% of units and 81.5% of revenue.
- **Margins fall as price rises.** Gross margin is 20.3% in class A against 31.8% in class C. A product-count view of "importance" and a profit view therefore differ slightly: three products change class between the revenue and gross-profit views.
- **The cut-offs matter a little.** With 70/90 cut-offs the counts are A 7, B 7, C 16 (revenue); with 85/97 they are A 12, B 6, C 12. The 10 class A products stay in A or B in both cases (7 stay A under 70/90, all 10 under 85/97), and no class C product ever moves into A.

## Fast, medium and slow movers

Before labelling any product, the notebook tested whether product volumes differ by more than chance, because a label means nothing if the ranking is noise.

- Every product sells between 548 and 593 units a month (average 572). The busiest sells 8.1% more than the quietest.
- Volumes do not differ beyond chance: Kruskal–Wallis p = 0.62, and shuffling product labels across lines gives a spread as large as the real one (p = 0.45; the observed spread is 1.01 times the chance spread).
- The ranking is not stable: the order of products in 2019–2021 does not predict the order in 2022–2024 (Spearman −0.09, p = 0.64).
- A bootstrap interval rule alone would label one product Fast and one Slow. With 30 products, about 0.75 of each are expected by chance, so **no product gets a label**. The table `movers_products.csv` keeps the interval-rule result and a rank-based reference split, labelled as ranks only.
- Units sold do not relate to margin % (Spearman −0.24, p = 0.21).

## Branch throughput

Orders and units of delivered orders per branch-month (432 branch-months, none empty).

| Branch | Orders a month (95% interval) | Units a month | Units per order | Share of orders |
|---|---:|---:|---:|---:|
| Chennai South Hub | 51.1 (49.1 to 53.1) | 3,527 | 69.1 | 20.4% |
| Kolkata East Depot | 47.4 (45.7 to 49.1) | 3,207 | 67.6 | 18.9% |
| Ahmedabad West Hub | 43.3 (41.7 to 44.9) | 2,975 | 68.8 | 17.3% |
| Delhi Central | 37.2 (36.0 to 38.6) | 2,574 | 69.1 | 14.9% |
| Pune Distribution | 37.1 (35.7 to 38.5) | 2,523 | 68.1 | 14.8% |
| Hyderabad Logistics | 34.4 (33.1 to 35.7) | 2,347 | 68.2 | 13.7% |

- Chennai handles 1.48 times the monthly orders of Hyderabad. Delhi and Pune cannot be told apart (their intervals overlap almost completely).
- Differences come from the **number of orders**, not their size: units per order are the same in every branch.
- No branch trends up or down over the six years, and the ranking is the same if cancelled orders are included (Spearman +0.94).

## Which series are ready to forecast? (note for Phase 3)

**All 40 monthly series (total revenue, units, orders and gross profit; 30 product series; 6 branch series) are ready for a simple level forecast: the average of earlier months with a prediction interval. None shows a trend or seasonal pattern that would justify a more complex model, and none of the five simple methods tested beats the plain average in a rolling back-test.** Totals vary by about 8% month to month (CV 0.07 to 0.08), so a 95% prediction interval is about ±16% of the monthly average; for single products and branches it is wider, about ±33% and ±31%. Any Phase 3 model should be judged against the plain average as its benchmark. Seasonality shows up in raw monthly totals (p = 0.02 to 0.04), but it disappears when months are converted to per-day rates (p = 0.42 to 0.75): it is month length, not demand. Revenue and gross profit drift down slightly (Spearman about −0.19) but not by more than chance (p = 0.11 and 0.12), so a trend should be tested again when more months are available.

How this was tested:

- **Trend:** Spearman correlation of the series with time, with Holm adjustment across the 30 products and across the 6 branches. None is significant.
- **Seasonality:** Kruskal–Wallis across the 12 calendar months, on raw totals and on per-day rates.
- **Back-test:** a rolling-origin test with 24 one-step forecasts (months 49 to 72) by five methods: the mean of all earlier months, a trailing 12-month mean, the last value, the same month last year (seasonal naive) and a linear trend. A method counts as better only if the 95% bootstrap interval of its error difference from the plain average lies wholly on the better side. No total passes. Across the 36 product and branch series, 1 of 144 comparisons passes, against about 3.6 expected by chance.
- **Seasonal naive is the worst method** for every total (7.1% to 8.2% error against 5.4% to 6.7% for the plain average).

## How the analysis was done

- **Unit and basis:** delivered orders only (18,033 of 20,000; 1,967 cancelled orders are set aside, as in Weeks 3 and 5). The delivered orders are the 18,033 invoices: their value including GST (₹29.25B) equals the invoice file, and the 17,640 reliable invoices come to ₹28.60B, the Q4 base.
- **Checks:** 43 pass/fail checks, including independent recomputation of the ABC classes with a plain loop, reconciliation of product, branch and month totals to the sales file, and a hand reproduction of the back-test baseline.
- **Reproducibility:** seed 42; 5,000 bootstrap resamples and 5,000 permutations; the notebook finds the merged data itself.

## Data limits

- **Sales and branch data only.** There are no capacity, staffing, pick-and-pack or dwell-time data, and the delivery dates look generated (Q7). "Throughput" here means orders and units sold, not warehouse capacity or speed.
- **No stock claims.** Stock, turnover and cover depend on the open stock-scale assumption and are handled in the stock work.
- **Very regular patterns.** Product volumes lie within 8% of each other, classes are identical in both periods, and the monthly series show no seasonality. Real demand is rarely this regular. The findings are worded to what the sales lines show, and the pattern is noted here as a limit.
- **Short history for seasonality.** Six years give six observations per calendar month, so a small seasonal effect could go undetected. The back-test, which does not depend on a single test, also finds none.
- **ABC cut-offs are a convention** (80/95). The sensitivity table shows how the counts change.

## Recommendation

1. Treat the 10 class A products as the focus for revenue attention, and note that their margins are the lowest (about 20%).
2. Do not use fast, medium or slow labels in Phase 3 or in reports: volumes are the same within chance.
3. Start Phase 3 forecasting from the plain average with prediction intervals, on per-day rates, and require any model to beat it in the same rolling back-test.
4. Do not use this data for branch capacity or speed claims. Record the missing capacity and timing data in the data dictionary.

## Files

| File | Contents |
|---|---|
| `phase2_coverage.ipynb` | The analysis, with every check |
| `validation_report_week06_coverage.csv` | 43 pass/fail checks |
| `coverage_outputs/` | 15 result tables (ABC products, summary, category, cut-off sensitivity, view agreement, stability; movers and tests; branch month, summary, tests, trends, by year; forecast readiness for all 40 series and the back-test totals) |
| `coverage_charts/` | 5 charts (ABC Pareto, movers, branch throughput, month-of-year, back-test) |
