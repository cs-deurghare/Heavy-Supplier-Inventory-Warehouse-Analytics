# W8-4: Do the customers fall into stable, meaningful segments?

**Question.** Phase 3 asks for RFM and segmentation. Built from recency, frequency and value, do the 500 customers form segments that are stable over time, predict later behaviour, show structure beyond chance and differ by region or customer type?
**Owner:** Salim Bello Muhammad (BI Analyst) · **Week 8** · **Notebook:** `w84_customer_segments.ipynb` (22 of 22 checks pass)

## Answer

**Five conventional RFM segments can be drawn, but they describe one end-of-2024 snapshot and nothing more.** Segments built from 2019-2021 and from 2022-2024 agree no better than chance (adjusted Rand index 0.005; 20.4% of customers stayed in the same segment against 21.8% expected by chance), they do not predict 2022-2024 revenue (Holm-adjusted p = 0.61) and k-means finds no more structure than a structureless cloud of the same shape (no k significant). No segment differs by region, customer type or industry segment after adjustment. This agrees with W7-2: customers are alike and past behaviour does not persist. Because every customer ordered in 2019 and 2024, no churn, tenure or lifetime claim is made.

| Segment (end of 2024) | Customers | Share of revenue (95% interval) | Median orders | Median days since last order |
|---|---|---|---|---|
| Champions | 70 (14.0%) | 17.6% (14.0 to 21.3) | 43 | 18 |
| Loyal | 86 (17.2%) | 21.2% (17.4 to 25.1) | 42 | 65.5 |
| Recent | 130 (26.0%) | 23.0% (19.5 to 26.6) | 33 | 15 |
| Slipping | 69 (13.8%) | 12.4% (9.8 to 15.3) | 33 | 46 |
| Quiet | 145 (29.0%) | 25.7% (22.0 to 29.6) | 33 | 100 |

The differences in orders between segments follow from how the segments are defined (frequency and value are part of the rule); they are not an independent finding.

## Evidence

| Test | Result |
|---|---|
| **Stability** (2019-2021 vs 2022-2024 segments) | Adjusted Rand index 0.005, permutation p = 0.09; same segment in both halves 20.4% (chance 21.8%) |
| **Stability of the scores** | Spearman between halves: recency -0.07 (p = 0.14), frequency +0.03, value -0.02; Holm-adjusted p 0.42 to 1.0 |
| **Prediction** | 2019-2021 segment against 2022-2024 orders: Holm-adjusted p = 0.15 (effect size 0.009); against revenue: p = 0.61 (effect size 0.000) |
| **Structure** | k-means, k = 2 to 6, silhouette 0.26 to 0.34 against a 95th-percentile null of 0.28 to 0.35 from structureless clouds that keep each measure's distribution and correlation; no k is significant (smallest Holm-adjusted p = 0.88) |
| **Profile** | Segment by region: raw permutation p = 0.097; by customer type: 0.56; by industry segment: 0.035 raw, Holm-adjusted 0.105. Cramér's V 0.09 to 0.13. Nothing survives adjustment; industry segment is the same weak lead W7-2 found |

## How the analysis was done

- **Basis:** delivered orders (18,033 of 20,000), revenue `line_total` before GST, history 2019 to 2024, 500 customers; recency is days to the end of the window (31 Dec 2024 for the full window and the second half, 31 Dec 2021 for the first). Recency, frequency and value are scored 1 to 5 by rank (100 customers per score).
- **Segments:** Champions (R 4-5, F+M average 4+), Loyal (R 1-3, F+M 4+), Recent (R 4-5, F+M below 4), Slipping (R 3, F+M below 4), Quiet (R 1-2, F+M below 4). Labels are conventional, not findings.
- **Tests:** adjusted Rand index with a 5,000-shuffle permutation null; Spearman with permutation p; Kruskal-Wallis with epsilon-squared; k-means silhouette against 300 Gaussian-copula null clouds per k; chi-square with a 2,000-shuffle permutation p (some region cells have expected counts below 5). Holm within each family. Seed 42.
- **Checks:** 22 pass/fail checks, including recency, frequency and value recomputed with a plain filter for 25 customers, the adjusted Rand index recomputed from the transition matrix by the pair-counting formula, and a check that the null clouds keep each measure's mean, spread and rank correlation.

## Data limits

- **The history is 2019 to 2024 and every customer ordered in both 2019 and 2024.** The data cannot show who is new or who has left; no tenure, churn or lifetime-value claim is made.
- **The data is very regular.** Segments of a population this uniform are ranked slices of a continuous spread, not groups; real customer data would usually show more.
- **Recency is measured to the last date in the order history,** not to today.
- **A first k-means null (a plain multivariate normal) showed apparent structure at k = 3.** A skewed measure raises the silhouette by itself, so the final null keeps each measure's own distribution; with it, nothing is significant.

## Recommendation

1. Use the segments only as a snapshot list for conversations with account managers, not as groups to treat differently.
2. Do not build churn, lifetime-value or targeting models on these segments: they are not stable and do not predict the next period.
3. If more data arrive (customer start dates, more years), repeat the stability test before acting; industry segment is the one lead worth re-testing.

## Files

| File | Contents |
|---|---|
| `w84_customer_segments.ipynb` | The analysis, with every check |
| `w84_outputs/` | Ten result tables: customer segments, segment summary, transition matrix, stability, prediction, k-means structure, profile tests and three profile tables |
| `w84_charts/` | Segment size and revenue share; segment transitions; k-means structure |
| `validation_report_week08_w84.csv` | The 22 checks |
