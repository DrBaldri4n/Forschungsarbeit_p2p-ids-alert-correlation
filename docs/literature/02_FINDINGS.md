# Literaturrecherche: Alert Fusion in Distributed IDS

## Suchanfrage 1

**Query:** `("Dempster-Shafer" OR "weighted voting" OR "bayesian consensus") AND ("collaborative intrusion detection" OR "distributed IDS") AND "alert fusion"`

| Titel | Jahr | Zusammenfassung / Abstract |
| :--- | :--- | :--- |
| **Alert Fusion of Intrusion Detection systems using Fuzzy Dempster shafer Theory** | 2017 | Kombiniert klassische Dempster-Shafer-Theorie mit Fuzzy-Logik. IDS-Ausgaben werden in linguistische Vertrauensgrade (low/medium/high) transformiert, um Unsicherheit und Widersprüche zu handhaben. Reduziert False Positives und verbessert die Priorisierung. |
| **A UNIFIED ALERT FUSION MODEL FOR INTELLIGENT ANALYSIS OF SENSOR DATA** | 2006 | Dissertation über ein Framework für Priorisierung, Clustering und Korrelation. Nutzt Fuzzy Cognitive Modeling für einen possibilistischen Ansatz und beschreibt dynamische Fusion für Misuse- und Anomalie-Sensoren. |
| **Enhancing Performance of Intrusion Detection Systems using Data Fusion Techniques** | 2017 | Stellt das **Reliable Alert Fusion (RAF)**\-Modell vor. Nutzt Informationstheorie, um die Zuverlässigkeit von Sensoren zu bewerten. Unzuverlässige Sensoren werden automatisch abgewertet, was die Erkennungsleistung auf Datensätzen wie NSL-KDD steigert. |
| **Enhancing security in smart healthcare systems... (Edge Computing / SS-RBFN)** | 2024 | Nutzt Salp Swarm Optimization und Neural Networks an der Edge für IoT-Healthcare. *Hinweis: Paper ist als "retracted" gekennzeichnet; Ergebnisse zur Accuracy (99,9%) sind kritisch zu hinterfragen.* |
| **An Investigation on Biometric Internet Security** | 2017 | Beschreibt ebenfalls ein RAF-Verfahren. Hier wird die Reliability explizit aus dem Konfliktpotenzial zwischen Sensoren abgeleitet, wenn kein Ground Truth vorliegt, um robuste Entscheidungen bei Widersprüchen zu treffen. |
| **Semantic-based Context-aware Alert Fusion for Distributed IDS** | 2013 | Fokus auf semantische Korrelation zur Reduktion von Duplikaten und irrelevanten Alarmen in verteilten Umgebungen, während die Erkennungsrate (z.B. von Snort) stabil bleibt. |

* * *

## Suchanfrage 2

**Query:** `("weighted voting" OR "majority voting" OR "Dempster-Shafer") AND ("intrusion detection" OR "anomaly detection") AND ("distributed" OR "peer-to-peer" OR "collaborative") AND "alert correlation"`

| Titel | Jahr | Zusammenfassung / Abstract |
| :--- | :--- | :--- |
|     |     |     |
|     |     |     |

* * *

## Analyse der Forschungslücke

### Problemstellung

Die vorliegende Literatur zeigt eine starke theoretische Basis in der mathematischen Fusion (Dempster-Shafer, Fuzzy), weist jedoch folgende Defizite auf:

1.  **Aktualität:** Ein Großteil der relevanten Grundlagenarbeiten stammt aus dem Zeitraum 2006–2017. Es gibt eine spürbare Lücke an aktuellen Publikationen (**ab 2020**).
2.  Fokus auf Fusion von Heterogenen IDS
