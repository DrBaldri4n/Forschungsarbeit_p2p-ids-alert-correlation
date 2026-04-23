from __future__ import annotations

from pathlib import Path
import pandas as pd
import warnings

from .config import TIME_COL, MAX_TIME_SKEW_SECONDS


def filter_reports_with_NaN(
    manifest: pd.DataFrame,
    h5_path: str | Path,
    key_col: str = "key",
) -> pd.DataFrame:
    '''
    Wenn NaN werte irgendwo in einem report auftauchen wird er ignoriert
    '''

    h5_path = Path(h5_path)

    keep = []
    for _, row in manifest.iterrows():
        key = row[key_col]
        original_name = row.get("original_name", None)

        df = pd.read_hdf(h5_path, key=key)

        # True wenn irgendwo im gesamten Report ein NaN steht (auch metric_name etc.)
        has_nan = df.isna().any(axis=None)
        if has_nan:
            warnings.warn(
                f"{key} ({original_name}) has NaN value(s) and got ignored",
                category=UserWarning,
                stacklevel=2,
            )
            continue

        keep.append(row)

    return pd.DataFrame(keep).reset_index(drop=True)

def filter_reports_by_time_skew(
    manifest: pd.DataFrame,
    h5_path: str | Path,
    key_col: str = "key",
) -> pd.DataFrame:
    '''
    Wenn der Median des Timewindows eines reports mehr als MAX_TIME_SKEW_SECONDS von der Referenzzeit (Median über alle Reports) abweicht, wird er ignoriert.
    '''
    h5_path = Path(h5_path)

    # 1) Pro Report eine repräsentative Zeit bestimmen (Median der start_time-Spalte)
    per_report_time: list[tuple[int, str, pd.Timestamp, str | None]] = []
    for i, row in enumerate(manifest.itertuples(index=False)):
        key = getattr(row, key_col)
        original_name = getattr(row, "original_name", None)

        # load report
        df = pd.read_hdf(h5_path, key=key)
        # konvertiere in datetime werte
        t = pd.to_datetime(df[TIME_COL], utc=True, errors="coerce")
        # Berechne median pro report
        per_report_time.append((i, key, t.median(), original_name))

    if not per_report_time:
        return manifest.iloc[0:0].copy()

    # 2) Referenzzeit: Median über alle Reports
    ref = pd.Series([x[2] for x in per_report_time]).median()

    # 3) Filter: Abweichung <= MAX_TIME_SKEW_SECONDS
    keep_rows = []
    for i, key, t_med, original_name in per_report_time:
        skew = abs((t_med - ref).total_seconds())
        if skew > MAX_TIME_SKEW_SECONDS:
            warnings.warn(
                f"{key} ({original_name}) time skew {skew:.1f}s > {MAX_TIME_SKEW_SECONDS}s; got ignored",
                UserWarning,
                stacklevel=2,
            )
            continue
        keep_rows.append(manifest.iloc[i])

    return pd.DataFrame(keep_rows).reset_index(drop=True)