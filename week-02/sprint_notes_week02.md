# Sprint Notes — Week 2

**Sprint focus:** Data integration — merging Sales/Customer/Supplier and Product/Inventory/Branch data into one validated dataset.

---

## 1. What Was Done

- Merged `sales_orders_header`, `sales_orders_lines`, `customers`, `products`, `suppliers`, and `invoices` into a single sales-side table (130,402 rows), with every join validated to prevent accidental row duplication.
- Combined the sales-side merge with `dim_product_inventory.csv` (product, inventory, and branch data) to produce the team's final `merged_dataset.csv` — 130,402 rows, 72 columns.
- Documented every join decision and key in a join log, alongside pass/fail validation checks.

## 2. Issues Found and How We Treated Them

| Issue | Detail | Resolution |
| :--- | :--- | :--- |
| **Duplicate invoice records** | 197 `invoice_id` values appeared more than once | Set aside before merging so they could not silently multiply rows; only unambiguous invoice records were joined in |
| **Column name collisions** | `branch_id` and `payment_terms` existed in two different tables with different meanings (order's fulfilling branch vs. customer's home branch) | Renamed explicitly after merging (`branch_id` / `customer_home_branch_id`, `order_payment_terms` / `customer_payment_terms`) to remove ambiguity |
| **Row-count inflation in an early draft** | An initial `merged_dataset.csv` uploaded to the repo had ~782,000 rows instead of the expected ~130,000 — traced to a join without a uniqueness check, which multiplied rows instead of matching them 1:1 | Rebuilt using `validate='many_to_one'` on every merge, which raises an error instead of silently duplicating rows when a key isn't unique |
| **Floating-point precision artifacts** | Monetary columns (`gst_amount`, `grand_total`, `line_grand_total`, `total_gst_amount`, `invoice_grand_total`, `total_paid`) contained values like `28392.000000000004` instead of `28392`, from floating-point arithmetic during GST calculations | Rounded all monetary float columns to 2 decimal places across both the sales merge and the final merged dataset |
| **Stock mismatches (carried from Week 1)** | 6 discrepancies remained between `stock_ledger` and `inventory_master` after initial reconciliation — 3 original, 3 introduced during corrections | Flagged for the Data Analyst to re-run validation on the corrected data and confirm final counts |

## 3. Team Collaboration

- Sales/customer/supplier merge and documentation: BI Analyst (Salim)
- Product/inventory/branch merge: BI Analyst (Chandrashekhar)
- Field-level cleaning and stock mismatch investigation: Data Analyst (Olufunmilola)
- Merged dataset structure review: Data Scientist (Abdibasid)
- Corrected files were shared via Google Drive for full team review before being pushed to GitHub, so everyone validated the final dataset before submission.

## 4. Status

Week 2 deliverables are complete, reviewed by the team, and ready for submission. The corrected `merged_dataset.csv` (with the row-duplication and precision issues fixed) replaces the earlier draft in the repository.
