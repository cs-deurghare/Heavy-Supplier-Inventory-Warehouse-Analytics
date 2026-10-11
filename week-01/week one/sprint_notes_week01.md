# Sprint Notes — Week 1
**Scrum Master:** Salim Bello Muhammad (BI Analyst)
**Phase:** Foundation & Exploration (Weeks 1–3)

## Sprint goal
Understand the dataset, clean it, validate it, and propose our first KPIs and analysis questions.

## Tasks and who did them
| Task | Owner | Status |
|---|---|---|
| Profile and clean sales-side and purchasing/stock tables (customers, sales_orders, invoices, payments, suppliers, purchase_orders, stock_ledger, inventory_master) | Olufunmilola Florence Peters | Done |
| Data dictionary + KPIs for products, inventory, warehouse | Chandrashekhar Deurghare | Done |
| Data dictionary + KPIs for sales, customers, suppliers | Salim Bello Muhammad | Done |
| Profiling/cleaning/validation notebook, repo setup, sprint notes | Scrum Master (Salim) | Done |
| Joined the team this week (Data Scientist) — reviewed Week 1 output, will lead forecasting in Phase 3 | Abdibasid Mohamed Ali | Done |

## What we found / problems
- 197 `invoice_id` values are reused across different sales orders, so payments for those invoices can't be matched to one order with certainty. Decision: excluded from payment analysis for now and flagged for the team to revisit.
- 14 of 180 product–branch pairs have a last `stock_ledger` balance that does not match `inventory_master.current_stock`. Decision: flagged as a data quality issue to investigate further in Week 2.
- `purchase_orders_header.received_date` is blank for all cancelled purchase orders — confirmed this is expected, not an error.
- The official Fields Documentation was not available yet, so the data dictionary is a draft based on column names and sample values; it will be corrected once the document is provided.

## Decisions made
- Proceed using the cleaned dataset produced by the notebook (dates converted, warehouse capacity converted to a number, text fields trimmed).
- Treat the two issues above as open items rather than silently fixing them, so they stay visible to reviewers.

## Deliverables in this folder
- `01_profiling_cleaning_validation.ipynb`
- `data_dictionary_DRAFT.md`
- `kpi_proposal.md`
- `sprint_notes_week01.md`

## Next week's plan
- Move into Phase 1 Week 2: finalise data cleaning and integration, merge tables into one working dataset, and run further validation.
- Confirm the data dictionary against the official Fields Documentation once received.
