# Week 3 — Product, Inventory & Warehouse KPI Summary (revised)
**Source:** `merged/inventory_with_ledger.csv` (180 product–branch pairs), `stock_ledger_enriched.csv`, `sales_orders_full.csv`, `purchase_orders_full.csv`

## 1. What changed and why
The first version reported a stock-health split (51% Optimal / 24% Low / 24% Overstock) and inventory turnover of 0.40–0.45. **Neither is a valid finding and both have been withdrawn:**
- The stock-health classes were cut at the 25th and 75th percentile of `current_stock`, so they come out as roughly 25/50/25 **by construction** whatever the data says.
- Turnover was units sold ÷ ~107,000 units of stock. As shown below, the stock level is not on the same scale as sales, so the ratio carries no performance information.

## 2. The stock scale problem — and its cause
| Field | Mean | Range |
|---|---:|---|
| `current_stock` | 107,240 | 88,853 – 121,013 |
| `opening_stock` | 183 | 80 – 300 |
| `max_stock` | 322 | 131 – 582 |
| `reorder_level` | 65 | 24 – 119 |
| `safety_stock` | 45 | 16 – 85 |

180 of 180 pairs sit above `max_stock`; none is below reorder level.

**Cause (answers locked Q11): the fields are not in different units; the inflow is on a different scale from the outflow.**
| Flow | Units |
|---|---:|
| Units sold (Delivered orders) | 1,234,939 |
| Units received on purchase orders | 22,387,123 (**18.1× sold**) |
| Ledger IN / OUT | 20,397,795 / 1,124,832 (18.1×) |

Stock starts at ~200 units (matching the thresholds) and then receives roughly 18 times more than it ships. Every product shows the same pattern (received ÷ sold = 17.4–19.2). Thresholds were set for the sales scale; PO quantities appear to be on a different scale. **Until the data owner confirms which side is right, stock-based KPIs (turnover, cover, stock health, stock value) should not be reported as performance findings.** Stock value at cost is ≈₹281B, against net sales of ₹23B.

`kpi_inventory_turnover.csv` keeps `received_to_sold_ratio` (the diagnostic) and an `indicative_turnover` column explicitly labelled as not valid.

## 3. Ledger vs inventory master
14 of 180 pairs differ (range −515 to +16 units). **13 of the 14 are negative** (ledger higher than `current_stock`), so the error is one-directional rather than random. The ledger chain itself is consistent in file order; only `ADJUSTMENT` rows (unsigned quantity, about half of which reduce stock) break it. Note that the affected pairs depend on ordering ledger rows by date then file position, **not** by `movement_id`; the set differs from earlier reports that used `movement_id`.
Full list: `kpi_stock_ledger_mismatches.csv`. Open for Warehouse/Ops: confirm the `ADJUSTMENT` sign convention and which source is authoritative.

## 4. Branch view (Delivered net revenue, stock, mismatches)
| Branch | Net revenue | Orders | Avg stock/product | Mismatched pairs | Capacity (sq ft) | Employees |
|---|---:|---:|---:|---:|---:|---:|
| Chennai South Hub | ₹4.68B | 3,677 | 107,808 | 1 | 41,890 | 81 |
| Kolkata East Depot | ₹4.34B | 3,413 | 104,127 | 1 | 29,880 | 49 |
| Ahmedabad West Hub | ₹3.99B | 3,115 | 105,166 | 2 | 34,120 | 63 |
| Delhi Central | ₹3.50B | 2,682 | 109,622 | 3 | 45,230 | 92 |
| Pune Distribution | ₹3.37B | 2,668 | 108,542 | 4 | 38,750 | 74 |
| Hyderabad Logistics | ₹3.08B | 2,478 | 108,176 | 3 | 36,210 | 57 |

Capacity and headcount come from the branches master (`data/branches.csv`) when it is available next to the notebook. Revenue per employee is highest at Kolkata (₹88.6M) and lowest at Delhi (₹38.0M) — a possible Phase 2 question.

**Files:** `kpi_stock_scale_check.csv`, `kpi_stock_scale_flows.csv`, `kpi_inventory_turnover.csv`, `kpi_stock_ledger_mismatches.csv`, `kpi_branch_summary.csv`; chart `08_received_vs_sold_by_product.png`.
