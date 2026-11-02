# Data-owner question pack — Heavy Supplier, Inventory & Warehouse Analytics

**From:** the CadetX analytics team (drafted by Ibrahim Khalil Umar, Week 5)
**To:** [data owner — name to be added]
**Purpose:** seven questions whose answers change what the team can report. Each lists the evidence, the question it blocks and what we will do with each answer.

---

### 1. How were purchase-order quantities set? *(blocks Q10, Q11)*
**Evidence.** Received units are 18.1× units sold in every product, unit of measure and year (ledger `IN` 20.40M vs `OUT` 1.12M). Purchase-order lines average 160 units (20 to 300); sales lines average 10.5 (1 to 20). `current_stock` is about 107,000 per pair against a `max_stock` of about 310.
**Question.** Were purchase-order quantities generated on a different scale from sales and stock settings? Is there a corrected quantity, a unit conversion or a known scaling?
**If yes:** we rebuild the stock KPIs (turnover, cover, stock health) on the corrected scale and re-run the replenishment analysis.
**If no:** we keep stock KPIs out of the submission and report sales-side KPIs only.

### 2. What is the sign convention for ledger adjustments? *(Q12)*
**Evidence.** Every `ADJUSTMENT` quantity is positive (5 to 50), yet `running_balance` applies **1,227 as additions and 1,227 as reductions** (Weeks 2 and 3 already noted that about half reduce the balance; Week 5 counted them exactly). The sign appears only in the balance, not in any column.
**Question.** Is there a field or rule that records whether an adjustment adds or removes stock (for example a reason code)? Why are exactly half negative?
**We will:** keep reading the sign from `running_balance`; a reason code would let us report shrinkage separately.

### 3. When was `inventory_master` extracted, and why do 14 pairs miss the last postings? *(Q12)*
**Evidence.** For 14 of 180 product–branch pairs, `current_stock` equals the ledger balance just before the last 1 or 2 movements (16 receipts and 1 sale, dated 2025-01-09 to 2025-01-24). It is not one cut-off date: 163 of the 166 matching pairs have later final movements.
**Question.** Is `current_stock` updated by a different process from the ledger, with a delay for some pairs? Which of the two is the system of record?
**We will:** use the ledger as the reference and note the 14 pairs as a timing difference of at most 0.45%.

### 4. Is there a price history? *(Q1, Q6)*
**Evidence.** Every one of the 130,402 order lines carries the master price: one price per product for all six years. A price effect is zero by construction.
**Question.** Is there price history, list-price changes or discounts anywhere? **Without it** we make no pricing conclusions and Q6 is limited to margin concentration and a labelled what-if.

### 5. What does the Cancelled status mean? *(Q3)*
**Evidence.** 9.84% of orders are cancelled; there is no reason field; cancelled orders still carry a delivery date.
**Question.** Is a cancellation reason recorded anywhere? Why does a cancelled order carry a delivery date? **Without it** Q3 reports where cancellation is concentrated but makes no cause claims.

### 6. Are `customer_since` and `last_purchase_date` maintained? *(Q5, Q13)*
**Evidence.** Many orders predate `customer_since` or follow `last_purchase_date`.
**Question.** Are these fields maintained, and which is the authoritative first and last order date? **Until answered** the team uses order dates from the sales orders instead.

### 7. What are the holding cost, ordering cost and service target? *(Q11)*
**Evidence.** The data holds no carrying-cost rate, ordering cost or target service level, so "minimise carrying cost without stockouts" cannot be priced.
**Question.** What annual holding-cost rate, cost per order and target service level (fill rate) does the business use? **With them** we can compare policies on total cost instead of stock value at cost.

---
**Reply format.** A short answer per item is enough. Items 1 and 3 decide whether the stock KPIs can be rebuilt, so they are the most urgent.
