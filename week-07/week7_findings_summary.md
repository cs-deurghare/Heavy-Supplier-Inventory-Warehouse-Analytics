# Week 7 Findings Summary
**CadetX Heavy Supplier, Inventory & Warehouse Analytics: Phase 3 (opening)**

**Items answered:** W7-1 (forecast baseline), W7-2 (customer behaviour), W7-3 (priority pack), W7-4 (lead-time robustness) and the Week 7 data dictionary.
**Source:** `07_deep_dive_analysis.ipynb` and the three folders in `standalone_question_reports/`, on the corrected Week 2 merged datasets. 105 of 105 notebook checks and 8 of 8 cross-checks pass.
**Basis:** delivered orders: 18,033 orders, 500 customers, net revenue (before GST) ₹22.96B, gross profit ₹4.95B (21.56%).

## At a glance

| Item | Finding in one line | Confidence |
|---|---|---|
| **W7-1** | A plain average of per-day rates is enough for all 40 monthly series; a trend challenger beats it in none. It misses a month by about 6% (totals) and 13% (products, branches); its 95% interval holds (96% of back-test months). | Strong |
| **W7-2** | Customers are alike: 36 orders each, one every 60 days, top 10% hold 14.3% of revenue. No group differs after adjustment, past behaviour does not predict later behaviour. No churn or tenure claim is possible. | Strong |
| **W7-4** | With lead times varying from 7 to 35 days, the existing reorder levels fill 93.6% of demand and the demand-based trigger 98.8% (99.2% lead-time-aware), for 19% to 25% more stock value. The trigger wins in every one of 1,000 simulated paths. In-sample; sales scale assumed. | Strong on the comparison; labelled assumption |
| **W7-3** | Four of the ten class A products earn less than the 21.56% portfolio margin (TA-800 17.96%, EB-600 19.75%, TC-45 18.34%, TB-900 17.19%). Branches differ in orders, not order size. 72 of 180 stock pairs fall under 95% fill, led by Sensors and Seals. | Strong (stock: labelled assumption) |

## W7-1: How well does a plain level forecast do, and can anything beat it?

- **Baseline:** mean of earlier per-day rates × days in the month, with a 95% interval. Rolling back-test, 24 one-step forecasts (Jan 2023 to Dec 2024).
- **Error (% of series mean):** totals 5.9%, products 12.7%, branches 12.9% (medians). Per-day rates improve all four totals over the Week 6 raw-month average (revenue 6.73% to 6.53%).
- **One challenger, a straight-line trend:** better in 15 series, worse in 25; **0 of 40** pass the bar set in advance (bootstrap interval wholly below zero and Holm-adjusted p below 0.05). 4 raw p-values fall below 0.05 against about 2 expected by chance, and three of those four favour the baseline.
- **No trend, no seasonality:** smallest Holm-adjusted p is 1.0 for trend and 1.0 for per-day seasonality. Seasonality in raw months (9 of 40) is month length.
- **Interval:** 96.1% of 960 back-test months inside; typical half-width ±15% (totals), ±35% (products), ±32% (branches).
- **2025 level:** revenue ₹3.82B, 3.9% above 2024, because the average returns to the six-year mean. It is a benchmark, not a prediction that the 2024 dip reverses.

**Recommendation.** Use the plain average with its interval as the Phase 3 benchmark; accept a more complex model only if it beats it by the same bar in the same back-test.

## W7-2: How do customers differ in recency, frequency and value?

- **Per customer (2019 to 2024):** median 36 orders (middle half 32 to 40), ₹45.3M revenue, an order every 60 days, last order 46 days before the end of the history.
- **Not concentrated:** top 10% hold 14.3% of revenue (95% interval 13.9% to 14.7%), Gini 0.125; the spread matches what shuffling orders across customers gives (p 0.16 to 0.43).
- **No group stands out:** region and customer type (eight tests, all Holm-adjusted p = 1.0); industry segment smallest raw p = 0.014, Holm-adjusted 0.14.
- **Does not persist:** orders and revenue in 2019–21 do not predict 2022–24 (Spearman +0.004 and −0.019).
- **No churn claim:** every customer ordered in 2019 and 2024 (Q13). Nine customers are quiet longer than their own longest earlier gap; descriptive only.

**Recommendation.** Do not segment customers by recency, frequency or value, and do not build churn or lifetime models from these lines.

## W7-3: Which products, branches and stock pairs need attention first?

- **Class A:** 10 products, 81.5% of revenue, margin 20.33%. **Below the portfolio margin:** TB-900 17.19%, TA-800 17.96%, TC-45 18.34%, EB-600 19.75%; against the portfolio margin they give up about ₹64M, ₹122M, ₹52M and ₹88M. They are the only four of 30 products below it.
- **Branches:** Chennai 51.1 orders a month, Kolkata 47.4, Ahmedabad 43.3, Delhi 37.2, Pune 37.1, Hyderabad 34.4 (intervals in the report); units per order 67.6 to 69.1. Delhi and Pune are not separable.
- **At-risk stock pairs:** 72 of 180 (existing reorder levels, fill under 95%), leaving 11.6% of their demand unmet. Sensors 5 of 6, Seals 9 of 12, five categories 3 of 6. *Sales scale assumed (Q10 unresolved); results rest on this assumption.*

**Recommendation.** Review the four low-margin class A products (TA-800 first) as a cost and price question, start the stock review with Sensors and Seals, and read branch differences as order counts only.

## W7-4: Does the demand-based reorder trigger still beat the existing levels when lead times vary?

- **Lead times are not constant:** 140,077 received purchase-order lines, 7 to 35 days, SD 6.7, 671 to 842 lines per pair. Week 6 used one rounded mean per pair.
- **Fill rate with lead times drawn per order (1,000 paths):** existing levels 93.6% (95% interval 93.4% to 93.8%, 81 of 180 pairs under 95%); trigger B at 95% service 98.8%; lead-time-aware B-LT at 95% service 99.2%. Against constant lead times variation takes 0.7 points off A and 0.3 to 0.8 off B.
- **Stock cost:** B at 95% holds 19% more stock value than A (₹469.5M against ₹395.0M), B-LT 25% more (₹493.4M). No holding or ordering cost exists, so no policy is called cost-optimal.
- **The trigger beats the existing levels in every path** (1,000 of 1,000) and, for B at 95%, in 159 of 180 pairs.
- **In-sample:** B's reorder points use the same history they are tested on. *Sales scale assumed (Q10 unresolved); results rest on this assumption.*
- **Data dictionary:** 184 fields in 7 files, each marked usable, usable with caution, unusable or not tested. The three customer date and value fields, recorded `current_stock`, `ledger_latest_balance`, `total_in_qty`, `balance_difference`, `stock_value_cost` and `below_reorder` are unusable.

**Recommendation.** Quote the fill-rate gap as an upper bound with the stock-cost trade-off beside it; ask the business for holding cost, ordering cost and a service target before choosing a policy.

## Data limits carried forward

1. Order history covers 2019 to 2024 only and every customer first ordered in 2019 and last ordered in 2024, so new and lost customers cannot be seen.
2. The data is very regular (product volumes within 8%, no seasonality, even customers); findings are worded to what the lines show.
3. No capacity, staffing or timing data; branch "throughput" means orders and units sold.
4. No price history: every line carries the product-master price, so margin gaps cannot be split into price and cost.
5. Stock scale (Q10) is an agreed working assumption, not a resolved fact.

## Open items

Q6 margin-concentration redo from Week 5; Q7 lead-time seasonality; the Week 4 notebook line "8%" to read "about 6% (10 of 180)"; updated `analysis_questions_locked.md`.

---
*Method notes.* Tests: Spearman, Kruskal-Wallis, bootstrap and sign-flip/permutation (5,000 resamples, seed 42), Holm adjustment. Re-run: `07_deep_dive_analysis.ipynb` inside the repository checkout.
