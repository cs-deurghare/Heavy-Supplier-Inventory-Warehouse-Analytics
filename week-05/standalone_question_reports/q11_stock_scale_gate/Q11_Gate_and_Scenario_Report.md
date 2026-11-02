# Week 5 · Q11 — Which replenishment policy fits? Gate and labelled scenario

**Owners:** Ibrahim Khalil Umar, with Abdibasid Mohamed Ali
**Notebook:** `05_q11_stock_scale_gate_and_scenario.ipynb` · **Validation:** 16 of 16 checks pass (`validation_report_week05_q11.csv`)
**Status:** **Blocked by Q10 for reportable stock KPIs.** Nothing below is a stock finding. The scenario is labelled `SCENARIO — sales-side scale assumed; not a reportable stock KPI` in every output file.

## 1. Gate — the Q10 block still holds
| Measure | Value |
|---|---|
| Ledger `IN` units / `OUT` units | **18.13×** |
| Median sales per pair per month | 84.3 units |
| Median purchase receipts per pair per month | 1,573 units |
| Median `max_stock` / `reorder_level` / `safety_stock` | 310.5 / 62 / 43.5 |
| Median `current_stock` | 107,790 (about 350× `max_stock`: the median of per-pair ratios is 349×, the ratio of the two medians is 347×) |

Monthly sales sit on the same scale as the thresholds; purchase receipts and `current_stock` do not.

**Why 84.3 here and about 95 in Week 4?** Two separate reasons, both checked in the notebook (`q11_demand_bridge_week4_vs_ledger.csv`):

| Step | Units per pair per month |
|---|---|
| Ledger `OUT`, median per pair (this report) | 84.3 |
| Delivered sales lines, median per pair, same period | 92.7 |
| Delivered sales lines, **mean** per pair (Week 4 style) | 94.8 |

The ledger holds 91.1% of delivered units and lines (107,165 of 117,656), and 84.3 ÷ 0.911 = 92.6, which matches the delivered-lines median. The remaining step is mean against median. The difference is therefore fully explained, and the scale conclusion does not change.

Until the data owner explains the purchase-order quantities, turnover, days of cover, stock-health classes and a replenishment policy **cannot be reported**.

## 2. Scenario — what the existing thresholds do against real demand
**Assumptions (all stated, none tested against the owner):** demand = ledger `OUT` per pair per day; lead time = mean actual lead time of received purchase-order lines per pair (17 to 19 days); lost sales when out of stock (no backorder); daily review; order-up-to policy; start stock = `opening_stock`. Purchase quantities and `current_stock` are not used.

- **Policy A (existing):** order up to `max_stock` when inventory position ≤ `reorder_level`.
- **Policy B (scenario):** the trigger is a demand-based reorder point (mean demand × lead time + z × demand SD × √lead time); the order-up-to level is that trigger plus the existing gap (`max_stock − reorder_level`), so each order is the same size as under A.

| Policy | Fill rate | Share of pair-days out of stock | Avg on-hand per pair (units) | Avg on-hand value at cost (₹M) | Orders placed | Pairs with fill < 95% |
|---|---|---|---|---|---|---|
| **A existing** | 94.3% | 1.40% | 152 | 392.6 | 4,457 | 72 |
| B, 90% service | 98.9% | 0.28% | 170 | 441.4 | 4,804 | 0 |
| B, 95% service | 99.4% | 0.16% | 180 | 468.3 | 4,839 | 0 |
| B, 99% service | 99.8% | 0.05% | 200 | 519.1 | 4,872 | 0 |

> **Do not quote these figures outside this labelled scenario.** Results such as "5.7% of demand lost" depend on three assumptions: lost sales with no backorder, `opening_stock` as the starting stock, and a constant lead time with no variability.

**Reading it.**
- The existing `reorder_level` is **not tied to each pair's demand or lead time**: its correlation with the demand-based reorder point is 0.09. It does track `safety_stock` (0.92).
- The existing level covers the *mean* demand during lead time for 114 of 180 pairs, but the 95% reorder point for only 23.
- Under these assumptions the existing thresholds lose about **5.7% of demand**. A demand-based trigger at 95% service cuts that to about **0.6%**, at the cost of about **19% more average stock value** (₹468M against ₹393M at unit cost).

## 3. What this does and does not support
- It supports a **question for the business**, not a recommendation: the reorder levels in `inventory_master` look set independently of demand and lead time, and a demand-based trigger would raise service at a stated stock cost.
- It does **not** identify the policy that "minimises carrying cost without stockouts". The data holds **no holding-cost rate, ordering cost or service target**, so carrying cost cannot be priced; stock value at cost is only a proxy.
- Lead time is the pair mean (17 to 19 days, no variability), demand comes from the ledger (about 91% of delivered lines), and results are one historical path, not a forecast.
- If the data owner confirms a corrected purchase scale, the stock KPIs must be rebuilt first and this scenario re-run on the corrected balances.

## 4. Decision requested from the team
1. Send the data-owner pack (`Data_Owner_Question_Pack.md`).
2. Agree that the scenario stays in the notebook and this report, **labelled**, and is not quoted in the findings summary as a stock result.

## Files
`05_q11_stock_scale_gate_and_scenario.ipynb` · `q11_outputs/` (scale gate, scenario pair results, summary, reorder points) · `q11_charts/q11_01_reorder_points_and_fill_rate.png` · `Data_Owner_Question_Pack.md` · `validation_report_week05_q11.csv`

**Re-run:** open the notebook anywhere inside the repository checkout and run all cells (about a minute); it finds `week-02/reports/week_02/merged` itself (or set `CADETX_MERGED`).
