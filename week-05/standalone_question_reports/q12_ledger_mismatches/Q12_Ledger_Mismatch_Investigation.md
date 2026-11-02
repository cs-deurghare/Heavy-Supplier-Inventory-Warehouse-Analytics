# Week 5 · Q12 — Why do 14 product–branch pairs differ from the ledger?

**Owner:** Ibrahim Khalil Umar (Data Analyst)
**Notebook:** `05_q12_ledger_mismatches.ipynb` · **Validation:** 18 of 18 checks pass (`validation_report_week05_q12.csv`)
**Data:** corrected Week 2 merged datasets (`inventory_with_ledger.csv`, `stock_ledger_enriched.csv`)

## Answer in one paragraph

The unsigned `ADJUSTMENT` quantity is real, but it is **not** the cause of the 14 mismatches. Every adjustment step in `running_balance` is exactly +qty or −qty, so the sign can be read from the balance, and the independent evidence is that every step and every opening reconciles (Finding 1). The 14 gaps come from `inventory_master.current_stock` being **behind the ledger by its last one or two movements**: in all 14 pairs, `current_stock` equals the ledger balance just before those movements, and the gap equals their net effect exactly.

## Findings

### 1. The adjustment sign is stored in `running_balance`, not in `quantity`
- All 2,454 `ADJUSTMENT` quantities are positive (5 to 50).
- Reading the step in `running_balance` for each movement: **1,227 adjustments were applied as +qty and 1,227 as −qty; none are anything else.** Exactly half are negative.
- Every `IN` and `OUT` step matches its quantity (234,776 of 234,776). The first step of each pair is measured against `opening_stock`: 167 pairs start with an `IN`/`OUT` that equals the opening ± its quantity, and the 13 that start with an adjustment move the balance by exactly its quantity.
- **What counts as evidence.** These three facts are the independent evidence for the sign reading: every adjustment step is exactly ±qty, every `IN`/`OUT` step matches, and every opening reconciles. The replay table below is **not** independent evidence for the sign reading: the "sign read from `running_balance`" row reproducing the ledger on 180 of 180 pairs is **true by construction**, because the sign comes from the same balance. It confirms the data are consistent. The real test of the unsigned-quantity hypothesis is the "all positive" and "all negative" rows, which reproduce the ledger on 0 of 180 pairs.
- **Provenance and correction.** The Week 2 and Week 3 reports already said that the `ADJUSTMENT` quantity is unsigned and that about half of the adjustments reduce the balance. The Week 4 caveat "every ledger adjustment is positive" and the Week 4 Q10 replay (which adds every adjustment) lost that point. "Positive" is true of the `quantity` column only. Week 5 adds the exact count (1,227 up, 1,227 down) and tests the hypothesis from the locked Q12 question. Effects on Week 4 and the proposed wording are in `../../week4_corrections_proposal/`.

| Replay reading | Pairs equal to ledger last balance | Pairs equal to `inventory_master` |
|---|---|---|
| All adjustments positive | 0 | 0 |
| All adjustments negative | 0 | 0 |
| Adjustments ignored | 1 | 1 |
| Sign read from `running_balance` (180 is by construction) | 180 | 166 |

### 2. What the 14 gaps are
- 14 of 180 pairs differ; 13 gaps are negative and one is positive (P028 · PUN001, +16).
- The gaps range from 16 to 515 units, at most 0.45% of the pair's balance.
- For **every one of the 14**, the gap equals minus the net effect of the **last movement (11 pairs) or last two movements (3 pairs)** in the ledger, and `current_stock` equals the ledger balance just before them.
- The missing movements are 16 purchase receipts (`IN`) and 1 sales issue (`OUT`), dated 2025-01-09 to 2025-01-24. The positive gap is the one pair whose missing movement is a sales issue. **None of them is an adjustment, so this finding does not depend on the sign reading.**
- Full list: `q12_outputs/q12_mismatch_explained.csv` (movement ids, reference ids and dates).

### 3. It is not a single snapshot date
If `inventory_master` were a snapshot taken on one date, every later movement would be missing everywhere. It is not: **163 of the 166 matching pairs** have a final movement later than the earliest missing one (matching pairs end between 2024-12-31 and 2025-01-28). The master is behind only for these 14 pairs.

## What this means
- **Use the ledger as the reference for balances.** Its steps and openings reconcile on all 180 pairs.
- **Never treat `ADJUSTMENT.quantity` as a signed number.** Any analysis that sums it (net adjustments, shrinkage) must take the sign from `running_balance`.
- The 14 mismatches are a master-table timing issue, not a ledger error. The size is small (≤0.45%), but the Q10 stock-scale issue is much larger and is unaffected: it is built on `IN` and `OUT`.

## Limits
- The data does not say **why** the master missed the last postings for these 14 pairs only. That needs the data owner (see `../q11_stock_scale_gate/Data_Owner_Question_Pack.md`, item 3).
- The sign recovery relies on `running_balance` being the true record. It reproduces every `IN`/`OUT` step exactly, so there is no sign of a problem, but no second source confirms it.

## Files
`05_q12_ledger_mismatches.ipynb` · `q12_outputs/` (4 CSVs) · `q12_charts/q12_01_sign_and_gap_explained.png` · `validation_report_week05_q12.csv`

**Re-run:** open the notebook anywhere inside the repository checkout and run all cells; it finds `week-02/reports/week_02/merged` itself (or set `CADETX_MERGED`).
