# Analysis Questions — Locked for Phase 2 (Weeks 4–6) — revised
**CadetX Heavy Supplier, Inventory & Warehouse Analytics**

Drawn from the corrected Week 3 KPI work. Questions that the data has already answered, or cannot answer, are marked.

## Sales & Revenue
1. Net revenue is flat to slightly declining (₹3.87B in 2019 → ₹3.68B in 2024) while order count is steady (≈3,000/yr). Average order value drifted from ₹1.28M to ₹1.24M — is this pricing, product mix or demand?
2. South and West generate 60.9% of net revenue; Central and North East only ~2% each. Is that market size or under-coverage?
3. 9.8% of orders are cancelled. Is cancellation concentrated by region, customer type, sales channel or product?

## Customer & Payments
4. ~~Is unpaid concentrated in specific customer types or regions?~~ **Answered in Week 3: no** — outstanding is 19.6–21.4% of value in every segment. Open follow-up: why is 86% of outstanding more than a year overdue, and is it collectable?
5. Government leads on revenue through order count, not order size. What does a customer-lifetime-value view show?

## Product & Margin
6. Engine Block EB-600 and Transmission Assembly TA-800 are 36.0% of net revenue at below-average margins (19.7%, 18.0% vs 21.6%). Where is the margin concentrated, and is pricing optimised on the top products?

## Operations
7. Lead time is 8.1 days on average and uniform by region — is there a seasonal pattern by month?

## Suppliers
8. Suppliers are statistically indistinguishable on on-time rate (84–86%), delay and cancellations, and every product is bought from every supplier. Is that real, and is there any basis for supplier selection/consolidation?
9. ~~Which suppliers tie to the highest-margin products?~~ **Not answerable** — no product–supplier specialisation exists in the data.

## Inventory & Data Quality
10. Purchase receipts are 18× units sold (PO spend ≈ ₹312B vs net sales ₹23B). Are the PO quantities or the sales quantities on the wrong scale? **Required before any stock KPI (turnover, cover, stock health, replenishment policy) can be reported.**
11. Once Q10 is resolved, what replenishment policy minimises carrying cost without stockouts?
12. 14 of 180 product–branch pairs differ between `inventory_master` and the ledger (13 negative). Is the cause the unsigned `ADJUSTMENT` quantities?
13. Customer master dates: many orders predate `customer_since` or follow `last_purchase_date`. Are those fields maintained, and should they be used?

---
**Status:** Locked for Phase 2 (Weeks 4–6), revised after validation against the corrected merged datasets.
