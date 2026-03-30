# Forschungsdesign: Kollaborative Intrusion Detection in P2P-Netzwerken

## 1\. Problemstellung

In einem **P2P-Netzwerk** verfügt jeder Peer über eine Instanz von **X Sicherheitsdetektoren**. Diese liefern im Intervall von **X-Sekunden** ein binäres Ergebnis (*"Attack: Yes/No"*) inklusive relevanter Feature-Extrakte.

Die lokal erzeugten Ergebnisse werden netzweit abgeglichen und zu einer **gewichteten Angriffswahrscheinlichkeit** aggregiert. Ziel ist es, durch kollektive Intelligenz **echte Angriffe von Fehlalarmen (False Positives) zu unterscheiden**.

Anstelle rein ML-basierter Cross-Validation liegt der Fokus auf **Distributed Decision-Making** und **Alarm Correlation**.

* * *

## 2\. Zielsetzung

1.  **Kernziel:** Identifikation und Evaluierung einer robusten Methode zur dezentralen Entscheidungsfusion.
2.  **Nachgelagertes Ziel:** Anwendung einer Cross-Validation auf öffentlichen Datensätzen, wobei das Datenset so gesplittet wird, dass es die Verteilung einzelner Peers simuliert.

* * *

## 3\. Strategische Säulen (Search & Analysis)

### Strategie 1: Method Identification (Core Algorithm)

**Fokus:** Mathematische Logik zur Transformation unsicherer Einzelalarme in eine robuste Gesamtentscheidung.

- **Mögliche Methoden:** Dempster–Shafer Theory (DST), Weighted Voting, Bayesian Consensus, Majority Voting.

- - **Dempster-Shafer-Evidenztheorie:** Dieses Verfahren kombiniert Hinweise aus verschiedenen Quellen unter Berücksichtigung von Unsicherheit und Unwissenheit, indem es Glaubwürdigkeitsgrade für Mengen von Hypothesen berechnet.
        
    - **Fuzzy-basierte Fusion:** Hierbei werden unscharfe Sensordaten mithilfe von linguistischen Variablen und Zugehörigkeitsfunktionen verarbeitet, um durch vordefinierte Regelwerke eine gemeinsame, interpretierbare Entscheidung zu treffen.
        
    - **Gewichtetes Voting:** Bei diesem einfachen Abstimmungsverfahren erhält jede Datenquelle ein spezifisches Gewicht basierend auf ihrer Zuverlässigkeit, wobei die finale Entscheidung durch die gewichtete Summe aller Einzelstimmen ermittelt wird.
        
    - **Bayes-basierte Konsensmodelle:** Dieses statistische Verfahren nutzt Vorwissen (A-priori-Wahrscheinlichkeit) und aktuelle Beobachtungen, um mittels der Bayes-Regel die Wahrscheinlichkeit für das Eintreten eines Ereignisses kontinuierlich zu aktualisieren.
        

- **Suchbegriffe:**
    
    > `("Dempster-Shafer" OR "weighted voting" OR "bayesian consensus") AND ("collaborative intrusion detection" OR "distributed IDS") AND "alert fusion"`
    
- **Ergebnis:** Identifikation von **5–10 Hauptreferenzen**, die mathematische Fusion konkret auf verteilte IDS anwenden.

### Strategie 2: Problem Solving (Validation of Goal)

**Fokus:** Ausschluss zentralisierter Server-Ansätze; Fokus auf rein dezentrale Kollaboration.

- **Suchbegriffe:**
    
    > `("Dempster-Shafer" OR "weighted voting" OR "Bayesian consensus" OR "majority voting") AND ("intrusion detection" OR "IDS") AND ("peer-to-peer" OR "P2P" OR "collaborative" OR "decentralized" OR "distributed") AND ("alert fusion" OR "alert correlation" OR "alert verification" OR "alert confidence" OR "false positive reduction") NOT ("SIEM" OR "centralized server" OR "cloud-based correlation")`
    

### Strategie 3: Evaluation & Datasets (Secondary Goal)

**Fokus:** Auswahl und Aufbereitung der Datengrundlage.

- **Vorgehen:** Splitting großer Datensätze in *N* Teile zur Simulation einer Peer-Infrastruktur.
- **Suchbegriffe:**
    
    > `"evaluation methodology" AND "collaborative intrusion detection" AND ("dataset" OR "simulation") AND ("CIC-IDS" OR "NSL-KDD" OR "UNSW-NB15")`
    
- **Ergebnis:** Festlegung des Datensatze und der Simulationsumgebung.

* * *

## 4\. Zielmatrix

| Zielbereich | Schwerpunkt | Erwartetes Ergebnis |
| :--- | :--- | :--- |
| **Methode (S1)** | Fusionsmechanismus | Vergleich: DST vs. Voting-Ansätze für P2P |
| **Validierung (S2)** | Kollaborationsnutzen | Quantifizierter Nachweis der FP-Reduktion |
| **Evaluation (S3)** | Realistische Tests | Modell für Peer-simulierte Dataset-Splits |

* * *

> **Nächster Schritt:** Möchtest du, dass ich basierend auf **Strategie 3** eine Tabelle erstelle, wie man die Datensätze (z. B. CIC-IDS2017) am besten auf $N$ Peers aufteilt, um verschiedene Angriffs-Szenarien zu simulieren?
