# Proposed Week 4 corrections — ledger adjustment sign

**Status: AGREED by the team (Salim, Ibrahim, Abdibasid, Chandrashekhar) and applied in Week 5.** The corrections are in the Week 4 Q10 notebook, report, findings summary, sprint notes and `Corrections_Log.md`; `week-03/analysis_questions_locked.md` records the answered questions.
**Raised by:** Ibrahim Khalil Umar, from the Week 5 Q12 work (`../standalone_question_reports/q12_ledger_mismatches/`).

## 1. What is wrong in Week 4

| Fact | Source |
|---|---|
| `ADJUSTMENT.quantity` is stored unsigned (5 to 50). `running_balance` applies **1,227 adjustments as additions and 1,227 as reductions**. | Q12 notebook, checks on adjustment steps |
| Weeks 2 and 3 already documented this (Week 2 report section 6.1; Week 3 inventory KPI summary: "about half of which reduce…"). | `week-02/Week_2_Cleaning_Validation_Report.md`, `week-03/inventory_kpi_summary.md` |
| Week 4 says "every ledger adjustment is positive" and the Week 4 Q10 replay **adds every adjustment** (`sgn = 1`, check "All ledger adjustments are positive"). | places listed below |

The headline Q10 finding is **not affected**: the 18.1× ratio uses `IN` and `OUT` only, and PO spend against cost of goods does not use adjustments.

## 2. Effect on the Q10 corrected-scale replay (Part D)
Same replay as Week 4 (divide every `IN` by k, start from `opening_stock`), re-run three ways. Script and output: `q10_replay_signed_adjustments_check.py` and `.csv`.

| k | Method | Avg balance | Days below zero | Days above max stock |
|---:|---|---:|---:|---:|
| 18.13 | Week 4 method (adjustments added) | 330 | 28.5% | 46.6% |
| 18.13 | Same order as ledger file, adjustments added | 329 | 28.5% | 46.5% |
| 18.13 | **Adjustments signed from `running_balance`** | **141** | **36.9%** | **37.8%** |
| 20 | Week 4 method | 40 | 40.3% | 32.6% |
| 20 | **Signed** | **−149** | **49.0%** | **22.7%** |

- Ordering by `movement_id` after date (Week 4) makes almost no difference; the adjustment sign is the whole effect.
- At k = 18.13 the average balance falls from about 330 to **141**, so the Week 4 sentence "the average balance (336) lands near the typical maximum stock (322)" **no longer holds**. The balance is also below zero on 37% of days, not 28%.
- What still holds: the scale gap itself, PO spend against cost of goods (₹17.2B vs ₹18.0B), the thresholds agreeing with sales, and the conclusion that the ledger cannot be used to test a replenishment policy.
- The Week 4 statement "dividing purchases by 18.1 leaves only 8% of the 180 pairs between 0 and `max_stock`" must be **re-run** on the signed replay before it is quoted; my check counts end-of-period balances (10 of 180 pairs at k = 18.13) and may use a different definition.

## 3. Places to change (current wording → proposed wording)

| File and line | Current | Proposed |
|---|---|---|
| `README.md` line 124 (Q10 row of the Week 4 table) | "…The ledger covers about 91% of both and every adjustment is positive." | "…The ledger covers about 91% of both. Adjustment quantities are stored unsigned and half reduce the balance (see Q12)." |
| `README.md` line 138 (Week 4 data caveat 4) | "Ledger: why is every inventory adjustment positive (5 to 50 units)?" | "Ledger: is there a reason code for adjustments? Quantities are stored unsigned (5 to 50) and half reduce the balance; the sign is only visible in `running_balance`." |
| `week-04/sprint_notes_week04.md` line 22 | "…every ledger adjustment positive" | "…ledger adjustment quantities unsigned (half reduce the balance)" |
| `week-04/sprint_notes_week04.md` line 25 | "why ledger adjustments are all positive" | "how the adjustment sign is recorded (only visible in `running_balance`)" |
| `week-04/week4_findings_summary.md`, Q10 section | "There is no clean fix inside the data. Dividing purchases by 18.1 leaves only 8% of the 180 pairs between 0 and `max_stock`…" | Re-run with signed adjustments, then update the figure; add one line that adjustments are signed from `running_balance` |
| `week-04/standalone_question_reports/q10_stock_scale/Q10_Stock_Scale_Investigation.md` line 54 (UI-Q10-03) | "Ledger adjustment quantities are all positive (5 to 50), treated here as additions" | "Ledger adjustment quantities are stored unsigned (5 to 50); half reduce the balance; sign read from `running_balance`" |
| Same report, section 5 table and paragraph | k = 18.1: 331 / 28% / 47% | Replace with the signed figures above and re-word the "near maximum stock" sentence |
| `q10_stock_scale.ipynb` (Part D, cells 10, 11 and 13) | `"ADJUSTMENT": 1` and check "All ledger adjustments are positive" | Sign from `running_balance` (as in the Q12 notebook) and replace the check |
| `week-03/analysis_questions_locked.md`, Q12 | open | Mark answered in Week 5: the unsigned quantity is real but is not the cause of the 14 gaps |

Weeks 2 and 3 are already correct and need no change.

## 4. Split (agreed)
- **Ibrahim:** re-run Q10 Part D with signed adjustments, update the Q10 report, notebook and validation checks.
- **Abdibasid:** review the re-run and the signed replay logic.
- **Chandrashekhar:** apply the README, sprint notes, findings summary and locked-questions edits **in one commit** with the Week 5 merge, so the repository never contradicts itself.

## 5. Not part of this proposal
The data-owner questions (adjustment reason code, why the master missed the last postings) are in `../standalone_question_reports/q11_stock_scale_gate/Data_Owner_Question_Pack.md`.
