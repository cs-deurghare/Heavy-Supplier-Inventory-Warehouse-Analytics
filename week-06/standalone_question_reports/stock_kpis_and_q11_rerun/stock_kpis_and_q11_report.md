# Stock KPIs and the Q11 replenishment comparison on the agreed sales scale

**Question.** On the working scale the team agreed (sales scale; Q10 unresolved), what do turnover, days of cover and stock health look like, and which replenishment trigger fits the demand? What changes if the sales scale is not the right reference?
**Owners:** Ibrahim Khalil Umar, with Abdibasid Mohamed Ali · **Week 6** · **Notebook:** `stock_kpis_and_q11_rerun.ipynb` (23 of 23 checks pass)

> **Every figure below rests on one assumption: that the sales scale is the right reference for stock.** Purchase receipts are 18.13 times units sold and nothing in the data explains it. See `stock_scale_note.md`. Do not quote any result here without that sentence.

## Answer

**On the working scale the existing reorder levels are not tied to demand: they fill 94.3% of demand and leave 72 of 180 product-branch pairs below a 95% fill. A trigger based on each pair's own demand and lead time fills 98.9% to 99.8% for 12% to 32% more stock value. Recorded `current_stock` cannot be used at all.**

| Working-scale KPI (existing policy) | Value |
|---|---|
| Average stock held | 152 units per pair; **₹392.6M** at cost |
| Cost of units sold per year | ₹2,718.8M |
| Portfolio turnover | **6.9 times a year** |
| Median days of cover | **52.6 days** (median lead time 18 days) |
| Pairs whose average cover is below their lead time | 4 of 180 |
| Stock health (bar: fill rate under 95% = at risk) | **72 at risk, 108 adequate** |

| Policy (working scale) | Fill rate | Share of pair-days out of stock | Average on hand per pair | Average stock value | Orders | Pairs below 95% |
|---|---|---|---|---|---|---|
| **A existing** (`reorder_level`, `max_stock`) | 94.3% | 1.40% | 152 | ₹392.6M | 4,457 | 72 |
| B, 90% service | 98.9% | 0.28% | 170 | ₹441.4M | 4,804 | 0 |
| B, 95% service | 99.4% | 0.16% | 180 | ₹468.3M | 4,839 | 0 |
| B, 99% service | 99.8% | 0.05% | 200 | ₹519.1M | 4,872 | 0 |

**Reading it.**
- Under policy A about 5.7% of demand goes unmet. Policy B at 95% service cuts that to 0.6% for ₹75.7M (19%) more average stock at cost. The existing levels were set independently of each pair's demand and lead time (Week 5: correlation 0.09 with the demand-based point).
- Average cover is wide (13 to 119 days); cover is above lead time for 176 of 180 pairs, so the at-risk pairs are caused by variation in daily demand, not by a lack of average stock.
- At-risk pairs by category: Seals 9 of 12, Sensors 5 of 6, Engine 11 of 24, Undercarriage 9 of 24, Hydraulic 8 of 36 (`stock_kpis_by_category.csv`). Stock value sits in Engine (₹120.8M), Hydraulic (₹119.9M) and Transmission (₹62.1M).
- These results reproduce the Week 5 labelled scenario exactly (fill rate, orders and pairs below 95% for all four policies). The new part is the KPIs, the sensitivity and the labelling as the agreed working result.

## Sensitivity: if the sales scale is not the right reference

| Case | Result |
|---|---|
| Recorded `current_stock` taken at face value | Median **38,272 days** of cover (more than 100 years); turnover 0.01 a year; every pair is above `max_stock` (about 350 times the median threshold) |
| Purchase scale taken as true (demand multiplied by 18.13, stored thresholds kept) | Existing thresholds fill **23.8%** of demand, with all 180 pairs below 95% and median cover 1.4 days |

The thresholds in `inventory_master` fit the sales scale and not the recorded stock. If a corrected purchase scale were ever confirmed, every KPI here would have to be rebuilt on it.

## How the analysis was done

- **Unit:** the product-branch pair (180). Daily demand is the ledger `OUT` per pair per day over 6.03 years; the ledger holds 91.1% of delivered sales units.
- **Lead time:** mean actual lead time of received purchase-order lines for the pair (17 to 19 days), held constant.
- **Simulation:** daily review; when on hand plus on order is at or below `s`, order up to `S`; lost sales; start stock = `opening_stock`. Policy B's `s` = mean lead-time demand + z × demand SD × √lead time, with `S = s + (max_stock − reorder_level)`.
- **KPIs:** turnover = units sold per year ÷ average on hand (value version at unit cost); cover = average on hand ÷ mean daily demand; health bar fixed in advance.
- **Checks:** 23, including the Week 5 figures reproduced for all four policies, a plain day-by-day re-implementation matching on five pairs, the KPIs recomputed by hand, and the sensitivity cases.
- **Reproducibility:** the notebook finds the merged data itself (or `CADETX_MERGED`) and asserts that every check passes.

## Data limits

- **The scale is an assumption, not a finding.** Nothing in the data confirms that sales or purchases are on the right scale; the choice rests on the stored thresholds fitting monthly sales.
- **No holding cost, ordering cost or service target.** The data cannot say which policy "minimises carrying cost without stockouts"; stock value at cost is only a proxy.
- **Constant lead time, one historical path.** Lead-time variation, backorders and forecast error are not modelled. Results are not forecasts.
- **Ledger covers about 91% of delivered units,** so demand is slightly understated.
- **Very regular patterns** (even lead times, level demand): findings are worded to what the lines show.

## Recommendation

1. Report stock KPIs only on the working scale, each with the assumption sentence above, and never quote recorded `current_stock`.
2. Treat the 72 at-risk pairs as the list to review first; start with Seals and Sensors.
3. Ask the business whether reorder levels are meant to follow demand and lead time; a demand-based trigger would raise service at the stated stock cost.
4. Rebuild everything if a corrected purchase scale ever becomes available.

## Files

| File | Contents |
|---|---|
| `stock_kpis_and_q11_rerun.ipynb` | The analysis, with every check |
| `validation_report_week06_stock.csv` | 23 pass/fail checks |
| `stock_outputs/` | 8 tables (scale gate, KPIs by pair, portfolio and category, policy results and summary, two sensitivity tables) |
| `stock_charts/` | 3 charts (fill rate by policy, days of cover, recorded against working cover) |
