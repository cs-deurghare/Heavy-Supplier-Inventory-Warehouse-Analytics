"""Combine every per-question Week 8 validation file into validation_report_week08.csv.
Run from anywhere: python combine_validation_week08.py
Expected check counts are asserted so a missing or short file is caught."""
from pathlib import Path
import pandas as pd
HERE = Path(__file__).resolve().parent
ITEMS = [("w81_supplier_reliability", "W8-1 Supplier reliability", 29),
         ("w82_supplier_risk", "W8-2 Supplier risk", 38),
         ("w83_stockout_reorder", "W8-3 Stockout and reorder", 31),
         ("w84_customer_segments", "W8-4 Customer segments", 22)]
frames = []
for folder, label, n_expected in ITEMS:
    f = HERE / "standalone_question_reports" / folder / (f"validation_report_week08_{folder[:3]}.csv")
    d = pd.read_csv(f)
    assert len(d) == n_expected, f"{label}: expected {n_expected} checks, found {len(d)}"
    d.insert(0, "Work_item", label)
    frames.append(d[["Work_item", "Check_Item", "Expected", "Actual", "Status"]])
V = pd.concat(frames, ignore_index=True)
V.insert(0, "Check_ID", range(1, len(V) + 1))
V.to_csv(HERE / "validation_report_week08.csv", index=False)
print(len(frames), "files,", len(V), "checks,", int((V.Status == "PASS").sum()), "pass")
assert (V.Status == "PASS").all()
