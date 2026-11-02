# Q5: What is a customer worth over time?

**Question.** Government leads on revenue through order count, not order size. What does a customer-lifetime-value view show?
**Owner:** Salim Bello Muhammad (BI Analyst) · **Week 5** · **Notebook:** `q5_customer_lifetime_value.ipynb` (34 of 34 checks pass)

## Answer

**Customers are worth almost the same over their lifetime, whatever their type, and no group of customers dominates.** Government leads on orders only because it has the most customers. Lifetime value here means observed gross profit over 2019 to 2024 on Delivered orders: it is a measurement, not a forecast.

| Finding | Evidence |
|---|---|
| Why Government leads | 22.8% of customers (114 of 500), 22.6% of orders (4,075), 22.0% of revenue. Each Government customer places 35.7 orders (all types 36.1) and its average order is the smallest (₹1.24M vs ₹1.28M to ₹1.29M for the others). It leads through **customer count**, not buying more often or in larger orders |
| Average lifetime value | ₹9.9M gross profit per customer (95% interval ₹9.7M to ₹10.1M; median ₹9.7M; 10th to 90th percentile ₹7.3M to ₹12.7M) |
| By customer type | Not different: Kruskal-Wallis p = 0.41, effect size ε² = 0.000. Means run from ₹9.57M (Government) to ₹10.21M (Dealer), a 6.7% spread that random labels produce 23% of the time (permutation p = 0.23). No pair differs after adjustment (smallest adjusted p = 0.57) |
| Concentration | Largest customer 0.37% of gross profit; top 5 customers 1.66%; top 10% of customers hold 14.2%; Gini 0.12. The 80/20 pattern does not exist here |
| Stability of value | A customer's 2019 to 2021 profit does not predict 2022 to 2024 profit (Spearman ρ = −0.03, interval −0.11 to 0.07). Customer value is mostly not a stable trait |
| Activity | All 500 customers ordered in both 2019 and 2024; at least 498 were active in every year. Median gap between orders is 41 days |
| Trend | Gross profit per active customer fell 4.9% from 2019 to 2024 (₹1.67M to ₹1.59M), the same fall seen in Q1 |

## Other segments, and one exploratory lead

Region, industry segment, rating and payment terms were tested together with customer type (five cuts, adjusted together). Region, rating and payment terms show nothing. **Industry segment is an exploratory lead**, and three further tests were run to settle it:

- **Size:** Manufacturing (₹10.5M) and Rental (₹10.3M) customers are worth about 6% to 12% more than Construction (₹9.7M) and Mining (₹9.3M). The effect size is small (ε² = 0.02).
- **Beyond chance:** the spread between the best and worst industry mean (₹1.12M) is larger than shuffled labels typically produce (₹0.59M; permutation p = 0.014).
- **Stable:** the industry ranking from 2019 to 2021 repeats in 2022 to 2024 (rank correlation 0.94). Both halves use the same 500 customers, so this shows stability inside the data, not independent confirmation.
- **Cause:** it comes from how often customers order (orders per customer, p = 0.034: Manufacturing 37.8 vs Mining 34.6), not from order size (p = 0.56) or margin (p = 0.83; all about 21.5%).
- **Caution:** once the five segment cuts are adjusted together it is p = 0.06, just short of significance.

So treat industry as an exploratory lead to re-test with more data, not as a finding. It does not change the main answer: customer type explains nothing and no customer group dominates.

## What the data cannot show

- **True customer lifetime, churn and acquisition.** Every customer is active for the full six years, so there are no new or lost customers. This is unusual for a real customer base and is a question for the data owner. Lifetime value here is the observed six-year profit, not a forecast: the data holds a single price list, so projecting forward would be an assumption.
- **Collected profit.** 19.8% of invoiced value is outstanding and 86% of that is more than a year overdue. As a sensitivity, each Delivered order is matched to its single invoice and its gross profit is reduced by that invoice's unpaid share, then summed per customer. This is indicative only: it assumes profit is lost in proportion to the unpaid share, and unpaid invoices may still be collected. Every type falls by about 21% to 22% (for example Government ₹9.57M to ₹7.45M, Dealer ₹10.21M to ₹8.03M), the outstanding share does not differ by type (p = 0.27), and the comparison between types stays the same (p = 0.23).

## Why order dates were used, not the customer master

For **58%** of customers the master's `customer_since` is later than their first Delivered order (every customer's first order is in 2019), and for **93%** `last_purchase_date` is earlier than their last order. The master's `total_purchase_value` adds up to 5.4% of Delivered revenue and has no relationship with it (correlation −0.08). These fields cannot be used for lifetime work; this is the Q13 question previewed.

## Questions for the data owner

1. Are all 500 customers meant to have traded for the whole 2019 to 2024 window, or does the extract keep only long-standing customers?
2. Are `customer_since`, `last_purchase_date` and `total_purchase_value` in the customer master maintained? Which should analysis use?
3. Is a customer acquisition or churn record held outside this extract?

## Recommendation

Do not build customer tiers or "key account" programmes on this data: there is no high-value group, value does not repeat from one period to the next, and customer type explains nothing. Treat Government's order lead as a customer-count effect. Revisit lifetime value if the data owner supplies acquisition and churn dates, and confirm the industry-segment effect (Manufacturing and Rental ahead, through order frequency) with more data before acting on it.

## Notes on method

- **Unit of analysis:** the customer (500 rows) for value and concentration; the order for the Government comparison.
- **Widest-gap interval.** The largest gap between two types (Dealer minus Government, ₹0.64M) has a plain bootstrap interval of ₹0.06M to ₹1.22M that excludes zero. That interval overstates the evidence because the pair was picked as the largest of 10 after looking. The fair test, whether the spread of the five type means exceeds what shuffled labels produce, gives p = 0.23. The first version of the check used the plain interval and failed; it was replaced with the permutation test, not loosened.
- **Customer activity.** The first version of the notebook expected all 500 customers active in every year; the data shows 498 in 2021 and 2022. The check and text now say "at least 99% of customers" (actual minimum 498) rather than "all".
- **Industry segment.** The first version called industry "worth re-testing" from its adjusted p-value (0.059) alone. Two further tests (permutation p = 0.014, ranking repeats across halves) and a driver check (order frequency) now show it is a consistent small lead. It stays unconfirmed because the five-cut adjustment is still above 0.05.
- Seed 42, 5,000 resamples (1,000 for the persistence interval).

## Files

| Item | Location |
|---|---|
| Notebook | `q5_customer_lifetime_value.ipynb` |
| Validation | `validation_report_week05_q5.csv` (34 checks) |
| Charts | `q5_charts/` (value by type, concentration and persistence, value per customer by year) |
| Outputs | `q5_outputs/` (customer table of 500 rows, distribution, by type, tests, pairwise, segments, industry detail, industry tests, replication and drivers, concentration, mean interval, yearly activity, persistence, after-outstanding sensitivity, master date check, widest gap) |

The notebook finds the merged data and the raw `customers.csv` itself (any folder inside the repository), or set `CADETX_MERGED` and `CADETX_RAW`.
