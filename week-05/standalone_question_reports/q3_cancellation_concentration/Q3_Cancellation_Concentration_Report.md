# Q3: Where is cancellation concentrated?

**Question.** 9.8% of orders are cancelled. Is cancellation concentrated by region, customer type, sales channel or product?
**Owner:** Salim Bello Muhammad (BI Analyst) · **Week 5** · **Notebook:** `q3_cancellation_concentration.ipynb` (27 of 27 checks pass)

## Answer

**No. Cancellation is spread evenly. It is not concentrated in any region, customer type, sales channel, payment term, industry, rating, warehouse type, order size or product.** The data cannot say *why* orders are cancelled, because no cancellation-reason field exists.

| Finding | Evidence |
|---|---|
| Size of the problem | 1,967 of 20,000 orders cancelled (9.84%), worth ₹2.49B of ₹25.45B placed (9.78% of value) |
| Segments | Across 12 cuts, the highest and lowest segment rates sit within 0.4 to 1.7 points of each other (month of year is the widest, at 3.8). The largest effect size is Cramér's V = 0.032 (0.1 would be "small") |
| Statistical test | Smallest raw p-value is 0.038 (month of year). After adjusting for the 12 cuts examined it is 0.45, so nothing is significant |
| Products | 30 products tested as "orders containing this product" against the rest. Two raw p-values fall below 0.05 (about 1.5 expected by chance); the smallest adjusted p-value is 0.35 |
| Customers | No customer-level driver: cancellation counts across 500 customers match a constant 9.8% rate (p = 0.84) |
| Cancelled vs delivered orders | Same value (median ₹1.01M vs ₹1.01M, p = 0.53), same number of lines (p = 0.58) |
| Whole scan | Shuffling the cancelled/delivered labels 5,000 times and re-running all 12 cuts finds a smallest p-value as low as the real one (0.038) in 37% of shuffles (family-wise p = 0.37). The real scan is no stronger than chance |
| Largest gap still allowed | For every segment with 1,000+ orders (45 segments), the 95% interval allows at most 2.1 points above the overall rate, so none cancels more than about 12% (typical allowance 0.8 points) |
| Time | 9.1% in 2019 to 10.9% in 2024, a rise of 1.7 points (95% interval 0.2 to 3.1). Equal-years test p = 0.27; trend test p = 0.030. A small upward drift, weak evidence |

## How the analysis was done

- **Unit of analysis: the order** (20,000 rows), because every line of an order carries the same status. A line-level test would count each order about 6.5 times and overstate the evidence.
- **Tests:** chi-square for every cut, with Cramér's V as the effect size and a 95% Wilson interval for every segment rate. All 12 cuts are adjusted together (Holm method), so looking at many cuts does not manufacture a finding.
- **Products:** a product cannot own an order that holds about 6.5 different products, so each product is tested as "orders containing it vs orders without it", with the 30 tests adjusted together. The same is done for the 15 categories.
- **Whole-scan check:** a permutation test shuffles the labels 5,000 times, repeats the 12-cut scan each time and records the smallest p-value. It answers "would a scan this strong appear by chance?" without relying on the Holm adjustment.
- **Base:** corrected Week 2 merged datasets; order value is `total_order_value` (ex-GST).

## How strong is "no concentration"?

A non-significant result only counts if the test could have seen a real gap. At 80% power, a typical segment (about 4,100 orders) would show a gap of about **1.5 points**. The smallest segment (North East, 422 orders) would only show a gap of about **4 points**. So:

- Large concentrations are ruled out for the main cuts. For every segment with 1,000+ orders, the data allows at most about 2.1 points above the overall rate, so none cancels more than about 12%.
- Small gaps, especially for the two small regions (Central and North East, about 420 orders each), cannot be excluded.
- Month of year is the one cut worth a second look: July is the lowest month at 7.4%. Its raw test gives p = 0.038, but after adjusting for 12 cuts it is p = 0.45, and the whole-scan permutation test gives p = 0.37. Treat it as a lead for a later year of data, not a finding.

The 2024 rate (10.9%) is higher than 2019 to 2023 combined (9.6%, p = 0.032), but 2024 was singled out after looking at the data, so this supports a weak trend without proving it. This matches the Week 4 conclusion.

## Data issue found

**All 1,967 cancelled orders still carry a delivery date, with the same lead time as delivered orders** (8.05 vs 8.06 days). A cancelled order should have no delivery. This looks like a system or data-generation artefact. Delivery dates of cancelled orders were therefore not used in any measure.

## Questions for the data owner

1. What does the `Cancelled` status mean in the source system (customer cancelled, credit rejected, stock-out, or a system status)?
2. Why do cancelled orders carry a delivery date with the usual lead time?
3. Is a cancellation reason or cancellation date recorded anywhere?

## Recommendation

Do not target any region, customer type, channel or product for cancellation reduction: the data gives no basis for it. Treat the cancellation rate as a company-wide figure (about 10%), watch the 2024 uptick over 2025, and ask the data owner what `Cancelled` represents before spending effort on causes.

## Note on one check

The detectable-gap check was first written with a threshold of 3 points for the smallest segment and failed (the real figure is 4.1). The threshold was not loosened to pass. Instead, a typical-segment check (under 3 points, actual 1.5) and a smallest-segment check (under 5 points, actual 4.1) are reported separately, and the text above states both numbers.

## Files

| Item | Location |
|---|---|
| Notebook | `q3_cancellation_concentration.ipynb` |
| Validation | `validation_report_week05_q3.csv` (27 checks) |
| Charts | `q3_charts/` (by year, segment rates, by month) |
| Outputs | `q3_outputs/` (segment tests and rates, by year, by month, product and category tests, customer heterogeneity, cancelled vs delivered, detectable gap, whole-scan permutation, ruled-out gaps, rise interval) |

The notebook finds the merged data itself (any folder inside the repository), or set `CADETX_MERGED`. Random seed 42, 5,000 resamples where resampling is used.
