# Analysis Questions — Locked for Phase 2 (Weeks 4–6)
**CadetX Heavy Supplier, Inventory & Warehouse Analytics**

Drawn from patterns found across both halves of the Week 3 KPI work (sales/customer/supplier and
product/inventory/warehouse), ready for deeper analysis in Phase 2.

## Sales & Revenue
1. Why is total revenue flat year-over-year (₹5.3B–₹5.5B, 2019–2024) despite steady order volume?
   Is this a pricing, demand, or market-saturation effect?
2. What is driving the revenue concentration in South and West regions (~68% of total), and is
   there untapped potential in Central / North East?

## Customer
3. Government and Corporate customers generate the most revenue — does this reflect account depth
   (fewer, larger customers) or order frequency? What would a customer-lifetime-value view show?
4. Is the 9.0% "Unpaid" order segment concentrated in specific customer types or regions, pointing
   to a credit-risk pattern worth flagging to finance?

## Product & Inventory
5. Which product categories and individual items drive the highest inventory turnover, and where
   are the bottlenecks?
6. Engine Block EB-600 and Transmission Assembly TA-800 account for ~36% of line revenue — how does
   that compare to their inventory turnover ratio? Are top-revenue products also the fastest-moving?
7. What proportion of inventory falls into each stock health category (Low / Optimal / Overstock)
   under the finalized quantile-based classification, and how can storage efficiency be improved
   once the `current_stock` vs. `max_stock` scale is recalibrated against source systems?
8. What data-driven replenishment policies can be established to minimize carrying costs while
   preventing stockouts?

## Operations
9. Delivery lead time is consistent (7.6–8.2 days) across all regions — is there a seasonal pattern
   (e.g. slower in peak months) that a monthly breakdown would reveal?
10. Now that the supplier join is in place, which suppliers are tied to the highest-margin vs.
    highest-volume products, and does that affect procurement priority?

## Data Quality (carried from earlier weeks)
11. Can the `current_stock` vs. `max_stock` / `reorder_level` / `safety_stock` scale mismatch be
    traced to its source — are these fields measuring different things, or is one of them a data
    error upstream? (For this submission, the quantile-based stock health classification is the
    finalized interim method — see data dictionary.)
12. Are the 6 `stock_ledger` vs. `inventory_master` mismatches carried from earlier weeks fully
    resolved, and if not, what is the root cause?
13. Does the "most recent purchase order" rule used to assign each product's primary supplier hold
    up across the full history, or should supplier changes over time be tracked explicitly instead
    of collapsed to one?

---
**Status:** Locked for Phase 2 (Weeks 4–6).
