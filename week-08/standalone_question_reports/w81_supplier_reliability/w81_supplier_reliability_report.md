# W8-1: Which suppliers deliver late or vary most, and how concentrated is purchasing?

**Question.** Using the purchase orders, how do the 8 suppliers differ in on-time delivery, cancellation, lead-time variation and share of spend, and are the differences larger than chance would produce?
**Owner:** Chandrashekhar Deurghare (BI Analyst) · **Week 8** · **Notebook:** `w81_supplier_reliability.ipynb` (29 of 29 checks pass)

## Answer

**The eight suppliers are statistically indistinguishable on timing, cancellation and share of spend.** About 85% of purchase orders arrive on or before the expected date for every supplier (84.2% to 85.3%), about 10% are cancelled (9.4% to 10.3%), and each supplier carries 12.1% to 12.9% of spend. No test comes near significance after adjustment (smallest Holm-adjusted p = 1.0). **What does differ is the contracted lead time (10 to 28 days), and within one supplier it hardly varies (standard deviation about 1.7 days).** No product depends on one supplier. The one real concentration is geographic: all eight suppliers are in China, 62% of spend in East China.

| Measure | Range across the 8 suppliers | Chance test (Holm-adjusted p) |
|---|---|---|
| On-time rate (received on or before expected date) | 84.2% to 85.3% | 1.0 |
| Cancelled POs | 9.4% to 10.3% | 1.0 |
| Average delay | 0.49 to 0.55 days | 1.0 |
| Lead time minus contract | +0.49 to +0.55 days | 1.0 |
| Spread of lead time (SD within supplier) | 1.65 to 1.78 days | 1.0 |
| Share of received spend | 12.1% to 12.9% | n/a (HHI 0.1250, minimum possible 0.125) |

## Evidence

| Finding | Result |
|---|---|
| **Delivery** | Overall 84.9% on time, 15.1% late, 4.5% early. A late PO is late by 1 to 7 days; 8.1% to 9.2% of each supplier's POs are 4 or more days late; the 95th percentile delay is 5 days (5.9 for one supplier) |
| **Lead time** | Mean actual lead time runs from 10.5 days (Qingdao, Guangzhou) to 28.5 days (Tianjin), always about half a day above contract. Within a supplier the 5th to 95th percentile spans about 5 days |
| **Over time** | On-time rate by order year 84.5% to 85.2% (p = 0.95); no trend across the 72 months (p = 0.83) |
| **Critical products** | POs containing a High-criticality line: 84.9% on time against 85.5% for the rest (p = 0.52) |
| **Reliability score** | The master `reliability_score` against observed on-time rate: Spearman -0.44, permutation p = 0.30 (8 suppliers). It does not track delivery and should not stand in for it |
| **Product dependence** | Every one of the 30 products is bought from all 8 suppliers; the largest supplier's share averages 13.3% (maximum 13.9%) against an even 12.5%. 3 of 30 products are above chance before adjustment (about 1.5 expected), none after Holm |
| **Geography and type** | East China 62.4% of spend, South China 24.7%, North China 12.9%; OEM 38.1%, Distributor 37.3%, Local Vendor 24.6% |

## How the analysis was done

- **Unit and basis:** the purchase order (24,000; 21,630 received, 2,370 cancelled), header fields checked constant across each PO's lines. On time means `delivery_delay_days <= 0`; lead time is received minus order date (both recomputed from the dates with no mismatches). Spend is `total_cost` before GST on received POs (₹312.03B).
- **Intervals and tests:** 95% bootstrap intervals over POs (5,000, seed 42); chi-square, Kruskal-Wallis and Levene across suppliers, Holm-adjusted together; Spearman with a 5,000-shuffle permutation p; a multinomial chance test of each product's concentration (2,000 draws).
- **Checks:** 29 pass/fail checks, including on-time rates for three suppliers recomputed with a plain loop, the critical-product flag recomputed on 200 sampled POs, HHI recomputed by loop, and totals reconciled to the merged file.

## Data limits

- **Timing and cancellation only.** There is no quality, defect, price-quote or cost-of-delay field, so "reliable" here means on time and not cancelled.
- **Procurement scale unresolved (Q10).** Purchase spend is about 14 times net sales revenue. Money figures are descriptive and carry the label `PROCUREMENT SCALE - purchase spend is about 14x sales revenue (Q10 unresolved); money figures are descriptive`; rates, shares and lead times do not depend on it.
- **Very regular data.** Delays of exactly zero days for about 80% of POs, and identical rates across suppliers, are rarely seen in real procurement data; the findings are worded to what this data shows.

## Recommendation

1. Do not rank or drop suppliers on reliability: the data cannot tell them apart. Do not use `reliability_score` as a proxy.
2. Treat lead time as the supplier decision that matters for stock: use each supplier's own mean lead time and a within-supplier SD of about 1.7 days (a feed for W8-3 and W8-2).
3. Record geographic concentration (all suppliers in China) as the one structural exposure; the data cannot price it.
4. Re-test with a quality or price field if one becomes available.

## Files

| File | Contents |
|---|---|
| `w81_supplier_reliability.ipynb` | The analysis, with every check |
| `w81_outputs/` | Nine result tables: scorecard, tests, lead-time spread, by year, time and criticality, criticality by supplier, region and type concentration, product concentration, reliability-score check |
| `w81_charts/` | On-time rates with intervals; lead time against contract; largest supplier's share per product |
| `validation_report_week08_w81.csv` | The 29 checks |
