# Sprint Notes — Week 02

**Role:** Scrum Master & BI Analyst  
**Owner:** Chandrashekhar  
**Team Members:** Salim, Olufunmilola, Abdibasid  
**Sprint Focus:** ERP Data Cleaning, Dimensional Merging, & Master Dataset Integration  

---

## 1. Executive Summary
During Week 02, the team successfully executed data integration across 12 raw ERP tables. As Scrum Master and Lead BI Analyst, Chandrashekhar led the technical pipeline execution, created core dimensions, resolved join dependencies, and finalized `merged_dataset.csv` alongside all sprint documentation.

---

## 2. Team Member Allocations & Contributions

### A. Chandrashekhar (Scrum Master & Lead BI Analyst)
- **Primary Task:** Dimension Table Creation & Overall Pipeline Assembly.
- **Key Deliverables:** 
  - Merged `inventory_master`, `products`, and `branches` tables into `dim_product_inventory.csv`.
  - Resolved overlapping column issues (`reorder_level_x`, `safety_stock_x`) by dropping redundant fields.
  - Assembled the master integration notebook (`02_data_integration_validation.ipynb`) and finalized `merged_dataset.csv`.

### B. Salim (BI Analyst / Data Integration Specialist)
- **Primary Task:** Sales, Customer, and Supplier Module Integration.
- **Key Deliverables:** 
  - Merged `sales_orders_lines` with `sales_orders_header` using `so_id`.
  - Joined Customer profiles (`customers`) and Supplier references (`suppliers`) to the transaction base.
  - Prepared the sales pipeline base for final master assembly.

### C. Olufunmilola (Data Analyst / Quality Assurance)
- **Primary Task:** Data Cleaning & Schema Validation.
- **Key Deliverables:**
  - Audited raw datasets for data type inconsistencies, duplicates, and missing values.
  - Standardized customer type classifications and transaction date formats across tables.

### D. Abdibasid (Data Analyst / Financial Reconciliation)
- **Primary Task:** Invoice Reconciliation & Purchase Order Audit.
- **Key Deliverables:**
  - Audited `invoices` table to handle duplicate `invoice_id` occurrences using composite keys (`invoice_key`).
  - Conducted null value analysis on `purchase_orders_header` (`received_date` fields).

---

## 3. Sprint Goals & Achievement Status
- [x] Merge core dimensions: `inventory_master`, `products`, and `branches` into `dim_product_inventory.csv`.
- [x] Integrate Sales pipeline (`sales_orders_lines`, `sales_orders_header`, `customers`, `invoices`).
- [x] Finalize `merged_dataset.csv` pipeline in `02_data_integration_validation.ipynb`.
- [x] Conduct schema validation and null check verification.
- [x] Finalize `data_dictionary.md` and `sprint_notes_week02.md` documentation.

---

## 3. Key Decisions & Technical Resolution Notes

### A. Null Value Investigation (`received_date`)
- **Finding:** Exactly 2,370 rows in `purchase_orders_header` contained null values in `received_date`.
- **Resolution:** Verified that all null instances correspond strictly to POs with `po_status = 'Cancelled'`. No fake dates (e.g., `1900-01-01`) were imputed to preserve metrics for Supplier Lead Time analytics.

### B. Composite Key Resolution
- **Finding:** Standard invoice joins produced duplicate risks due to multiple line linkages.
- **Resolution:** Maintained composite key structure (`invoice_key = invoice_id + so_id`) ensuring 100% join integrity without revenue inflation.

### C. Overlapping Column Disambiguation
- **Finding:** Redundant attributes (`reorder_level`, `safety_stock`) across `inventory_master` and `products` caused column suffixing (`_x`, `_y`).
- **Resolution:** Cleaned overlapping columns before left-joining to produce clean, production-ready schema naming.

### D. Duplicate Invoice Prevention
- **Finding:** Joins on `invoice_id` alone risk revenue duplication across multi-line orders.
- **Resolution:** Implemented composite matching on `so_id` to maintain exact line-level financial accuracy.

---

## 4. Final Submission Artifacts
1. `02_data_integration_validation.ipynb` — Full reproducible Python Notebook
2. `dim_product_inventory.csv` — Reusable product-inventory dimension table
3. `merged_dataset.csv` — Comprehensive master analytical dataset
4. `data_dictionary.md` — Schema definition document
5. `sprint_notes_week02.md` — Sprint governance report
