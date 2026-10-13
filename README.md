# Heavy Supplier, Inventory & Warehouse Analytics

![Project](https://img.shields.io/badge/Project-Heavy%20Supplier%20Analytics-blue?style=for-the-badge)
![Sprint](https://img.shields.io/badge/Sprint-Week%2002%20Complete-brightgreen?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Validated-success?style=for-the-badge)

A CadetX Virtual Work Experience project analyzing a heavy machinery supplier's sales, inventory, purchasing, and warehouse operations across 12 relational data tables, to support data-driven decisions on stock management, supplier performance, and customer value.

---

## 1. Project Overview

This repository holds the code, cleaned data, documentation, and findings produced by the team over the course of a 12-week programme. Week 1 focused on **profiling, cleaning, and validating** the raw dataset. Week 2 built on that foundation to **merge and integrate** the data into a single analysis-ready dataset.

**Dataset:** 12 source tables covering sales orders, customers, products, suppliers, purchase orders, invoices, payments, stock ledger, branches, and inventory.

---

## 2. Team

This project is delivered by a four-person analytics team working in an agile sprint structure with rotating weekly leadership:

| Name | Role | Focus |
| :--- | :--- | :--- |
| Chandrashekhar Deurghare | BI Analyst | Product, inventory, and warehouse data integration and reporting |
| Salim Bello Muhammad | BI Analyst | Sales, customer, and supplier data integration and reporting |
| Olufunmilola Florence Peters | Data Analyst | Data quality, field-level cleaning, and validation |
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

## 4. What We Did

- **Profiled** every table: row/column counts, data types, missing values, and duplicate checks.
- **Cleaned** key fields: converted date columns to proper datetime format, trimmed whitespace from text fields, and parsed numeric values out of mixed text fields (e.g. extracting `45230` from `"45230 sqft"` in `warehouse_capacity_sqft`).
- **Validated** the cleaned data with 20 explicit checks (pass/fail), rather than assuming the data was clean after one pass.

---

## 5. Key Findings & How We Treated Them

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
| `merged_dataset.csv` (split by year) | Final combined dataset — sales, customer, supplier, product, inventory, and branch data in one table (130,402 rows, 72 columns) |
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

## 7. Tools Used

- **Python 3** with **pandas** for profiling, cleaning, and validation
- **Jupyter Notebook** for a documented, reproducible workflow
- **GitHub** for version control and team collaboration

---

## 8. Repository Structure

```
├── week-01/                 # Week 1 notebook, data dictionary, KPI proposal, sprint notes
├── week02/                  # Week 2 deliverables
├── processed_data/          # Cleaned tables, ready for merging and analysis
├── raw_data/                # Original source tables
└── README.md
```

---

## 9. Status

Week 1 and Week 2 deliverables are complete, validated, and submitted. Subsequent weeks build directly on the cleaned, merged, and validated data established here.
