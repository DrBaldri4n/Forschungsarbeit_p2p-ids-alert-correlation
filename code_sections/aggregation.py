from __future__ import annotations

from pathlib import Path
import pandas as pd
import numpy as np

from .config import BASE_WEIGHT, MAX_WEIGHT, K, BINARY_INDICATORS, BINARY_COLS, BINARY_THRESHOLD


def add_report_weight(
    df_counts: pd.DataFrame,
    n_col: str = "n_attacks",
    out_col: str = "weight",
) -> pd.DataFrame:
    """
        
    """
    out = df_counts.copy()
    n = pd.to_numeric(out[n_col], errors="coerce").fillna(0).to_numpy()
    out[out_col] = BASE_WEIGHT + (MAX_WEIGHT - BASE_WEIGHT) * (1.0 - np.exp(-K * n))
    return out

def aggregate_weighted_reports(
    weights_df: pd.DataFrame,
    h5_path: str | Path = "reports.h5",
    key_col: str = "key",
    weight_col: str = "weight",
    cols: tuple[str, ...] = ("latest_value", "avg", "min", "max", "median", "increase", "sum"),
) -> pd.DataFrame:
    """
    Aggregiert report_00001, report_00002, ... zu einem neuen Report:
    für jede Zelle der `cols`:
      agg = (Σ report_i * weight_i) / (Σ weight_i)

    Alle Reports müssen gleiche Zeilenanzahl haben und gleiche Index/Zeilenreihenfolge).
    """
    h5_path = Path(h5_path)

    num = None  # Numerator: Σ(df * w)
    denom = 0.0

    validate_same_metrics(weights_df, h5_path=h5_path, key_col=key_col)

    for _, r in weights_df.iterrows():
        key = r[key_col]
        w = float(r[weight_col])

        df = pd.read_hdf(h5_path, key=key)  # lädt DataFrame unter dem Key.
        x = df.loc[:, list(cols)].apply(pd.to_numeric, errors="coerce")

        if num is None:
            num = x * w
        else:
            # addiert elementweise; Align passiert über Index/Columns (muss matchen).
            num = num.add(x * w, fill_value=0)

        denom += w

    if num is None:
        raise ValueError("weights_df ist leer, nichts zu aggregieren.")
    if denom == 0:
        raise ValueError("Summe der Weights ist 0, Division nicht möglich.")

    agg = num / denom
    return agg

def validate_same_metrics(
    weights_df: pd.DataFrame,
    h5_path: str | Path,
    key_col: str = "key",
) -> None:
    '''
    Prüft das nur aggregiert wird wenn alle Reports die gleichen metric_name Zeilen haben (gleicher Index, gleiche Reihenfolge).
    '''
    h5_path = Path(h5_path)

    ref_index = None
    ref_key = None

    for _, r in weights_df.iterrows():
        key = r[key_col]
        df = pd.read_hdf(h5_path, key=key)

        if ref_index is None:
            ref_index = df.index
            ref_key = key
            continue

        if not ref_index.equals(df.index):
            raise ValueError(
                f"Metric mismatch: {key} has different metric_name/Order as {ref_key}."
            )

def binarize_indicators(aggregated_values: pd.DataFrame) -> pd.DataFrame:
    '''
    Für die in BINARY_INDICATORS gelisteten Zeilen (Index) werden die Werte in BINARY_COLS anhand von BINARY_THRESHOLD binarisiert:
    Wenn Wert >= BINARY_THRESHOLD folgt 1, sonst 0.
    Damit Attack Indicators keine Komma Werte haben.
    '''
    out = aggregated_values.copy()

    mask = out.index.astype(str).isin(BINARY_INDICATORS)
    if not mask.any():
        return out

    cols = [c for c in BINARY_COLS if c in out.columns]
    out.loc[mask, cols] = (out.loc[mask, cols] >= BINARY_THRESHOLD).astype("int64")
    return out