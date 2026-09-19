"""Reproduce core reliability diagnostics on the public sample."""
from pathlib import Path
import pandas as pd

DATA = Path(__file__).resolve().parents[1] / "data" / "sample_anonymised_data.csv"

def add_reliability_score(df):
    out = df.copy()
    out["abs_strength_gap"] = out["strength_difference"].abs()
    out["reliability_adjustment"] = 0
    ha = out["predicted_result"].isin(["HOME", "AWAY"])
    out.loc[ha & out["abs_strength_gap"].between(20, 29), "reliability_adjustment"] = 6
    out.loc[ha & (out["abs_strength_gap"] >= 30), "reliability_adjustment"] = 10
    out["reliability_score"] = out["result_confidence_score"] + out["reliability_adjustment"]
    return out

def main():
    df = pd.read_csv(DATA)
    for c in ["result_correct","result_confidence_score","strength_difference"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    scored = add_reliability_score(df)
    print(f"Rows: {len(scored):,}")
    print(f"Sample result accuracy: {scored['result_correct'].mean():.3%}")
    eligible = scored[scored["predicted_result"].isin(["HOME","AWAY"]) & (scored["result_confidence_score"] >= 70)]
    for gap in (10,20,30):
        x = eligible[eligible["abs_strength_gap"] >= gap]
        print(f"gap >= {gap}: n={len(x):,}, accuracy={x['result_correct'].mean():.3%}")

if __name__ == "__main__":
    main()
