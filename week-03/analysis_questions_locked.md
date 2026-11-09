# Analysis Questions — Locked for Phase 2 (Weeks 4–6) — revised
**CadetX Heavy Supplier, Inventory & Warehouse Analytics**

Drawn from the corrected Week 3 KPI work. Questions that the data has already answered, or cannot answer, are marked.

## Sales & Revenue
1. Net revenue is flat to slightly declining (₹3.87B in 2019 → ₹3.68B in 2024) while order count is steady (≈3,000/yr). Average order value drifted from ₹1.28M to ₹1.24M — is this pricing, product mix or demand?
   **Answered in Week 4:** a fall of 5.0% (₹192.0M), mostly volume (78%); price cannot be tested (one price list).
2. South and West generate 60.9% of net revenue; Central and North East only ~2% each. Is that market size or under-coverage?
   **Answered in Week 4:** the gap is the size of the customer base; a customer is worth the same in every region; Central and North East have no branch.
3. 9.8% of orders are cancelled. Is cancellation concentrated by region, customer type, sales channel or product?
   **Answered in Week 5 (Q3): no.** Cancellation is not concentrated by any segment or product (smallest adjusted p = 0.35); the 2019 to 2024 rise is weak, post-hoc evidence. No cancellation reason exists in the data.

## Customer & Payments
4. ~~Is unpaid concentrated in specific customer types or regions?~~ **Answered in Week 3: no** — outstanding is 19.6–21.4% of value in every segment. **Follow-up answered in Week 6:** the outstanding money is old because the invoices are old (about 20% of every due year's value is still open); no late payment in the data arrives after 75 days; whether it will be collected is not testable (no collection or write-off records), so the Q4 report gives a labelled exposure range of ₹1.43B to ₹5.71B.
5. Government leads on revenue through order count, not order size. What does a customer-lifetime-value view show?
   **Answered in Week 5 (Q5):** customers are worth about the same whatever the type (type p = 0.41); no customer dominates; Government leads because it has the most customers. Industry segment is an exploratory lead to re-test.

## Product & Margin
6. Engine Block EB-600 and Transmission Assembly TA-800 are 36.0% of net revenue at below-average margins (19.7%, 18.0% vs 21.6%). Where is the margin concentrated, and is pricing optimised on the top products?
   **Answered in Week 5 (Q6):** the drag is concentrated in these two products (0.91 points of portfolio margin, about ₹210M); portfolio margin is stable over time; pricing cannot be tested (no price history); a labelled price what-if is arithmetic only.

## Operations
7. Lead time is 8.1 days on average and uniform by region — is there a seasonal pattern by month?
   **Answered in Week 5 (Q7): no.** Lead time is an even 1 to 15 day spread with no seasonal pattern (p = 0.85); a month index does not improve a forecast. The delivery date looks generated or planned.

## Suppliers
8. Suppliers are statistically indistinguishable on on-time rate (84–86%), delay and cancellations, and every product is bought from every supplier. Is that real, and is there any basis for supplier selection/consolidation?
   **Answered in Week 4:** suppliers are not distinguishable except on lead time (10.5 to 28.5 days).
9. ~~Which suppliers tie to the highest-margin products?~~ **Not answerable** — no product–supplier specialisation exists in the data.

## Inventory & Data Quality
10. Purchase receipts are 18× units sold (PO spend ≈ ₹312B vs net sales ₹23B). Are the PO quantities or the sales quantities on the wrong scale? **Required before any stock KPI (turnover, cover, stock health, replenishment policy) can be reported.**
   **Week 4: unexplained in the data.** There is no data owner to ask, so from Week 6 the team uses the sales scale as the working reference and labels every stock result as resting on that assumption (`week-06/stock_scale_note.md`). Replay with signed adjustments is in the Q10 report.
11. Once Q10 is resolved, what replenishment policy minimises carrying cost without stockouts?
   **Answered in Week 6 on the agreed sales scale (labelled working result):** the existing reorder levels fill 94.3% of demand (72 of 180 pairs below 95%); a demand-based trigger fills 98.9% to 99.8% for 12% to 32% more stock value; no cost data exists, so no policy is called cost-optimal. Stock KPIs: turnover 6.9 a year, median cover 52.6 days. Every figure rests on the sales-scale assumption.
12. 14 of 180 product–branch pairs differ between `inventory_master` and the ledger (13 negative). Is the cause the unsigned `ADJUSTMENT` quantities?
   **Answered in Week 5 (Q12):** the unsigned `ADJUSTMENT` quantity is real (1,227 added, 1,227 removed, visible only in `running_balance`) but is **not** the cause. The master is behind the ledger by its last one or two movements for all 14 pairs.
13. Customer master dates: many orders predate `customer_since` or follow `last_purchase_date`. Are those fields maintained, and should they be used?
   **Answered in Week 6 (Q13): no.** `customer_since` is after the first order for 58.4% of customers, `last_purchase_date` is before the last order for 93.0%, and `total_purchase_value` is 5.4% of delivered revenue; all three are Unusable and tenure, recency and value must be derived from the order lines.

---
**Status:** Locked for Phase 2 (Weeks 4–6), revised after validation against the corrected merged datasets. Updated after Week 6: Q1 to Q8, Q12 and Q13 answered (including the Q4 follow-up); Phase 2 coverage (ABC, movers, branch throughput, forecast readiness) done; Q10 stays unexplained and Q11 and the stock KPIs are answered on the agreed sales scale, labelled as resting on that assumption.
