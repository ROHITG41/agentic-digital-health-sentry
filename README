# Autonomous Chiller Plant Sizing & Hydronic Tier Sentry

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://rohit-kumar-chiller-sentry.streamlit.app)
![Python 3.12](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Standards](https://img.shields.io/badge/Standards-ASHRAE%2090.1%20%7C%20Uptime%20Tier-059669)
![Cognitive LLM](https://img.shields.io/badge/Cognitive%20LLM-gemini--3.8--flash-7C3AED)
![Architecture](https://img.shields.io/badge/Architecture-Deterministic--Cognitive%20Agent-1E3A8A)

> **Dataset & Confidentiality Note:** This application is an independent engineering architecture demonstration validated on representative, anonymized project datasets.

---

### Executive Problem Statement
Early-stage concept sizing of central chilled-water plants for mission-critical facilities frequently suffers from rule-of-thumb oversizing, excessive header velocities causing pipe erosion, and mismatches between $N+1$ vs. $2N$ dual-loop piping topologies and Uptime Institute Tier III/IV concurrent maintainability requirements.

### Operational Value
* **Eliminates Sizing & Hydraulic Errors:** Executes exact thermodynamic mass flow balances, Hazen-Williams friction head loss, pipe velocity bounds, and pump Brake Horsepower (BHP) calculations on native CPU.
* **Verifies Tier Topology Early:** Audits header redundancy and isolation topologies against Uptime Institute Tier III/IV continuous cooling principles before tender specifications are issued.
* **Accelerates Concept DBR Synthesis:** Compiles verified hydraulic calculations into a structured Concept Design Basis Report (DBR) for rapid engineering review.

---

### System Architecture

```mermaid
flowchart TD
    classDef client fill:#EFF6FF,stroke:#2563EB,stroke-width:2px,color:#1E3A8A;
    classDef deterministic fill:#ECFDF5,stroke:#059669,stroke-width:2px,color:#064E3B;
    classDef logic fill:#FAF5FF,stroke:#7C3AED,stroke-width:2px,color:#4C1D95;
    classDef output fill:#F8FAFC,stroke:#475569,stroke-width:2px,color:#0F172A;

    subgraph INGRESS ["1. PLANT LOAD & HYDRONIC PARAMETERS"]
        UI["Streamlit Cloud Interface<br/><b>Cooling Tonnage, Loop Delta-T, Pipe NPS & Tier Target</b>"]:::client
    end

    subgraph CPU_GATE ["2. DETERMINISTIC CPU THERMODYNAMIC & HYDRONIC ENGINE"]
        direction TB
        FLOW["<b>Mass Flow & Friction Physics (CPU)</b><br/>GPM = (Tons x 24) / Delta-T<br/>Hazen-Williams Head Loss & Velocity Check"]:::deterministic
        PUMP["<b>Pumping Power & Redundancy Audit</b><br/>Computes Pump BHP & N+1 vs. 2N Loop Topology"]:::deterministic
        FLOW --> PUMP
    end

    subgraph COGNITIVE ["3. COGNITIVE ENGINEERING BENCHMARKING"]
        LLM["<b>Google Gemini Engine (gemini-3.8-flash)</b><br/>Benchmarks Efficiency against ASHRAE 90.1<br/>Evaluates Concurrent Maintainability & Failure Modes"]:::logic
    end

    subgraph DELIVERABLE ["4. CONCEPT DESIGN DELIVERABLE"]
        DBR["<b>Executive Concept Design Basis Report (DBR)</b><br/>Verified Plant Schedule & Downloadable Memo"]:::output
    end

    UI --> FLOW
    PUMP -->|Verified Hydronic & BHP Metrics| LLM
    LLM --> DBR
```

---

### Core Engineering Equations Enforced on CPU
1. **Chilled Water Volumetric Flow Rate:**  
   $$\text{GPM} = \frac{Q_{\text{tons}} \times 24}{\Delta T_{\text{CHW}}}$$
2. **Hazen-Williams Friction Head Loss:**  
   $$h_f = 0.2083 \left(\frac{100}{C}\right)^{1.852} \frac{Q^{1.852}}{d^{4.8655}} \times \frac{L}{100}$$

---

### Technology Stack
* **Runtime & UI:** Python 3.12, Streamlit Community Cloud
* **Scientific & Validation Engine:** NumPy, Pydantic v2
* **Cognitive Synthesis:** Google GenAI SDK (`gemini-3.8-flash`)

### Author & Architect
**Rohit Kumar, PMP, CEng, CEA, FSEr (TÜV)**  
Cross-Technology Technical Architect | Mission-Critical Infrastructure & Applied AI Solutions  
[LinkedIn](https://www.linkedin.com/in/rohitg41) | [Live Application](https://rohit-kumar-chiller-sentry.streamlit.app)

---

### Enterprise Advisory & Custom Architecture
Available for technical consulting, custom agentic workflow development, and private enterprise deployments.  
**Connect:** [LinkedIn](https://www.linkedin.com/in/rohitg41) | **Email:** `grohit41@gmail.com`

---

### Intellectual Property & Licensing
**Copyright © 2026 Rohit Kumar. All Rights Reserved.**  
This repository and its source code are published solely for technical portfolio evaluation and architectural demonstration. Unauthorized copying, redistribution, or commercial deployment is prohibited without prior written consent.
