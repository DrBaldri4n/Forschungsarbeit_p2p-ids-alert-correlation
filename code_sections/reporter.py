import time
import requests
import csv
import statistics
from datetime import datetime, timedelta
from queries import get_queries  # liefert NUR Basis-PromQL-Expressions zurück

# === KONFIGURATION ===
PROMETHEUS_URL = "http://192.168.0.25"  # Prometheus-Endpunkt
IPFS_API_URL = "http://localhost:3001"  # IPFS API-Endpunkt
OUTPUT_CSV = "threat_report.csv"

# Zeitraum
TIMESPAN = 1  # Minuten
END_TIME = datetime.utcnow()
START_TIME = END_TIME - timedelta(minutes=TIMESPAN)
STEP = "30s"

# Zusätzliche Zeitversätze (in Sekunden)
OFFSETS = [0, -30, -60]


def query_prometheus_range(query, start, end, step):
    """Fragt Prometheus nach einem Zeitbereich (range query)."""
    url = f"{PROMETHEUS_URL}/api/v1/query_range"
    params = {
        "query": query,
        "start": start.isoformat() + "Z",
        "end": end.isoformat() + "Z",
        "step": step,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    result = response.json()

    if result["status"] != "success":
        raise RuntimeError(f"Fehler bei Abfrage: {result}")

    return result["data"]["result"]


def compute_basic_stats(values):
    """Berechne avg, min, max, median aus einer Liste von Floats."""
    if not values:
        return None
    try:
        avg = sum(values) / len(values)
        mn = min(values)
        mx = max(values)
        med = statistics.median(values)
    except Exception:
        return None

    return {"avg": avg, "min": mn, "max": mx, "median": med}


def compute_increase(values):
    """Berechnet eine einfache 'increase' Approximation aus einer Liste von Floats."""
    if len(values) < 2:
        return None
    inc = 0.0
    prev = values[0]
    for v in values[1:]:
        delta = v - prev
        if delta > 0:
            inc += delta
        prev = v
    return inc


def main():
    QUERIES = get_queries(START_TIME, END_TIME)

    with open(OUTPUT_CSV, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # Kopfzeile
        writer.writerow([
            "metric_name",
            "instance",
            "offset",
            "start_time",
            "end_time",
            "num_samples",
            "latest_value",
            "avg",
            "min",
            "max",
            "median",
            "increase",
            "sum"
        ])

        for metric_name, promql in QUERIES.items():
            print(f"Metrik: {metric_name} | Query: {promql}")
            for offset in OFFSETS:
                offset_end = END_TIME + timedelta(seconds=offset)
                offset_start = offset_end - timedelta(minutes=TIMESPAN)

                series_list = query_prometheus_range(promql, offset_start, offset_end, STEP)

                for series in series_list:
                    metric_labels = series.get("metric", {})
                    instance = metric_labels.get("instance", "unknown")

                    raw_values = []
                    for ts, value_str in series.get("values", []):
                        try:
                            v = float(value_str)
                        except ValueError:
                            continue
                        raw_values.append(v)

                    if not raw_values:
                        continue

                    stats = compute_basic_stats(raw_values)
                    inc = compute_increase(raw_values)
                    total_sum = sum(raw_values)
                    latest_value = raw_values[-1] if raw_values else ""

                    if stats is None:
                        continue

                    writer.writerow([
                        metric_name,
                        instance,
                        f"{offset}s",
                        offset_start.isoformat() + "Z",
                        offset_end.isoformat() + "Z",
                        len(raw_values),
                        f"{latest_value:.6f}",
                        f"{stats['avg']:.6f}",
                        f"{stats['min']:.6f}",
                        f"{stats['max']:.6f}",
                        f"{stats['median']:.6f}",
                        f"{inc:.6f}" if inc is not None else "",
                        f"{total_sum:.6f}",
                    ])

    print(f"CSV-Datei erstellt: {OUTPUT_CSV}")


if __name__ == "__main__":
    main()
    #time.sleep(TIMESPAN)  # Der Report wird nur einmal pro Minute aktualisiert
    #print("Warte auf nächste Aktualisierung...")
    #
    # Hier testweise eine testdatei veröffentlichen
    cid = publish_csv("./testfile.csv", IPFS_API_URL)
