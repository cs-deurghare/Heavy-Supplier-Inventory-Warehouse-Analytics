# Data Dictionary — merged_dataset.csv
**Week 3 — CadetX Heavy Supplier, Inventory & Warehouse Analytics**
**Source:** `merged_dataset.csv` (2019–2024, 89 columns after the supplier rebuild, 130,402 rows)
**Grain:** one row per sales order line item

**Note on this version:** the dataset was rebuilt from the 10 raw source tables to bring in
supplier fields (Section 9), which were missing from earlier versions. Any column that existed
under the same name in more than one source table (e.g. `city`, `region`, `lead_time_days`,
`unit_price`) was explicitly renamed before merging so nothing in this file is ambiguous — see
the per-section notes below for what changed.

---

## 1. Order-level fields

| Column | Type | Description |
| :--- | :--- | :--- |
| `so_id` | string | Sales order ID — unique per order, repeats across line items |
| `customer_id` | string | Customer reference key |
| `branch_id` | string | Branch that fulfilled the order |
| `order_date` | date | Date the order was placed |
| `delivery_date` | date | Date the order was delivered |
| `order_status` | string | Order lifecycle status (e.g. Completed, Cancelled) |
| `order_payment_terms` | string | Payment terms agreed for this order |
| `total_order_value` | int | Order value before tax |
| `total_gst_amount` | float | GST amount for the full order |
| `grand_total` | float | Order value including tax — used for all revenue KPIs |
| `sales_channel` | string | Channel the order came through (e.g. Direct, Dealer, Online) |

## 2. Customer fields

| Column | Type | Description |
| :--- | :--- | :--- |
| `customer_type` | string | Government / Corporate / Dealer / Fleet Owner / Retail |
| `industry_segment` | string | Customer's industry segment |
| `customer_city`, `customer_state`, `customer_pincode`, `customer_region` | string/int | Customer location |
| `customer_home_branch_id` | string | Customer's home branch (distinct from the fulfilling `branch_id`) |
| `credit_limit` | int | Customer's approved credit limit |
| `current_balance` | int | Customer's outstanding balance at time of snapshot |
| `customer_payment_terms` | string | Standing payment terms for this customer |
| `customer_since` | date | Date the customer relationship began |
| `customer_last_purchase_date` | date | Customer's most recent purchase date on record |
| `total_purchase_value` | int | Customer's lifetime purchase value |
| `customer_rating` | int | Internal customer rating score |

## 3. Line-item / product fields

| Column | Type | Description |
| :--- | :--- | :--- |
| `line_number` | int | Line sequence within the order |
| `product_id` | string | Product reference key |
| `quantity` | int | Units ordered on this line |
| `unit_price` | int | Price per unit for this line |
| `gst_rate` | int | GST rate applied (%) |
| `line_total` | int | Line value before tax |
| `gst_amount` | float | GST amount for this line |
| `line_grand_total` | float | Line value including tax |
| `product_name`, `category` | string | Product identification |
| `product_list_price`, `unit_cost` | int | Catalog price and unit cost (`product_list_price` renamed from the products table's own `unit_price` to avoid colliding with the line-item `unit_price` above) |

## 4. Invoice & payment fields

| Column | Type | Description |
| :--- | :--- | :--- |
| `invoice_id` | string | Invoice reference — blank for orders not yet invoiced |
| `invoice_date`, `due_date` | date | Invoice issue and due dates |
| `invoice_grand_total` | float | Invoiced amount |
| `payment_status` | string | Paid / Partially Paid / Unpaid / **Not Invoiced** (label applied for orders with no matching invoice) |
| `total_paid` | float | Amount paid to date |

**Note:** 197 `invoice_id` values were duplicated in the raw invoices table and were set aside during the merge rather than joined — see Week 2 sprint notes.

## 5. Inventory fields

| Column | Type | Description |
| :--- | :--- | :--- |
| `opening_stock`, `current_stock` | int | Stock levels at period start / current |
| `reorder_level`, `safety_stock`, `max_stock` | int | Inventory planning thresholds |
| `warehouse_bin` | string | Storage bin location |

**Data-quality finding (Week 3):** `current_stock` sits on a materially different
numeric scale (~88,000–121,000) than `max_stock` / `reorder_level` / `safety_stock`
(~16–582). A health classification that compares `current_stock` directly against
`max_stock` is not usable as-is — every row would register as "Overstock." Likely
explanation: `current_stock` represents a different unit of measure or aggregation
level (e.g. cumulative warehouse-wide units vs. per-SKU shelf capacity) than the other
three fields, which were not recalibrated to match in the source data provided.

**Finalized treatment for this submission:** the stock health KPI uses a quantile-based
classification on `current_stock` alone (25th/75th percentile) rather than a direct
comparison to `max_stock`. This is documented as a known limitation rather than a blocker —
recommend the Data Analyst trace the scale discrepancy to its source system in Phase 2, so
the classification can be rebuilt on a true like-for-like comparison if warranted.

## 6. Branch / warehouse fields

| Column | Type | Description |
| :--- | :--- | :--- |
| `branch_name`, `branch_city`, `branch_state`, `branch_region` | string | Fulfilling branch identity and location |
| `warehouse_type` | string | Warehouse classification |
| `warehouse_capacity_sqft` | int | Warehouse floor capacity |
| `service_center_available` | string | Whether the branch has a service center |
| `manager_id` | int | Branch manager reference |
| `total_employees` | int | Branch headcount |
| `avg_monthly_revenue`, `monthly_operational_cost` | int | Branch-level financial snapshot |
| `market_demand_index` | int | Regional demand indicator |

## 7. Product specification fields

| Column | Type | Description |
| :--- | :--- | :--- |
| `machine_type`, `brand`, `model_compatibility` | string | Product classification |
| `margin_percentage` | float | Product margin |
| `weight_kg`, `dimensions_cm` | float/string | Physical specifications |
| `material_type` | string | Construction material |
| `warranty_months` | int | Warranty period |
| `max_stock_level`, `product_lead_time_days` | int | Procurement planning fields (`product_lead_time_days` renamed from the products table's own `lead_time_days` to avoid colliding with the supplier's `lead_time_days` in Section 9) |
| `criticality_level`, `usage_frequency` | string | Operational classification |
| `uom` | string | Unit of measure |
| `last_purchase_price`, `product_last_purchase_date` | int/date | Most recent procurement record (`product_last_purchase_date` renamed to avoid colliding with `customer_last_purchase_date`) |
| `product_gst_rate` | int | Catalog GST rate for this product (distinct from the line-item `gst_rate` in Section 3) |

## 8. Derived fields (computed for Week 3 KPIs, not in the raw merge)

| Column | Type | Description |
| :--- | :--- | :--- |
| `stock_health_status` | string | `Low Stock` / `Optimal Stock` / `Overstock`, derived from the 25th/75th percentile of `current_stock` across the full dataset (see data-quality note above) |
| `inventory_turnover_ratio` | float | `total_units_sold ÷ avg_inventory_level` per product |

## 9. Supplier fields (new — previously missing, now resolved)

Earlier versions of this dataset had no supplier information at all, despite documentation
describing a supplier join. Root cause: `purchase_orders_header.csv` has no `product_id`, so the
only valid path from a product to its supplier is `purchase_orders_lines` (has `product_id`) →
`purchase_orders_header` (has `supplier_id`) → `suppliers`. This join existed in an earlier
revision of the Week 2 notebook but was never carried into the final table, and was later removed
from the notebook entirely.

The dataset has since been rebuilt from all 10 raw source tables with this join included. Each
product's supplier is assigned from its **most recent purchase order** (a product can appear on
POs from more than one supplier over time) — flagged for team confirmation in case a different
rule is preferred.

| Column | Type | Description |
| :--- | :--- | :--- |
| `supplier_id` | string | Supplier reference key, assigned via the product's most recent purchase order |
| `supplier_name` | string | Supplier's name |
| `supplier_type` | string | OEM / Distributor / Local Vendor |
| `product_category` | string | Product category this supplier is registered to supply (supplier-level field — compare against the row's own `category` in Section 3) |
| `supplier_city`, `supplier_province`, `supplier_region`, `supplier_pincode` | string/int | Supplier location |
| `supplier_lead_time_days` | int | Supplier's typical lead time |
| `reliability_score` | float | Supplier reliability score |
| `import_duty_rate` | float | Import duty rate applicable to this supplier |
| `china_tax_id` | string | Supplier's China tax ID (populated for overseas suppliers only) |
