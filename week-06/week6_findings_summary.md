# Week 6 findings summary

Four packages were completed on the corrected Week 2 merged datasets (delivered orders, 18,033 of 20,000): the Q4 payment follow-up, the Phase 2 coverage items, Q13, and the stock KPIs with the Q11 rerun on the agreed sales scale. Each has its own folder in `standalone_question_reports/` with a notebook, outputs, charts, report and validation file. All 134 checks pass (`validation_report_week06.csv`). The working assumption for stock is in `stock_scale_note.md`.

## Answers

| Q | Question | Answer | Strength |
|---|---|---|---|
| **Q4 follow-up** | Why is most of the outstanding money over a year old? | **Because the invoices are old.** About 20% of the value due in every full year (2019 to 2024) is still open (chi-square p = 0.82, no downward trend p = 0.77), so the 86% of outstanding more than a year past due mirrors the 85% of invoiced value that fell due over a year ago. No payment in the data arrives more than 75 days after the due date; the 5,274 open invoices past that point (₹5.71B, 98% of outstanding) have no precedent of closing. No customer type, region, term, channel or customer stands out (smallest Holm-adjusted p = 0.34). Exposure range if 25% to 100% of those balances were never collected: ₹1.43B to ₹5.71B (5.0% to 20.0% of invoiced value). The data has no collection or write-off records, so whether the money will be collected is not tested. | Strong (age pattern); scenario only (exposure) |
| **Coverage: ABC** | Which products matter most? | **Ten products (class A) make 81.5% of revenue** (B: 7 products, 14.1%; C: 13 products, 4.4%). Classes follow unit price (Spearman +1.00), not volume (+0.17); class A has the lowest gross margin (20.3% against 31.8% in class C). The classes are identical in 2019 to 2021 and 2022 to 2024 (kappa 1.00). | Strong |
| **Coverage: movers** | Which products are fast or slow? | **None.** Monthly volumes run from 548 to 593 units, only 8.1% apart, and are equal within chance (Kruskal-Wallis p = 0.62; chance-label test p = 0.45); the ranking does not hold across periods (rho −0.09). No fast or slow labels are given. | Strong |
| **Coverage: branches** | How busy is each branch? | **Branches differ in how many orders they handle, not in order size.** Orders a month: Chennai 51.1, Kolkata 47.4, Ahmedabad 43.3, Delhi 37.2, Pune 37.1, Hyderabad 34.4 (effect size 0.44). Units per order are equal (67.6 to 69.1, p = 0.57). No branch trends up or down. The data holds no capacity or timing records, so throughput means orders and units sold. | Strong |
| **Coverage: forecast readiness** | Which series can be forecast in Phase 3? | **All 40 monthly series** (totals, 30 products, 6 branches) are ready for a simple level forecast: no trend after Holm adjustment, no seasonality once months are put on a per-day basis, and no method beats the plain average in a rolling back-test (1 of 144 comparisons against 3.6 expected by chance). Prediction intervals: about ±16% for totals, ±31% for branches, ±33% for products. | Strong |
| **Q13** | Are the customer master dates maintained? | **No.** `customer_since` is after the first order for 58.4% of customers; `last_purchase_date` is earlier than the last order for 93.0%; `total_purchase_value` is 5.4% of delivered revenue with no customer within 10%. Rank correlations with the order-derived values are −0.04, −0.01 and −0.09. The gaps do not differ by region or customer type (smallest Holm-adjusted p = 0.75). All three fields are **Unusable**: tenure, recency and value must come from the order lines. | Strong |
| **Stock KPIs and Q11 rerun** | On the agreed sales scale, which replenishment trigger fits, and what are the stock KPIs? | **The existing reorder levels are not tied to demand.** Policy A fills 94.3% of demand with 72 of 180 pairs below a 95% fill; stock KPIs: average stock ₹392.6M, turnover 6.9 a year, median cover 52.6 days against an 18-day lead time. A demand-based trigger fills 98.9% to 99.8% for 12% to 32% more stock value (95% service: 99.4%, ₹468.3M). Recorded `current_stock` gives 38,272 days of cover and cannot be used; at the purchase scale the stored thresholds would fill only 23.8%. **Every figure rests on the sales-scale assumption** (Q10 unresolved). No holding or ordering cost exists, so no policy is called cost-optimal. | Labelled working result; sensitivity shown |

## Corrections made during the week

- **Q4 title and wording** promised an answer on collectability that the data cannot give. Title, question and notebook introduction now state that collectability is not tested (raised on the Week 6 plan slides by Chandrashekhar).
- **Q4 check 8 description** now states the real counts (75 overpaid and 92 short by exactly 0.01).
- **"Data owner" wording** in Weeks 3 to 5 reports replaced: the dataset is supplied with the programme, so open items are called data limits, and the Q11 question pack is marked not applicable for sending.
- **Q13 first version** was replaced by a rebuilt package (25 checks, a verdict bar fixed in advance, group tests with Holm adjustment).
- **Movers:** a bootstrap interval rule alone labels one product Fast and one Slow; with 30 products about 0.75 of each are expected by chance, so no label is given.

## Data issues carried forward

1. **Order history covers 2019 to 2024 only**, and every customer first ordered in 2019 and last ordered in 2024, so the orders cannot show who is new or who has left.
2. **The data is very regular** (product volumes within 8%, identical ABC classes in both periods, no seasonality, `customer_since` spread evenly over ten years). Findings are worded to what the lines show.
3. **No capacity, staffing or timing data** exist for branch throughput claims.
4. **Stock scale (Q10)** remains an agreed working assumption (sales scale), not a resolved fact; all stock results are labelled accordingly.
