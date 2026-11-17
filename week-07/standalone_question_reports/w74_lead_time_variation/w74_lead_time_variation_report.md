# W7-4: Does the demand-based trigger still beat the existing levels when lead times vary?

**Question.** The Q11 comparison (Weeks 5 and 6) used one constant lead time per product-branch pair (17 to 19 days). The purchase orders show lead times from 7 to 35 days. Does a demand-based reorder trigger (policy B) still beat the existing reorder levels (policy A) when each order's lead time is drawn from the pair's own history?
**Owner:** Ibrahim Khalil Umar · **Week 7, W7-4** · reviewer: Abdibasid Mohamed Ali · **Notebook:** `w74_lead_time_variation.ipynb` (30 of 30 checks pass; folder and file names aligned with W7-1 to W7-3 in the combined package)

> **Every figure below rests on one assumption: that the sales scale is the right reference for stock.** "Sales scale assumed (Q10 unresolved); results rest on this assumption." There are no holding or ordering cost data, so no policy is called cost-optimal.

## Answer

**Yes, on fill rate. With lead times drawn from the history, policy A fills 93.6% of demand (81 of 180 pairs below 95%) and every demand-based variant fills 98.1% or more. B beats A in all 1,000 simulated lead-time paths. The gain is real but costs stock: 12.6% to 31.5% more average stock value, and lead-time variation takes 0.3 to 0.8 points off B's fill rate.**

| Policy (working scale) | Fill, constant lead (Week 6) | Fill, lead time varies | 95% range over 1,000 paths | Pairs below 95% | Avg stock value | Extra stock vs A | Orders |
|---|---:|---:|---|---:|---:|---:|---:|
| **A existing** (`reorder_level`, `max_stock`) | 94.3% | **93.6%** | 93.4 to 93.8 | 81 | ₹395.0M | | 4,424 |
| B 90% (mean-lead trigger) | 98.9% | **98.1%** | 98.0 to 98.3 | 1 | ₹444.7M | +12.6% | 4,760 |
| B 95% | 99.4% | **98.8%** | 98.6 to 98.9 | 0 | ₹469.5M | +18.9% | 4,804 |
| B 99% | 99.8% | **99.5%** | 99.4 to 99.6 | 0 | ₹519.5M | +31.5% | 4,853 |
| B-LT 90% (lead-time-aware trigger) | n/a | 98.6% | 98.5 to 98.7 | 0 | ₹461.8M | +16.9% | 4,793 |
| B-LT 95% | n/a | 99.2% | 99.1 to 99.3 | 0 | ₹493.4M | +24.9% | 4,832 |
| B-LT 99% | n/a | 99.7% | 99.7 to 99.8 | 0 | ₹552.0M | +39.8% | 4,874 |

The constant-lead columns reproduce Week 6 exactly (fill, orders, stock value and 72 pairs below 95% for A).

## What the tests say

| Claim | Test | Result |
|---|---|---|
| B fills more than A when lead times vary | Same lead-time draws for every policy; compare per path | B beats A in **1,000 of 1,000** paths, for all six B variants |
| Size of the gain | Portfolio fill difference, 2.5th to 97.5th percentile over paths | B 95%: **+5.2 points** (4.9 to 5.4); B 90%: +4.5 (4.3 to 4.8); B 99%: +5.9 (5.7 to 6.1) |
| The gain is not one or two pairs | Bootstrap over the 180 pairs of each pair's mean fill difference (5,000 resamples, seed 42) | B 95%: +5.0 points on average per pair, interval **4.2 to 5.8**; B 90% 3.6 to 5.1; B 99% 4.9 to 6.5 |
| It does not help every pair | Pairs with higher or lower fill than A | B 95%: higher for 159, lower for 20 (one equal); B 99%: higher for 174, lower for 4 |
| Lead-time variation hurts every policy | Constant against varying, same policy | A −0.7 points, B 90% −0.8, B 95% −0.6, B 99% −0.3 |

## Reading it

- **The ranking holds.** Variable lead times lower fill for every policy, but A falls to 93.6% with 81 pairs below 95%, while B at 95% still fills 98.8% with none below 95%.
- **B's trigger ignores lead-time variation, and that costs it.** The Week 6 trigger uses the mean lead time only. A lead-time-aware trigger (B-LT: adds the variance of lead-time demand, from each pair's lead-time SD) fills more at each service level, for more stock: B-LT 90% gives 98.6% for ₹461.8M, against B 95% at 98.8% for ₹469.5M. Neither trigger dominates: the two curves are close, so the choice depends on how much stock the business will hold.
- **The lead-time spread is large and uniform.** SD 6.7 days on a 17.9-day mean (a third of the mean), for all 180 pairs (pair SD 6.3 to 7.0). Lead times cluster on a few values (about 10, 12, 16, 18 to 19, 26 and 28 days), probably set by supplier, but the pair history pools all suppliers, as in Week 6.
- **Same conclusion about cost as before.** The extra fill needs more stock. With no holding or ordering cost, the data cannot say which point is best; it can say what each point costs and buys.

## How the analysis was done

- **Unit:** the product-branch pair (180). Demand is the ledger `OUT` per pair per day over 2,203 days (91.1% of delivered units); one historical demand path for every run.
- **Lead time:** for every order placed, a lead time is drawn at random from that pair's own received purchase-order lines (671 to 842 lines per pair, 140,077 in all). Draws are independent, so orders can cross.
- **Simulation:** as in Weeks 5 and 6: daily review; when on hand plus on order is at or below `s`, order up to `S`; lost sales; start stock = `opening_stock`. A uses `reorder_level` and `max_stock`; B uses `s` = mean lead-time demand + z × demand SD × √lead time with `S = s + (max_stock − reorder_level)`, z = 1.28, 1.645, 2.33. B-LT replaces the variance term with lead time × demand variance + demand² × lead-time variance.
- **Replications:** 1,000 lead-time paths, seed 42, common random numbers across policies. Intervals are percentiles over paths; the pair-level interval is a 5,000-resample bootstrap.
- **Checks:** 30, including the Week 6 results reproduced exactly with a constant lead time, the vectorised simulator matched to a plain day-by-day loop on five pairs for the same draws, and the claims above re-derived from the outputs. The notebook finds the merged data itself (or `CADETX_MERGED`) and asserts that every check passes.

## Data limits

- **The scale is an assumption, not a finding.** If a corrected purchase scale were confirmed, this comparison would have to be rebuilt on it (`week-06/stock_scale_note.md`).
- **No holding cost, ordering cost or service target.** Stock value at cost is a proxy; none of these policies is called cost-optimal.
- **In-sample.** Policy B's reorder points use the demand mean and SD of the same 2,203 days they are tested on, so B's fill rates (98.1% to 99.8%) are in-sample figures. Policy A's levels were not estimated from this history. Read the gap as an upper bound on what a demand-based trigger would deliver on new data.
- **One demand path, lost sales, no backorders, no demand-forecast error.** Only lead time is varied here. Results are not forecasts.
- **Lead-time draws pool every supplier for a pair and treat orders as independent.** Real lead times may depend on the supplier or on earlier orders, which the data does not show.
- **Very regular data.** Lead times cluster on a few values and demand is level. Findings are worded to what the simulation shows.

## Recommendation

1. Report the demand-based trigger as beating the existing levels **on fill rate under variable lead times**, quoting 93.6% against 98.1% to 99.5% **(in-sample)**, with the sales-scale sentence and the stock-cost trade-off beside it.
2. If a demand-based trigger is adopted, size it with the lead-time SD (B-LT) or accept the 0.3 to 0.8-point loss shown for the mean-lead version.
3. Ask whether holding and ordering costs can be estimated; until then present the fill against stock value curve (`w74_03_fill_vs_stock_value.png`) rather than a best policy.

## Files

| File | Contents |
|---|---|
| `w74_lead_time_variation.ipynb` | The analysis, with every check |
| `validation_report_week07_w74.csv` | 30 pass/fail checks |
| `w74_outputs/` | 6 tables (policy summary, pair results, comparison against A, pairs below 95%, lead time by pair, reorder points) |
| `w74_charts/` | 3 charts (lead-time distribution, fill rate constant against varying, fill against stock value) |
