# Week 1: Data Profiling Report

## Heavy Supplier, Inventory & Warehouse Analytics

**Report type:** Data Profiling and Quality Assessment  
**Project phase:** Phase 1 — Foundation & Exploration  
**Reporting period:** Week 1  
**Status:** Initial profiling completed; selected data-quality issues require further investigation.

---

## 1. Executive Summary

This report documents the initial data profiling of the Heavy Supplier, Inventory & Warehouse Analytics project. The objective was to understand the structure, completeness, uniqueness, and relationships of the available datasets before proceeding with data cleaning, integration, and business analytics.

The profiling covered **12 CSV datasets containing 704,733 records** in total.

The initial assessment identified missing values in purchase order headers, repeated identifiers in the invoices and payments datasets, repeated product identifiers in the inventory master, and relationships between operational tables that passed basic reference checks.

No exact duplicate rows were identified during the initial profiling.

The results provide a foundation for improving data reliability before developing inventory, supplier, warehouse, customer, and financial performance analyses.

### Key Findings

| Profiling area | Finding |
|---|---|
| Number of datasets | 12 CSV files |
| Total records | 704,733 |
| Exact duplicate rows | None identified |
| Missing cells | 2,370 |
| Main missing-value issue | `received_date` in `purchase_orders_header` |
| Repeated invoice identifiers | 196 distinct identifiers |
| Repeated payment identifiers | 201 distinct identifiers |
| Relationship checks | 17 candidate relationships passed basic reference checks |
| Main follow-up | Investigate identifier uniqueness and business rules |

**Important:** Passing a basic relationship check does not prove that a relationship is fully valid. Parent-key uniqueness, business meaning, and expected table grain must also be reviewed.

---

## 2. Project Objectives

The Week 1 profiling exercise was designed to:

1. Understand the structure and size of each dataset.
2. Identify missing values and assess their distribution.
3. Detect exact duplicate rows and repeated identifiers.
4. identify candidate primary keys and foreign-key relationships.
5. Validate whether child records reference existing parent records.
6. Document data-quality risks that could affect future analysis.
7. Establish priorities for data cleaning and integration.

---

## 3. Dataset Overview

The project contains 12 datasets covering business entities, purchasing, inventory, sales, invoices, payments, and stock movements.

| Dataset | Number of records | Primary profiling focus |
|---|---:|---|
| `stock_ledger` | 237,230 | Stock movements and inventory history |
| `purchase_orders_lines` | 155,495 | Purchased products and order-line records |
| `sales_orders_lines` | 130,402 | Products included in sales orders |
| `purchase_orders_header` | 24,000 | Purchase order information |
| `sales_orders_header` | 20,000 | Sales order information |
| `payments` | 19,257 | Payment transactions and identifiers |
| `invoices` | 18,033 | Invoice information and order references |

The remaining datasets include branches, customers, products, suppliers, and inventory master records.

**Note:** The seven datasets above are the largest or most operationally significant tables identified in the initial review. The total record count of 704,733 covers all 12 datasets.

---

## 4. Data Quality Assessment

### 4.1 Missing Values

The initial profiling identified **2,370 missing cells**, all reported in the `received_date` column of `purchase_orders_header`.

| Dataset | Column | Missing values | Total rows | Missing percentage |
|---|---|---:|---:|---:|
| `purchase_orders_header` | `received_date` | 2,370 | 24,000 | 9.88% |

The missing percentage is calculated as:$$\text{Missing Percentage} = \left( \frac{\text{Missing Values}}{\text{Total Rows}} \right) \times 100$$For the purchase order received date:$$\left( \frac{2,370}{24,000} \right) \times 100 \approx 9.88\%$$
**Interpretation:** Approximately 9.88% of purchase order records have no recorded received date. This may affect calculations involving supplier lead time, order completion, and delivery performance.

**Recommended action:**

- Determine whether the missing dates represent orders that have not yet been received, incomplete records, or unavailable historical information.
- Compare the records with purchase order status and related operational data.
- Do not automatically replace missing dates with an average or an arbitrary date.
- Preserve the original value and document any approved cleaning rule.

### 4.2 Exact Duplicate Rows

The initial profiling did not identify any exact duplicate rows across the reviewed datasets.

This is a positive initial finding, but it does not guarantee that every business transaction is unique. Two rows may contain different values while sharing the same transaction identifier.

**Recommended action:** Continue checking business-key uniqueness and potential duplicate transactions during data cleaning.

### 4.3 Repeated Identifiers

Repeated identifiers were identified in the `invoices` and `payments` datasets.

| Dataset | Identifier | Distinct identifiers repeated | Rows involved in repeated identifiers | Occurrences beyond the first |
|---|---|---:|---:|---:|
| `invoices` | `invoice_id` | 196 | 393 | 197 |
| `payments` | `payment_id` | 201 | 403 | 202 |

#### Invoice identifiers

The `invoice_id` field contains 196 distinct identifiers that appear more than once. These repeated identifiers involve 393 rows, with 197 occurrences beyond the first.

This requires investigation because an invoice identifier is commonly expected to identify one invoice. However, the correct rule must be confirmed from the dataset specification and business requirements.

#### Payment identifiers

The `payment_id` field contains 201 distinct identifiers that appear more than once. These repeated identifiers involve 403 rows, with 202 occurrences beyond the first.

Repeated payment IDs could indicate duplicated transactions, identifier-generation problems, or another dataset-specific rule. The available profiling results alone do not establish the cause.

**Recommended actions:**

1. Inspect the complete records for repeated identifiers.
2. Compare dates, amounts, customers, invoice references, and other available transaction attributes.
3. Determine the intended uniqueness rule for each identifier.
4. Confirm whether repeated identifiers are valid before removing any rows.
5. Document the investigation and its final outcome.

### 4.4 Repeated Product Identifiers in Inventory Master

The `inventory_master` dataset contains 180 rows involving 30 distinct repeated `product_id` values, with 150 occurrences beyond the first.

This does not automatically mean the records are incorrect. A product may have inventory records for multiple branches or locations.

**Recommended action:** Check whether the intended unique key is `product_id` alone or a composite key such as `(product_id, branch_id)`. Validate the actual business grain before classifying these rows as duplicates.

---

## 5. Candidate Key Assessment

The following fields were identified as candidate unique identifiers during initial profiling.

| Dataset | Candidate identifier | Expected purpose |
|---|---|---|
| `branches` | `branch_id` | Identifies a branch |
| `customers` | `customer_id` | Identifies a customer |
| `products` | `product_id` | Identifies a product |
| `suppliers` | `supplier_id` | Identifies a supplier |
| `purchase_orders_header` | `po_id` | Identifies a purchase order |
| `sales_orders_header` | `so_id` | Identifies a sales order |

These are candidate keys, not a declaration that all key constraints have been formally enforced.

Before using them in joins or database constraints, verify that each field is non-null and unique within its parent dataset.

The repeated `invoice_id` and `payment_id` values require particular attention before either field is treated as a unique primary key.

---

## 6. Relationship Validation

A total of 17 candidate relationships were evaluated using the supplied relationship validation results.

The reported checks showed:

- Zero missing child-key values across the listed relationships.
- Zero unmatched non-null child values across the listed relationships.

This indicates that the tested child values had matching parent references under the checks performed.

### 6.1 Candidate Relationships

| Child dataset | Child field | Parent dataset | Parent field |
|---|---|---|---|
| `customers` | `branch_id` | `branches` | `branch_id` |
| `inventory_master` | `product_id` | `products` | `product_id` |
| `inventory_master` | `branch_id` | `branches` | `branch_id` |
| `purchase_orders_header` | `supplier_id` | `suppliers` | `supplier_id` |
| `purchase_orders_header` | `branch_id` | `branches` | `branch_id` |
| `purchase_orders_lines` | `po_id` | `purchase_orders_header` | `po_id` |
| `purchase_orders_lines` | `product_id` | `products` | `product_id` |
| `sales_orders_header` | `customer_id` | `customers` | `customer_id` |
| `sales_orders_header` | `branch_id` | `branches` | `branch_id` |
| `sales_orders_lines` | `so_id` | `sales_orders_header` | `so_id` |
| `sales_orders_lines` | `product_id` | `products` | `product_id` |
| `invoices` | `so_id` | `sales_orders_header` | `so_id` |
| `invoices` | `customer_id` | `customers` | `customer_id` |
| `invoices` | `branch_id` | `branches` | `branch_id` |
| `payments` | `invoice_id` | `invoices` | `invoice_id` |
| `stock_ledger` | `product_id` | `products` | `product_id` |
| `stock_ledger` | `branch_id` | `branches` | `branch_id` |

### 6.2 Interpretation and Limitations

The relationship checks are encouraging, but further validation is necessary.

**Parent-key uniqueness:** A foreign-key relationship normally references a unique parent key. Because repeated `invoice_id` values were identified, the relationship between `payments.invoice_id` and `invoices.invoice_id` requires additional review. Matching values alone do not establish that the parent field is a valid unique key.

**Inventory grain:** The repeated `inventory_master.product_id` values may be expected if inventory is recorded by branch. The correct key should be determined from the business rules.

**Sales-order relationship:** The supplied check for `sales_orders_lines.so_id` against `sales_orders_header.so_id` reported no missing or unmatched child references. This supports the basic validity of that reference, subject to confirming parent-key uniqueness.

**Recommended next step:** Add parent-key uniqueness checks, null checks, and business-rule validation to the relationship report before marking all relationships as fully validated.

---

## 7. Initial Business and Analytical Implications

The profiling findings highlight several areas that could influence later analysis.

| Area | Potential impact | Priority |
|---|---|---|
| Missing received dates | Supplier lead-time and delivery-performance calculations may be incomplete | High |
| Repeated invoice IDs | Invoice counts, revenue summaries, and joins may be inaccurate if duplicates are invalid | High |
| Repeated payment IDs | Payment totals and transaction counts may be affected | High |
| Inventory product IDs | Inventory summaries may be incorrect if the table grain is misunderstood | High |
| Candidate relationships | Joins may multiply records when parent keys are not unique | High |
| Exact duplicate rows | No exact duplicates were identified in the initial review | Monitor |

These are potential impacts, not confirmed business losses or errors. The effect of each issue depends on its cause and the analytical method used.

---

## 8. Recommended Data Cleaning Plan

The following actions are recommended before building the project's analytical models and dashboards.

### Priority 1 — Investigate Critical Quality Issues

- [ ] Review all purchase orders with missing `received_date`.
- [ ] Investigate repeated `invoice_id` values.
- [ ] Investigate repeated `payment_id` values.
- [ ] Confirm whether the candidate parent keys are unique and non-null.
- [ ] Review the `payments` to `invoices` relationship before using it in financial aggregations.

### Priority 2 — Confirm Dataset Structure

- [ ] Define the business grain of every dataset.
- [ ] Confirm primary and composite keys.
- [ ] Document foreign-key relationships.
- [ ] Validate date and numeric data types.
- [ ] Check for invalid values and inconsistent category labels.

### Priority 3 — Prepare for Integration

- [ ] Clean records only after defining and documenting the applicable rules.
- [ ] Preserve original source data.
- [ ] Generate cleaned datasets separately from raw datasets.
- [ ] Re-run data-quality checks after cleaning.
- [ ] Save profiling and validation summaries for reproducibility.

---

## 9. Limitations

This report documents the results currently available from the initial profiling exercise.

The following points remain important:

1. Repeated identifiers have not automatically been classified as invalid transactions.
2. The missing received dates have not yet been assigned a confirmed business explanation.
3. Candidate relationships have passed basic reference checks, but not all have been proven valid under parent-key uniqueness and business rules.
4. No exact duplicate rows were identified, but other forms of duplication may still exist.
5. The profiling results do not, by themselves, establish supplier performance, inventory efficiency, or financial performance.

These limitations should be resolved progressively during data cleaning and integration.

---

## 10. Conclusion

The Week 1 data profiling exercise established an initial understanding of the structure and quality of the Heavy Supplier, Inventory & Warehouse Analytics datasets.

The 12 datasets contain 704,733 records. No exact duplicate rows were identified, while missing received dates and repeated transaction identifiers were highlighted for investigation. The 17 candidate relationships passed basic child-reference checks, but additional uniqueness and business-rule validation is required.

The next phase should focus on resolving or documenting the identified data-quality issues, confirming the intended grain and keys of each dataset, and producing validated datasets suitable for integration and business analytics.

**Week 1 outcome:** Initial data profiling completed. Data cleaning and deeper relationship validation are the next priorities.

---

## Appendix A — Key Definitions

| Term | Definition |
|---|---|
| Data profiling | Examining data structure, completeness, uniqueness, and consistency |
| Missing value | A field that has no recorded value |
| Exact duplicate row | A row identical to another row across all evaluated columns |
| Repeated identifier | An identifier appearing in more than one row |
| Primary key | A field or set of fields that uniquely identifies a record |
| Foreign key | A field or set of fields referencing a key in another dataset |
| Composite key | A unique identifier formed from two or more fields |
| Data grain | What one row represents in a dataset |
| Referential integrity | The consistency of references between related datasets |

## Appendix B — Suggested Project Artifacts

Keep the following files in the project's documentation or reports directory, as applicable:

```text
reports/
├── Week_1_Data_Profiling_Report.md
├── dataset_overview.csv
├── missing_values_summary.csv
├── duplicate_identifier_summary.csv
└── relationship_validation_summary.csv
```

Only include the CSV artifacts after generating and validating them from the profiling notebook.
