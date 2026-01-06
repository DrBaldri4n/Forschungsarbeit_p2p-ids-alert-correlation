# Literaturrecherche: Alert Fusion in Distributed IDS

## Suchanfrage 1

- **Dempster-Shafer-Evidenztheorie:** Dieses Verfahren kombiniert Hinweise aus verschiedenen Quellen unter Berücksichtigung von Unsicherheit und Unwissenheit, indem es Glaubwürdigkeitsgrade für Mengen von Hypothesen berechnet.
    
- **Fuzzy-basierte Fusion:** Hierbei werden unscharfe Sensordaten mithilfe von linguistischen Variablen und Zugehörigkeitsfunktionen verarbeitet, um durch vordefinierte Regelwerke eine gemeinsame, interpretierbare Entscheidung zu treffen.
    
- **Gewichtetes Voting:** Bei diesem einfachen Abstimmungsverfahren erhält jede Datenquelle ein spezifisches Gewicht basierend auf ihrer Zuverlässigkeit, wobei die finale Entscheidung durch die gewichtete Summe aller Einzelstimmen ermittelt wird.
    
- **Bayes-basierte Konsensmodelle:** Dieses statistische Verfahren nutzt Vorwissen (A-priori-Wahrscheinlichkeit) und aktuelle Beobachtungen, um mittels der Bayes-Regel die Wahrscheinlichkeit für das Eintreten eines Ereignisses kontinuierlich zu aktualisieren.
    

**Query:** `("Dempster-Shafer" OR "weighted voting" OR "bayesian consensus") AND ("collaborative intrusion detection" OR "distributed IDS") AND "alert fusion"`

| Titel | Jahr | Zusammenfassung / Abstract |
| :--- | :--- | :--- |
| Alert Fusion of Intrusion Detection systems using Fuzzy Dempster shafer Theory | 2017 | chlägt ein Alert-Fusion-Framework für Intrusion Detection Systeme vor, das klassische Dempster-Shafer-Evidenztheorie mit Fuzzy-Logik kombiniert, um Unsicherheit, Vagheit und teils widersprüchliche Alarme mehrerer IDS zu behandeln. IDS-Ausgaben werden zunächst über Fuzzy-Mitgliedsfunktionen in linguistische Vertrauensgrade (z.B. low/medium/high) transformiert, anschließend mit einer modifizierten Dempster-Shafer-Kombinationsregel fusioniert und schließlich in eine aggregierte Alarmkonfidenz überführt, die zur Reduktion von False Positives und zur Priorisierung relevanter Angriffe genutzt wird. Experimente mit mehreren heterogenen Sensoren zeigen, dass der fuzzy-DS-Ansatz sowohl Erkennungsrate als auch Alarmqualität gegenüber einfacher Voting- oder klassischer DS-Fusion verbessert. |
| A UNIFIED ALERT FUSION MODEL FOR INTELLIGENT ANALYSIS OF SENSOR DATA | 2006 | Die Dissertation stellt ein einheitliches Alert-Fusion-Modell vor, das drei Hauptaufgaben – Alert-Priorisierung, Alert-Clustering und Alert-Korrelation – in einem gemeinsamen Framework kombiniert, um aus Multi-Sensor-IDS-Daten einen globalen Sicherheitszustand mit Confidence-Score abzuleiten. Kern ist ein possibilistischer Ansatz mit Fuzzy Cognitive Modeling, der Unsicherheit und Vagheit in den Sensordaten abbildet, eine neue mehrstufige Clustering-Methode für inexacte Ähnlichkeiten bereitstellt und ein abstraktes Incident-Modell für skalierbare, unsichere Korrelation nutzt. Zusätzlich wird ein dynamischer Fusionsmechanismus beschrieben, der bei Misuse-Sensoren Cluster- und Korrelationsresultate zusammenführt und bei Anomalie-Sensoren Evidenz aus primären und sekundären Sensoren verknüpft, was insgesamt zu besserer Situationswahrnehmung im verteilten IDS führt. |
| Enhancing Performance of Intrusion Detection Systems using Data Fusion Techniques | 2017 | Die Arbeit entwickelt ein \*\*Reliable Alert Fusion (RAF)\*\*‑Modell, das Alerts mehrerer heterogener IDS mittels erweiterter Dempster‑Shafer‑Evidenztheorie so fusioniert, dass insbesondere unzuverlässige Sensoren automatisch „abgewertet“ werden. Zentrales Element ist eine Informations­theorie‑basierte Definition von IDS‑Reliability: Bei bekanntem Ground Truth werden wahre und falsche Alarme zur Zuverlässigkeitsschätzung genutzt, bei unbekanntem Ground Truth wird Reliability aus Konflikten zwischen IDS‑Entscheidungen über dasselbe Ereignis abgeleitet und in die Fusionsregel eingerechnet. Simulationen auf DARPA99, KDD99 und NSL‑KDD zeigen, dass RAF gegenüber Einzel‑IDS und klassischer DS‑Fusion die Erkennungsleistung steigert und die False‑Positive‑Rate deutlich reduziert, insbesondere in Szenarien mit komplementären bzw. konfligierenden IDS‑Aussagen. |
| Enhancing security in smart healthcare systems... (Edge Computing / SS-RBFN) | 2024 | *Der Artikel präsentiert ein intelligentes Edge-Computing‑Framework für \*\*Smart-Healthcare‑Systeme\*\*, das Sicherheitsbedrohungen in IoT‑basierten medizinischen Umgebungen mit einer kombinierten Salp Swarm Optimization–Radial Basis Function Neural Network‑Methode (SS‑RBFN) erkennen soll. Sensordaten (inkl. EHR‑Kontext) werden an der Edge vorverarbeitet, dann vom SS‑RBFN‑Modell in „normal“ vs. „bösartig“ klassifiziert und vor der Übertragung in die Cloud zusätzlich per RSA verschlüsselt, um Vertraulichkeit zu gewährleisten. Auf einem IoT‑Healthcare‑Datensatz erreicht das Modell laut Evaluation sehr hohe Kennzahlen (≈99,9 % Accuracy, ≈99,8 % Precision, niedrige Latenz ~1,2 s) und übertrifft damit mehrere Vergleichsmodelle, der Artikel ist jedoch nachträglich als „retracted“ gekennzeichnet und sollte daher mit Vorsicht zitiert werden.* |
| An Investigation on Biometric Internet Security | 2017 | Der Artikel führt ein \*\*Reliable Alert Fusion (RAF)\*\*‑Verfahren für mehrere, heterogene IDS ein, das klassische Dempster‑Shafer‑Fusion explizit um eine modellierte Zuverlässigkeit jedes Sensors ergänzt, um robuste Entscheidungen trotz widersprüchlicher Alarme zu treffen. Die Reliability wird dabei aus wahren und falschen Alarmen (bei bekanntem Ground Truth) bzw. aus Konflikten zwischen IDS‑Entscheidungen (bei unbekanntem Ground Truth) hergeleitet und als Gewicht in eine neue Fusionsregel eingebracht, sodass wenig vertrauenswürdige IDS den Gesamtentscheid nur schwach beeinflussen. |
| Semantic-based Context-aware Alert Fusion for Distributed IDS | 2013 | Das Paper stellt einen \*\*semantikbasierten, kontext‑sensitiven Alert‑Fusion‑Ansatz\*\* für verteilte IDS vor. Szenario zeigt die Evaluation, dass der Ansatz die Zahl irrelevanter/duplizierter Alarme deutlich senkt, während die Detection Rate von Snort und ISS RealSecure beibehalten wird. |

* * *

## Suchanfrage 2

**Query:** `("Dempster-Shafer" OR "weighted voting" OR "Bayesian consensus" OR "majority voting") AND ("intrusion detection" OR "IDS") AND ("peer-to-peer" OR "P2P" OR "collaborative" OR "decentralized" OR "distributed") AND ("alert fusion" OR "alert correlation" OR "alert verification" OR "alert confidence" OR "false positive reduction") NOT ("SIEM" OR "centralized server" OR "cloud-based correlation")`

| Titel | Jahr | Zusammenfassung / Abstract |
| :--- | :--- | :--- |
| Exploiting the Outcome of Outlier Detection for Novel Attack Pattern Recognition on Streaming Data | 2021 | Framework zur **Echtzeit-Analyse und Korrelation von Alerts** aus **unsupervisierten Anomalie-basierten IDS** in **Streaming-Umgebungen**. Es adressiert Probleme wie **Concept Drift** und **fehlende Unterstützung für Streaming-Daten**, indem es Alerts kontinuierlich korreliert, zu Clustern zusammenfasst und **„Fingerabdruck“-ähnliche Signaturen** generiert, die Angriffsbeziehungen, Datenmerkmale und zeitliche Dynamik abbilden. Diese Signaturen ermöglichen das Erkennen und Vergleichen sowohl bekannter als auch bisher unbekannter Angriffsmuster. |
| <span style="color: rgb(0, 0, 0);">Machine Learning and Reputation Based Misbehavior Detection in Vehicular Communication Networks</span> | 2020 | **Misbehavior Detection System (MDS)** für Fahrzeugnetze, das interne Angriffe wie Sybil-, DoS- und Falschwarnungsangriffe erkennt, die durch reine Kryptografie nicht zuverlässig abgefangen werden können. Das System kombiniert **Machine-Learning-Klassifikation** mit einem **Reputationssystem**, das für jedes Fahrzeug einen Vertrauenswert führt und diesen mit einer **Dempster-Shafer-basierten kollaborativen Entscheidungsfindung** zu einem gemeinsamen Urteil über das (Fehl‑)Verhalten von Fahrzeugen und deren Nachrichten zusammenführt. |
| Systematic Literature Review of Security Event Correlation Methods | 2022 | **Literaturüberblick 2010–2021: Kriterien wie **verwendete Korrelationsmethoden, Wissensextraktion, Datenquellen, Architekturansätze und Evaluationsmetriken** klassifiziert und verglichen, inklusive der eingesetzten Datensätze und Metriken zur Bewertung.** |
| On_Holistic_Multi-Step_Cyberattack_Detection_via_a_Graph-based_Correlation_Approach | 2022 | Ansatz zur **Erkennung mehrstufiger Cyberangriffe** auf digitalisierte Stromverteilnetze, in denen Angreifer mehrere koordinierte Schritte ausführen, um ihr Ziel zu erreichen. Dazu wird eine **graphbasierte Cyber-Intelligence-Datenbank** aufgebaut, die heterogene Daten als Wissensbasis integriert, und darauf aufbauend ein **modellbasierter Alert-Korrelationsansatz** verwendet, der IDS-Meldungen und andere Hinweise zu zusammenhängenden Angriffssequenzen (Attack Campaigns) verknüpft. Ziel ist es, durch diese korrelierte Sicht eine höhere **situationale Awareness** zu erreichen |
| Optimization Scheme of Collaborative Intrusion Detection System Based on Blockchain Technology | 2025 | Das Abstract beschreibt ein **Blockchain-basiertes kollaboratives Intrusion-Detection-Framework (BCIDF)**, das die Erkennungsleistung von CIDS verbessert, indem mehrere Knoten gemeinsam Angriffe detektieren und ihre Erkenntnisse sicher austauschen. Durch einen **Alternating Random Assignment Selection Mechanism (ARASM)** werden geeignete Domain-Leader-Knoten ausgewählt, um den Netzwerkverkehr aufzuteilen und Konflikt- bzw. Kollisionsdomänen bei der Alarmübermittlung zu verkleinern. Für die eigentliche Angriffserkennung nutzt das System einen **Weighted Random Forest (WRF)** als Ensemble-Lernverfahren, das kollaborative Detection-Ergebnisse über die Knoten hinweg integriert und auf dem NSL-KDD-Datensatz eine höhere Erkennungsgenauigkeit als klassische IDS-Ansätze zeigt. |
| Collaborative intrusion detection using weighted ensemble averaging deep neural network for coordinated attack detection in heterogeneous network | 2024 | **kollaboratives Intrusion-Detection-System (CIDS)**, das speziell auf die Erkennung koordinierter Angriffe in heterogenen Netzwerken mit vielen unterschiedlichen Geräten und Systemen abzielt. Es nutzt dazu ein **Weighted Ensemble Averaging Deep Neural Network (WEA-DNN)**, in dem mehrere unterschiedlich aufgebaute und auf verschiedenen Datenteilmengen trainierte DNN-Modelle kombiniert werden; die Gewichte der einzelnen Modelle werden mittels **Differential Evolution** optimiert, um ihren Beitrag zur gemeinsamen Entscheidung zu bestimmen. |

* * *

## Analyse der Forschungslücke

**Aktuelle theoretische Basis**

- Häufig eingesetzte Verfahren sind **Dempster-Shafer-Evidenztheorie**, **fuzzy-basierte Fusion**, **gewichtetes Voting** sowie **Bayes-basierte Konsensmodelle**.
    
- Ziel dieser Ansätze ist primär die **Reduktion von False Positives** sowie die **Erhöhung der Detektionsrate** durch die Kombination mehrerer, heterogener Detektoren.
    

**Häufige Einschränkungen in bestehenden Arbeiten**

- Viele Konzepte setzen eine **zentrale Fusionsinstanz** oder zumindest **koordinierende Knoten** voraus.
    
- Es fehlen Arbeiten, die sich explizit mit **Alert Fusion in vollständig dezentralen P2P-Netzwerken** befassen.
    
- **Dynamische, lernende Gewichtsanpassungen der Peers** (z. B. basierend auf vergangener Fehlalarm-Historie) werden selten bis gar nicht adressiert.
