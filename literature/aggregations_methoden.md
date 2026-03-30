# Methoden zur Aggregation variabler Peer-Daten

## 1. Statistische Aggregation

Erzeugt pro Zeitstempel Statistiken über alle aktiven Peers (Mittelwert, Min, Max, Varianz pro Feature, Anzahl aktiver Peers). Dies ergibt einen festen Vektor, unabhängig von der aktuellen Anzahl an Geräten.

**Im Paper:** Debar & Wespi "Aggregation and Correlation of Intrusion-Detection Alerts" (RAID 2001), **Section 5.3 "The Aggregation Relationship Situations"** – Erklärung der Aggregation nach bestimmten Kriterien zur Erstellung von kondensierter Alert-Übersicht.

Debar & Wespi: [https://wenke.gtisc.gatech.edu/ids-readings/Herve_Debar_IDS_Correlation_Raid01.pdf]

---

## 2. Padding + Masking

Ein fester Vektor mit maximalen Slots (n_max) wird erzeugt. Fehlende Peers werden mit Nullen gefüllt; eine Maske markiert belegte vs. leere Slots.

**Im Paper:** Vaswani et al. "Attention Is All You Need" (NIPS 2017), **Section 3.2 "Multi-Head Attention"** und **Section 3.1 "Encoder and Decoder Stacks"** – Erklärung von Masking-Mechanismen zur Behandlung variabler Sequenzlängen.

Vaswani et al.:[https://arxiv.org/abs/1706.03762]

---

## 3. Deep Sets (Sum/Max Pooling)

Jede Ladesäule wird durch ein neuronales Netz f in ein Embedding z_i transformiert. Diese Embeddings werden global aggregiert via **Summen-** oder **Max-Pooling**, was Permutationsinvarianz garantiert.

**Im Paper:** Zaheer et al. "Deep Sets" (NIPS 2017), **Section 3.1 "Architecture Invariant model"** und **Theorem 2** – Mathematische Charakterisierung permutationsinvarianter Funktionen: `f(X) = ρ(Σ φ(x))` für Summen-Pooling oder mit Max-Variante in **Equation 4**.

Zaheer et al.:[https://arxiv.org/abs/1703.06114]

---

## 4. Set2Set / Attention-basierte Aggregation

Ein Attention-Mechanismus lernt, welche Peers wichtiger sind. Embeddings z_i werden mit gelernten Gewichten w_i kombiniert, sodass auffällige Peers mehr Einfluss haben.

**Im Paper:** Vinyals, Bengio & Kudlur "Order Matters: Sequence to Sequence for Sets" (ICLR 2016), **Section 4.2 "Attention Mechanisms"** und **Section 4.3 "Read, Process, Write"** – Erklärung der content-based attention für permutationsinvariante Aggregation von Set-Elementen (Equations 3–7).

Vinyals, Bengio & Kudlur: [https://arxiv.org/abs/1511.06391]

---

## 5. GNN + Pooling (E-GraphSAGE)

Peers werden als Graph-Knoten modelliert; ihre Beziehungen als Kanten. Ein Graph Neural Network propagiert Informationen über Kanten; ein globales Pooling über alle Knoten erzeugt einen festen Graph-Vektor.

**Im Paper:** Lo et al. "E-GraphSAGE: A Graph Neural Network-based Intrusion Detection System for IoT" (IEEE/IFIP 2022), **Section IV.A "E-GraphSAGE Model" und Section IV.B "E-GraphSAGE NIDS"** – Erklärung von Edge Embedding (Equation 5) und Aggregation über Nachbarschaften (Equation 4: `h^k(N_v) = AGG_k(e^{k-1}_{uv}, u ∈ N_v)`).

Lo et al.: [https://arxiv.org/abs/2103.16329]