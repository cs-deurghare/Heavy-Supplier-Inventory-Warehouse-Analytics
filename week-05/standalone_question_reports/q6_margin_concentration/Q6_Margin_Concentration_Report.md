# Q6: Where is margin concentrated?

**Question.** Engine Block EB-600 and Transmission Assembly TA-800 are about 36% of net revenue at below-average margin. Where is margin concentrated, what drags the portfolio margin, and what would a price change do?
**Owner:** Chandrashekhar Deurghare (BI Analyst) · **Week 5** · **Notebook:** `q6_margin_concentration.ipynb` (38 of 38 checks pass)
**Base:** Delivered orders, corrected Week 2 merged datasets. Net revenue = `line_total` (ex-GST); gross profit = quantity × (unit price − unit cost).

## Answer

**Margin is not concentrated in a few products; the drag is.** The two biggest products earn less per rupee than the rest, and together they pull the 21.56% portfolio margin down by about 0.9 points. Over time the portfolio margin does not move.

| Finding | Evidence |
|---|---|
| The two big products | EB-600 and TA-800 are **35.9% of net revenue** (₹8.24B of ₹22.96B) but **31.7% of gross profit**. EB-600: ₹4.857B revenue, ₹959.2M gross profit, margin 19.75%. TA-800: ₹3.388B revenue, ₹608.6M gross profit, margin 17.96% |
| The rest of the portfolio | The other 28 products earn **22.99%**, against 21.56% overall |
| Size of the drag | Contribution to the portfolio margin gap (revenue share × margin difference): TA-800 −0.53 points, EB-600 −0.38, Turbocharger TB-900 −0.28, Track Chain TC-45 −0.23. Together EB-600 and TA-800 take 0.91 points off. Had both earned the portfolio margin, gross profit would be **₹210M higher (4.2%)** |
| Who lifts it | Idler Wheel IW-55 (+0.17), Fuel Pump FP-350 (+0.14), Wheel Rim WR-24 (+0.12), Boom Cylinder BC-400 (+0.12). All small |
| Concentration | Revenue is concentrated (top 2 = 35.9% against 6.7% if equal; Gini 0.63) and gross profit is less so (top 2 = 31.7%; Gini 0.58). Across the 30 products, revenue and margin move in opposite directions (Spearman −0.94); price and margin do too (−0.93): the expensive heavy components carry the thinnest margins |
| Margin range | 17.2% (Turbocharger) to 45.8% by product. Categories: Transmission 17.96%, Engine 20.13%, Hydraulic 22.64%, up to 41.9% for the tiny Lubricants line |
| Over time | Portfolio margin runs 21.52% to 21.58% across 2019 to 2024, a spread of 0.06 points that shuffled year labels beat (permutation p = 0.84). Each product's margin is fixed by the price list, so only mix could move it, and it hardly does |
| The 2024 fall in EB-600 | EB-600 fell ₹71.3M from 2023 to 2024 (49% of the total fall of ₹146.7M), the largest of the 30 product changes. But a scan of 30 products with shuffled year labels produces a largest change of about ₹50M typically, and ₹71.3M or more in 25% of shuffles (p = 0.25). The 95% interval for EB-600 runs from −₹174M to +₹30M. It was picked after looking, so it is **not established** |

## Scenario: a price change on EB-600 and TA-800 (not evidence)

Volume held constant, unit cost unchanged, effect on six years of Delivered gross profit. **This is arithmetic, not a forecast**: the data holds one price list and no price history, so how customers would respond cannot be measured.

| Price change | EB-600 uplift | TA-800 uplift | Break-even volume loss (EB-600 / TA-800) |
|---|---|---|---|
| +1% | ₹48.6M (+5.1% of its gross profit) | ₹33.9M (+5.6%) | 4.8% / 5.3% |
| +2% | ₹97.1M (+10.1%) | ₹67.8M (+11.1%) | 9.2% / 10.0% |
| +3% | ₹145.7M (+15.2%) | ₹101.6M (+16.7%) | 13.2% / 14.3% |

The break-even volume loss is how much volume could fall before the price rise stops paying. A 3% rise on both would add about ₹247M, 5.0% of gross profit, if no volume were lost. The data does not say how much would be lost, so **no pricing recommendation follows from it**.

## Data issue found

The product master's `margin_percentage` is a **markup on cost**, not a margin on price, for 29 of 30 products (EB-600: master 24.6%, actual margin on price 19.75%). One product, Engine Oil Filter OF-90, is inconsistent with both bases (master 37.3%, markup 60.0%, margin on price 37.5%). Always use gross profit ÷ revenue for margin, never the master field.

## Questions for the data owner

1. Is there a price history, list-price change or discount record? Every line carries the master price for all six years.
2. Is `margin_percentage` meant to be a margin on price or a markup on cost, and is the OF-90 value an error?
3. Is `unit_cost` a standard cost or the actual purchase cost? It is a single value per product for six years, so cost changes cannot be seen.

## Recommendation

Treat EB-600 and TA-800 as the portfolio's margin drag (about 0.9 points, ₹210M against the portfolio margin), and look at supplier cost and price list for those two first. Do not claim a price rise would pay: the break-even volume losses above are the only thing the data supports. Do not describe the 2024 EB-600 fall as established.

## Notes on method

- **Contribution to the margin gap** = revenue share × (product margin − portfolio margin). The 30 values (and the 15 category values) sum to exactly zero, which is checked.
- **No sampling error on margins.** One unit price and one unit cost per product for six years (checked on every line), so a product's margin is exact, not an estimate.
- **2024 scan.** Order labels (2023 or 2024) are shuffled 5,000 times (seed 42) and the largest absolute product change recorded each time. EB-600 and total intervals are order-level bootstrap intervals (5,000 resamples).
- **Mix test.** Year labels are shuffled across orders 5,000 times and the best-to-worst yearly margin spread recorded.
- **Corrections to the first version of Q6.** The earlier package gave the what-if uplift as ₹4.86M for +1% on EB-600; the correct figure is ₹48.57M (1% of ₹4.857B), so every uplift figure was ten times too small and the base gross profit was shown as ₹95.9M instead of ₹959.2M. It also read a superseded dataset path, used typed-in tables, wrote empty CSV files and used static checks. All of that is replaced here. The "low-risk 1% to 2% price adjustments" recommendation was dropped because the data cannot support it.
- **First check that failed.** The first version of the master-margin check said the field matched the markup for all 30 products; it matches 29 (OF-90 is the exception). The claim and check were corrected, not loosened silently.

## Files

| Item | Location |
|---|---|
| Notebook | `q6_margin_concentration.ipynb` |
| Validation | `validation_report_week05_q6.csv` (38 checks) |
| Charts | `q6_charts/` (margin by product, contribution to the margin gap, price scenario) |
| Outputs | `q6_outputs/` (product table, category table, concentration, yearly margin and mix, mix permutation, 2023 to 2024 change by product, EB-600 tests, price scenario, master margin definition) |

The notebook finds the merged data itself (any folder inside the repository), or set `CADETX_MERGED`.
