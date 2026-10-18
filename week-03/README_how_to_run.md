# Week 3 — how to run
1. Put the five Week-2 merged datasets in a folder named `merged/` next to the notebook (or in `data/merged/`, `../reports/week_02/merged/`):
   `sales_orders_full.csv`, `invoices_with_payments.csv`, `purchase_orders_full.csv`, `inventory_with_ledger.csv`, `stock_ledger_enriched.csv`.
2. Optional: `data/branches.csv` adds warehouse capacity and headcount to the branch table.
3. Run all cells of `03_kpi_calculations.ipynb` (the charts display inline and are also saved as PNGs). It writes `kpi_outputs/`, `exploratory_charts/` and `validation_report_week03.csv`, and stops with an assertion if any check fails.
`data_dictionary_columns.csv` lists the columns of the five merged datasets (the earlier 89-column data dictionary described a file that is no longer used).
