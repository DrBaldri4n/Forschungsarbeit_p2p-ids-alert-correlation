from __future__ import annotations

from pathlib import Path
import pandas as pd

from .config import ATTACK_INDICATORS, ATTACK_VALUE_COL


def count_attack_ongoing_per_report(
    manifest: pd.DataFrame,
    h5_path: str | Path = "reports.h5",
) -> pd.DataFrame:
    """
    Für jeden Report (manifest['key']):
    - Report aus HDF5 lesen
    - Zeile `needle` finden (Index==needle oder irgendwo in der Zeile als Zellwert)
    - Wenn value_col == 1 -> n_attacks += 1
    Ergebnis: pro Report genau ein Counter n_attacks.
    """
    h5_path = Path(h5_path)

    out = []
    for _, row in manifest.iterrows():
        key = row["key"]
        original_name = row.get("original_name", None)

        df = pd.read_hdf(h5_path, key=key)

        n_attacks = 0

        for needle in ATTACK_INDICATORS:
            # Zeile finden: entweder Index == needle oder irgendwo in einer Zeile als Zellwert
            if needle in df.index:
                hits = df.loc[[needle]]
            else:
                mask = df.astype(str).eq(needle).any(axis=1)
                hits = df.loc[mask]

            if len(hits) > 0:
                vals = pd.to_numeric(hits[ATTACK_VALUE_COL], errors="coerce")
                n_attacks += int((vals == 1).sum())

        out.append({"key": key, "original_name": original_name, "n_attacks": n_attacks})

    return pd.DataFrame(out)