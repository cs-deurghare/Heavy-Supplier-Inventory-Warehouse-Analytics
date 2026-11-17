# W7-2: How do customers differ in recency, frequency and value?

**Question.** Using only the delivered order lines (as the Q13 rule requires), how do the 500 customers differ in how recently, how often and how much they buy, and are those differences real or what chance alone would produce?
**Owner:** Salim Bello Muhammad (BI Analyst) · **Week 7** · **Notebook:** `w72_customer_behaviour.ipynb` (22 of 22 checks pass)

## Answer

**Customers are remarkably alike. They buy about 36 times each over six years, about once every 60 days, and no group of customers stands out. The differences that exist are no larger than chance would produce, and a customer's past ordering does not predict their later ordering.** Value is spread almost evenly: the top 10% of customers hold 14.3% of revenue. Because every customer ordered in 2019 and again in 2024, the order lines describe behaviour but cannot show who is new or who has left, so **no churn, tenure or lifetime claim is made**.

| Measure (per customer, 2019 to 2024) | Median | Middle half (25th to 75th) | Range |
|---|---|---|---|
| Delivered orders | **36** | 32 to 40 | 21 to 56 |
| Revenue before GST | **₹45.3M** | ₹38.4M to ₹52.4M | ₹17.7M to ₹85.0M |
| Average order value | ₹1.27M | ₹1.13M to ₹1.40M | ₹0.74M to ₹1.96M |
| Days since last order (to 31 Dec 2024) | **46** | 20 to 84 | 0 to 358 |
| Average days between orders | **60** | 54 to 67 | 38 to 95 |
| Longest silence between two orders (days) | 240 | 202 to 294 | 115 to 532 |

Every customer ordered more than once; 77% ordered in the last 90 days of the history and all 500 within the last 358 days.

## Evidence

| Finding | Result |
|---|---|
| **Value is not concentrated** | Top 10% of customers: **14.3%** of revenue (95% interval 13.9% to 14.7%); top 20%: 26.6% (26.1% to 27.2%). Gini 0.125 for revenue (0.117 to 0.133) and 0.094 for orders |
| **Spread matches chance** | Shuffling which customer owns each order gives a revenue Gini of 0.123 against the observed 0.125 (p = 0.21), a top-10% share of 14.2% against 14.3% (p = 0.16), and giving every order to a random customer reproduces the spread in order counts (SD 6.0 against 6.0, p = 0.43) |
| **No difference by region or customer type** | Eight tests (orders, revenue, recency, average gap, each by region and by type): smallest raw p = 0.24; all Holm-adjusted p = 1.0; effect sizes 0.000 to 0.004 |
| **Industry segment** | Orders and revenue by industry segment: smallest raw p = 0.014 (revenue), Holm-adjusted p = 0.14, effect size 0.019: not significant once ten tests are counted |
| **Behaviour does not persist** | Orders 2019 to 2021 against 2022 to 2024: Spearman +0.004 (p = 0.92); revenue: −0.019 (p = 0.66). Customers who bought more early did not buy more later |
| **Frequency and order size are unrelated** | Orders against average order value: Spearman −0.004 (p = 0.94) |
| **Orders and recency** | Spearman −0.135 (Holm-adjusted p = 0.009): customers with more orders ordered more recently. This is expected by construction: more orders in a fixed window make a recent order more likely. It is not a separate behaviour |
| **Quiet longer than ever** | 9 of 500 customers (1.8%) have been quiet since their last order for longer than their own longest earlier gap. Descriptive only, not a churn measure |

## How the analysis was done

- **Unit and basis:** the customer (500); delivered orders (18,033 of 20,000; cancelled orders set aside as in earlier weeks); revenue is `line_total` before GST. The customer master's own date and value fields are not used (Q13). Region, customer type and industry segment come from `customers_clean.csv`.
- **Measures:** orders, revenue, average order value, days from last order to the end of the history (31 Dec 2024), mean and longest gap between orders.
- **Tests:** Kruskal-Wallis with epsilon-squared (clipped at 0) for group differences, Holm-adjusted across ten tests; Spearman with a 5,000-shuffle permutation p-value for relationships (Holm across four); bootstrap intervals over customers (5,000) for concentration; a chance test shuffling customer labels across orders. Seed 42.
- **Checks:** 22 pass/fail checks, including 50 customers recomputed with a plain filter, totals reconciled to the sales file (18,033 orders, ₹22.96B), the Gini recomputed by the pairwise formula, and counts recomputed by loop.
- **Reproducibility:** the notebook finds the merged and clean folders itself (or `CADETX_MERGED` and `CADETX_CLEAN`) and asserts that every check passes.

## Data limits

- **The history is 2019 to 2024, and every customer first ordered in 2019 and last ordered in 2024** (Q13). The order lines cannot show who is new, who has gone, or how long anyone has been a customer, so tenure, churn and lifetime value are out of reach on this data.
- **The data is very regular.** Customers order a similar number of times, at similar intervals and in similar sizes, and a customer's earlier behaviour tells nothing about later behaviour. Real customer data is rarely this uniform. The findings are worded to what the order lines show.
- **Recency is measured to the last date in the order history,** not to today.
- **Industry segment** (smallest raw p = 0.014) is the only lead above chance before adjustment; it should be re-tested on more data rather than acted on.

## Recommendation

1. Do not segment customers by recency, frequency or value in Phase 3: the spread is no larger than chance and does not persist.
2. Do not build churn or lifetime-value models from these lines; record the 2019 to 2024 window and the missing customer start dates in the data dictionary.
3. If Phase 3 needs customer groups, use region, customer type or industry segment only as labels, not as drivers; no group differs after adjustment.
4. Re-test the industry-segment lead if more data becomes available.

## Files

| File | Contents |
|---|---|
| `w72_customer_behaviour.ipynb` | The analysis, with every check |
| `validation_report_week07_w72.csv` | 22 pass/fail checks |
| `w72_outputs/` | 8 tables (customer metrics for all 500 customers, summary quartiles, concentration with intervals, chance test, group tests, group medians, stability and relationships, quiet-customer description) |
| `w72_charts/` | 3 charts (Lorenz curve with chance range, orders per customer, past against later orders) |
