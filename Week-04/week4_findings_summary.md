# Week 4 Findings Summary
**CadetX Heavy Supplier, Inventory & Warehouse Analytics — Phase 2 (Deep-Dive Analysis)**

**Questions answered:** Q1 (revenue drift), Q2 (regional concentration), Q8 (supplier differentiation), Q10 (stock-scale gap)
**Source:** `04_deep_dive_analysis.ipynb` (Week-04_final_v2) on the corrected Week-2 merged datasets. 37 of 37 validation checks pass.
**Basis:** net revenue = `line_total` (ex-GST) of Delivered orders = ₹22.96B (20,000 orders, 130,402 lines, 500 customers).

---

## At a glance

| Q | Finding in one line | Confidence |
|---|---|---|
| **Q1** | Revenue fell ₹146.7M (−3.8%) in 2024. About 57% is fewer delivered orders and 43% is lower value per order, but the fall itself is **not statistically distinguishable from no change**. Price cannot be tested. | Descriptive; weak statistical support |
| **Q2** | South + West hold about 61% of revenue because they hold about 62% of customers. A customer is worth the same in every region. | Strong |
| **Q8** | Suppliers are **not distinguishable** on on-time rate, delay, cancellations, cost or reliability score. The only real difference is lead time (10.5 to 28.5 days). | Strong |
| **Q10** | Purchases are **18.1× sales**, for every product, unit of measure and year. The purchase side is the outlier. **Stock KPIs cannot be reported yet.** | Strong on the gap; cause unknown |

---

## Q1 — Why is revenue flat to slightly declining despite steady order volume?

**Finding.** Net revenue went from ₹3.87B (2019) to ₹3.68B (2024). The drop from 2023 to 2024 was ₹146.7M (−3.84%).

- **Price is not testable.** Every one of the 130,402 order lines carries the product-master price: one price per product for all six years. The data is a single price list, so a price effect is zero by construction. This is a data limitation, not evidence that prices were frozen.
- **What the 2023 → 2024 fall is made of** (log-mean decomposition; the shares move by less than 1 point under any step order):

  | Component | ₹M | Share of the fall |
  |---|---|---|
  | Product mix | −58.0 | 39.6% |
  | Cancellation rate | −49.0 | 33.4% |
  | Orders placed | −33.8 | 23.0% |
  | Basket size | −5.8 | 4.0% |

  Order volume (placed + cancellation) is about 57%; value per delivered order (mix + basket) is about 43%.
- **Where the mix effect sits.** Engine (−₹97.6M) and Hydraulic (−₹46.8M) fell; Transmission grew (+₹20.5M). Largest product drops: Engine Block EB-600 (−₹71.3M), Swing Motor SWM-350 (−₹45.2M), Turbocharger TB-900 (−₹27.6M).
- **Cancellations.** The rate was 9.1% (2019) and 10.9% (2024). 2024 is higher than the 2019–2023 pool (10.86% vs 9.63%, p = 0.031), but 2024 was picked after looking, the six yearly rates are consistent with one constant rate (p = 0.27), and the trend is weak (p = 0.030). Cancellations are spread evenly across regions, channels, customer types and payment terms. **No cancellation-reason field exists** in the data.

**How strong is it.** The bootstrap 95% interval for the 2023 → 2024 change is **−7.8% to +0.4%**, which includes zero. The product-mix share is not distinguishable from noise (permutation p = 0.35) and its sign flips from year to year. Present the split as **descriptive**, not as proven causes.

**Recommendation.** Do not report a pricing conclusion. Report the drift as small and not statistically established. Ask the data owner for price history and for a cancellation-reason field before attributing causes.

---

## Q2 — Is the regional concentration market size or under-coverage?

**Finding.** South (31.6%) and West (29.3%) hold **about 61%** of net revenue and 61.8% of customers. Revenue share and customer share are nearly the same in every region.

| Region | Revenue share | Customers | ₹M per customer |
|---|---|---|---|
| South | 31.6% | 158 | 46.0 |
| West | 29.3% | 151 | 44.6 |
| East | 17.7% | 87 | 46.6 |
| North | 17.2% | 82 | 48.0 |
| Central | 2.2% | 11 | 45.6 |
| North East | 2.1% | 11 | 43.1 |

- **A customer is worth the same everywhere.** Revenue per customer (p = 0.275) and orders per customer (p = 0.427) do not differ by region; effect sizes are negligible (ε² 0.003 and 0.000). Value per order is ₹1.24M to ₹1.30M in every region.
- **Central and North East have no branch** and only 11 customers each. Their customers buy like everyone else (ratio 0.97, 95% interval 0.88 to 1.06).
- **Branch count does not explain value per customer:** regions with 1 branch (East, North) and 2 branches (South, West) look the same.

**How strong is it.** The 60.9% has a 95% bootstrap interval of **56.5% to 65.3%** over customers, so quote "about 61%". No customer drives it (largest 0.37% of revenue; top 5 together 1.68%; without them South + West is 62.0%). With only 22 customers in Central and North East, a gap bigger than about 12% is ruled out, but a smaller one cannot be excluded.

**What the data cannot say.** Whether Central and North East are *small* markets or *unserved* markets. There is no market-potential field.

**Recommendation.** Describe the concentration as customer-base size. Test customer acquisition in Central and North East before investing in branches, and add regional market-size data for the next review. If new customers behaved like existing ones (an assumption, not tested), each would be worth about ₹45M over six years.

---

## Q8 — Are suppliers really indistinguishable, and is there any basis to select or consolidate?

**Finding.** Delivery outcomes belong to the whole purchase order, so they are tested **per PO** (21,630 received POs). Every product is bought from all 8 suppliers, so no supplier is specialised (this is why Q9 was closed).

| Dimension | Range across the 8 suppliers | Test | Verdict |
|---|---|---|---|
| On-time rate | 84.2% – 85.3% | p = 0.97 | Not distinguishable |
| Delay | 0.49 – 0.55 days | p = 0.88 | Not distinguishable |
| PO cancellations | 9.4% – 10.3% | p = 0.91 | Not distinguishable |
| Unit cost (index) | 0.999 – 1.001 | p = 0.84 | No supplier is cheaper |
| `reliability_score` | 3, 4, 5 → on-time 84.6–85.1% | — | Does not predict performance |
| **Lead time** | **10.5 – 28.5 days** | p < 1e-300, ε² = 0.93 | **The one real difference** |

- Lead time is a **contract term**, not an observed outcome: actual lead time = contract lead days + delay, exactly.
- Supplier types overlap (Distributor 10.5–18.5 days, Local Vendor 10.5–12.5, OEM 19.5–28.5), so read lead time **supplier by supplier**, not by type.

**Recommendation.** The only data-supported basis for choosing or consolidating suppliers is **lead time**. SUP0002, SUP0006 and SUP0007 (10.5–12.6 days) would let the business hold less safety stock with no price or reliability penalty. **Hold any consolidation decision until Q10 is resolved**, because the purchase quantities themselves are suspect.

*Correction note:* an earlier draft tested on-time and delay per PO *line* and called small differences "statistically detectable". Lines on one PO share the same supplier and dates, so that overstated the evidence. The per-PO result above replaces it.

---

## Q10 — Which side is on the wrong scale: purchases or sales?

**Finding.** Purchase receipts are **22.39M units against 1.23M sold: 18.1×**. The ledger shows the same ratio (IN 20.40M vs OUT 1.12M = 18.1×).

- **It is not a unit-of-measure issue and not product-specific.** The ratio is 17.4× to 19.2× for every one of the 30 products, ≈18× for piece, set and cartridge, and about the same in every year.
- **Where it comes from.** PO lines average 160 units (range 20–300); sales lines average 10.5 (range 1–20). That is 15.2× larger lines, times 1.19× more lines.
- **Which fields agree with which scale.** Per product–branch pair, sales are about 95 units a month. `max_stock` (≈322), `reorder_level` (≈65) and `safety_stock` (≈45) fit that scale. Purchases arrive at about 1,730 units a month (5.4× `max_stock` every month), and `current_stock` (≈107,000) is simply the ledger balance built from those purchases. The purchase side, and everything derived from it, is the outlier.
- **There is no clean fix inside the data.** Dividing purchases by 18.1 leaves only 8% of the 180 pairs between 0 and `max_stock`; the ratio varies from 13× to 26× across pairs. The ledger covers about 91% of received PO lines and delivered sales lines.

**Impact.** Stock turnover, days of cover, stock-health classes and replenishment policy **cannot be reported**. Q11 stays blocked.

**Recommendation.** Treat PO quantities and `current_stock` as unreliable. Raise with the data owner whether the PO quantities were generated on a different scale. Until it is answered, report sales-side KPIs only and keep stock KPIs out of the submission.

---

## Open questions for the data owner

1. Is there a price history, or is the master price list the only price in the data? (Q1)
2. Is a cancellation reason recorded anywhere? (Q1)
3. Is there market-potential or customer-prospect data for Central and North East? (Q2)
4. Were purchase-order quantities generated on a different scale from sales and stock settings? (Q10)

## Next (Weeks 5–6)

Q3, Q5, Q6, Q7 and Q11 in Week 5; the Q4 follow-up, Q12 and Q13 in Week 6. Q11 depends on the Q10 answer.

---

*Method notes.* Tests are Kruskal-Wallis, chi-square, permutation and bootstrap (5,000 resamples, seed 42). The Q1 split uses the log-mean (LMDI) method. Q2 robustness tests follow Ibrahim Khalil's Q2 package; the Q8 per-PO correction follows Salim's version. Re-run: `04_deep_dive_analysis.ipynb` with the five corrected merged files in a `merged/` folder.
