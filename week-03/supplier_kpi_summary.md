# Week 3 — Supplier KPI Summary (revised)
**Source:** `merged/purchase_orders_full.csv` (155,495 PO lines, 24,000 POs)

## What changed and why
The first version assigned each product to one supplier (the supplier on its most recent PO) and reported supplier **sales** revenue. That does not work: **every one of the 30 products is bought from all 8 suppliers** (the top supplier's share per product averages 13.3%; an even split would be 12.5%). The "most recent PO" rule therefore picks whichever supplier happened to come last — for 15 products that last PO was a *Cancelled* one — and the supplier revenue split reflected that arbitrary choice, not any real supplier relationship.

Supplier KPIs are now computed directly from purchase-order activity.

## Supplier performance (Received POs)
| Supplier | Type | Spend (ex-GST) | Share | On-time rate | Avg delay (days) | Actual vs contract lead time | PO cancel rate | Reliability score |
|---|---|---:|---:|---:|---:|---|---:|---:|
| Tianjin OEM Supplies | OEM | ₹40.26B | 12.9% | 85.3% | 0.48 | 28.5 vs 28 | 9.5% | 3 |
| Shenzhen OEM Supplies | OEM | ₹39.44B | 12.6% | 85.3% | 0.48 | 19.5 vs 19 | 9.9% | 5 |
| Hangzhou OEM Supplies | OEM | ₹39.25B | 12.6% | 84.2% | 0.54 | 26.5 vs 26 | 9.6% | 4 |
| Shanghai Distributor Supplies | Distributor | ₹39.19B | 12.6% | 85.4% | 0.53 | 16.5 vs 16 | 10.2% | 4 |
| Qingdao Distributor Supplies | Distributor | ₹39.11B | 12.5% | 85.6% | 0.48 | 10.5 vs 10 | 9.4% | 3 |
| Suzhou Local Vendor Supplies | Local Vendor | ₹39.05B | 12.5% | 84.3% | 0.55 | 12.6 vs 12 | 9.9% | 5 |
| Ningbo Distributor Supplies | Distributor | ₹38.03B | 12.2% | 84.4% | 0.51 | 18.5 vs 18 | 10.2% | 3 |
| Guangzhou Local Vendor Supplies | Local Vendor | ₹37.72B | 12.1% | 85.0% | 0.51 | 10.5 vs 10 | 10.3% | 5 |

## Findings
- **Suppliers are practically indistinguishable.** On-time rates span 84.2–85.6%, average delay 0.48–0.55 days, cancellation 9.4–10.3%, spend share 12.1–12.9%.
- Every supplier delivers on average about half a day later than its contracted lead time.
- The supplier `reliability_score` does **not** track observed performance (correlation with on-time rate −0.2 across 8 suppliers); it should not be used as a proxy for delivery performance.
- **Purchase spend (~₹312B ex-GST) is about 14× net sales revenue (₹23B), and units received are 18× units sold.** This is the same scale problem that affects stock (see inventory summary) and should be confirmed with the data owner before any procurement conclusions are drawn.
- Locked question Q10 (suppliers vs highest-margin products) cannot be answered from this data because there is no product–supplier specialisation.

**File:** `kpi_outputs/kpi_supplier_performance.csv`; chart `07_supplier_spend_and_on_time.png`.
