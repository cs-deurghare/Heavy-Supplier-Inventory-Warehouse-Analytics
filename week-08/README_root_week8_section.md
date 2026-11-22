## Week 8: Phase 3, supplier reliability, supplier risk, stockout prediction and customer segments (complete)

**Status:** W8-1, W8-2, W8-3 and W8-4 are complete with 120 of 120 notebook checks passing. Folder `week-08/`, combined notebook `08_deep_dive_analysis.ipynb`, validation `validation_report_week08.csv`, findings `week8_findings_summary.md`.

- **W8-1 supplier reliability:** the 8 suppliers cannot be told apart (on time 84.2% to 85.3%, cancelled 9.4% to 10.3%, spend share 12.1% to 12.9%; all Holm-adjusted p = 1.0). Lead time differs by contract (10 to 28 days) but varies about 1.7 days within a supplier. No product depends on one supplier; all suppliers are in China.
- **W8-2 supplier risk:** a three-pillar risk score ranks SUP0003 first, but no pair keeps its order in 95% of 5,000 resamples and halves of the data do not reproduce the ranking; do not rank suppliers by it.
- **W8-3 stockout and reorder (sales scale assumed, Q10 unresolved):** existing levels leave 78 of 180 pairs below 95% fill in 2023-2025 (93.8%); a lead-time-aware reorder point at 95% service meets 99.3% for 25.6% more stock value. No policy is called cost-optimal.
- **W8-4 customer segments:** five RFM segments exist as labels but are not stable (adjusted Rand index 0.005), do not predict later revenue and do not differ by region, type or industry after adjustment. Snapshot list only; no churn or tenure claim.
