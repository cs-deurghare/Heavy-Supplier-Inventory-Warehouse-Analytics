# Data Dictionary (DRAFT)

Built from column names and sample values only. Everything marked **(confirm)** must be checked against the CadetX Fields Documentation.docx.

## How the tables connect
- customers → sales_orders_header (`customer_id`); branches → most tables (`branch_id`)
- sales_orders_header → sales_orders_lines (`so_id`) → products (`product_id`)
- sales_orders_header → invoices (`so_id`) → payments (`invoice_id`)
- suppliers → purchase_orders_header (`supplier_id`) → purchase_orders_lines (`po_id`) → products (`product_id`)
- stock_ledger (`product_id` + `branch_id`) links movements to products and branches; `reference_id` points to an SO, PO or adjustment
- inventory_master: one row per product and branch (30 products x 6 branches = 180 rows)

## Tables

| Table | Rows | What it holds | Key column(s) |
|---|---|---|---|
| branches | 6 | Warehouse/branch details: type, capacity (sq ft as text), staff, revenue, operating cost, demand index | branch_id |
| customers | 500 | Customer type, industry, location, credit limit, balance, payment terms, rating | customer_id |
| products | 30 | Product catalogue: cost, price, margin %, GST rate, weight, lead time, criticality, stock levels | product_id |
| suppliers | 8 | Supplier type, product category, lead time, reliability score, import duty rate | supplier_id |
| inventory_master | 180 | Stock setup per product and branch: opening, reorder level, safety stock, max stock, current stock, bin | product_id + branch_id |
| sales_orders_header | 20,000 | One row per sales order: dates, status (Delivered/Cancelled), channel, totals | so_id |
| sales_orders_lines | 130,402 | Products on each sales order: quantity, unit price, line totals, GST | so_id + line_number |
| invoices | 18,033 | One invoice per delivered order: dates, totals, payment status (Paid/Partially Paid/Unpaid) | invoice_id (**not unique**, see notes) |
| payments | 19,257 | Payments against invoices: date, amount, method | payment_id |
| purchase_orders_header | 24,000 | One row per purchase order: supplier, dates, status (Received/Cancelled), totals | po_id |
| purchase_orders_lines | 155,495 | Products on each purchase order: quantity, unit cost, GST | po_id + line_number |
| stock_ledger | 237,230 | Every stock movement: IN (from PO), OUT (to SO), ADJUSTMENT, with running balance | movement_id |

## Columns that need explaining
| Table.column | Meaning (from names and values) |
|---|---|
| branches.warehouse_capacity | Text like "45230 sqft"; notebook adds numeric `warehouse_capacity_sqft` |
| branches.market_demand_index | Demand score for the branch's market **(confirm scale)** |
| customers.current_balance | Amount the customer currently owes **(confirm)** |
| customers.payment_terms | Advance, Net 15, Net 30, Net 45 or Net 60 |
| products.margin_percentage | Profit margin on the product **(confirm how calculated)** |
| products.criticality_level / usage_frequency | High, Medium or Low |
| suppliers.reliability_score | Whole number from 3 to 5 in this data **(confirm scale)** |
| suppliers.china_tax_id | Supplier tax identifier **(confirm)** |
| sales_orders_header.sales_channel | Field Sales, Dealer Network, Counter Sale or Online |
| stock_ledger.movement_type | IN, OUT or ADJUSTMENT (reference_type PO, SO or ADJ) |
| stock_ledger.running_balance | Stock on hand after that movement |
| inventory_master.reorder_level / safety_stock / max_stock | Reorder trigger, buffer stock and upper limit **(confirm)** |

## Data notes from Week 1 checks
- 197 `invoice_id` values are reused for different sales orders; payments for these are ambiguous.
- 14 of 180 product-branch pairs have a last ledger balance that differs from `inventory_master.current_stock`.
- `purchase_orders_header.received_date` is blank only for the 2,370 cancelled POs (expected).
