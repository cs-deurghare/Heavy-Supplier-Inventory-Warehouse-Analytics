# W7-3: Which products, branches and stock pairs need attention first?

**Question.** Which products, branches and stock pairs should the team look at first? A one-page pack: the 10 class A products with revenue, price and margin; a branch table with orders a month and intervals; the 72 at-risk stock pairs by category.
**Owner:** Chandrashekhar Deurghare (BI Analyst) · **Week 7** · corrected version · **Notebook:** `w73_priority_pack.ipynb` (26 of 26 checks pass)

> **Stock results rest on one assumption: sales scale assumed (Q10 unresolved).** The product and branch tables use sales data only and do not depend on it.

## Answer

**Look first at four low-margin class A products, at the Sensors and Seals stock, and treat the branch ranking as real but about order count, not order size.**

1. **Ten products make 81.5% of revenue, and four of them earn less than the 21.56% portfolio margin:** Engine Block EB-600 (19.75%), Transmission Assembly TA-800 (17.96%), Track Chain TC-45 (18.34%) and Turbocharger TB-900 (17.19%). Measured against the portfolio margin, they give up about ₹122M (TA-800), ₹88M (EB-600), ₹64M (TB-900) and ₹52M (TC-45) of gross profit. These are the only four of the 30 products below the portfolio margin.
2. **Branches differ in order count, not order size.** Chennai handles 51.1 delivered orders a month and Hyderabad 34.4 (1.48 times); units per order are 67.6 to 69.1 everywhere.
3. **72 of 180 product-branch pairs fall under a 95% fill rate with the existing reorder levels.** Sensors (5 of 6 pairs) and Seals (9 of 12) are the worst categories; Brakes, Cooling, Lubricants, Pins & Bushes and Transmission have 3 of 6. The weakest single pair is P027 at Chennai (72.2% filled).

## 1. The 10 class A products

| Product | Category | Revenue (₹M) | Share | List price (₹) | Realised margin | Against portfolio (21.56%) |
|---|---|---:|---:|---:|---:|---:|
| P015 Engine Block EB-600 | Engine | 4,857 | 21.2% | 119,000 | **19.75%** | −1.81 pts |
| P014 Transmission Assembly TA-800 | Transmission | 3,388 | 14.8% | 83,500 | **17.96%** | −3.60 pts |
| P021 Boom Cylinder BC-400 | Hydraulic | 1,934 | 8.4% | 46,200 | 22.94% | +1.38 |
| P019 Swing Motor SWM-350 | Hydraulic | 1,653 | 7.2% | 39,800 | 21.61% | +0.05 |
| P004 Track Chain TC-45 | Undercarriage | 1,627 | 7.1% | 39,800 | **18.34%** | −3.22 |
| P010 Turbocharger TB-900 | Engine | 1,476 | 6.4% | 34,900 | **17.19%** | −4.37 |
| P011 Hydraulic Cylinder HC-200 | Hydraulic | 1,162 | 5.1% | 27,600 | 22.10% | +0.54 |
| P001 Hydraulic Pump HP-300 | Hydraulic | 1,012 | 4.4% | 24,500 | 22.65% | +1.09 |
| P030 Fuel Pump FP-350 | Engine | 911 | 4.0% | 21,900 | 25.11% | +3.55 |
| P022 Control Valve CV-75 | Hydraulic | 698 | 3.0% | 16,900 | 24.26% | +2.70 |
| **Class A** | | **18,718** | **81.5%** | | **20.33%** | −1.23 |

- **Class A** uses the Week 6 convention (rank by revenue, A while the share before the product is under 80%) and is the same ten products as Week 6. Revenue is before GST on delivered orders; margin is realised, `(line_total − quantity × unit_cost) ÷ line_total`, from the order lines.
- **Price decides the class** (Week 6): the ten products sell about the same units, so the expensive ones are class A, and expensive products earn lower margins.
- **"Gross profit given up"** is `(portfolio margin − product margin) × revenue`. It is an accounting comparison, not a forecast of what a price or cost change would earn. Whether a margin gap is a cost or a price effect cannot be separated here: every order line carries the product-master price (Q1).

## 2. Branch table

| Branch | Orders a month (95% interval) | Units per order | Share of orders |
|---|---:|---:|---:|
| Chennai South Hub | 51.1 (49.1 to 53.1) | 69.1 | 20.4% |
| Kolkata East Depot | 47.4 (45.7 to 49.1) | 67.6 | 18.9% |
| Ahmedabad West Hub | 43.3 (41.6 to 44.9) | 68.8 | 17.3% |
| Delhi Central | 37.2 (36.0 to 38.6) | 69.1 | 14.9% |
| Pune Distribution | 37.1 (35.6 to 38.4) | 68.1 | 14.8% |
| Hyderabad Logistics | 34.4 (33.1 to 35.7) | 68.2 | 13.7% |

Interval: bootstrap over 72 months (5,000 resamples, seed 42). Chennai, Kolkata and Ahmedabad are clearly separated from the rest; **Delhi and Pune cannot be told apart.** "Throughput" means delivered orders and units sold; the data has no capacity or timing records.

## 3. At-risk stock pairs (sales scale assumed, Q10 unresolved)

The 72 pairs are those the Week 6 stock package marks **At risk** (fill rate under 95% with the existing `reorder_level` and `max_stock`). Together they leave 11.6% of their demand unmet.

| Category | Pairs | At risk | Share at risk |
|---|---:|---:|---:|
| Sensors | 6 | 5 | 83% |
| Seals | 12 | 9 | 75% |
| Brakes, Cooling, Lubricants, Pins & Bushes, Transmission | 6 each | 3 each | 50% |
| Engine | 24 | 11 | 46% |
| Undercarriage | 24 | 9 | 38% |
| Filters | 12 | 4 | 33% |
| Attachments, Belts, Cabin | 6 each | 2 each | 33% |
| Electrical | 18 | 5 | 28% |
| Hydraulic | 36 | 8 | 22% |

The full list (pair, product, branch, fill rate, unmet demand, stockout days, cover) is in `w73_outputs/w73_at_risk_stock_pairs.csv`, every row labelled. The risk comes from daily demand variation, not from a lack of average stock (Week 6). Small categories (Sensors, Seals) have few pairs, so read the share with care.

## How the analysis was done

- **Basis:** 18,033 delivered orders, ₹22.96B revenue, ₹4.95B gross profit. Nothing in the pack is estimated: margins come from `unit_cost` on the order lines.
- **At-risk list:** read from `week-06/.../stock_outputs/stock_kpis_by_pair.csv` and checked: 180 pairs, 72 with fill rate under 95%, the category counts equal the Week 6 category table (15 of 15), and demand equals the ledger total (1,124,832).
- **Checks:** 26, all computed from the data, with exact values (no tolerance on revenue or order counts).
- **Reproducibility:** the notebook finds the merged data and the Week 6 stock outputs itself (or `CADETX_MERGED` and `CADETX_WEEK6_STOCK`) and asserts that every check passes.

## Recommendation

1. Review the four class A products below the portfolio margin, TA-800 first, as a cost and price question for the business. The data can show the gap but not its cause.
2. Start the stock review with Sensors and Seals, then the categories at 50%. Quote every stock figure with the sales-scale sentence.
3. Do not read branch differences as capacity or speed.

## Files

| File | Contents |
|---|---|
| `w73_priority_pack.ipynb` | The analysis, with every check |
| `validation_report_week07_w73.csv` | 26 pass/fail checks |
| `w73_outputs/` | 5 tables (class A pack, branch table, 72 at-risk pairs, at-risk by category, margin for all 30 products) |
| `w73_charts/` | 3 charts (class A revenue and margin, branch orders with intervals, at-risk pairs by category) |
