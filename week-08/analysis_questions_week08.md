## Phase 3: Week 8 questions
W8-1. Which suppliers deliver late or vary most in lead time, and how concentrated is purchasing?
   **Answered in Week 8 (W8-1):** none stand out. On time 84.2% to 85.3%, cancelled 9.4% to 10.3%, spend share 12.1% to 12.9% (all Holm-adjusted p = 1.0); lead time differs by contract (10 to 28 days) but varies about 1.7 days within a supplier; no product depends on one supplier; all suppliers are in China.
W8-2. How exposed are we to each supplier, and how firm is the ranking?
   **Answered in Week 8 (W8-2):** a three-pillar risk score puts SUP0003 first, but no pair of suppliers keeps its order in 95% of 5,000 resamples, SUP0003 is riskiest in 41.5% of them and rankings from two halves of the data do not agree; the suppliers cannot be separated on risk. The exposure that exists is single-country (all in China, East China 62.4% of spend).
W8-3. Which stock pairs are likely to run out, and when should they reorder?
   **Answered in Week 8 (W8-3), on the sales-scale assumption (Q10 unresolved):** existing reorder levels leave 78 of 180 pairs below 95% fill in 2023-2025 (93.8% overall); a lead-time-aware reorder point fitted on 2019-2022 at 95% service meets 99.3% with no pair below 95%, for 25.6% more stock value. `reorder_level` alone ranks the at-risk pairs as well as the full risk score (AUC 0.97).
W8-4. Which customer segments follow from the Week 7 RFM work, and are they real?
   **Answered in Week 8 (W8-4):** five conventional segments can be drawn but are not stable (adjusted Rand index 0.005), do not predict later revenue (p = 0.61), show no structure beyond chance and do not differ by region, type or industry after adjustment; use as a snapshot list only. No churn or tenure claim is possible.
