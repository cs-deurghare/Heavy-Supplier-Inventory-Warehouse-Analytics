# Sprint Notes — Week 2

**Sprint focus:** Data integration — merging Sales/Customer/Supplier and Product/Inventory/Branch data into one validated dataset, and re-validating the merged outputs.

---

## 1. What Was Done

- Merged `sales_orders_header`, `sales_orders_lines`, `customers`, `products`, `suppliers`, and `invoices` into a single sales-side table (130,402 rows), with every join validated to prevent accidental row duplication.
- Combined the sales-side merge with `dim_product_inventory.csv` (product, inventory, and branch data) to produce the team's final `merged_dataset.csv` — 130,402 rows, 72 columns.
- Documented every join decision and key in a join log, alongside pass/fail validation checks.
- Independently re-validated the merged datasets against the cleaned source files (row counts, keys, totals, derived fields) and corrected the cleaning notebook so the fixes are reproducible. All 12 notebook checks now pass, and 9 of 9 checks on the rebuilt merged files pass.

## 2. Issues Found and How We Treated Them

| Issue | Detail | Resolution |
| :--- | :--- | :--- |
| **Duplicate invoice records** | 196 `invoice_id` values (393 rows) were shared by different transactions (different order, customer, date and amount), so they are not true duplicates | Flagged with `duplicate_invoice_id_flag`; none deleted. Payments are not attached to these invoices (see next row) |
| **Payments inflated by repeated invoice IDs** | Payments were joined on `invoice_id`, so each row sharing a repeated ID received the combined payments of all of them. Total paid was overstated by about ₹518M (23.83B vs 23.31B in the payments file). This caused 247 false "Paid" mismatches and 312 negative outstanding balances | Payments are now joined only to unique `invoice_id`s. The 393 repeated-ID rows get empty payment fields and `payment_total_reliable = False`. Mismatches are now 0, and total paid ties exactly to the payments file. Needs a Finance/IT fix at source (renumber IDs) |
| **Incorrect `line_profit`** | Profit was calculated from `margin_percentage`, which in the products table is a markup on cost, not a margin on price. This overstated profit on all 130,402 sales lines (7.06B, 27.8% margin) | Recalculated as `quantity × (unit_price − unit_cost)`: 5.49B profit, 21.6% margin. **To confirm:** whether `merged_dataset.csv` uses the same profit calculation |
| **Column name collisions** | `branch_id` and `payment_terms` existed in two different tables with different meanings (order's fulfilling branch vs. customer's home branch) | Renamed explicitly after merging (`branch_id` / `customer_home_branch_id`, `order_payment_terms` / `customer_payment_terms`) to remove ambiguity |
| **Row-count inflation in an early draft** | An initial `merged_dataset.csv` uploaded to the repo had ~782,000 rows instead of the expected ~130,000 — traced to a join without a uniqueness check, which multiplied rows instead of matching them 1:1 | Rebuilt using `validate='many_to_one'` on every merge, which raises an error instead of silently duplicating rows when a key isn't unique |
| **Floating-point precision artifacts** | Monetary columns (`gst_amount`, `grand_total`, `line_grand_total`, `total_gst_amount`, `invoice_grand_total`, `total_paid`) contained values like `28392.000000000004` instead of `28392`, from floating-point arithmetic during GST calculations | Rounded all monetary float columns to 2 decimal places across both the sales merge and the final merged dataset |
| **Ledger ordering** | Ordering stock movements by `movement_id` is wrong because IDs are not chronological (56,583 false breaks in running balance). In date and file order the ledger is consistent; the only breaks are 1,222 `ADJUSTMENT` rows, whose quantity is unsigned although about half reduce stock | Ordering changed to date, then file position. Sign convention for `ADJUSTMENT` to be confirmed by Warehouse/Ops |
| **Stock mismatches (carried from Week 1)** | 6 discrepancies remained between `stock_ledger` and `inventory_master` after initial reconciliation — 3 original, 3 introduced during corrections. **Note:** re-running on the cleaned source files gives 14 mismatched product–branch pairs (range −515 to +299 units), so the two counts need reconciling | Flagged for the Data Analyst to re-run validation on the corrected data and confirm the final count |

## 3. Team Collaboration

- Sales/customer/supplier merge and documentation: BI Analyst (Salim)
- Product/inventory/branch merge: BI Analyst (Chandrashekhar)
- Field-level cleaning and stock mismatch investigation: Data Analyst (Olufunmilola)
- Merged dataset structure review: Data Scientist (Abdibasid)
- Corrected files were shared via Google Drive for full team review before being pushed to GitHub, so everyone validated the final dataset before submission.

## 4. Status

Week 2 deliverables are complete, reviewed by the team, and ready for submission. The corrected `merged_dataset.csv` (with the row-duplication and precision issues fixed) replaces the earlier draft in the repository.

**Open items before sign-off**
- Confirm `merged_dataset.csv` uses the corrected `line_profit` and the safe payment join.
- Finance/IT: fix the 196 repeated invoice IDs (and 201 repeated payment IDs) at source.
- Warehouse/Ops: confirm the `ADJUSTMENT` sign convention and the authoritative stock source.
- Data Analyst: reconcile the 6 vs 14 stock mismatch counts.