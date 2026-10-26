# Week 4: Q10 Stock-scale investigation (preview, not a submitted deliverable)
**Locked question (Q10).** Purchase receipts are 18x units sold (PO spend about Rs 312B vs net sales Rs 23B). Are the PO quantities or the sales quantities on the wrong scale?

**Run it** from anywhere inside the repository checkout (it searches parent folders for the merged files), or set `CADETX_MERGED` to the merged folder. Tested from a clean copy of the repository layout.

**Reproduce with:** `q10_stock_scale.ipynb` (executed, 19 of 19 checks pass, see `validation_report_week04_q10.csv`).

**Data:** corrected Week-2 merged files (`purchase_orders_full`, `sales_orders_full`, `stock_ledger_enriched`, `inventory_with_ledger`). Evidence table: `evidence_q10_stock_scale.csv`.

## 1. Answer
**The PO side is on the larger scale. Every sign points to the quantity per purchase-order line, not to sales and not to the stock thresholds.** The data cannot say why, so the data owner still has to confirm it.

## 2. Where the 18x comes from
| Step | Purchase orders | Sales | Ratio |
|---|---:|---:|---:|
| Order lines | 155,495 | 130,402 | 1.19x |
| Average quantity per line | 159.9 | 10.5 | 15.2x |
| Units (received POs vs delivered orders) | 22.39M | 1.23M | **18.1x** (1.19 x 15.2) |

The gap is almost all quantity per line. The two tables have a similar number of lines, but a PO line is about 15 times bigger than a sales line. PO quantities run flat from 20 to 300 per line (quartiles 90/160/230); sales quantities run flat from 1 to 20 (6/10/15).

## 3. What it is not
- **Not a unit-of-measure problem.** The units ratio is the same for piece (18.1x), cartridge (18.0x) and set (18.4x), and every one of the 30 products sits between 17.4x and 19.2x.
- **Not a product effect.** Quantity per line does not differ by product on either side (ANOVA p = 0.14 for POs, 0.40 for sales).
- **Not a price problem.** PO unit cost averages 1.06x the product-master cost, so the money gap (17.3x against sales cost of goods) follows the quantity gap.

## 4. Which side is correct
| Test | Result | Reading |
|---|---|---|
| Reorder level in days of delivered sales | median 20 days | Sensible on the sales scale; on the PO scale it would be about 1 day |
| Maximum stock in days of delivered sales | median 100 days | Sensible on the sales scale |
| PO spend if quantity is divided by 18.1 | Rs 17.2B vs sales cost of goods Rs 18.0B | Matches within 4% |
| Typical PO line vs maximum stock | 160 vs 310 | One PO line is about half of max stock, which is a normal order size |
| PO lines per product-branch per year | 130 received | Demand needs only about 7 a year at 160 per line |

The stock thresholds and sales agree with each other, and PO spend only reconciles to sales cost after scaling the PO quantity down by about 18. Sales scaled up by 18 would give revenue of about Rs 410B and would not match the thresholds.

## 5. Corrected-scale check
Replaying the ledger with every IN quantity divided by a factor k:
| k | Average balance | Share of days below zero | Share of days above max stock |
|---:|---:|---:|---:|
| 1 (as is) | 53,627 | 0% | 100% |
| 10 | 2,860 | 0% | 96% |
| 18.1 | 331 | 28% | 47% |
| 20 | 40 | 40% | 33% |

At k = 18.1 the average balance (336) lands near the typical maximum stock (322), but the balance still goes negative on 28% of days. That is because PO timing in the data does not respond to stock level, so replenishment logic is not in the data. The scale is therefore a good fit, the replenishment behaviour is not, and the ledger cannot be used to test a replenishment policy (Q11) without more information.

## 6. Open issues and caveats
| ID | Issue | Impact | Owner |
|---|---|---|---|
| UI-Q10-01 | PO line quantity is about 15x sales line quantity, in every product | Confirm the correct PO quantities, or the intended number of POs | Data owner |
| UI-Q10-02 | Ledger holds about 91% of both PO receipts and delivered sales (IN 20.40M of 22.39M, OUT 1.12M of 1.23M) | Small side gap; the 18.1x ratio holds inside the ledger | Data owner |
| UI-Q10-03 | Ledger adjustment quantities are all positive (5 to 50), treated here as additions | The sign convention is not documented | Data owner |
| UI-Q10-04 | Replenishment timing does not respond to stock level | Q11 (replenishment policy) cannot be answered from this ledger | Data owner |

**Reading limits.** The 18x is a scale gap, not a measured error in any one field, and a correction factor of about 18 is an estimate. Stock-based KPIs stay not reportable until the data owner confirms the PO quantities.
