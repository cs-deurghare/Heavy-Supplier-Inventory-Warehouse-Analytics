# Q13: Are the customer master dates maintained, and should they be used?

**Question.** The customer master holds `customer_since`, `last_purchase_date` and `total_purchase_value`. Phase 3 retention and churn work would use them for tenure, recency and value. Do they agree with the order lines for all 500 customers, and should they be used?
**Owner:** Chandrashekhar Deurghare (BI Analyst) · **Week 6** · **Notebook:** `q13_customer_master_dates.ipynb` (25 of 25 checks pass)

## Answer

**No. None of the three fields agrees with the order lines, and none should be used for tenure, recency, value or churn.** The gaps are not a regional or customer-type problem: they look the same everywhere. Tenure, recency and value for Phase 3 must be derived from the order lines.

| Field | Compared with | Result | Verdict |
|---|---|---|---|
| `customer_since` | Date of the first order | **58.4% of customers are "customers since" a date after they had already ordered** (41.6% before). Only 1.2% are within 30 days. Rank correlation with the first order −0.04 (permutation p = 0.37). Spread evenly over 2015 to 2024 (Kolmogorov–Smirnov p = 0.92), while all 500 customers first ordered in 2019 | **Unusable** |
| `last_purchase_date` | Date of the last order | **93.0% are earlier than the last order**, 6.8% later (by up to 272 days), 6.6% within 30 days. Rank correlation −0.01 (p = 0.92). Only 154 of 500 show a 2024 date, although all 500 ordered in 2024 | **Unusable** |
| `total_purchase_value` | Delivered revenue from the order lines | Adds up to ₹1.24B against ₹22.96B of revenue (**5.4%**). **No customer is within 10%** of their revenue. Rank correlation −0.09, the wrong direction | **Unusable** |

| Gap pattern | Result |
|---|---|
| By region and by customer type (six tests, Holm-adjusted) | Smallest raw p = 0.124; smallest Holm-adjusted p = 0.75; largest effect size 0.007 |
| `customer_since` by its own year | Customers dated 2015 to 2018 have no contradiction (their first order in 2019 follows them). **All 242 customers dated 2020 or later had already ordered in 2019**, before their "since" date |

## How the verdicts were set

A bar was fixed before looking at the results: a field is **usable** if at least 95% of customers are within tolerance (30 days for the dates, 10% for value) **and** the rank correlation with the order-derived value is at least 0.9; **usable with a caveat** if the correlation is at least 0.5; otherwise **unusable**. Every field is below the lowest of these on both measures.

## How the analysis was done

- **Unit and basis:** the customer (500, all with delivered orders). History is rebuilt from the delivered order lines (18,033 orders): first order, last order, order count and revenue before GST. A sensitivity run on all orders gives the same picture (58.6% and 93.4%).
- **Tests:** Spearman correlation with a permutation test (5,000 shuffles) for independence; Kolmogorov–Smirnov against a uniform spread; Kruskal–Wallis with an epsilon-squared effect size by region and by type, Holm-adjusted across six tests. Seed 42.
- **Checks:** 25 pass/fail checks, including a plain-filter recomputation of the history for 50 customers, order and revenue totals reconciled to the sales file, every customer's first order in 2019 and last order in 2024, and the verdicts re-derived from the bar.
- **Reproducibility:** the notebook finds the merged and clean folders itself (or `CADETX_MERGED` and `CADETX_CLEAN`) and asserts that every check passes.

## Data-dictionary rule

| Do not use | Use instead |
|---|---|
| `customer_since` for tenure, cohorts or churn | First order date from the delivered order lines |
| `last_purchase_date` for recency or churn | Last order date from the delivered order lines |
| `total_purchase_value` for value or segmentation | Customer revenue and order count from the order lines |

The three fields stay in the master as reference only. Tenure from the orders starts in 2019, so customers' earlier history cannot be rebuilt.

## Data limits

- **The order history covers 2019 to 2024 only.** All customers first ordered in 2019 and last ordered in 2024, so the orders cannot show who is new, who has left or how long anyone has been a customer.
- **The master fields might describe something other than these orders,** for example business through another channel. Nothing in the data says so, and the dataset has no owner to ask, so the report states that the fields disagree with the orders and treats that as a limit.
- **Very regular patterns.** `customer_since` is spread evenly over ten years and the 2019 and 2024 order years are the same for all 500 customers. Real customer data is rarely this regular. The findings are worded to what the order lines show.
- **Value measured before GST.** Using revenue including GST gives the same rank correlation (−0.09).

## Recommendation

1. Mark all three fields **Unusable** in the data dictionary with the rule above.
2. Build Phase 3 retention, recency and value measures from the order lines, with the 2019 to 2024 window stated.
3. Do not apply any regional or customer-type correction: the gaps do not differ by group.

## Files

| File | Contents |
|---|---|
| `q13_customer_master_dates.ipynb` | The analysis, with every check |
| `validation_report_week06_q13.csv` | 25 pass/fail checks |
| `q13_outputs/` | 6 result tables (customer comparison for all 500 customers, field verdicts, group tests, group medians, since-by-year, year comparison) |
| `q13_charts/` | 4 charts (since gap, year mismatch, last-purchase gap, value against revenue) |
