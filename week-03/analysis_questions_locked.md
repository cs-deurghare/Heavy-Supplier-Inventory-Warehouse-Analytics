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
4. ~~Is unpaid concentrated in specific customer types or regions?~~ **Answered in Week 3: no** — outstanding is 19.6–21.4% of value in every segment. Open follow-up: why is 86% of outstanding more than a year overdue, and is it collectable?
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
   **Week 4: unexplained in the data.** There is no data owner to ask, so from Week 6 the team uses the sales scale as the working reference and labels every stock result as resting on that assumption. Replay with signed adjustments is in the Q10 report.
11. Once Q10 is resolved, what replenishment policy minimises carrying cost without stockouts?
   **Week 5 (Q11): gate and labelled sales-side scenario run.** To be rerun on the agreed sales scale in Week 6; until then it must not be quoted as a stock result.
12. 14 of 180 product–branch pairs differ between `inventory_master` and the ledger (13 negative). Is the cause the unsigned `ADJUSTMENT` quantities?
   **Answered in Week 5 (Q12):** the unsigned `ADJUSTMENT` quantity is real (1,227 added, 1,227 removed, visible only in `running_balance`) but is **not** the cause. The master is behind the ledger by its last one or two movements for all 14 pairs.
13. Customer master dates: many orders predate `customer_since` or follow `last_purchase_date`. Are those fields maintained, and should they be used?
   **Previewed in Week 5 (Q5):** `customer_since` is after the first order for 58% of customers and `last_purchase_date` is before the last order for 93%; to be completed in Week 6.

---
**Status:** Locked for Phase 2 (Weeks 4–6), revised after validation against the corrected merged datasets. Updated after Week 5: Q1, Q2, Q3, Q5, Q6, Q7, Q8 and Q12 answered; Q10 and Q11 to be completed in Week 6 on the agreed sales scale; Q4 follow-up and Q13 planned for Week 6.
