# Sprint Notes — Week 3
**CadetX Heavy Supplier, Inventory & Warehouse Analytics**
**Sprint focus:** First KPI calculations, data dictionary finalization, and locked analysis questions

---

## 1. What Was Done

**Sales, customer & supplier KPIs:**
- Calculated top-line and segmented KPIs from the full 130,402-row, 20,000-order dataset
  (2019–2024): total revenue, average order value, revenue by year, customer type, and region,
  delivery lead time, top products, and payment status breakdown.
- Reapplied the `payment_status` → "Not Invoiced" label (2,360 orders) after it was found to have
  reverted to blank in a later copy of the dataset.
- **Root-caused and fixed the missing supplier data.** `purchase_orders_header.csv` has no
  `product_id`, so the only valid path from a product to its supplier is
  `purchase_orders_lines` (has `product_id`) → `purchase_orders_header` (has `supplier_id`) →
  `suppliers`. This join was present in an earlier revision of the Week 2 merge notebook but was
  never carried into the final `master_df`, and was dropped from the notebook entirely in a later
  revision — which is why no supplier columns ever reached `merged_dataset.csv`. Rebuilt the full
  merge from all 10 raw source tables with this join included, assigning each product's supplier
  from its most recent purchase order. Supplier fields are now populated on 100% of rows
  (130,402/130,402), and the supplier mix KPI — blocked since the original scope assignment — is
  now calculated (see `kpi_supplier_mix.csv`).

**Product, inventory & warehouse KPIs:**
- Calculated inventory turnover ratio, total units sold, and average inventory level per product
  across all 30 SKUs.
- Built a stock health classification (Low Stock / Optimal Stock / Overstock) using quantile
  thresholds on `current_stock`, after finding that a direct comparison to `max_stock` was not
  usable (see Issues below).
- Calculated warehouse-level capacity and average stock by branch and region.

**Shared:**
- Finalized a single data dictionary covering all 89 columns of the rebuilt `merged_dataset.csv`
  (including the new supplier fields), plus the derived fields produced for Week 3 KPIs.
- Consolidated and locked 13 analysis questions across sales, customer, product/inventory,
  operations, and data quality for Phase 2.
- Built exploratory charts (sales, inventory, and supplier mix) and a single reproducible notebook
  covering all three scopes.
- Ran a validation report confirming row counts, data types, absence of null/infinite values, no
  ambiguous merge columns, and the resolved supplier join.

## 2. Issues Found and How We Treated Them

| Issue | Detail | Resolution |
| :--- | :--- | :--- |
| **Supplier data missing** | No `supplier_id` or `supplier_name` column existed anywhere in `merged_dataset.csv` or `sales_customer_supplier_merged.csv`, across all 6 years | **Resolved.** Rebuilt the full merge from raw source tables with the product→supplier join (`purchase_orders_lines` → `purchase_orders_header` → `suppliers`) included. Supplier fields now populated on 100% of rows. Each product's supplier is assigned from its most recent purchase order — the finalized rule for this submission; a different rule (e.g. most frequent supplier) can be swapped in for Phase 2 if the team prefers |
| **`current_stock` vs. `max_stock` scale mismatch** | `current_stock` sits in the ~88,000–121,000 range, while `max_stock` / `reorder_level` / `safety_stock` sit in the tens-to-low-hundreds range — a direct comparison marks every row as "Overstock" | **Finalized for this submission.** Adopted a quantile-based stock health classification (25th/75th percentile of `current_stock`) as the method used throughout. Tracing the scale mismatch to its source is carried forward as a Phase 2 data-quality question, not a blocker here |
| **`payment_status` reverted to blank** | A later copy of the complete dataset had `payment_status` blank again for 2,360 "not yet invoiced" orders, despite this being fixed and agreed in Week 2 | Reapplied the "Not Invoiced" label before running KPIs |
| **9.0% of orders fully Unpaid** | Found during payment status breakdown — not previously quantified | Finding documented and flagged for financial reconciliation review in Phase 2; does not block this submission |
| **Duplicate deliverable filenames with different scope** | Two independently-produced versions of `data_dictionary.md`, `analysis_questions_locked.md`, `kpi_tables.csv`, and `sprint_notes_week03.md` existed — one covering sales/customer, one covering product/inventory — which would have silently overwritten each other on upload | Merged into single combined versions covering both scopes (this document and its companion files) |
| **Column name collisions from the full rebuild** | Rebuilding the merge from all 10 raw tables surfaced ambiguous `_x`/`_y`-suffixed columns (e.g. `city`, `region`, `lead_time_days`, `unit_price` exist in multiple source tables) | **Resolved.** Every colliding column was explicitly renamed before merging (e.g. `customer_city`, `supplier_region`, `product_lead_time_days`) — zero ambiguous columns remain in the final file |

## 3. Key Findings

**Sales/customer:**
- Total revenue 2019–2024: ₹32.4B across 20,000 orders, essentially flat year-over-year
- Government and Corporate customers generate the most revenue; spread is fairly even across types
- South and West regions account for ~68% of total revenue
- Average delivery lead time: 8.06 days, consistent across all regions
- Top 2 products (Engine Block EB-600, Transmission Assembly TA-800) = ~36% of line revenue
- 61.3% of orders fully paid, 17.9% partially paid, 11.8% not yet invoiced, 9.0% unpaid

**Product/inventory:**
- Inventory turnover ratio is tightly clustered (0.40–0.45) across all 30 products — no single
  product stands out as a clear fast- or slow-mover
- Stock health distribution: ~51% Optimal Stock, ~24% Low Stock, ~24% Overstock, under the
  finalized quantile-based classification (see Issues above)
- Warehouse capacity and average stock vary by branch/region — full table in
  `kpi_warehouse_capacity.csv`

**Supplier:**
- Supplier gap resolved — 7 of 8 suppliers are currently matched to at least one tracked product
- Suzhou Local Vendor Supplies and Ningbo Distributor Supplies account for the largest share of
  line revenue; full breakdown in `kpi_supplier_mix.csv`

Full tables in `sales_kpi_summary.md`, `kpi_inventory_turnover.csv`,
`kpi_stock_health_distribution.csv`, `kpi_warehouse_capacity.csv`, and `kpi_supplier_mix.csv`.


