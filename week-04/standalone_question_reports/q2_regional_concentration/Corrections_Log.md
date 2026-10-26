# Corrections Log: Q2 Regional Concentration

| # | Issue in the earlier version | Correction |
|---|---|---|
| 1 | Findings text answered the wrong questions | Rewritten around Q2 (regional concentration) |
| 2 | Revenue used all order statuses (South + West 61.18%) | Delivered orders only, ex-GST: 60.95%, matching the Week 3 KPI report |
| 3 | An "18x corrected" claim was not supported by any output | Removed; Q2 makes no stock-scale claim |
| 4 | Average order value was calculated per sales line | Calculated per delivered order (Rs 1.24M to Rs 1.30M) |
| 5 | Regional differences were stated without tests | Added customer-level Kruskal-Wallis tests and a bootstrap ratio |
| 6 | "Under-coverage drives the disparity" was asserted | Replaced with a stated limit: market size and unserved market cannot be separated |
| 7 | Invented tracker and hard-coded text cells | Removed; every number is produced by the notebook |
| 8 | `D:\` paths and leftover error cells | Portable folder search; notebook runs with 0 errors |
| 9 | No validation | 16 checks, all PASS (`validation_report_week04_q2.csv`) |
| 10 | No effect sizes or uncertainty on the concentration | Added epsilon-squared, a bootstrap interval for the South + West share, a top-customer check and a branch-link test (Cramér's V) |
