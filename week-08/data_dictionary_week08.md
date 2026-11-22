# Data dictionary update, Week 8: supplier fields

**Owner:** Ibrahim Khalil Umar · **Task:** W8-3 · **Full column list:** `data_dictionary_week08.csv` (196 columns: the Week 7 dictionary plus the supplier master `suppliers_clean.csv`; 29 columns updated this week, marked `updated_in = week-08`)

Usability labels: **Usable**, **Usable with caution** (read the note), **Unusable**, **Not tested**, **Not flagged**. Earlier updates (customer fields, stock-scale label, missing capacity data) are in `week-07/data_dictionary_week07.md` and carry over unchanged.

## What the supplier fields can and cannot measure

| Field | Verdict | What the data shows |
|---|---|---|
| `supplier_lead_days` / master `lead_time_days` | **Usable** | The **promised** lead time. It equals `expected_delivery_date` minus `order_date` on all 140,077 received lines. One fixed value per supplier: 10, 10, 12, 16, 18, 19, 26 and 28 days |
| `expected_delivery_date` | Usable with caution | The promised date. Lateness can be measured against it, but the pattern is very regular and the dates may be generated |
| `delivery_delay_days` | Usable with caution | Received date minus promised date: −3 to +7 days for **every** supplier. 80.5% on the promised date, 4.5% early (85.0% on or before), 15.1% late, counted per line (W8-1 counts per PO: 84.9% on or before); share late is 14.4% to 15.9% of lines for each supplier, so lateness does not separate suppliers |
| `lead_time_actual_days` | **Usable** | Received minus order date (promised lead plus delay). **93% of its variance is between suppliers**; within one supplier the SD is only 1.6 to 1.8 days (W8-3) |
| `reliability_score` | Usable with caution | 3, 4 or 5, one value per supplier. It does not track measured lateness (Spearman 0.38 with share late across 8 suppliers at line level, p = 0.36; W8-1 at PO level finds -0.44 with the on-time rate, permutation p = 0.30; low power with 8 suppliers) and every supplier is late about 15% of the time. Do not rank suppliers by it |
| `lead_time_days` (product master) | Usable with caution | Not the supplier lead time: equals the supplier's promised lead on only 4.6% of lines |
| `po_status` | Usable | 15,418 of 155,495 lines (9.9%) are Cancelled, 9.3% to 10.7% by supplier. No cancellation reason is recorded |
| Spend (`line_total`, `total_cost`) | Usable with caution | Nearly equal across suppliers (₹37.7B to ₹40.3B each). Quantities sit on the unresolved purchase scale (receipts 18.13 times sales), so spend cannot be compared with sales revenue |
| `china_tax_id` (supplier master) | **Unusable** | The city prefix matches the supplier's city for none of the 8 suppliers (for example SUP0001 Shenzhen carries a SUZHOU id) |
| `import_duty_rate` (supplier master) | Not tested | Rates 5 to 15; no duty amount appears on purchase-order lines, so use cannot be checked |

## Structure that matters for analysis
- **All 8 suppliers supply every product-branch pair** (each pair has 8 suppliers on its received lines), so supplier does not separate products, categories or branches. The supplier's `product_category` is a label that does not restrict what it supplies.
- **A pair's lead-time spread is mostly the supplier mix.** The 7 to 35 day range in Weeks 5 to 7 comes from orders landing on suppliers with different promised leads, plus a small −3 to +7 day delay. Week 7 noted that the clusters were "probably set by supplier"; this confirms it.
- **Delivery performance cannot separate suppliers on these fields.** Any supplier ranking in W8-1 and W8-2 has to use the lead-time level (promised lead), spend and supply concentration, with the sameness of lateness stated as a finding.
- **Promised dates do exist**, so lateness is measurable; whether they are real promises is not verifiable (the dataset is supplied with the programme, so this is a data limit, not a question for an owner).
