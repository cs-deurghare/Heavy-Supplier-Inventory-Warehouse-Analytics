# Week 2 — Data Cleaning, Integration & Validation Report
## Heavy Supplier, Inventory & Warehouse Analytics

**Report date:** 2026-10-18  
**Source notebook:** `week-02/02_data_cleaning_integration_validation_FIXED.ipynb` (revised)  
**Report folder:** `reports/week_02/`  
**Status:** Complete — 12 of 12 checks passed (revision 2: invoice–payment join, ledger ordering and merged-dataset fixes applied)

---

## 1. Executive Summary

| Metric | Value |
|---|---|
| Datasets processed | 12 CSV files |
| Total records | 605,141 |
| Row count change from Week 1 | 0 (no records added or removed) |
| Missing cells (raw) | 2,370 (all in `received_date`) |
| Exact duplicate rows | 0 |
| Candidate primary keys validated | 6 — all valid |
| Foreign-key relationships validated | 17 — all pass |
| Repeated `invoice_id` values | 196 (0 fully identical rows) |
| Repeated `payment_id` values | 201 (0 fully identical rows) |
| Inventory balance mismatches | 14 product–branch pairs |
| Date columns parsed | 12 — 0 new nulls introduced |
| Cleaned datasets exported | 12 |
| Open issues requiring business input | 5 |
| Invoice–payment mismatches (Paid) | 0 after fix (247 before; all caused by repeated `invoice_id`) |
| Invoice rows with reliable payment totals | 17,640 of 18,033 (393 repeated-ID rows set to `payment_total_reliable = False`) |
| Merged datasets rebuilt | 5 — corrected `line_profit`, safe payment join |

> [!IMPORTANT]
> **Revision 2 — what changed since the first version of this report**
> 1. **Invoice–payment join fixed.** Payments were previously attached by `invoice_id`, so each of the 393 rows sharing a repeated ID received the full payment total of all of them. This overstated total paid by **₹518M** (23.83B vs the 23.31B in the payments file) and produced the 247 "mismatches" and 312 negative outstanding balances. Payments are now attached only to invoices with a unique `invoice_id`.
> 2. **Ledger ordering fixed.** `movement_id` is not chronological, so it must not be used to order same-day movements. The ledger is now ordered by date then file position, in which `running_balance` chains correctly.
> 3. **`line_profit` in the merged sales file corrected.** It had been computed from `margin_percentage`, which is a *markup on cost*, overstating profit (7.06B, 27.8% margin vs the correct 5.49B, 21.6%).
> 4. Check 10 now passes; the earlier "11 / 12" result and the statement that *"use `row_key` for joins"* have been replaced (see Section 7.4 and 10).

**Key principle applied throughout:** No records were deleted. All decisions are additive
(flag columns, surrogate keys, documented findings). Source CSV files were not modified.

---

## 2. Task 1 — Dataset Load & Baseline Verification

All 12 CSV files were loaded successfully. Row counts match the Week-1 notebook
output exactly — no records were inserted, deleted, or corrupted between weeks.

| Dataset | Week-1 Rows | Current Rows | Match |
|---|---:|---:|---|
| `branches` | 6 | 6 | ✅ |
| `customers` | 500 | 500 | ✅ |
| `inventory_master` | 180 | 180 | ✅ |
| `invoices` | 18,033 | 18,033 | ✅ |
| `payments` | 19,257 | 19,257 | ✅ |
| `products` | 30 | 30 | ✅ |
| `purchase_orders_header` | 24,000 | 24,000 | ✅ |
| `purchase_orders_lines` | 155,495 | 155,495 | ✅ |
| `sales_orders_header` | 20,000 | 20,000 | ✅ |
| `sales_orders_lines` | 130,402 | 130,402 | ✅ |
| `stock_ledger` | 237,230 | 237,230 | ✅ |
| `suppliers` | 8 | 8 | ✅ |
| **Total** | **605,141** | **605,141** | **✅** |

> [!NOTE]
> The Week-1 written report incorrectly stated 704,733 total records. The notebook output (605,141) was correct. The written report has been corrected.

---

## 3. Task 2 — Missing Received Dates Investigation

**Dataset:** `purchase_orders_header`  
**Column:** `received_date`  
**Missing count:** 2,370 (9.875% of 24,000 rows)

### Cross-tab: PO Status × received_date presence

| PO Status | Date Present | Date Missing | Total | Missing % |
|---|---:|---:|---:|---:|
| Cancelled | 0 | 2,370 | 2,370 | 100.00% |
| Received | 21,630 | 0 | 21,630 | 0.00% |

### Finding

The missing-value pattern is **perfectly aligned with business status**:
- Every cancelled order has a null `received_date` (100%).
- Every received order has a date (0% missing).

This is structural evidence — not a data error — that `received_date` is
populated only when goods are physically received. A cancelled order is
never received, so no date is recorded.

### Decision

**Retain all 2,370 rows. No imputation applied.**  
Null `received_date` is valid and expected for `po_status = Cancelled`.

> [!IMPORTANT]
> **Action required (UI-04):** The procurement team must formally confirm that
> Cancelled POs are never expected to have a received_date. Until confirmed,
> exclude `po_status = Cancelled` from all lead-time and delivery KPI calculations.

---

## 4. Task 3 — Repeated Identifier Investigation

### 4.1 Repeated `invoice_id` (196 values)

| Metric | Count |
|---|---:|
| Total invoice rows | 18,033 |
| Distinct `invoice_id` values | 17,836 |
| `invoice_id` values appearing > 1 time | 196 |
| Rows belonging to repeated IDs | 393 |
| Extra occurrences (beyond first) | 197 |
| IDs with identical SO, customer, date, and amount | **0** |

**Detailed diversity analysis for the 196 repeated IDs:**

| Characteristic | Count |
|---|---:|
| Linked to multiple distinct `so_id` | 196 |
| Linked to multiple distinct `customer_id` | 196 |
| Linked to multiple distinct `invoice_date` | 196 |
| Linked to multiple distinct `grand_total` | 196 |
| Linked to multiple distinct `branch_id` | 166 |

**Example — `invoice_id` appearing 3 times:**  
The single ID appearing 3 times links three entirely different transactions
with different sales orders, customers, branches, dates, and amounts.

**Assessment:** These are **not duplicate records**. The same numeric ID
was issued to separate, unrelated transactions — indicating an invoice
numbering defect in the source system.

**Cleaning action applied:**
- Added `row_key` surrogate integer column (1 → 18,033) to each invoice row.
- Added `duplicate_invoice_id_flag = True` for the 393 affected rows.
- **Zero rows deleted.**

> [!WARNING]
> **Open issue UI-01:** 196 invoice IDs are non-unique. Finance/IT must confirm
> the intended uniqueness rule and assess whether re-numbering is possible without
> disrupting downstream references. Until resolved, payments cannot be attributed to these invoices (see Section 7.4); `row_key` identifies the invoice rows but payments reference only `invoice_id`.

---

### 4.2 Repeated `payment_id` (201 values)

| Metric | Count |
|---|---:|
| Total payment rows | 19,257 |
| Distinct `payment_id` values | 19,055 |
| `payment_id` values appearing > 1 time | 201 |
| Rows belonging to repeated IDs | 403 |
| Extra occurrences (beyond first) | 202 |
| IDs with identical invoice, date, and amount | **0** |

**Detailed diversity analysis for the 201 repeated IDs:**

| Characteristic | Count |
|---|---:|
| Linked to multiple distinct `invoice_id` | 201 |
| Linked to multiple distinct `payment_date` | 201 |
| Linked to multiple distinct `payment_amount` | 201 |
| Linked to multiple distinct `payment_method` | 168 |

**Assessment:** Same pattern as invoices — a **payment ID generation defect**.
No row is a true duplicate.

**Cleaning action applied:**
- Added `row_key` surrogate integer column (1 → 19,257).
- Added `duplicate_payment_id_flag = True` for the 403 affected rows.
- **Zero rows deleted.**

> [!WARNING]
> **Open issue UI-02:** 201 payment IDs are non-unique. Finance/IT must review
> the payment ID generation logic in the source system. Use `row_key` as the row identifier.

---

## 5. Task 4 — Candidate Key & Relationship Validation

### 5.1 Primary Key Validation

| Dataset | Key Column | Total Rows | Nulls | Duplicates | Valid |
|---|---|---:|---:|---:|---|
| `branches` | `branch_id` | 6 | 0 | 0 | ✅ |
| `customers` | `customer_id` | 500 | 0 | 0 | ✅ |
| `products` | `product_id` | 30 | 0 | 0 | ✅ |
| `suppliers` | `supplier_id` | 8 | 0 | 0 | ✅ |
| `purchase_orders_header` | `po_id` | 24,000 | 0 | 0 | ✅ |
| `sales_orders_header` | `so_id` | 20,000 | 0 | 0 | ✅ |

All 6 candidate primary keys are unique and non-null. ✅

### 5.2 Foreign-Key Referential Integrity (17 Relationships)

All 17 relationships passed with **zero unmatched child references**.

| Child Table | Child Column | Parent Table | Parent Column | Unmatched | Status |
|---|---|---|---|---:|---|
| `customers` | `branch_id` | `branches` | `branch_id` | 0 | ✅ |
| `inventory_master` | `product_id` | `products` | `product_id` | 0 | ✅ |
| `inventory_master` | `branch_id` | `branches` | `branch_id` | 0 | ✅ |
| `purchase_orders_header` | `supplier_id` | `suppliers` | `supplier_id` | 0 | ✅ |
| `purchase_orders_header` | `branch_id` | `branches` | `branch_id` | 0 | ✅ |
| `purchase_orders_lines` | `po_id` | `purchase_orders_header` | `po_id` | 0 | ✅ |
| `purchase_orders_lines` | `product_id` | `products` | `product_id` | 0 | ✅ |
| `sales_orders_header` | `customer_id` | `customers` | `customer_id` | 0 | ✅ |
| `sales_orders_header` | `branch_id` | `branches` | `branch_id` | 0 | ✅ |
| `sales_orders_lines` | `so_id` | `sales_orders_header` | `so_id` | 0 | ✅ |
| `sales_orders_lines` | `product_id` | `products` | `product_id` | 0 | ✅ |
| `invoices` | `so_id` | `sales_orders_header` | `so_id` | 0 | ✅ |
| `invoices` | `customer_id` | `customers` | `customer_id` | 0 | ✅ |
| `invoices` | `branch_id` | `branches` | `branch_id` | 0 | ✅ |
| `payments` | `invoice_id` | `invoices` | `invoice_id` | 0 | ✅ |
| `stock_ledger` | `product_id` | `products` | `product_id` | 0 | ✅ |
| `stock_ledger` | `branch_id` | `branches` | `branch_id` | 0 | ✅ |

> [!NOTE]
> `inventory_master` grain is `(product_id, branch_id)` — a composite key
> of 30 products × 6 branches = 180 rows. No duplicate composite key exists.
> This resolves the Week-1 flag of "30 repeated product IDs" — it is by design.

---

## 6. Task 5 — Inventory Balance Reconciliation

**Method:** For each `(product_id, branch_id)` pair, the latest `running_balance`
in `stock_ledger` (by `movement_date`, then file position — see 6.1) was compared against
`inventory_master.current_stock`.

### Summary

| Metric | Value |
|---|---:|
| Total product–branch pairs checked | 180 |
| Pairs where `current_stock` = ledger balance | 166 |
| **Pairs with a mismatch** | **14** |

### 14 Mismatch Detail

| Product | Branch | Master Balance | Ledger Balance | Difference | # Movements |
|---|---|---:|---:|---:|---:|
| P002 | CHN001 | 105,885 | 106,182 | −297 | 1,462 |
| P004 | PUN001 | 104,859 | 105,024 | −165 | 1,242 |
| P011 | HYD001 | 107,771 | 107,635 | +136 | 1,248 |
| P014 | AHM001 | 105,345 | 105,046 | +299 | 1,316 |
| P018 | PUN001 | 111,530 | 111,382 | +148 | 1,271 |
| P021 | DEL001 | 115,902 | 116,107 | −205 | 1,258 |
| P025 | HYD001 | 113,613 | 114,128 | −515 | 1,271 |
| P026 | PUN001 | 105,190 | 105,335 | −145 | 1,230 |
| P026 | HYD001 | 108,348 | 108,546 | −198 | 1,264 |
| P028 | DEL001 | 106,744 | 106,967 | −223 | 1,298 |
| P028 | PUN001 | 105,401 | 105,385 | +16 | 1,244 |
| P029 | DEL001 | 108,622 | 108,702 | −80 | 1,238 |
| P029 | PUN001 | 109,429 | 109,487 | −58 | 1,270 |
| P029 | KOL001 | 105,010 | 105,249 | −239 | 1,419 |

**Observations:**
- Differences are small (range: −515 to +299 units) relative to stock levels (100K+).
- Both positive and negative differences exist — this is not a systematic one-directional error.
- High-movement products/branches dominate (1,200–1,462 movements each).
- The differences may arise from timing: `inventory_master` may have been snapshotted at a different point than the last ledger entry, or from the unsigned `ADJUSTMENT` quantities (see 6.1).

### 6.1 Ledger integrity check (added in revision 2)

`running_balance` was tested row by row: previous balance + signed movement (IN +, OUT −) = current balance.

| Ordering | Chain breaks (of 237,050 steps) | Breaks by type |
|---|---:|---|
| Date, then **file position** (correct) | 1,222 | all `ADJUSTMENT` |
| Date, then `movement_id` (incorrect) | 56,583 | mixed |

- `movement_id` is **not chronological** and must not be used as a tie-break. The latest-balance logic now uses file position (the 14 mismatches are unchanged by this).
- Every IN and OUT movement chains correctly. The only breaks are 1,222 of 2,454 `ADJUSTMENT` rows: their `quantity` is stored unsigned, but those adjustments *reduce* the balance. The direction can be recovered from the change in `running_balance`.

**Cleaning action:** No correction applied. Both values are retained.
The reconciliation detail is saved to `task5_inventory_balance_reconciliation.csv`.

> [!WARNING]
> **Open issue UI-03:** 14 product–branch pairs have a discrepancy between
> `inventory_master.current_stock` and the latest `stock_ledger.running_balance`.
> Warehouse/Operations must confirm which is the authoritative balance source
> **and the `ADJUSTMENT` sign convention**. Until confirmed: use `stock_ledger.running_balance`
> (ordered by date, then file position) for time-series analysis; treat
> `inventory_master.current_stock` as the operational snapshot value.

---

## 7. Task 6 — Dataset Integration

### 7.1 Integration Principle Applied

> **Aggregate the many side before joining to the one side.**  
> This prevents row multiplication (fan-out) that would inflate financial totals.

All joins were validated by asserting `len(result) == len(header_table)` after every merge.

### 7.2 Sales Order: Header vs Lines Reconciliation

| Metric | Result |
|---|---:|
| Sales order headers | 20,000 |
| Header rows after join | 20,000 ✅ (no fan-out) |
| SO `grand_total` matching line sum (±₹1) | 20,000 |
| SO `grand_total` mismatching line sum | 0 |
| SO headers with no line data | 0 |

**Result:** ✅ All 20,000 sales orders — header totals exactly match aggregated line totals.

### 7.3 Purchase Order: Header vs Lines Reconciliation

| Metric | Result |
|---|---:|
| Purchase order headers | 24,000 |
| Header rows after join | 24,000 ✅ (no fan-out) |
| PO `grand_total` matching line sum (±₹1) | 24,000 |
| PO `grand_total` mismatching line sum | 0 |

**Result:** ✅ All 24,000 purchase orders — header totals exactly match aggregated line totals.

### 7.4 Invoice vs Payment Reconciliation (revised)

**Cause of the original mismatches.** `payments.invoice_id` is the only link from a payment to an
invoice, and `invoice_id` is not unique in `invoices` (UI-01). Aggregating payments by `invoice_id`
and joining back gave every row that shares a repeated ID the *combined* payments of all of them.

**Fix applied.** Payment fields are populated only for the 17,640 invoice rows with a unique
`invoice_id`. The 393 repeated-ID rows keep NaN payment fields and `payment_total_reliable = False`
rather than a wrong number. `outstanding_amount` is calculated only where payments are reliable.

| Metric | Before fix | After fix |
|---|---:|---:|
| Invoice rows | 18,033 | 18,033 (no fan-out) |
| Total paid in merged invoices | 23,827,028,417 | 22,795,333,904 |
| Payments file total | 23,308,879,671 | 23,308,879,671 |
| Overstatement vs payments file | +518,148,746 | none — ties exactly to payments on unique IDs |
| Paid invoices checked | 12,536 | 12,264 (reliable rows) |
| Paid invoice total ≈ payment total (±₹1) | 12,289 | **12,264 (100%)** |
| **Mismatches** | **247** | **0** |
| Negative `outstanding_amount` rows | 312 | 0 |

All 247 original mismatches (and all 312 negative balances) were rows with
`duplicate_invoice_id_flag = True`; none occurred on unique IDs. **There is no payment recording error.**

**Payment status vs actual money (reliable rows).** All five consistency tests return 0:
no Paid invoice is under- or over-paid, no Unpaid invoice has payments, and no Partially Paid
invoice is fully paid or unpaid.

> [!CAUTION]
> **Open issue UI-05 (driven by UI-01):** The 393 repeated-ID invoices (272 Paid, 82 Partially Paid,
> 39 Unpaid) have no reliable payment total, and `row_key` cannot fix this because payments reference
> only `invoice_id`. Their payments cannot be attributed until Finance/IT renumber the IDs at source.
> Exclude them from payment-aging and outstanding calculations, or report them separately.

### 7.5 Payment Coverage by Invoice Status (reliable rows)

| Payment Status | Has Payment Record | No Payment Record | Reliable Rows | Excluded (repeated ID) | Total Rows |
|---|---:|---:|---:|---:|---:|
| Paid | 12,264 | 0 | 12,264 | 272 | 12,536 |
| Partially Paid | 3,578 | 0 | 3,578 | 82 | 3,660 |
| Unpaid | 0 | 1,798 | 1,798 | 39 | 1,837 |
| **Total** | **15,842** | **1,798** | **17,640** | **393** | **18,033** |

Payment records exist for every Paid and Partially Paid invoice and for no Unpaid invoice, as expected.

### 7.6 Date Type Coercions

All 12 date columns were parsed from string to `datetime64` with **zero new nulls introduced**.

| Dataset | Column | Type After | Pre-Nulls | Post-Nulls | New Nulls |
|---|---|---|---:|---:|---:|
| `customers` | `customer_since` | datetime64[us] | 0 | 0 | 0 ✅ |
| `customers` | `last_purchase_date` | datetime64[us] | 0 | 0 | 0 ✅ |
| `invoices` | `invoice_date` | datetime64[us] | 0 | 0 | 0 ✅ |
| `invoices` | `due_date` | datetime64[us] | 0 | 0 | 0 ✅ |
| `payments` | `payment_date` | datetime64[us] | 0 | 0 | 0 ✅ |
| `products` | `last_purchase_date` | datetime64[us] | 0 | 0 | 0 ✅ |
| `purchase_orders_header` | `order_date` | datetime64[us] | 0 | 0 | 0 ✅ |
| `purchase_orders_header` | `expected_delivery_date` | datetime64[us] | 0 | 0 | 0 ✅ |
| `purchase_orders_header` | `received_date` | datetime64[us] | 2,370 | 2,370 | 0 ✅ |
| `sales_orders_header` | `order_date` | datetime64[us] | 0 | 0 | 0 ✅ |
| `sales_orders_header` | `delivery_date` | datetime64[us] | 0 | 0 | 0 ✅ |
| `stock_ledger` | `movement_date` | datetime64[us] | 0 | 0 | 0 ✅ |

---

## 8. Task 7 — Before/After Quality Comparison

| Dataset | Rows Before | Rows After | Row Δ | Missing Before | Missing After | New Columns |
|---|---:|---:|---:|---:|---:|---:|
| `branches` | 6 | 6 | 0 | 0 | 0 | 0 |
| `customers` | 500 | 500 | 0 | 0 | 0 | 0 |
| `inventory_master` | 180 | 180 | 0 | 0 | 0 | 0 |
| `invoices` | 18,033 | 18,033 | 0 | 0 | 0 | **+2** |
| `payments` | 19,257 | 19,257 | 0 | 0 | 0 | **+2** |
| `products` | 30 | 30 | 0 | 0 | 0 | 0 |
| `purchase_orders_header` | 24,000 | 24,000 | 0 | 2,370 | 2,370 | 0 |
| `purchase_orders_lines` | 155,495 | 155,495 | 0 | 0 | 0 | 0 |
| `sales_orders_header` | 20,000 | 20,000 | 0 | 0 | 0 | 0 |
| `sales_orders_lines` | 130,402 | 130,402 | 0 | 0 | 0 | 0 |
| `stock_ledger` | 237,230 | 237,230 | 0 | 0 | 0 | 0 |
| `suppliers` | 8 | 8 | 0 | 0 | 0 | 0 |

**Columns added:**
- `invoices`: `row_key` (surrogate integer), `duplicate_invoice_id_flag` (boolean)
- `payments`: `row_key` (surrogate integer), `duplicate_payment_id_flag` (boolean)

**Zero rows deleted from any dataset.**

---

## 8A. Task 8 — Merged Datasets Rebuilt (added in revision 2)

The five merged analytical files are now built in the notebook (Task 8) with a row-count assertion
after every join (`validate="many_to_one"`).

| File | Grain | Rows |
|---|---|---:|
| `sales_orders_full.csv` | SO line | 130,402 |
| `purchase_orders_full.csv` | PO line | 155,495 |
| `invoices_with_payments.csv` | invoice `row_key` | 18,033 |
| `inventory_with_ledger.csv` | (product, branch) | 180 |
| `stock_ledger_enriched.csv` | movement | 237,230 |

**Corrections to the earlier merged files**

| Issue | Earlier merged file | Corrected |
|---|---|---|
| `line_profit` | `line_total × margin_percentage` — wrong on all 130,402 rows (`margin_percentage` is a markup on cost, not a margin on price). Total profit 7.06B, margin 27.8% | `quantity × (unit_price − unit_cost)`. Total profit **5.49B, margin 21.6%** |
| Total paid | 23.83B (inflated by repeated invoice IDs) | 22.80B on reliable rows; ties to payments file |
| `outstanding_amount` | 312 negative values | 0 negative; null where payments are unreliable |
| Overdue logic | Fixed date hidden in code; counted any non-Paid status | Explicit `as_of_date` column (latest invoice due date); overdue only if outstanding > 0 and payments reliable |
| Ledger "latest balance" | Tie-broken by `movement_id` | Tie-broken by file position |

**Validation of merged outputs:** 9 of 9 tests pass (row counts, `line_total` sums, `line_profit` formula on every
row, margin ≤ 100%, no negative outstanding, total paid ≤ payments file, overdue implies unpaid).

> [!NOTE]
> The rebuilt merged files carry fewer columns than the earlier versions (inventory 22 vs 39, ledger 15 vs 26,
> sales 42 vs 41, invoices 36 vs 35). Additional branch/product attributes can be added back if needed.

---

## 9. Validation Checklist

| # | Check | Result | Detail |
|---|---|---|---|
| 1 | All 12 datasets loaded, row counts match Week-1 | ✅ PASS | 605,141 rows |
| 2 | Missing `received_date` fully explained by Cancelled status | ✅ PASS | 2,370 nulls = Cancelled only |
| 3 | Repeated `invoice_id`: 0 fully identical duplicate rows | ✅ PASS | 196 IDs flagged; 0 identical |
| 4 | Repeated `payment_id`: 0 fully identical duplicate rows | ✅ PASS | 201 IDs flagged; 0 identical |
| 5 | All 6 candidate PKs unique & non-null | ✅ PASS | 0 failures |
| 6 | All 17 FK relationships: 0 unmatched references | ✅ PASS | 0 failures |
| 7 | Inventory balance reconciliation completed | ✅ PASS | 14 mismatches documented |
| 8 | SO `grand_total` matches line sum (±₹1) | ✅ PASS | 0 mismatches |
| 9 | PO `grand_total` matches line sum (±₹1) | ✅ PASS | 0 mismatches |
| 10 | Paid invoice total ≈ payment amount (±₹1) | ✅ PASS | 0 mismatches on 12,264 reliable Paid invoices (247 before fix, all from UI-01) |
| 11 | Date columns parsed without new nulls | ✅ PASS | 0 warned |
| 12 | All 12 cleaned datasets exported | ✅ PASS | 12 files in `clean/` |

**Score: 12 / 12 checks passed.** Check 10 previously failed (247 mismatches). Root cause was the
join on non-unique `invoice_id` (UI-01), not the payment data; the join is fixed and repeated-ID invoices
are excluded from payment totals. Task 8 adds a ledger-integrity test and 9 merged-output tests, all passing.

---

## 10. Open Issues Log

| Issue ID | Area | Description | Impact | Mitigation | Owner |
|---|---|---|---|---|---|
| **UI-01** | Invoices | 196 `invoice_id` values shared across distinct transactions (393 rows) | Payments cannot be attributed to these invoices; aggregating by ID double-counts; drives UI-05 | Payments joined only to unique IDs; repeated IDs flagged `payment_total_reliable = False` | Finance / IT |
| **UI-02** | Payments | 201 `payment_id` values shared across distinct transactions | Payment totals incorrect if ID treated as unique | Use `row_key`; filter on `duplicate_payment_id_flag` | Finance / IT |
| **UI-03** | Inventory | 14 product–branch pairs: `current_stock` ≠ ledger balance | Incorrect stock levels in reorder and valuation | Use ledger `running_balance` (ordered by date, file position); confirm `ADJUSTMENT` sign convention | Warehouse / Ops |
| **UI-04** | Purchase Orders | 2,370 null `received_date` for Cancelled POs (treated as expected by design) | Low — exclude Cancelled from lead-time KPIs | Document business rule; filter in KPI queries | Procurement |
| **UI-05** | Invoice–Payment match | 393 repeated-ID invoices have no reliable payment total (247 false mismatches before fix, all caused by UI-01) | Outstanding/aging excludes these rows (₹ value of these invoices to be reported separately) | Excluded via `payment_total_reliable`; resolve by renumbering IDs at source | Finance |

---

## 11. Cleaning Decisions Record

| Task | Dataset | Action | Records Affected | Decision |
|---|---|---|---|---|
| Task 2 | `purchase_orders_header` | Investigated 2,370 null `received_date` values | 2,370 | Retain — null is valid for Cancelled status |
| Task 3-A | `invoices` | Investigated 196 repeated `invoice_id` values | 393 | Retain + added `row_key` and `duplicate_invoice_id_flag` |
| Task 3-B | `payments` | Investigated 201 repeated `payment_id` values | 403 | Retain + added `row_key` and `duplicate_payment_id_flag` |
| Task 4 | Multiple | Validated 6 PKs and 17 FKs | 0 | No action required |
| Task 5 | `inventory_master` + `stock_ledger` | Reconciled 180 balance pairs | 14 | Document; await business sign-off on authoritative source |
| Task 6-D | Multiple | Parsed 12 date columns to `datetime64` | 0 new nulls | Date types corrected in cleaned copies |
| Task 6-C | `invoices` + `payments` | Root-cause analysis of 247 mismatches; join corrected | 247 mismatches, 393 rows unreliable | Fixed: payments attached only to unique `invoice_id`; repeated IDs NaN + `payment_total_reliable = False` |
| Task 5 | `stock_ledger` | Latest-balance tie-break changed from `movement_id` to file position | 0 (14 mismatches unchanged) | `movement_id` is not chronological |
| Task 8-A | `stock_ledger` | Running-balance chain test | 1,222 `ADJUSTMENT` rows | All breaks are unsigned adjustments; IN/OUT chain correctly |
| Task 8-B | merged outputs | Rebuilt 5 merged datasets | 130,402 sales lines | `line_profit` corrected; safe payment join; 9/9 tests pass |

---

## 12. Output Files

All outputs are in `reports/week_02/`.

| File | Description | Size |
|---|---|---|
| `clean/branches_clean.csv` | Cleaned branches | 0.8 KB |
| `clean/customers_clean.csv` | Cleaned customers (datetime cols) | 57 KB |
| `clean/inventory_master_clean.csv` | Cleaned master | 6.6 KB |
| `clean/invoices_clean.csv` | Cleaned invoices + `row_key` + flag | 1,853 KB |
| `clean/payments_clean.csv` | Cleaned payments + `row_key` + flag | 1,176 KB |
| `clean/products_clean.csv` | Cleaned products (datetime col) | 4.6 KB |
| `clean/purchase_orders_header_clean.csv` | Cleaned PO header (datetime cols) | 2,521 KB |
| `clean/purchase_orders_lines_clean.csv` | Cleaned PO lines | 10,575 KB |
| `clean/sales_orders_header_clean.csv` | Cleaned SO header (datetime cols) | 2,043 KB |
| `clean/sales_orders_lines_clean.csv` | Cleaned SO lines | 6,904 KB |
| `clean/stock_ledger_clean.csv` | Cleaned ledger (datetime col) | 14,532 KB |
| `clean/suppliers_clean.csv` | Cleaned suppliers | 1.0 KB |
| `task1_baseline_comparison.csv` | Week-1 vs current row counts | 0.5 KB |
| `task2_received_date_status_analysis.csv` | PO status × date cross-tab | 0.1 KB |
| `task3a_invoice_id_duplicate_analysis.csv` | 196 repeated invoice ID detail | 4.9 KB |
| `task3b_payment_id_duplicate_analysis.csv` | 201 repeated payment ID detail | 4.2 KB |
| `task4a_primary_key_validation.csv` | PK uniqueness results | 0.4 KB |
| `task4b_foreign_key_validation.csv` | FK integrity results (17 rels.) | 1.2 KB |
| `task5_inventory_balance_reconciliation.csv` | Full 180-pair comparison | 8.9 KB |
| `task5_inventory_balance_mismatches.csv` | 14 mismatch rows | 0.8 KB |
| `task6_date_coercion_summary.csv` | Date parse results | 0.8 KB |
| `task6_integration_validation_summary.csv` | SO/PO/Inv integration | 0.3 KB |
| `task6c_paid_invoice_payment_mismatches.csv` | 247 root-cause detail (naive join) | 16.3 KB |
| `task6c_payment_status_consistency.csv` | Payment status vs actual payments (reliable rows) | 0.2 KB |
| `merged/sales_orders_full.csv` | Merged sales lines, corrected `line_profit` | 45.0 MB |
| `merged/purchase_orders_full.csv` | Merged PO lines | 57.3 MB |
| `merged/invoices_with_payments.csv` | Invoices + safe payment join | 5.5 MB |
| `merged/inventory_with_ledger.csv` | Inventory + ledger balance | 25 KB |
| `merged/stock_ledger_enriched.csv` | Enriched ledger | 27.5 MB |
| `merged/merged_datasets_manifest.csv` | Merged dataset manifest | 0.2 KB |
| `task7_before_after_quality_comparison.csv` | Before/after metrics | 0.6 KB |
| `task7_clean_export_manifest.csv` | Cleaned export manifest | 0.6 KB |
| `task7_cleaning_audit_log.csv` | Full cleaning decision log | 1.5 KB |
| `task7_week2_validation_checklist.csv` | 12-item pass/fail checklist | 1.2 KB |
| `task7_unresolved_issues.csv` | 5 open issues register | 1.7 KB |

---

## 13. Conclusion

Week 2 completed a thorough investigation, cleaning, integration, and validation of the 
Heavy Supplier Analytics datasets. The pipeline is clean: **zero records were deleted**,
**zero dates were invented**, and **every decision was recorded in the audit log**.

The most significant finding is the **non-unique identifier defect** affecting
`invoices` (196 IDs) and `payments` (201 IDs). These have been flagged and mitigated
with surrogate keys and by excluding the affected rows from payment totals. Resolving this at the source system is the highest-priority action
before Week-3 financial analytics can be considered fully reliable.

The **inventory balance reconciliation** revealed 14 small discrepancies
between the operational snapshot (`inventory_master`) and the transactional ledger
(`stock_ledger`). These are documented and will inform the choice of balance source
in Week-3 analytics.

**All datasets are ready for Week-3 analytical use** from the `clean/` folder,
with the following caveats:
- For invoices and payments: use `payment_total_reliable` — payment totals, outstanding amounts and aging are valid only for the 17,640 unique-ID invoices. Never join payments to invoices on a repeated `invoice_id`; `row_key` alone cannot attribute payments.
- For sales profit: use the corrected `line_profit` (`quantity × (unit_price − unit_cost)`); `margin_percentage` is a markup, not a margin.
- For inventory balances: prefer `stock_ledger.running_balance` (ordered by date then file position, never `movement_id`); treat `ADJUSTMENT` quantities as unsigned until the sign convention is confirmed.
- Exclude `po_status = Cancelled` from lead-time KPIs.

**Next (Week 3):** Supplier performance metrics, inventory turnover analysis,
payment aging, financial KPI dashboards, and reorder alert models.