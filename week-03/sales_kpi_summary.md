# Week 3 — Sales, Customer & Payment KPI Summary (revised)
**Source:** `merged/sales_orders_full.csv` (130,402 lines, 20,000 orders) and `merged/invoices_with_payments.csv` (18,033 invoices), 2019–2024
**Notebook:** `03_kpi_calculations.ipynb` — all figures below are reproduced there and written to `kpi_outputs/`.

> **Revision note.** The first version reported "revenue" of ₹32.42B. That figure was `grand_total`
> (**including GST**) summed over **all** orders, **including 1,967 Cancelled orders**. Revenue is now
> **net of GST and excludes Cancelled orders**; the other figures are shown separately.

## 1. Definitions
| Term | Definition | Value |
|---|---|---:|
| **Net revenue** | ex-GST value of Delivered orders | **₹22.96B** |
| Gross revenue | incl. GST, Delivered orders | ₹29.25B |
| GST collected | Delivered orders | ₹6.30B |
| Cancelled value | ex-GST value of Cancelled orders (not revenue) | ₹2.49B |

## 2. Top-line KPIs (Delivered orders unless stated)
| KPI | Value |
|---|---:|
| Orders (total / delivered / cancelled) | 20,000 / 18,033 / 1,967 |
| Cancellation rate | 9.84% |
| Net revenue | ₹22,958,987,430 |
| Average order value (net) | ₹1,273,165 |
| Gross profit | ₹4.95B |
| Gross margin (% of net revenue) | 21.6% |
| Avg / median delivery lead time | 8.06 / 8.0 days |

## 3. Net revenue by year
| Year | Net revenue | Orders | YoY |
|---|---:|---:|---:|
| 2019 | ₹3.87B | 3,031 | — |
| 2020 | ₹3.92B | 3,038 | +1.2% |
| 2021 | ₹3.85B | 3,038 | −1.7% |
| 2022 | ₹3.82B | 2,948 | −0.9% |
| 2023 | ₹3.82B | 3,022 | +0.2% |
| 2024 | ₹3.68B | 2,956 | −3.8% |

Revenue is flat to slightly declining (2024 is the lowest year, −5% vs 2019); order volume is steady, so the decline comes from value per order, not order count.

## 4. Net revenue by customer type
| Customer type | Net revenue | Share | Avg order value | Orders |
|---|---:|---:|---:|---:|
| Government | ₹5.05B | 22.0% | ₹1.24M | 4,075 |
| Corporate | ₹4.72B | 20.5% | ₹1.28M | 3,672 |
| Dealer | ₹4.68B | 20.4% | ₹1.29M | 3,633 |
| Fleet Owner | ₹4.41B | 19.2% | ₹1.28M | 3,457 |
| Retail | ₹4.10B | 17.8% | ₹1.28M | 3,196 |

Government leads through order count; average order values are very similar (₹1.24–1.29M).

## 5. Net revenue by region
| Region | Net revenue | Share | Orders |
|---|---:|---:|---:|
| South | ₹7.26B | 31.6% | 5,722 |
| West | ₹6.73B | 29.3% | 5,335 |
| East | ₹4.05B | 17.6% | 3,161 |
| North | ₹3.94B | 17.2% | 3,029 |
| Central | ₹0.50B | 2.2% | 406 |
| North East | ₹0.47B | 2.1% | 380 |

South and West = 60.9% of net revenue.

## 6. Delivery lead time by region (days)
Central 7.56 · North East 7.72 · East 7.94 · North 8.00 · South 8.13 · West 8.16 — consistent; no regional bottleneck.

## 7. Top products (net revenue, Delivered lines)
| Product | Net revenue | Share | Gross profit | Margin |
|---|---:|---:|---:|---:|
| Engine Block EB-600 | ₹4.86B | 21.2% | ₹0.96B | 19.7% |
| Transmission Assembly TA-800 | ₹3.39B | 14.8% | ₹0.61B | 18.0% |
| Boom Cylinder BC-400 | ₹1.93B | 8.4% | ₹0.44B | 22.9% |
| Swing Motor SWM-350 | ₹1.65B | 7.2% | ₹0.36B | 21.6% |
| Track Chain TC-45 | ₹1.63B | 7.1% | ₹0.30B | 18.3% |

The top two products = 36.0% of net revenue, at below-average margins (19.7% and 18.0% vs 21.6% overall).

## 8. Order status and payment status
**Every Delivered order has exactly one invoice; every Cancelled order has none.** The earlier "Not Invoiced" group (2,360) was wrong: it combined 1,967 Cancelled orders with 393 orders whose invoices had been set aside. Those 393 invoices are now included.

| Order status | Orders | % of orders |
|---|---:|---:|
| Invoiced (Delivered) | 18,033 | 90.2% |
| Cancelled (no invoice) | 1,967 | 9.8% |

| Payment status (invoices) | Invoices | % of invoices | Invoice value incl. GST | % of value |
|---|---:|---:|---:|---:|
| Paid | 12,536 | 69.5% | ₹20.30B | 69.4% |
| Partially Paid | 3,660 | 20.3% | ₹5.97B | 20.4% |
| Unpaid | 1,837 | 10.2% | ₹2.98B | 10.2% |

## 9. Outstanding, overdue and credit risk
Payment totals are only reliable for **17,640 invoices** (unique `invoice_id`). The other **393 repeated-ID invoices (₹654M incl. GST)** cannot be matched to their payments and are excluded from the figures below.

| Metric | Value |
|---|---:|
| As-of date (latest invoice due date in data) | 2025-03-14 |
| Total outstanding (reliable invoices) | ₹5.80B |
| Overdue invoices | 5,375 |
| Outstanding more than 365 days overdue | ₹4.99B (86% of outstanding; 4,595 invoices) |

**Credit-risk concentration (answers the locked Q4):** outstanding is 19.6–21.4% of invoice value in every customer type and 18.6–20.9% in every region; Unpaid invoices are 9.1–11.0% of invoices in every customer type. **There is no concentration by customer type or region.** Corporate is slightly highest (21.4%). The issue is ageing — most outstanding money is over a year old — not a segment.

---
**Files:** `kpi_outputs/kpi_tables.csv`, `kpi_revenue_by_year.csv`, `kpi_revenue_by_month.csv`, `kpi_revenue_by_customer_type.csv`, `kpi_revenue_by_region.csv`, `kpi_lead_time_by_region.csv`, `kpi_top_products.csv`, `kpi_order_status.csv`, `kpi_payment_status_breakdown.csv`, `kpi_outstanding_summary.csv`, `kpi_payment_aging.csv`, `kpi_credit_risk_by_customer_type.csv`, `kpi_credit_risk_by_region.csv`; charts in `exploratory_charts/`.
