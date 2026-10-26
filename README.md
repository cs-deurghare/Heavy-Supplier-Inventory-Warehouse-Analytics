# Heavy Supplier, Inventory & Warehouse Analytics

![Project](https://img.shields.io/badge/Project-Heavy%20Supplier%20Analytics-blue?style=for-the-badge)
![Sprint](https://img.shields.io/badge/Sprint-Week%2004%20Complete-brightgreen?style=for-the-badge)
![Validation](https://img.shields.io/badge/Validation-All%20checks%20passing-success?style=for-the-badge)

A CadetX Virtual Work Experience project analysing a heavy machinery supplier's sales, inventory, purchasing and warehouse operations across 12 relational data tables, to support evidence-based decisions on stock management, supplier performance and customer value.

---

## 1. Project Overview

This repository holds the code, cleaned data, documentation and findings produced over a 12-week programme.

| Phase | Weeks | Focus |
| :--- | :--- | :--- |
| Foundation | 1 | Profile, clean and validate the 12 raw tables |
| Integration | 2 | Merge the tables into analysis-ready datasets and validate every join |
| Measurement | 3 | Calculate the first KPIs and lock the analysis questions |
| Deep dive | 4 | Answer four locked questions (Q1, Q2, Q8, Q10) with tested, reproducible analysis |

**Dataset:** 12 source tables covering sales orders, customers, products, suppliers, purchase orders, invoices, payments, stock ledger, branches and inventory.

---

## 2. Team

A four-person analytics team working in agile sprints with rotating weekly leadership.

| Name | Role | Focus | Week 4 question |
| :--- | :--- | :--- | :--- |
| Chandrashekhar Deurghare | BI Analyst | Product, inventory and warehouse data integration and reporting | Q2 Regional concentration |
| Salim Bello Muhammad | BI Analyst | Sales, customer and supplier data integration and reporting | Q1 Revenue drift |
| Ibrahim Khalil Umar | Data Analyst | Data quality, field-level cleaning and validation | Q10 Stock scale |
| Abdibasid Mohamed Ali | Data Scientist | Dataset structure review and forecasting readiness | Q8 Supplier differentiation, plus review of all four findings |

---

## 3. Current Status and Authoritative Data

Weeks 1 to 4 are complete. Every notebook runs end to end with no errors and stops if any of its validation checks fail.

**The authoritative dataset is the set of corrected Week 2 merged files** in `week-02/reports/week_02/merged/`:
`sales_orders_full.csv`, `invoices_with_payments.csv`, `purchase_orders_full.csv`, `inventory_with_ledger.csv` and `stock_ledger_enriched.csv`.
Weeks 3 and 4 both read these files. Net revenue is ex-GST and Delivered-only; the first Week 3 draft reported a higher figure that included GST and cancelled orders, and was corrected. The single 89-column merged file described in earlier drafts of this README is **superseded** and is not used by any current notebook.

**Revenue definition used everywhere:** net revenue is `line_total` (ex-GST) of **Delivered** orders only, by order year. Total net revenue is ₹22.96B across 18,033 delivered orders (20,000 orders in total).

---

## 4. Week 1: Profiling and Initial Cleaning

| Deliverable | Location |
| :--- | :--- |
| `Week_1_Complete_Data_Profiling.ipynb` | `week-01/week one/`: profiles all 12 tables, with initial cleaning (dates, text trimming, numeric parsing) |
| `Week_1_Data_Profiling_Report.md` and profiling CSVs | `week-01/reports/`: column profiles, candidate keys, relationships, duplicate and data-quality issue log |
| `data_dictionary_DRAFT.md`, `kpi_proposal.md`, `sprint_notes_week01.md` | `week-01/week one/` |
| `processed_data/` | Processed tables ready for downstream work |

**What we did:** profiled all 12 CSV tables (structure, completeness, uniqueness and relationships), applied initial cleaning, drafted the data dictionary and proposed the first KPIs.

| Finding | What we found | How we treated it |
| :--- | :--- | :--- |
| Repeated invoice identifiers | 196 `invoice_id` values appear more than once (393 rows, 197 occurrences beyond the first) | Flagged, not deleted. Week 2 confirmed they are different transactions that share an ID, not true duplicates |
| Repeated payment identifiers | `payment_id` values reused across payments | Flagged; Week 2 counted 201 and used a surrogate row key |
| Missing values | Missing `received_date` in purchase order headers | Week 2 showed all 2,370 are Cancelled purchase orders |
| Mixed-format numbers and dates | Values such as `"45230 sqft"` stored as text; date formats varied | Parsed programmatically; unparseable values flagged, not dropped |
| Stock differences | `stock_ledger` balances differ from `inventory_master` for some product and branch pairs | Reconciled in Week 2 (14 pairs); carried forward as an open question |

---

## 5. Week 2: Cleaning, Integration and Validation

| Deliverable | Location |
| :--- | :--- |
| `02_data_cleaning_integration_validations.ipynb` | `week-02/`: cleans, validates and merges the tables |
| `Week_2_Cleaning_Validation_Report.md`, `sprint_notes_week02.md` | `week-02/`: report (12 of 12 checks pass) and sprint notes |
| `reports/week_02/merged/` | The five corrected merged datasets and a manifest (see Section 3) |
| `reports/week_02/clean/` | The 12 cleaned tables |
| `reports/week_02/task*.csv` | Key and foreign-key validation (6 primary keys, 17 foreign keys, all valid), audit log, before and after comparison, unresolved issues and validation checklist |

| Finding | What we found | How we treated it |
| :--- | :--- | :--- |
| Payments inflated by repeated invoice IDs | Joining payments on `invoice_id` overstated total paid by about ₹518M and caused 247 false "Paid" mismatches | Payments are joined only to unique invoice IDs; the 393 repeated-ID rows carry `payment_total_reliable = False` |
| Incorrect `line_profit` | Profit was derived from `margin_percentage`, which is a markup on cost, not a margin on price | Recalculated as quantity x (unit price - unit cost): 21.6% margin |
| Ledger ordering | `movement_id` is not chronological | Ordered by date, then file position; 14 product and branch pairs still differ from `inventory_master` and are documented |
| Row-count inflation in an early draft | An early merge produced about 782,000 rows instead of about 130,000 | Rebuilt with `validate='many_to_one'` on every merge so non-unique keys fail loudly |
| Column name collisions | `branch_id` and `payment_terms` carried different meanings in two tables | Renamed explicitly after merging |
| Floating-point artefacts | Values like `28392.000000000004` | Rounded monetary columns to 2 decimal places |

Five issues needing business input are recorded in `reports/week_02/task7_unresolved_issues.csv`.

---

## 6. Week 3: KPI Calculations

| Deliverable | Description |
| :--- | :--- |
| `03_kpi_calculations.ipynb` | Sales, payment, supplier and inventory KPIs on the five corrected merged datasets, executed end to end |
| `Week3_KPI_Report.md` | Full KPI report with method, definitions and limitations (22 of 22 validation checks pass) |
| `sales_kpi_summary.md`, `inventory_kpi_summary.md`, `supplier_kpi_summary.md` | Write-ups by KPI area |
| `kpi_outputs/` | KPI result tables |
| `analysis_questions_locked.md` | 13 analysis questions locked for Weeks 4 to 6 |
| `validation_report_week03.csv`, `exploratory_charts/`, `data_dictionary_columns.csv` | Validation, charts and column dictionary |

**Headlines**
1. Net revenue is flat to slightly declining (₹3.87B in 2019 to ₹3.68B in 2024) while order volume is steady.
2. South and West generate 60.9% of net revenue. Two products, EB-600 and TA-800, are 36.0% of revenue at below-average margins. Gross margin is 21.6%.
3. Payment risk is an ageing problem, not a segment problem: outstanding is 19% to 21% of value in every customer type and region, but most of it is over a year old.
4. The 8 suppliers are practically indistinguishable on delivery, cancellation and cost.
5. Stock-based KPIs cannot be reported yet: purchase receipts are 18 times units sold, so stock sits on a different scale from its own thresholds.

---

## 7. Week 4: Deep Dive (Q1, Q2, Q8, Q10)

`week-04/04_deep_dive_analysis.ipynb` answers all four questions (37 of 37 validation checks pass). `week-04/standalone_question_reports/` holds one self-contained folder per question for Q1, Q2 and Q10 (26, 16 and 19 checks), each with its own notebook, outputs, charts and report. All were tested from a clean copy of the repository layout.

| Question | Answer |
| :--- | :--- |
| **Q1 Revenue drift** | Delivered revenue fell ₹192.0M (-4.96%) from 2019 to 2024. In the price/volume/mix bridge, volume explains 78% (-₹150.1M) and product mix 22% (-₹41.9M, not distinguishable from noise, p = 0.47). Price cannot be tested because the data holds one price list. There is no evidence of a fall in demand. 76% of the fall lands in 2024 (-₹146.7M, -3.8%), but that step is not distinguishable from no change (interval -7.8% to +0.4%). Cancellation rose from 9.1% to 10.9%, but the evidence is weak (all-years p = 0.27) and no segment explains it. |
| **Q2 Regional concentration** | South (31.63%) and West (29.32%) hold 60.95% of revenue (interval 56.5% to 65.3%) and 61.8% of customers. A customer is worth about the same in every region (₹43M to ₹48M, p = 0.275). The gap is the size of the customer base. Central and North East have 11 customers each and no branch. The data cannot separate a small market from an unserved one. |
| **Q8 Supplier differentiation** | Tested per purchase order, the 8 suppliers are not distinguishable on on-time rate (84.2% to 85.3%, p = 0.97), delay (p = 0.88), cancellation (p = 0.91) or unit cost (p = 0.84). They differ only on lead time (10.5 to 28.5 days). |
| **Q10 Stock scale** | Unresolved. Received units are 18.1 times units sold and purchase spend is 17.3 times cost of goods sold, in every product. PO lines are about 15 times larger than sales lines. The ledger covers about 91% of both and every adjustment is positive. Stock KPIs stay not reportable until the data owner explains the PO quantities. |

Supporting files in `week-04/`: `week4_findings_summary.md` (includes a method note reconciling the two Q1 decompositions), `sprint_notes_week04.md`, `Corrections_Log.md`, `README_how_to_run.md`.

### Week 4 methods
- Revenue change is split exactly into price, volume and mix; volume is further split into orders placed, cancellation rate and basket size (log-mean method).
- Tests: Welch t, bootstrap intervals (5,000 resamples, seed 42), permutation tests (5,000 shuffles), chi-square, Cochran-Armitage trend, Kruskal-Wallis with effect sizes, Cramér's V and ANOVA.
- Purchase-order lines share a supplier and dates, so on-time, delay and lead time are tested per purchase order, not per line.
- Claims are worded to match their tests: a result is called "not established" or "weak evidence" when the test does not support more.

### Week 4 data caveats (questions for the data owner)
1. Pricing: the data holds one price list, so a price effect cannot be measured. Is there price history?
2. Cancellations: there is no reason field, and cancelled orders carry a delivery date. What does the Cancelled status mean?
3. Stock scale: how were purchase-order quantities (20 to 300 per line) set, against sales lines of 1 to 20?
4. Ledger: why is every inventory adjustment positive (5 to 50 units)?

---

## 8. How to Run

Open any notebook anywhere inside the repository checkout and run all cells. Each notebook searches its own folder and every parent folder for the corrected merged files (`week-02/reports/week_02/merged`) and, for Q1, the Week 3 baseline (`week-03/kpi_outputs`). Otherwise set the environment variables `CADETX_MERGED` and `CADETX_KPI` to those folders. If the data cannot be found, the notebook stops with a message saying so. Each notebook writes its outputs, charts and a validation report next to itself and asserts that every check passes. Please keep all weekly folders lowercase (`week-01` to `week-04`).

---

## 9. Tools Used

- **Python 3** with **pandas**, **NumPy** and **SciPy** for profiling, cleaning, merging, statistical testing and validation
- **Jupyter Notebook** for a documented, reproducible workflow
- **matplotlib** for charts
- **GitHub** for version control and team collaboration

---

## 10. Repository Structure

```
├── processed_data/                 # Cleaned tables
├── raw_data/                       # Original source tables
├── week-01/                        # Profiling notebook and report, data dictionary draft, KPI proposal
├── week-02/                        # Cleaning and integration notebook, validation reports, corrected merged datasets
│   └── reports/week_02/merged/     # Authoritative merged datasets
├── week-03/                        # KPI notebook, KPI report, locked analysis questions
│   ├── kpi_outputs/                # KPI result tables
|   └── README_how_to_run.md
├── week-04/                        # Deep dive
│   ├── 04_deep_dive_analysis.ipynb # All four questions, 37 checks
│   ├── analysis_charts/  analysis_outputs/  validation_report_week04.csv
│   ├── standalone_question_reports/  # q1_revenue_drift, q2_regional_concentration, q10_stock_scale
│   ├── Corrections_Log.md
│   ├── sprint_notes_week04.md
│   └── week4_findings_summary.md
└── README.md
```

---

## 11. Next Steps (Weeks 5 to 6)

- Q3 Cancellations: test whether cancellation is concentrated by region, customer type, channel or product, building on the Q1 finding.
- Resolve the open data-owner questions in Section 7, then revisit Q10 and the stock KPIs that depend on it.
- Continue through the remaining locked questions in `week-03/analysis_questions_locked.md`.

## 10. Status

Weeks 1 through 3 are complete, validated, and submitted. The Week 3 `merged_dataset.csv` (with supplier data included) is the current authoritative dataset and the base for all Phase 2 work. Two items are carried forward as Phase 2 analysis questions rather than open issues: tracing the `current_stock` scale mismatch to its source, and the 6 `stock_ledger` vs. `inventory_master` mismatches carried from earlier weeks.
Week 1 and Week 2 deliverables are complete, validated, and submitted. Subsequent weeks build directly on the cleaned, merged, and validated data established here.
