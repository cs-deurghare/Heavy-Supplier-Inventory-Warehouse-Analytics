# Week 3 — Sales, Customer & Supplier KPI Summary
**Source:** `sales_customer_supplier_merged.csv` — 130,402 line items / 20,000 unique orders, 2019–2024

---

## 1. Top-Line KPIs

| KPI | Value |
| :--- | :--- |
| Total Revenue (2019–2024) | ₹32,424,754,555.80 |
| Average Order Value | ₹1,621,237.73 |
| Total Orders | 20,000 |
| Average Delivery Lead Time | 8.06 days |
| Median Delivery Lead Time | 8.0 days |

## 2. Revenue by Year

| Year | Revenue |
| :--- | :--- |
| 2019 | ₹5.40B |
| 2020 | ₹5.50B |
| 2021 | ₹5.42B |
| 2022 | ₹5.41B |
| 2023 | ₹5.39B |
| 2024 | ₹5.30B |

Revenue is essentially flat year-over-year — no clear growth or decline trend across the 6-year window.

## 3. Revenue by Customer Type

| Customer Type | Revenue | Avg Order Value | Orders |
| :--- | :--- | :--- | :--- |
| Government | ₹7.21B | ₹1,585,122 | 4,551 |
| Corporate | ₹6.63B | ₹1,631,995 | 4,064 |
| Dealer | ₹6.61B | ₹1,645,193 | 4,016 |
| Fleet Owner | ₹6.22B | ₹1,623,363 | 3,834 |
| Retail | ₹5.75B | ₹1,625,846 | 3,535 |

Fairly even spread — Government leads on volume of orders and total revenue, but average order value is consistent (~₹1.6M) across all five segments.

## 4. Revenue by Region

| Region | Revenue | Orders |
| :--- | :--- | :--- |
| South | ₹10.33B | 6,384 |
| West | ₹9.51B | 5,923 |
| East | ₹5.69B | 3,491 |
| North | ₹5.54B | 3,333 |
| Central | ₹0.70B | 447 |
| North East | ₹0.66B | 422 |

South and West together account for ~68% of total revenue. Central and North East are comparatively small markets — worth flagging for the Data Scientist's forecasting review.

## 5. Delivery Lead Time by Region

| Region | Avg Lead Time (days) |
| :--- | :--- |
| Central | 7.56 |
| North East | 7.80 |
| East | 7.90 |
| North | 8.03 |
| South | 8.13 |
| West | 8.15 |

Consistent across regions (7.6–8.2 days) — no single region is a bottleneck.

## 6. Top 5 Products by Revenue

| Product | Revenue | Units Sold |
| :--- | :--- | :--- |
| Engine Block EB-600 | ₹6.89B | 45,222 |
| Transmission Assembly TA-800 | ₹4.81B | 45,035 |
| Boom Cylinder BC-400 | ₹2.74B | 46,364 |
| Swing Motor SWM-350 | ₹2.34B | 45,971 |
| Track Chain TC-45 | ₹2.32B | 45,575 |

Engine Block EB-600 and Transmission Assembly TA-800 together make up ~36% of total line revenue.

## 7. Payment Status Breakdown

| Status | Orders | % of Orders |
| :--- | :--- | :--- |
| Paid | 12,264 | 61.3% |
| Partially Paid | 3,578 | 17.9% |
| Not Invoiced | 2,360 | 11.8% |
| Unpaid | 1,798 | 9.0% |

The 9.0% fully Unpaid segment is worth a closer look — recommend flagging this for financial reconciliation review.

## 8. Supplier Mix — Previously Blocked, Now Resolved

Earlier versions of the merged dataset did not contain a `supplier_id` or `supplier_name`
column. Root cause: the only valid path from a product to its supplier runs through
`purchase_orders_lines` → `purchase_orders_header` → `suppliers` (the purchase order header
table has no `product_id`); this join was present in an earlier revision of the Week 2 notebook
but was never carried into the final table.

The dataset has been rebuilt from the raw source tables with this join included. Supplier fields
are now populated on 100% of rows. See `kpi_supplier_mix.csv` and Part C of
`03_kpi_calculations.ipynb` for the supplier mix KPI.

---

**Files delivered:**
- `03_kpi_calculations.ipynb` — full reproducible notebook (sales/customer, product/inventory/warehouse, and supplier KPIs)
- `kpi_tables.csv` — top-line KPI summary
- `kpi_revenue_by_year.csv`, `kpi_revenue_by_month.csv`, `kpi_revenue_by_customer_type.csv`, `kpi_revenue_by_region.csv`, `kpi_lead_time_by_region.csv`, `kpi_top_products.csv`, `kpi_payment_status_breakdown.csv`, `kpi_supplier_mix.csv`
- `exploratory_charts/` — charts (monthly revenue trend, revenue by customer type, revenue by region, lead time distribution, top products, supplier revenue mix)
