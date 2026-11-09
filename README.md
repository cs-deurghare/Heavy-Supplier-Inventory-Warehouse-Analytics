# Heavy Supplier, Inventory & Warehouse Analytics

![Project](https://img.shields.io/badge/Project-Heavy%20Supplier%20Analytics-blue?style=for-the-badge)
![Sprint](https://img.shields.io/badge/Sprint-Week%2006%20Complete-brightgreen?style=for-the-badge)
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
| Deep dive | 5 | Answer Q3, Q5, Q6, Q7 and Q12, and run the Q11 gate with a labelled scenario |
| Deep dive | 6 | Close Phase 2: Q4 follow-up, Q13, stock KPIs and Q11 on the agreed scale, ABC classes, fast and slow movers, branch throughput (complete) |

**Dataset:** 12 source tables covering sales orders, customers, products, suppliers, purchase orders, invoices, payments, stock ledger, branches and inventory.

---

## 2. Team

A four-person analytics team working in agile sprints with rotating weekly leadership.

| Name | Role | Focus | Week 4 question | Week 5 questions |
| :--- | :--- | :--- | :--- | :--- |
| Chandrashekhar Deurghare | BI Analyst | Product, inventory and warehouse data integration and reporting | Q2 Regional concentration | Q6 Margin concentration |
| Salim Bello Muhammad | BI Analyst | Sales, customer and supplier data integration and reporting | Q1 Revenue drift | Q3 Cancellation, Q5 Customer lifetime value |
| Ibrahim Khalil Umar | Data Analyst | Data quality, field-level cleaning and validation | Q10 Stock scale | Q11 gate and scenario, Q12 Ledger mismatches |
| Abdibasid Mohamed Ali | Data Scientist | Dataset structure review and forecasting readiness | Q8 Supplier differentiation, plus review of all four findings | Q7 Lead-time seasonality, review of all Week 5 findings |

---

## 3. Current Status and Authoritative Data

Weeks 1 to 6 are complete. Every notebook runs end to end with no errors and stops if any of its validation checks fail.

**The authoritative dataset is the set of corrected Week 2 merged files** in `week-02/reports/week_02/merged/`:
`sales_orders_full.csv`, `invoices_with_payments.csv`, `purchase_orders_full.csv`, `inventory_with_ledger.csv` and `stock_ledger_enriched.csv`.
Weeks 3, 4 and 5 all read these files. Net revenue is ex-GST and Delivered-only; the first Week 3 draft reported a higher figure that included GST and cancelled orders, and was corrected. The single 89-column merged file described in earlier drafts of this README is **superseded** and is not used by any current notebook.

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

`week-04/04_deep_dive_analysis.ipynb` answers all four questions (37 of 37 validation checks pass). `week-04/standalone_question_reports/` holds one self-contained folder per question for Q1, Q2 and Q10 (26, 16 and 24 checks), each with its own notebook, outputs, charts and report. All were tested from a clean copy of the repository layout.

| Question | Answer |
| :--- | :--- |
| **Q1 Revenue drift** | Delivered revenue fell ₹192.0M (-4.96%) from 2019 to 2024. In the price/volume/mix bridge, volume explains 78% (-₹150.1M) and product mix 22% (-₹41.9M, not distinguishable from noise, p = 0.47). Price cannot be tested because the data holds one price list. There is no evidence of a fall in demand. 76% of the fall lands in 2024 (-₹146.7M, -3.8%), but that step is not distinguishable from no change (interval -7.8% to +0.4%). Cancellation rose from 9.1% to 10.9%, but the evidence is weak (all-years p = 0.27) and no segment explains it. |
| **Q2 Regional concentration** | South (31.63%) and West (29.32%) hold 60.95% of revenue (interval 56.5% to 65.3%) and 61.8% of customers. A customer is worth about the same in every region (₹43M to ₹48M, p = 0.275). The gap is the size of the customer base. Central and North East have 11 customers each and no branch. The data cannot separate a small market from an unserved one. |
| **Q8 Supplier differentiation** | Tested per purchase order, the 8 suppliers are not distinguishable on on-time rate (84.2% to 85.3%, p = 0.97), delay (p = 0.88), cancellation (p = 0.91) or unit cost (p = 0.84). They differ only on lead time (10.5 to 28.5 days). |
| **Q10 Stock scale** | Unresolved. Received units are 18.1 times units sold and purchase spend is 17.3 times cost of goods sold, in every product. PO lines are about 15 times larger than sales lines. The ledger covers about 91% of both. Adjustment quantities are stored unsigned and half reduce the balance (see Q12). Nothing in the data explains the PO quantities. The team uses the sales scale as the working reference from Week 6 and labels every stock result as resting on that assumption. |

Supporting files in `week-04/`: `week4_findings_summary.md` (includes a method note reconciling the two Q1 decompositions), `sprint_notes_week04.md`, `Corrections_Log.md`, `README_how_to_run.md`.

## 8. Week 5: Deep Dive (Q3, Q5, Q6, Q7, Q11, Q12)

`week-05/standalone_question_reports/` holds one self-contained folder per question, each with its own notebook, outputs, charts, report and validation file. **167 of 167 checks pass** (`week-05/validation_report_week05.csv`) and every notebook was re-run from a clean copy of the repository layout with identical outputs.

| Question | Answer |
| :--- | :--- |
| **Q3 Cancellation** (27 checks) | Not concentrated anywhere. 1,967 of 20,000 orders cancelled (9.84%, ₹2.49B). Across 12 cuts and 30 products nothing is significant after adjustment (smallest adjusted p = 0.35 for products, 0.45 for cuts; whole-scan permutation p = 0.37). The rise from 9.1% (2019) to 10.9% (2024) is weak, post-hoc evidence. |
| **Q5 Customer lifetime value** (34 checks) | A customer is worth about the same whatever the type (mean ₹9.9M observed gross profit, type p = 0.41). No customer dominates (largest 0.37%, top 10% hold 14.2%). Government leads on orders because it has the most customers. Industry segment is an exploratory lead to re-test (adjusted p = 0.059). |
| **Q6 Margin concentration** (38 checks) | EB-600 and TA-800 are 35.9% of revenue but 31.7% of gross profit and pull the 21.56% portfolio margin down by 0.91 points (about ₹210M). The portfolio margin is stable over time. A price what-if is arithmetic only (no price history); the 2024 EB-600 fall is within chance. |
| **Q7 Lead-time seasonality** (34 checks) | Not seasonal. Lead time is an even spread of 1 to 15 days (mean 8.06); month p = 0.85, no yearly wave, and a month index does not improve a forecast. The delivery date looks generated or planned. |
| **Q11 Replenishment policy** (16 checks) | Gate and labelled scenario in Week 5; Week 6 reruns it on the agreed sales scale. Ledger receipts are 18.13 times units sold. On the sales side the existing thresholds fill 94.3% of demand; a demand-based trigger at 95% service gives 99.4% for about 19% more stock value. Not a stock finding until it is rerun on the agreed scale. |
| **Q12 Ledger mismatches** (18 checks) | The 14 pairs differ because `inventory_master.current_stock` is behind the ledger by its last one or two movements (gaps 16 to 515 units, at most 0.45%). Adjustment quantities are stored unsigned, with 1,227 applied as additions and 1,227 as reductions; this is not the cause. |

**Correction to a Week 4 caveat.** "Every ledger adjustment is positive" is true of the `quantity` column only: half of the adjustments reduce the balance (visible in `running_balance`). The Week 4 headline Q10 result (18.1 times) is unaffected, but the corrected-scale replay changes when adjustments are signed: at k = 18.1 the average balance is 142 (not 330) and the balance is below zero on 37% of days (not 28%). The Q10 notebook, report, findings summary, sprint notes and `Corrections_Log.md` in `week-04/` were updated accordingly (Q10 now has 24 checks), and `week-03/analysis_questions_locked.md` records the answered questions. These changes were agreed by the team; the reasoning is in `week-05/week4_corrections_proposal/`.

Supporting files in `week-05/`: `05_deep_dive_analysis.ipynb` (master notebook: re-runs all six question notebooks and rebuilds the combined validation), `week5_findings_summary.md`, `sprint_notes_week05.md`, `Corrections_Log_week05.md`, `validation_report_week05.csv`, `README_how_to_run.md`, `week4_corrections_proposal/`.

### Data limits (documented)
The dataset is supplied with the programme and cannot be clarified, so these are stated as limits rather than questions:
1. Pricing: one price list, so a price effect cannot be measured.
2. Cancellations: no reason field, and cancelled orders carry a delivery date.
3. Stock scale: PO quantities (20 to 300 per line) against sales lines of 1 to 20; the sales scale is the working reference.
4. Ledger: adjustment quantities are stored unsigned (5 to 50) and half reduce the balance; the sign is visible only in `running_balance`.
5. Customer master dates and `total_purchase_value` do not agree with the order history (Q13).

### Week 4 methods
- Revenue change is split exactly into price, volume and mix; volume is further split into orders placed, cancellation rate and basket size (log-mean method).
- Tests: Welch t, bootstrap intervals (5,000 resamples, seed 42), permutation tests (5,000 shuffles), chi-square, Cochran-Armitage trend, Kruskal-Wallis with effect sizes, Cramér's V and ANOVA.
- Purchase-order lines share a supplier and dates, so on-time, delay and lead time are tested per purchase order, not per line.
- Claims are worded to match their tests: a result is called "not established" or "weak evidence" when the test does not support more.

## 9. Week 6: Phase 2 Close (complete)

`week-06/standalone_question_reports/` holds one self-contained folder per question. The Q4 follow-up (43 checks), the Phase 2 coverage (43), Q13 (25) and the stock KPIs with the Q11 rerun (23) are complete, 134 of 134 checks in `week-06/validation_report_week06.csv`; the open items are in Section 13.

| Question | Answer |
| :--- | :--- |
| **Q4 follow-up Payments and ageing** (43 checks) | The outstanding money is old because the invoices are old. About 20% of the value due in every full year (2019 to 2024) is still open (chi-square p = 0.82, no downward trend, p = 0.77), so the 86% of outstanding that is over a year past due mirrors the 85% of invoiced value that fell due over a year ago. No payment in the data arrives more than 75 days after the due date; the 5,274 open invoices past that point (₹5.71B, 98% of outstanding) have no precedent of closing. No customer type, region, payment term, channel or customer stands out (smallest Holm-adjusted p = 0.34). Exposure range if 25% to 100% of the past-75-day balances were never collected: ₹1.43B to ₹5.71B (5.0% to 20.0% of invoiced value). The data holds no collection or write-off records, so it cannot say whether the money will be collected. |
| **Phase 2 coverage ABC, movers, branches and forecast readiness** (43 checks) | Ten products (class A) make 81.5% of revenue (B: 7 products, 14.1%; C: 13 products, 4.4%); the classes follow unit price, not volume, and class A has the lowest gross margin (20.3% against 31.8% in class C). No product is a fast or slow mover: monthly volumes run from 548 to 593 units, only 8% apart, and are equal within chance (Kruskal-Wallis p = 0.62; the product ranking does not hold across periods, rho = -0.09). Branches differ in how many orders they handle (Chennai 51.1 a month to Hyderabad 34.4) but not in order size, and none trends up or down. All 40 monthly series (totals, 30 products, 6 branches) are ready for a simple level forecast: no trend after Holm adjustment, no seasonality once months are put on a per-day basis, and no method beats the plain average in a rolling back-test. The data holds no capacity or timing records, so throughput means orders and units sold. |
| **Q13 Customer master dates** (25 checks) | The three customer master fields do not agree with the order lines. `customer_since` is after the first order for 58.4% of customers (all 242 customers dated 2020 or later had already ordered in 2019); `last_purchase_date` is earlier than the last order for 93.0%; `total_purchase_value` is 5.4% of delivered revenue and no customer is within 10% of their revenue. Rank correlations with the order-derived values are −0.04, −0.01 and −0.09, and the gaps do not differ by region or customer type (smallest Holm-adjusted p = 0.75). All three fields are **Unusable**: tenure, recency and value for Phase 3 must be derived from the order lines, whose history covers 2019 to 2024 only. |
| **Stock KPIs and Q11 rerun** (23 checks) | On the agreed sales scale (Q10 unresolved), the existing reorder levels fill 94.3% of demand and leave 72 of 180 pairs below a 95% fill. Stock KPIs: average stock ₹392.6M at cost, turnover 6.9 times a year, median cover 52.6 days against an 18-day lead time. A trigger based on each pair's demand and lead time fills 98.9% to 99.8% for 12% to 32% more stock value (95% service: 99.4%, ₹468.3M). Recorded `current_stock` gives 38,272 days of cover and cannot be used; at the purchase scale the stored thresholds would fill only 23.8%. The data has no holding or ordering cost, so no policy is called cost-optimal. **Every figure rests on the sales-scale assumption** (`week-06/stock_scale_note.md`). |

---

## 10. How to Run

Clone the repository and open any notebook (for example `week-05/05_deep_dive_analysis.ipynb`), then run all cells. Each notebook automatically finds the data it needs inside the repository: the corrected merged files in `week-02/reports/week_02/merged`, the raw `customers.csv` in `raw_data` (Q5), and the Week 3 baseline in `week-03/kpi_outputs` (Q1). Each notebook writes its outputs, charts and a validation report next to itself, and every check passes.

---

## 11. Tools Used

- **Python 3** with **pandas**, **NumPy** and **SciPy** for profiling, cleaning, merging, statistical testing and validation
- **Jupyter Notebook** for a documented, reproducible workflow
- **matplotlib** for charts
- **GitHub** for version control and team collaboration

---

## 12. Repository Structure

```
├── processed_data/                 # Cleaned tables
├── raw_data/                       # Original source tables
├── week-01/                        # Profiling notebook and report, data dictionary draft, KPI proposal
├── week-02/                        # Cleaning and integration notebook, validation reports, corrected merged datasets
│   └── reports/week_02/merged/     # Authoritative merged datasets
├── week-03/                        # KPI notebook, KPI report, locked analysis questions
│   ├── kpi_outputs/                # KPI result tables
│   └── README_how_to_run.md
├── week-04/                        # Deep dive
│   ├── 04_deep_dive_analysis.ipynb # All four questions, 37 checks
│   ├── analysis_charts/  analysis_outputs/  validation_report_week04.csv
│   ├── standalone_question_reports/  # q1_revenue_drift, q2_regional_concentration, q10_stock_scale
│   ├── Corrections_Log.md
│   ├── sprint_notes_week04.md
│   ├── README_how_to_run.md
│   └── week4_findings_summary.md
├── week-05/                        # Deep dive (Q3, Q5, Q6, Q7, Q11, Q12)
│   ├── 05_deep_dive_analysis.ipynb   # Master notebook: re-runs all six, 25 checks, combined validation
│   ├── standalone_question_reports/  # q3_cancellation_concentration, q5_customer_lifetime_value, q6_margin_concentration,
│   │                                 # q7_lead_time_seasonality, q11_stock_scale_gate, q12_ledger_mismatches
│   │
│   ├── validation_report_week05.csv  # 167 checks
│   ├── validation_report_week05_master.csv  # 25 checks of the master notebook
│   ├── Corrections_Log_week05.md
│   ├── sprint_notes_week05.md
│   ├── README_how_to_run.md
│   └── week5_findings_summary.md
├── week-06/                        # Phase 2 close
│   ├── standalone_question_reports/  # q4_payment_followup, phase2_coverage, q13_customer_master_dates, stock_kpis_and_q11_rerun (each: notebook, report, outputs, charts, validation)
│   ├── validation_report_week06.csv  # 134 checks
│   ├── stock_scale_note.md
│   ├── corrections_log_week06.md
│   ├── sprint_notes_week06.md
│   ├── readme_how_to_run.md
│   └── week6_findings_summary.md
└── README.md
```

---

## 13. Open Items After Week 6

- Keep every stock result labelled as resting on the sales-scale assumption (`week-06/stock_scale_note.md`); rebuild first if a corrected purchase scale is ever confirmed.
- Re-test the Q5 industry-segment lead and the Q3 2024 cancellation uptick when more data is available.

---

## 14. Status

Weeks 1 to 6 are complete and validated (Week 6: Q4 follow-up, Phase 2 coverage, Q13, and stock KPIs with the Q11 rerun; 134 of 134 checks pass). The five corrected Week 2 merged datasets in `week-02/reports/week_02/merged/` are the authoritative data and the base for all later work; the earlier single `merged_dataset.csv` is no longer used.

Documented limits, carried forward rather than closed:

- **Stock scale (Q10).** Purchase receipts are about 18.1 times units sold and nothing in the data explains why. The dataset is supplied with the programme, so there is no data owner to ask. The team agreed to use the sales scale as the working reference (the stored stock thresholds fit monthly sales) and to label every stock result as resting on that assumption.
- **Ledger mismatches (Q12).** The 14 `stock_ledger` versus `inventory_master` product-branch mismatches are explained in Week 5 as the master being behind the ledger by its last one or two movements. Why only these 14 pairs cannot be determined from the data.
- **Week 4 adjustment-sign corrections** made in Week 5 (Q10 notebook and report, findings summary, sprint notes, `Corrections_Log.md`) were agreed by the team.

Week 6 builds directly on this cleaned, merged and validated data.
