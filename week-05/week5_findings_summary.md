# Week 5 findings summary

Six questions were answered on the corrected Week 2 merged datasets (Delivered orders, net revenue ex-GST, ₹22.96B). Each has its own folder in `standalone_question_reports/` with a notebook, outputs, charts, report and validation file. All 167 checks pass (`validation_report_week05.csv`), and every notebook was re-run from a clean copy of the repository layout with identical outputs.

## Answers

| Q | Question | Answer | Strength |
|---|---|---|---|
| **Q3** | Where is cancellation concentrated? | **Nowhere.** 1,967 of 20,000 orders cancelled (9.84%, ₹2.49B). No region, customer type, channel, payment term, industry, rating, warehouse type, order size or product stands out: smallest raw p = 0.038 (month), 0.45 after adjusting for 12 cuts, 0.37 in a whole-scan permutation test; largest Cramér's V = 0.032. For every segment with 1,000+ orders, none cancels more than about 12%. The rate rose from 9.1% (2019) to 10.9% (2024), 1.7 points (interval 0.2 to 3.1), but the 2024 step was singled out after looking, so it is weak, post-hoc evidence. | Strong (no concentration); weak (the rise) |
| **Q5** | What is a customer worth over time? | **About the same whatever the type.** Mean observed gross profit ₹9.9M per customer (95% interval ₹9.7M to ₹10.1M). Customer type does not matter (Kruskal-Wallis p = 0.41). No customer dominates: the largest is 0.37% of gross profit, the top 10% hold 14.2% (Gini 0.12). Government leads on orders only because it has the most customers (22.8%). A customer's 2019 to 2021 value does not predict 2022 to 2024 (ρ = −0.03). Industry segment is an **exploratory lead** to re-test (raw permutation p = 0.014, adjusted p = 0.059; Manufacturing and Rental about 6% to 12% ahead through order frequency). | Strong (type, concentration); exploratory (industry) |
| **Q6** | Where is margin concentrated? | **The drag, not the margin, is concentrated.** EB-600 and TA-800 are 35.9% of revenue but 31.7% of gross profit (margins 19.75% and 17.96% against 21.56%; the other 28 products earn 22.99%). They pull the portfolio margin down by 0.91 points, about ₹210M of gross profit. Revenue and margin move in opposite directions across products (Spearman −0.94). The portfolio margin is stable over time (21.52% to 21.58%, p = 0.84). The 2024 EB-600 fall (₹71.3M) is the largest of 30 product changes but within chance (p = 0.25). A labelled price what-if (+1% on EB-600 = ₹48.6M with volume held; break-even volume loss 4.8%) is arithmetic, not evidence. | Strong (margins are exact); not established (2024 fall); scenario only (price) |
| **Q7** | Is lead time seasonal? | **No.** Lead time is an even spread of 1 to 15 days (mean 8.06). Monthly means run 7.92 to 8.20 days (Kruskal-Wallis p = 0.85, ε² = 0); no yearly wave (p = 0.83); no trend by year (p = 0.96). A typical month would show a gap of 0.32 days, so larger gaps are ruled out. Order volume and revenue follow month length (p = 0.37); a month-of-year index does not beat a plain average on a 2024 hold-out. Customer region has a weak lead (raw p = 0.008, adjusted 0.08). | Strong |
| **Q11** | Which replenishment policy fits? | **Gate and labelled scenario only in Week 5; rerun on the agreed sales scale in Week 6.** Ledger receipts are 18.13 times units sold; median `current_stock` is about 350 times `max_stock`. Monthly sales (84.3 per pair, 92.7 in delivered lines, 94.8 as a mean) match the thresholds (max 310.5, reorder 62, safety 43.5). Scenario on the sales side: the existing reorder levels fill 94.3% of demand and are not tied to demand (correlation 0.09 with a demand-based reorder point); a demand-based trigger at 95% service gives 99.4% fill for about 19% more stock value (₹468M against ₹393M). These figures depend on stated assumptions and must not be quoted as stock results. | Gate: strong; scenario: labelled |
| **Q12** | Why do 14 pairs miss the ledger? | **The master is behind the ledger by its last one or two movements.** For all 14 pairs the gap equals the net effect of the last 1 or 2 movements (16 receipts and 1 sale, 2025-01-09 to 2025-01-24; gaps 16 to 515 units, at most 0.45%). The unsigned `ADJUSTMENT` quantity is real (1,227 applied as additions and 1,227 as reductions, visible only in `running_balance`) but is **not** the cause. | Strong |

## Corrections to earlier work

- **Week 4 adjustment sign (agreed by the team and applied in the Week 4 files).** "Every ledger adjustment is positive" is true of the `quantity` column only: 1,227 adjustments add to the balance and 1,227 reduce it. The Q10 corrected-scale replay was re-run with adjustments signed from `running_balance`: at k = 18.1 the average balance is 142 (not 330), 37% of days are below zero (not 28%), and 10 of 180 pairs (5.6%) end between 0 and `max_stock` (end-of-period balance, the stated definition). The headline Q10 result (the 18.1× scale gap, PO spend within 4% of cost of goods, thresholds that fit sales) is unaffected, but the replay no longer "lands near maximum stock". Q10 now has 24 checks.
- **The earlier "8% of pairs" figure** could not be reproduced and has been replaced by the stated definition above.
- **Q11 scenario independently re-implemented** and matched exactly on all four policies (fill rate, on-hand, orders, stock value, pairs below 95%).
- **Q6 first version** was replaced: its price what-if was ten times too small (see `Corrections_Log_week05.md`).

## Data issues found this week

1. **Cancelled orders carry a delivery date** with the usual lead time (8.05 days).
2. **Delivery lead time is an even spread of 0 to 15 days** that responds to nothing, including for cancelled orders: it looks generated or planned.
3. **The customer master dates are unreliable:** `customer_since` is after the first order for 58% of customers, `last_purchase_date` is before the last order for 93%, and `total_purchase_value` is 5.4% of Delivered revenue.
4. **Every customer is active for all six years:** there are no new or lost customers.
5. **The product master `margin_percentage` is a markup on cost** for 29 of 30 products, not a margin; Engine Oil Filter OF-90 is inconsistent with both.
6. **Ledger adjustment sign** is stored only in `running_balance`.

## Data limits and open questions (documented)

The dataset is supplied with the programme, so there is no data owner to ask. The items below are stated as limits in every output that depends on them.

The evidence for each item is in `standalone_question_reports/q11_stock_scale_gate/Data_Owner_Question_Pack.md`, kept as a reference list. In order of effect: (1) how purchase-order quantities were set (the team uses the sales scale as the working reference for Q10 and Q11); (2) whether `delivery_date` is actual or planned (it looks generated or planned); (3) what the `Cancelled` status means (no reason is recorded); (4) whether there is a price history (there is one price list); (5) how adjustments are signed (only `running_balance` shows it) and why the master missed the last postings for 14 pairs; (6) which customer dates are maintained (Q13 tests this); (7) holding cost, ordering cost and service target (Q11 states its assumptions); (8) the meaning of `margin_percentage` and the OF-90 value.

## Recommendations

1. Do not target any region, customer type, channel or product for cancellation reduction; watch the 2024 uptick over 2025.
2. Do not build customer tiers or key-account programmes on lifetime value; re-test industry segment with more data.
3. Look at supplier cost and the price list for EB-600 and TA-800 first; make no pricing claim until a price history and volume response are available.
4. Quote delivery lead time as one company-wide figure (about 8 days, 1 to 15); do not plan around seasonality; state that the delivery date looks generated or planned.
5. Report stock KPIs and the replenishment policy only on the agreed sales scale, labelled as resting on that assumption.
6. Keep the data limits documented in the README; the agreed Week 4 adjustment-sign corrections go in with the Week 5 commit.
