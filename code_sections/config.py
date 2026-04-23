from __future__ import annotations
from pathlib import Path

MODULE_DIR = Path(__file__).resolve().parent

# Einheitliche Ordner
TMP_DIR = MODULE_DIR / "reports_tmp"

# TIME_Window bei versetzten zeiten
TIME_COL = "start_time"
MAX_TIME_SKEW_SECONDS = 90
WINDOW_SECONDS = 60


# Detection vorhersagen:
ATTACK_INDICATORS: tuple[str, ...] = (
    "attack_ongoing",
    "ids_hardware_attack_prediction",
    "ids_xlstm_attack_probability",
    "ids_transformer_attack_probability",
    "transformer_prediction",
    "ids_power_lstm_anomaly",
    "ids_wattmeter",
    "ids_power_isolation_forest_anomaly"
)

ATTACK_VALUE_COL: str = "latest_value"

# Gewichtungs-Parameter
BASE_WEIGHT: float = 1.0
MAX_WEIGHT: float = 3.0
K: float = 0.1

# HDF5-Store Verhalten
H5_FILENAME: str = "reports.h5"

# Aggregation / Export
AGG_COLS: tuple[str, ...] = (
    "latest_value", "avg", "min", "max", "median", "increase", "sum"
)
AGG_OUT_CSV_NAME: str = "aggregated_threat_report.csv"

# Attack Indicators dürfen keine komma werte haben
BINARY_INDICATORS: tuple[str, ...] = ATTACK_INDICATORS
BINARY_COLS: tuple[str, ...] = AGG_COLS
BINARY_THRESHOLD: float = 0.5  # >=0.5 => 1 sonst 0
