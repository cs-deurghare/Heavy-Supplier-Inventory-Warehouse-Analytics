# Data dictionary update, Week 7

**Owner:** Ibrahim Khalil Umar · **Task:** W7-4 · **Full column list:** `data_dictionary_week07.csv` (184 columns: the five merged files from Week 3, plus `customers_clean.csv` and `branches_clean.csv`; columns `usability` and `note` added)

This update records three things the team has found since Week 3. Usability labels: **Usable**, **Usable with caution** (read the note), **Unusable** (do not use for the stated purpose), **Not tested**, and **Not flagged** (no issue found, not individually verified).

## 1. Customer fields: unusable (Q13, Week 6)

| Field (`customers_clean.csv`) | Verdict | Why | Use instead |
|---|---|---|---|
| `customer_since` | **Unusable** | After the customer's first order for 58.4% of customers; rank correlation with the first order −0.04 | First delivered order date |
| `last_purchase_date` | **Unusable** | Earlier than the customer's last order for 93.0%; rank correlation −0.01 | Last delivered order date |
| `total_purchase_value` | **Unusable** | 5.4% of delivered revenue; no customer within 10%; rank correlation −0.09 | Revenue and order count from the order lines |

The gaps look the same in every region and customer type (smallest Holm-adjusted p = 0.75), so no group correction applies. Tenure, recency and value for Phase 3 are derived from the order lines, which cover 2019 to 2024 only: every customer first ordered in 2019 and last ordered in 2024, so the orders cannot show who is new or who has left. The three fields stay in the master as reference only.

## 2. Stock-scale label (Q10 unresolved)

Purchase receipts in the ledger are **18.13 times** units sold, and recorded `current_stock` is about **350 times** `max_stock`. Nothing in the data explains this. The team works on the **sales scale** because the stored thresholds (`max_stock`, `reorder_level`, `safety_stock`) fit monthly sales.

| Field | Label |
|---|---|
| `opening_stock`, `reorder_level`, `safety_stock`, `max_stock` | Usable with caution, on the sales scale only |
| `current_stock`, `ledger_latest_balance`, `stock_value_cost`, `below_reorder`, `balance_difference` | **Unusable** for turnover, cover or health; shown only as a sensitivity |
| `total_in_qty`; purchase-order `quantity` and values | Not a stock-scale reference; money spent is valid as recorded |
| `total_out_qty`, ledger `OUT` | Usable as demand (91% of delivered units) |

**Every stock result carries this sentence:** *"Sales scale assumed (Q10 unresolved); results rest on this assumption."* The unscaled case is shown as a sensitivity, never as a result. Two further stock-field rules: ledger `ADJUSTMENT` quantities are unsigned (read the sign from steps in `running_balance`), and the 14 stock-master mismatches are the master lagging the ledger by its last one or two movements.

## 3. Missing data (capacity, timing, cost)

| Missing | Effect |
|---|---|
| **Warehouse capacity use.** `branches.warehouse_capacity` is one static text figure per branch (for example "45230 sqft"). There is no utilisation, bin, pallet or volume data to set against it | No capacity or utilisation claim; branch "throughput" means orders and units sold |
| **Staffing and timing.** One headcount per branch; no shifts, pick-and-pack times or dwell times. Delivery dates look generated or planned (Q7) | No speed, staffing or service-time claim |
| **Holding cost, ordering cost, service-level target** | No replenishment policy is called cost-optimal; stock value at cost is only a proxy |
| **Backorder, collection, credit-note and write-off records** | Lost sales are assumed in the stock simulation; collectability cannot be tested (Q4) |
| **Customer history before 2019** | Tenure, new and churned customers cannot be derived |

## Other limits worth carrying
- `margin_percentage` is a markup on cost for 29 of 30 products (Engine Oil Filter OF-90 is the exception: its 37.3 matches a margin on price, 37.5%, not a markup, 60.0%); use `line_margin_pct` for margin on price.
- `invoice_id` is not unique (197 reused ids; 393 invoices, 2.2% of value, cannot be matched to payments); payment totals are reliable only where `payment_total_reliable` is true.
- `lead_time_actual_days` (received purchase-order lines) ranges 7 to 35 days with SD 6.7, the same spread for all 180 pairs; use the distribution, not only the mean (W7-4).
- The data is very regular (product volumes within 8%, identical ABC classes in both periods, evenly spread `customer_since`). Findings are worded to what the lines show.
- The dataset is supplied with the programme, so open items are data limits, not questions for an owner.
