# Sprint Notes — Week 1

## Sprint Information

- **Project:** Heavy Supplier, Inventory & Warehouse Analytics
- **Sprint:** Week 1
- **Scrum Master:** Salim Bello Muhammad (BI Analyst)
- **Phase:** Phase 1 — Foundation & Exploration (Weeks 1–3)
- **Sprint Status:** Completed

---

## 1. Sprint Goal

Understand the available datasets, perform initial data profiling and cleaning, validate data quality and relationships, and propose the first set of business KPIs and analytical questions.

## 2. Tasks and Team Responsibilities

| Task | Owner | Status |
|---|---|---|
| Profile and clean sales-side, purchasing, and stock tables, including customers, sales orders, invoices, payments, suppliers, purchase orders, stock ledger, and inventory master | Olufunmilola Florence Peters | Completed |
| Prepare the data dictionary and propose KPIs for products, inventory, and warehouse operations | Chandrashekhar Deurghare | Completed |
| Prepare the data dictionary and propose KPIs for sales, customers, and suppliers | Salim Bello Muhammad | Completed |
| Develop the profiling, cleaning, and validation notebook; set up the repository; and document sprint notes | Salim Bello Muhammad (Scrum Master) | Completed |
| Join the team as Data Scientist, review Week 1 outputs, and prepare to lead forecasting activities in Phase 3 | Abdibasid Mohamed Ali | Completed |

## 3. Work Completed

During Week 1, the team completed the initial data profiling and cleaning activities and prepared the first documentation and analytical proposals.

Key outcomes included:

- Reviewed the available datasets and their structures.
- Performed initial data cleaning, including date conversion, numeric conversion of warehouse capacity, and trimming of text fields.
- Examined missing values, repeated identifiers, and relationships between datasets.
- Prepared draft data dictionaries for inventory, warehouse, sales, customer, and supplier analysis.
- Proposed initial business KPIs for subsequent analytical work.
- Established the project repository and documented sprint progress.

The outputs provide a foundation for the next stage of data cleaning, integration, and validation.

## 4. Findings, Problems, and Open Issues

### 4.1 Reused Invoice Identifiers

**Finding:** The profiling review identified 197 occurrences beyond the first for repeated `invoice_id` values. These repeated identifiers appear across different sales orders.

**Potential impact:** Payments linked to a repeated invoice identifier may not be attributable to one specific order with confidence until the identifier issue is resolved.

**Decision:** Exclude the affected invoice records from payment analysis for now and flag them for further investigation.

**Follow-up:** Review the invoice identifiers, their associated sales orders, and the relevant payment references before including the affected records in financial analysis.

### 4.2 Inventory Balance Mismatches

**Finding:** Fourteen of the 180 product–branch pairs have a last recorded `stock_ledger` balance that does not match `inventory_master.current_stock`.

**Potential impact:** Inventory reports may be inconsistent if the two sources are used without reconciliation.

**Decision:** Retain the issue as an open data-quality item rather than adjusting the balances without evidence.

**Follow-up:** Investigate stock movements, balance calculations, and the intended reconciliation rules during Week 2.

### 4.3 Missing Purchase Order Received Dates

**Finding:** `purchase_orders_header.received_date` is blank for cancelled purchase orders.

**Assessment:** The team confirmed that these missing dates are expected for cancelled orders and are not considered errors under the current business understanding.

**Decision:** Preserve the missing values rather than filling them artificially.

**Follow-up:** Document this rule in the data dictionary and verify that the treatment remains consistent with the official Fields Documentation when it becomes available.

### 4.4 Official Fields Documentation Not Yet Available

**Finding:** The official Fields Documentation had not been provided by the end of Week 1.

**Impact:** The current data dictionary is a draft based on column names and sample values. Some field meanings and business rules therefore remain subject to confirmation.

**Decision:** Continue using the draft documentation for initial analysis while clearly marking assumptions and unconfirmed definitions.

**Follow-up:** Update the data dictionary after receiving the official documentation.

## 5. Decisions Made

The team agreed to the following decisions:

1. Proceed with the cleaned datasets produced by the profiling notebook.
2. Retain the completed transformations, including date conversion, warehouse-capacity numeric conversion, and text-field trimming.
3. Keep the repeated invoice identifiers and inventory balance mismatches visible as open data-quality issues.
4. Exclude affected invoice records from payment analysis until their relationships can be established reliably.
5. Preserve expected missing received dates for cancelled purchase orders.
6. Treat the current data dictionary as a draft until it can be checked against the official Fields Documentation.
7. Avoid silently changing records when the correct business rule has not yet been confirmed.

## 6. Deliverables

The following project artifacts are listed as Week 1 deliverables:

| File | Purpose |
|---|---|
| `01_profiling_cleaning_validation.ipynb` | Notebook containing profiling, cleaning, and validation work |
| `data_dictionary_DRAFT.md` | Draft definitions of dataset fields and their meanings |
| `kpi_proposal.md` | Initial KPI proposals for business analysis |
| `sprint_notes_week01.md` | Record of sprint activities, findings, decisions, and follow-up work |

## 7. Next Week's Plan — Phase 1, Week 2

The next sprint will focus on finalising data cleaning, integrating datasets, and strengthening validation.

### Planned Activities

- [ ] Investigate the repeated invoice identifiers and determine the appropriate treatment.
- [ ] Reconcile the 14 product–branch inventory balance mismatches.
- [ ] Finalise data-cleaning rules and document their rationale.
- [ ] Integrate relevant tables into a working analytical dataset.
- [ ] Validate join results, record counts, key uniqueness, and relationships.
- [ ] Review missing values and confirm that expected missing dates are handled consistently.
- [ ] Obtain the official Fields Documentation, if available.
- [ ] Update the draft data dictionary against the official field definitions.
- [ ] Re-run data-quality checks after integration.
- [ ] Document unresolved issues and the decisions required from the team.

### Expected Week 2 Outputs

- Updated profiling and cleaning notebook.
- Integrated working dataset.
- Updated data-quality and relationship validation summaries.
- Revised data dictionary, where official definitions are available.
- Week 2 sprint notes documenting progress and outstanding issues.

## 8. Sprint Review Summary

Week 1 established the project's initial data-quality baseline and produced the first set of documentation and KPI proposals. The team identified important issues involving repeated invoice identifiers and inventory balance mismatches, while confirming that missing received dates for cancelled purchase orders are expected under the current business understanding.

The next sprint will focus on resolving or documenting these issues, integrating the datasets, and improving validation before the project advances to deeper business analytics.

**Overall outcome:** Week 1 activities are marked as completed, with specific data-quality investigations and documentation updates carried forward into Week 2.

---

*Document: `sprint_notes_week01.md`*  
*Project: Heavy Supplier, Inventory & Warehouse Analytics*

