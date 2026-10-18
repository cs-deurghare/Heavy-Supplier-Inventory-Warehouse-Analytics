# Week 3 — Product, Inventory & Warehouse KPI Summary
**Source:** `merged_dataset.csv` — 130,402 rows, 2019–2024, 30 tracked products

---

## 1. Data-Quality Finding: Stock Field Scale Mismatch

| Field | Range (full dataset) |
| :--- | :--- |
| `current_stock` | 88,853 – 121,013 |
| `max_stock` | 131 – 582 |
| `reorder_level` | 24 – 119 |
| `safety_stock` | 16 – 85 |

`current_stock` is on a completely different numeric scale than the other three thresholds. A
direct comparison (e.g. `current_stock >= max_stock` → "Overstock") would classify every single
row as overstocked, which is not a usable result. Most likely explanation: these fields represent
different units or aggregation levels in the source data rather than a single entry error.

**Finalized approach for this submission:** stock health is classified using the 25th/75th
percentile of `current_stock` alone, rather than compared against `max_stock`. This is documented
as a known limitation, carried forward as a Phase 2 question for the Data Analyst to trace to its
source rather than left open in this deliverable.

## 2. Inventory Turnover by Product

All 30 tracked products show a turnover ratio tightly clustered between **0.40 and 0.45** —
no single product stands out as a clear fast- or slow-mover at this level of aggregation.

| Rank | Product | Category | Turnover Ratio |
| :--- | :--- | :--- | :--- |
| 1 | Pressure Sensor PS-90 | Sensors | 0.45 |
| 2 | Swing Motor SWM-350 | Hydraulic | 0.45 |
| 3 | Radiator RD-250 | Cooling | 0.44 |
| 4 | Boom Cylinder BC-400 | Hydraulic | 0.44 |
| 5 | O-Ring Set OR-50 | Seals | 0.44 |

Full table in `kpi_inventory_turnover.csv`.

## 3. Stock Health Distribution

| Status | Row Count | % of Rows |
| :--- | :--- | :--- |
| Optimal Stock | 66,770 | 51.2% |
| Overstock | 31,841 | 24.4% |
| Low Stock | 31,791 | 24.4% |

Roughly even split between Low Stock and Overstock outside the optimal band — worth a closer
look once the scale question above is resolved, since the current classification is based on
relative distribution within the dataset rather than a fixed, meaningful threshold.

## 4. Warehouse Capacity by Branch

Six branches tracked, with average current stock ranging ~104,000–110,000 units and warehouse
capacity and headcount varying by region. Full table in `kpi_warehouse_capacity.csv`.

---

**Status:** Finalized for this submission using the quantile-based method above. The turnover and
stock-health figures are directionally useful and ready to present; tracing the `current_stock`
scale to its source is carried forward as a Phase 2 data-quality question rather than a blocker
on this deliverable.
