# Q4 follow-up: Why is most of the outstanding money over a year old?

**Question.** Week 3 found ₹5.80B outstanding on reliable invoices, 86% of it more than 365 days past due, with no customer type or region standing out. Why is the money so old? Whether it will be collected is not tested, because the data has no collection records.
**Owner:** Salim Bello Muhammad (BI Analyst) · **Week 6** · **Notebook:** `q4_payment_followup.ipynb` (43 of 43 checks pass)

## Answer

**The money is old because the invoices are old, and nothing in the data shows a late payment ever closing an old invoice.** About 20% of the value due in every full year (2019 to 2024) is still open, so the age of the outstanding balance simply mirrors the age of the invoiced value. The data cannot say whether the money *will* be collected, because it holds no collection, dispute, credit-note or write-off records.

| Finding | Evidence |
|---|---|
| Open share is the same for every due year | 19.6% to 21.1% of invoiced value is open in each year 2019 to 2024. Chi-square p = 0.82 (Cramér's V 0.011); no downward trend (p = 0.77); 2024 minus 2019 is +0.78 points, 95% interval −1.61 to +3.10 |
| The age mix mirrors the invoices | 85.3% of invoiced value fell due more than 365 days before the as-of date; 86.0% of outstanding value is more than 365 days past due. The gap is +0.65 points (95% interval −0.57 to +1.69) |
| Payments never arrive very late | The latest payment in the data came 75 days after the due date (full settlements: 45 days). 5,274 open invoices, worth ₹5.71B (98% of outstanding), are now past that point and have no precedent of closing |
| Older invoices are not collected more | Among invoices past the 75-day window, the share still open is 28.9% to 30.8% at every age band (76–180, 181–365, 366–730, over 730 days) |
| Open balances split evenly | ₹2.92B on 1,798 unpaid invoices and ₹2.89B on 3,578 partly paid ones. Partly paid invoices were paid between 20% and 80%, spread evenly (Kolmogorov–Smirnov p = 0.76), with no link to age (Spearman ρ = +0.003) |
| Nobody stands out | Six cuts (payment terms, customer type, customer region, industry segment, sales channel, branch region): smallest raw p = 0.056, smallest Holm-adjusted p = 0.34, largest Cramér's V = 0.021. Open value share is 18.6% to 22.1% in every segment |
| Customers are spread as chance would give | Spread of customer open share is 7.27 points against 7.61 expected by chance (p = 0.92); the 50 customers owing most hold 18.4% of outstanding against 18.7% by chance (p = 0.75) |
| Payment terms make no practical difference | `Advance` invoices, which should be paid before delivery, are open 29.3% of the time against 30.8% for the other terms (p = 0.07) |

## How the analysis was done

- **Unit of analysis:** the invoice. 17,640 invoices have a unique `invoice_id`, so their payments can be attributed. The 393 repeated-ID invoices (₹654M including GST, open issue UI-01) are set aside, as in Week 3.
- **Definitions (same as Week 3):** outstanding = invoice total including GST minus total paid; days past due = as-of date minus due date; as-of date = 2025-03-14, the latest due date in the data.
- **Steps:** (1) open share by due year, tested with chi-square and a Cochran–Armitage trend test, plus a bootstrap interval for the 2024 against 2019 difference; (2) a comparison of the age mix of outstanding value with the age mix of invoiced value; (3) the distance from the due date to the last payment, and the open share by age among invoices past the 75-day window; (4) the make-up of open balances; (5) six cuts tested together (Holm adjustment) and a customer-clustering permutation test; (6) a labelled exposure range.
- **Reproducibility:** seed 42, 5,000 permutations and bootstrap resamples (1,000 for the age-mix interval); the notebook finds the merged data itself and asserts that every check passes.

## How strong is "the open share does not fall with age"?

If late payments eventually closed old invoices, the open share would be lower for 2019 than for 2024. The 2024 minus 2019 difference is +0.78 points with an interval of −1.61 to +3.10, so a fall larger than about 1.6 points is ruled out. The trend test points the same way (p = 0.77). The result also holds when the comparison is restricted to invoices past the 75-day window (28.9% to 30.8% open at every age).

## Exposure range (scenario, not forecast)

The balances past the 75-day window total ₹5.71B. If part of them were never collected:

| Never collected, share of past-75-day balances | Exposure | Share of outstanding | Share of invoiced value (₹28.60B) |
|---:|---:|---:|---:|
| 25% | ₹1.43B | 24.6% | 5.0% |
| 50% | ₹2.85B | 49.2% | 10.0% |
| 75% | ₹4.28B | 73.8% | 15.0% |
| 100% | ₹5.71B | 98.4% | 20.0% |

The table is a planning range. It is not a prediction, because the data does not say how much of this money the business has already written off or recovered outside the invoice records.

## Data limits

- **No collection, dispute, credit-note or write-off records.** The data shows that old invoices have not been paid, not whether the business expects to collect them. Any claim about collectability needs that information.
- **As-of date is the latest due date in the data (2025-03-14), not today.** Ageing is relative to that date.
- **Very regular payment patterns.** Partly paid invoices were paid between exactly 20% and 80%, spread evenly, and the open share is about the same in every year. Real collections rarely look this regular. The findings above are worded to what the invoices show, and the pattern is noted here as a limit.
- **Paid-in-advance invoices.** Invoices with `Advance` terms are open about as often as the others, so the payment terms do not appear to be reflected in payment behaviour.
- **Repeated invoice IDs (UI-01).** 393 invoices (₹654M) cannot be matched to payments and are excluded; their share of invoice value is 2.2%.

## Recommendation

1. Describe the 86% as an age effect, not a growing backlog: a steady ~20% of each year's invoiced value has stayed open, and the share does not fall with age.
2. Treat the ₹5.71B past the 75-day window as the exposure to plan around, using the range above, until collection or write-off information is available.
3. Do not rank customers, regions or terms for credit risk from this data: none stands out.
4. Record the limits above in the project data dictionary and carry them into Phase 3 retention and churn work.

## Files

| File | Contents |
|---|---|
| `q4_payment_followup.ipynb` | The analysis, with every check |
| `validation_report_week06_q4.csv` | 43 pass/fail checks |
| `q4_outputs/` | 12 result tables (due year, age mix, lateness, window-closed, composition, partial payments, segment tests and rates, customer open share, customer clustering test, exposure range, due-year tests) |
| `q4_charts/` | 4 charts (open share by due year, payment lateness, age mix, customer clustering) |
