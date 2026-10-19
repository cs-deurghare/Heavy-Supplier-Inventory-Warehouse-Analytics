# Heavy Supplier, Inventory & Warehouse Analytics

![Project](https://img.shields.io/badge/Project-Heavy%20Supplier%20Analytics-blue?style=for-the-badge)
![Sprint](https://img.shields.io/badge/Sprint-Week%2003%20Complete-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Validated-success?style=for-the-badge)

A CadetX Virtual Work Experience project analyzing a heavy machinery supplier's sales, inventory, purchasing, and warehouse operations across 12 relational data tables, to support data-driven decisions on stock management, supplier performance, and customer value.

---

## 1. Project Overview

This repository holds the code, cleaned data, documentation, and findings produced by the team over the course of a 12-week programme. Week 1 focused on **profiling, cleaning, and validating** the raw dataset. Week 2 **merged and integrated** the data into a single analysis-ready dataset. Week 3 built the first round of **KPI calculations**, closed a data gap found in the Week 2 merge, and locked the analysis questions for Phase 2.

**Dataset:** 12 source tables covering sales orders, customers, products, suppliers, purchase orders, invoices, payments, stock ledger, branches, and inventory.

---

## 2. Team

This project is delivered by a four-person analytics team working in an agile sprint structure with rotating weekly leadership:

| Name | Role | Focus |
| :--- | :--- | :--- |
| Chandrashekhar Deurghare | BI Analyst | Product, inventory, and warehouse data integration and reporting |
| Salim Bello Muhammad | BI Analyst | Sales, customer, and supplier data integration and reporting |
| Ibrahim Khalil umar | Data Analyst | Data quality, field-level cleaning, and validation |
| Abdibasid Mohamed Ali | Data Scientist | Dataset structure review and forecasting readiness |

Leadership of each weekly sprint rotates across the team.

---

## 3. Week 1 Deliverables

| Deliverable | Description |
| :--- | :--- |
| `01_profiling_cleaning_validation.ipynb` | Jupyter notebook profiling all 12 tables, cleaning key fields, and running validation checks |
| `data_dictionary_DRAFT.md` | Column-level data dictionary covering all 12 tables |
| `kpi_proposal.md` | Proposed KPIs and analysis questions for the project |
| `sprint_notes_week01.md` | Sprint progress notes and task log |
| `processed_data/` | Cleaned versions of all 12 source tables, ready for downstream merging and analysis |

---

## 4. What We Did (Week 1)

- **Profiled** every table: row/column counts, data types, missing values, and duplicate checks.
- **Cleaned** key fields: converted date columns to proper datetime format, trimmed whitespace from text fields, and parsed numeric values out of mixed text fields (e.g. extracting `45230` from `"45230 sqft"` in `warehouse_capacity_sqft`).
- **Validated** the cleaned data with 20 explicit checks (pass/fail), rather than assuming the data was clean after one pass.

---

## 5. Week 1 Key Findings & How We Treated Them

| Finding | What We Found | How We Treated It |
| :--- | :--- | :--- |
| **Duplicate invoice records** | 197 `invoice_id` values appeared more than once in the invoices table | Flagged and set aside rather than merged blindly, to avoid silently duplicating rows in any table that joins on `invoice_id`. Documented for the team before any merge work began. |
| **Stock discrepancies** | 14 mismatches between `stock_ledger` cumulative quantities and `inventory_master` recorded balances | Investigated by recalculating cumulative inflows/outflows from the stock ledger (sorted chronologically) and comparing against recorded balances, to confirm which figures were reliable before using either table downstream. |
| **Mixed-format numeric fields** | Some numeric fields (e.g. warehouse capacity) were stored as text with units attached | Extracted the numeric value programmatically rather than dropping or guessing at the field. |
| **Inconsistent date formats** | Date fields varied in format across tables | Standardized all date fields using safe, error-tolerant conversion, with any unparseable dates flagged rather than silently discarded. |

All findings and decisions are documented in the Week 1 notebook and sprint notes so the reasoning is traceable, not just the result.

---

## 6. Week 2 Deliverables

| Deliverable | Description |
| :--- | :--- |
| `02_sales_customer_supplier_merge.ipynb` | Notebook merging sales orders, customers, suppliers, and invoices into one table |
| `03_final_integration.ipynb` | Notebook combining the sales-side merge with product, inventory, and branch data |
| `merged_dataset.csv` (split by year) | Combined dataset — sales, customer, product, inventory, and branch data in one table (130,402 rows, 72 columns) |
| `sprint_notes_week02.md` | Sprint progress notes, issues found, and how each was resolved |
| `join_log_week02.csv` / validation files | Documented join keys and pass/fail validation checks |

### Week 2 Findings & How We Treated Them

| Finding | What We Found | How We Treated It |
| :--- | :--- | :--- |
| **Column name collisions** | `branch_id` and `payment_terms` appeared in two tables with different meanings | Renamed explicitly after merging to remove ambiguity |
| **Row-count inflation** | An early merge produced ~782,000 rows instead of the expected ~130,000, from a join without a uniqueness check | Rebuilt using `validate='many_to_one'` on every merge to catch non-unique keys instead of silently duplicating rows |
| **Floating-point precision artifacts** | Monetary columns contained values like `28392.000000000004` instead of `28392` | Rounded all monetary columns to 2 decimal places across the dataset |
| **Stock discrepancies (carried from Week 1)** | 6 mismatches remained between `stock_ledger` and `inventory_master` | Flagged for re-validation after corrections |

---

## 7. Week 3 Deliverables

| Deliverable | Description |
| :--- | :--- |
| `merged_dataset.csv` (full + split by year) | **Rebuilt** from all 10 raw source tables to close the supplier data gap found this week — now 130,402 rows, 89 columns, with supplier fields populated on 100% of rows |
| `03_kpi_calculations.ipynb` | Reproducible notebook covering sales/customer, product/inventory/warehouse, and supplier KPIs, executed end-to-end with no errors |
| `data_dictionary.md` | Updated to document all 89 columns, the new supplier fields, and every column renamed to resolve cross-table name collisions |
| `analysis_questions_locked.md` | 13 analysis questions locked for Phase 2 (Weeks 4–6), across sales, customer, product/inventory, operations, and data quality |
| `sprint_notes_week03.md` | Sprint progress notes, issues found, and how each was resolved |
| `sales_kpi_summary.md` / `inventory_kpi_summary.md` | Write-ups of the sales/customer and product/inventory/warehouse KPI results |
| `kpi_supplier_mix.csv` + other `kpi_*.csv` files | KPI result tables |
| `validation_report_week03.csv` | Pass/fail validation checks for the Week 3 dataset and KPIs |
| `exploratory_charts/` | Revenue, lead time, product, inventory turnover, and supplier mix charts |

### What We Did (Week 3)

- Calculated top-line and segmented **sales/customer KPIs**: total revenue, average order value, revenue by year/customer type/region, delivery lead time, top products, and payment status breakdown.
- Calculated **product, inventory & warehouse KPIs**: inventory turnover ratio per product, a stock health classification, and warehouse capacity by branch.
- **Found and fixed a data gap carried from Week 2:** the merged dataset had no supplier information at all. Traced the root cause, rebuilt the merge with supplier data correctly joined in, and calculated the supplier mix KPI that had been blocked.
- Finalized a single data dictionary and a locked set of analysis questions for Phase 2.
- Ran a validation report confirming row counts, data types, the resolved supplier join, and no ambiguous merge columns.

### Week 3 Findings & How We Treated Them

| Finding | What We Found | How We Treated It |
| :--- | :--- | :--- |
| **Supplier data missing** | No `supplier_id` or `supplier_name` column existed anywhere in the merged dataset, despite earlier documentation describing a supplier join | **Resolved.** Root cause: `purchase_orders_header` has no `product_id`, so the only valid path from a product to its supplier is `purchase_orders_lines` → `purchase_orders_header` → `suppliers`. This join existed in an earlier revision of the Week 2 notebook but was never carried into the final table. Rebuilt the full merge from all 10 raw tables with the join included; supplier fields now populated on 100% of rows, each product's supplier assigned from its most recent purchase order |
| **`current_stock` vs. `max_stock` scale mismatch** | `current_stock` sits in the ~88,000–121,000 range, while `max_stock` / `reorder_level` / `safety_stock` sit in the tens-to-low-hundreds range — a direct comparison marks every row as "Overstock" | Adopted a quantile-based stock health classification (25th/75th percentile of `current_stock`) as the finalized method for this submission; tracing the scale mismatch to its source is carried forward as a Phase 2 question |
| **`payment_status` reverted to blank** | A later copy of the dataset had `payment_status` blank again for orders with no matching invoice, despite this being fixed and agreed in Week 2 | Reapplied the "Not Invoiced" label before running KPIs |
| **Column name collisions from the full rebuild** | Rebuilding the merge from all 10 raw tables surfaced ambiguous columns (e.g. `city`, `region`, `lead_time_days`, `unit_price` exist in more than one source table) | Every colliding column explicitly renamed before merging (e.g. `customer_city`, `supplier_region`, `product_lead_time_days`) — zero ambiguous columns in the final file |
| **9.0% of orders fully unpaid** | Found during the payment status breakdown, not previously quantified | Documented and flagged for financial reconciliation review in Phase 2 |

---

## 8. Tools Used

- **Python 3** with **pandas** for profiling, cleaning, merging, and validation
- **Jupyter Notebook** for a documented, reproducible workflow
- **matplotlib** / **seaborn** for exploratory charts
- **GitHub** for version control and team collaboration

---

## 9. Repository Structure

```
├── processed_data/          # Cleaned tables, ready for merging and analysis
├── raw_data/                # Original source tables
├── week-01/                 # Week 1 notebook, data dictionary, KPI proposal, sprint notes
├── week-02/                 # Week 2 deliverables, data dictionary, dim product inventory, sprint notes
├── week-03/                 # Week 3 KPI notebook, updated data dictionary, locked analysis questions, sprint notes
└── README.md
```

---

## 10. Status

Weeks 1 through 3 are complete, validated, and submitted. The Week 3 `merged_dataset.csv` (with supplier data included) is the current authoritative dataset and the base for all Phase 2 work. Two items are carried forward as Phase 2 analysis questions rather than open issues: tracing the `current_stock` scale mismatch to its source, and the 6 `stock_ledger` vs. `inventory_master` mismatches carried from earlier weeks.
Week 1 and Week 2 deliverables are complete, validated, and submitted. Subsequent weeks build directly on the cleaned, merged, and validated data established here.
