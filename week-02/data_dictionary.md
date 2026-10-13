# Data Dictionary — Merged Dataset (Week 02)

This document provides a comprehensive schema and data dictionary for the finalized `merged_dataset.csv` produced during Week 02 of the Heavy Machinery ERP Analytics Project.

---

## 1. Primary Entity Identifiers
| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `so_id` | String / Object | Unique Sales Order Identifier |
| `so_line_id` | String / Object | Line item identifier within a Sales Order |
| `customer_id` | String / Object | Unique Customer Identifier |
| `product_id` | String / Object | Unique Product SKU Identifier |
| `branch_id` | String / Object | Unique Branch / Warehouse Identifier |
| `invoice_id` | String / Object | Invoice Identifier |
| `invoice_key` | String / Object | Composite Key (`invoice_id` + `so_id`) to resolve duplicates |

---

## 2. Product & Inventory Dimensions
| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `product_name` | String / Object | Full commercial name of the machinery/part |
| `category` | String / Object | Product category classification |
| `unit_price` | Float64 | Base selling price per unit |
| `opening_stock` | Int64 / Float64 | Initial stock count at the start of period |
| `current_stock` | Int64 / Float64 | Reconciled current stock count |
| `reorder_level` | Int64 / Float64 | Minimum stock threshold triggering replenishment |
| `safety_stock` | Int64 / Float64 | Buffer stock reserved for emergency demand |
| `warehouse_bin` | String / Object | Bin location code within the warehouse |

---

## 3. Branch & Customer Attributes
| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `branch_name` | String / Object | Name of the warehouse/branch facility |
| `city` | String / Object | City location of branch/customer |
| `state` | String / Object | State location of branch/customer |
| `customer_name` | String / Object | Full legal name of the purchasing customer entity |
| `customer_type` | String / Object | Customer segment (e.g., Enterprise, Retail, Industrial) |

---

## 4. Financial & Order Metrics
| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `order_qty` | Int64 / Float64 | Quantity ordered in the sales order line |
| `unit_price_so` | Float64 | Unit price charged on the sales order |
| `order_date` | Date / String | Date on which the sales order was created |
| `invoice_date` | Date / String | Date on which invoice was generated |
| `payment_status` | String / Object | Status of invoice payment (e.g., Paid, Unpaid, Pending) |
| `grand_total` | Float64 | Final invoiced total including taxes |
