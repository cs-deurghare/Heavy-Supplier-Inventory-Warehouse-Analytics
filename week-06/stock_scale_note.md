# Stock-scale note: the working assumption for all stock results

**Prepared for the team · Week 6 · Owners:** Ibrahim Khalil Umar, with Abdibasid Mohamed Ali

## The issue
Purchase receipts in the stock ledger are **18.13 times** units sold (20.4M units in against 1.12M out), and median `current_stock` is about 350 times `max_stock`. Nothing in the data explains the gap (Q10, Week 4; reproduced in Weeks 5 and 6). The dataset is supplied with the programme, so there is no data owner to ask.

## What the team agreed
1. **The sales scale is the working reference.** The stored thresholds (`max_stock`, `reorder_level`, `safety_stock`; medians 310.5, 62 and 43.5) fit monthly sales (about 84 to 95 units per pair), not receipts or recorded stock.
2. **Purchase quantities and `current_stock` are not used** for stock KPIs.
3. **Every stock result carries one sentence:** *"Sales scale assumed (Q10 unresolved); results rest on this assumption."* The label is written into the output files and charts of `stock_kpis_and_q11_rerun`.
4. **The unscaled case is always shown as a sensitivity,** not as a result.
5. **If a corrected purchase scale is ever confirmed,** all stock KPIs and the Q11 comparison are rebuilt on it first.

## What this does not claim
It does not claim the sales scale is correct, only that it is the only scale the stored thresholds agree with. The 18.13 ratio, the 350 times gap and the sensitivity results are facts about the data; the choice of reference is the assumption.
