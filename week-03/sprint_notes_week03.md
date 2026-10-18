# Sprint Notes — Week 3 (revised)
**CadetX Heavy Supplier, Inventory & Warehouse Analytics**
**Sprint focus:** First KPI calculations, validated against the corrected Week-2 merged datasets, and locked analysis questions

---

## 1. What Was Done
- Rebuilt the KPI notebook (`03_kpi_calculations.ipynb`) on the five corrected Week-2 merged datasets, reading them by explicit name with row-count, key-uniqueness and total-reconciliation checks (22 checks, all passing).
- **Sales & customer KPIs:** net revenue (ex-GST, Delivered orders), average order value, gross profit and margin, revenue by year/month/customer type/region, delivery lead time, top products with margin.
- **Payment KPIs:** order status, payment-status breakdown, outstanding and overdue amounts with ageing buckets, credit-risk concentration by customer type and region.
- **Supplier KPIs:** spend, on-time rate, delay, actual vs contracted lead time and cancellation rate per supplier, from purchase orders.
- **Inventory KPIs:** stock-scale diagnostic, units received vs sold per product, ledger-vs-master reconciliation, branch view.
- Produced 8 charts, KPI CSVs, revised summaries, and a column dictionary for the five merged datasets.

## 2. Corrections Made to the First Week-3 Version

| Issue | What was wrong | Resolution |
| :--- | :--- | :--- |
| **Revenue overstated / mislabelled** | The headline ₹32.42B was `grand_total` (includes GST) over all orders, including 1,967 Cancelled orders | Net revenue is now ex-GST and Delivered-only: **₹22.96B**. Gross incl. GST (₹29.25B), GST and cancelled value (₹2.49B) are reported separately. Average order value ₹1.27M (was ₹1.62M) |
| **"Not Invoiced" label wrong** | 2,360 orders = 1,967 Cancelled orders + 393 orders whose invoices had been set aside | Replaced by **Cancelled (1,967)**; the 393 repeated-ID invoices are back in the invoiced base. Payment mix is now Paid 69.5% / Partially Paid 20.3% / Unpaid 10.2% of 18,033 invoices |
| **Supplier assignment arbitrary** | "Supplier of most recent PO" per product — but every product is bought from all 8 suppliers (top supplier ≈13% share; 15 products were decided by a Cancelled PO) | Withdrawn. Supplier KPIs now come from PO activity; suppliers are essentially indistinguishable (on-time 84–86%, cancellations 9–10%) |
| **Stock health / turnover not valid** | Quantile classes are ~25/50/25 by construction; turnover divided units sold by ~107,000 units of stock | Withdrawn as findings. Replaced by a diagnostic: units received are **18.1×** units sold, so stock far exceeds `max_stock` for all 180 pairs |
| **Profit not reported** | Corrected `line_profit` (price − cost) now available | Added: gross profit ₹4.95B, margin 21.6%; top-2 products have below-average margins |
| **Unreliable payment totals** | 393 repeated-ID invoices cannot be matched to their payments | Outstanding/overdue computed on 17,640 reliable invoices only; the 393 (₹654M incl. GST) reported separately |
| **Notebook not reproducible** | Read `merged_dataset_ALL.csv`, which was not in the submission; 2 cells unexecuted; summaries cited non-existent files | New notebook reads the five merged files by name, runs end to end, with outputs saved |
| **Stale deliverables** | `kpi_tables.csv` said supplier mix unavailable; mismatch count quoted as 6 | Regenerated from the notebook; mismatch count is **14** |

## 3. Key Findings
**Sales/customer**
- Net revenue ₹22.96B over 2019–2024 (18,033 delivered orders); flat to slightly declining, 2024 lowest (−3.8% YoY, −5% vs 2019).
- Government (22.0%) and Corporate (20.5%) lead, but average order value is similar across all types (₹1.24–1.29M).
- South and West = 60.9% of net revenue; Central and North East ≈ 2% each.
- Top 2 products (Engine Block EB-600, Transmission Assembly TA-800) = 36.0% of net revenue at below-average margin (19.7%, 18.0% vs 21.6% overall).
- 9.8% of orders are cancelled; lead time is 8.06 days on average and consistent across regions.

**Payments**
- ₹5.80B outstanding on reliable invoices; **86% of it is more than a year overdue**. As-of date is the latest due date in the data (2025-03-14).
- **No concentration by customer type or region** (outstanding 19.6–21.4% of value across all types) — the issue is ageing, not a segment.

**Supplier**
- Spend is evenly spread (12.1–12.9% per supplier); on-time rate 84.2–85.6%; average delay about half a day for every supplier; `reliability_score` does not track observed performance.

**Inventory**
- Receipts are 18× sales in every product; stock thresholds are on the sales scale. Stock-based KPIs are not reportable until the data owner confirms the PO/stock quantities.
- 14 product–branch pairs differ between master and ledger (13 negative), pointing to the unsigned `ADJUSTMENT` quantities.

## 4. Open Items for Phase 2
- Data owner: confirm purchase-order and stock quantities (18× scale gap; PO spend ≈ ₹312B vs sales ₹23B).
- Warehouse/Ops: `ADJUSTMENT` sign convention and authoritative stock source.
- Finance/IT: renumber the 196 repeated invoice IDs (and 201 repeated payment IDs) so payments can be attributed.
- Customer master dates look inconsistent (many orders predate `customer_since`) — not re-checked in this version, carry forward.

Full tables: `sales_kpi_summary.md`, `supplier_kpi_summary.md`, `inventory_kpi_summary.md`, `kpi_outputs/`.
