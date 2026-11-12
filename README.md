# Autonomous Digital Health Portfolio & ADHICS Sentry

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://rohit-kumar-health-sentry.streamlit.app)
![Python 3.12](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Compliance](https://img.shields.io/badge/Compliance-UAE%20ADHICS%20%7C%20EVM-059669)
![Cognitive LLM](https://img.shields.io/badge/Cognitive%20LLM-gemini--3.8--flash-7C3AED)
![Architecture](https://img.shields.io/badge/Architecture-Deterministic--Cognitive%20Agent-1E3A8A)

> **Dataset & Confidentiality Note:** This application is an independent engineering architecture demonstration validated on representative, anonymized project datasets.

---

### Executive Problem Statement
Healthcare capital programs and hospital digital transformation initiatives require simultaneous governance across two distinct dimensions: **financial/schedule project controls** (Earned Value Management) and **strict sovereign health-data security regulations** such as the Abu Dhabi Healthcare Information and Cyber Security Standard (ADHICS). Tracking these in disconnected spreadsheets obscures budget slippage and compliance gaps until late-stage commissioning.

### Operational Value
* **Unified Cost & Schedule Visibility:** Deterministically computes Cost Performance Index (CPI), Schedule Performance Index (SPI), and Estimate at Completion (EAC) across multi-stream healthcare programs.
* **Proactive Regulatory Alignment:** Audits clinical system deployments against ADHICS data residency, access control, and encryption requirements prior to go-live.
* **Executive Steering Synthesis:** Translates raw EVM variances and compliance flags into actionable intervention briefs for program directors.

---

### System Architecture

```mermaid
flowchart TD
    classDef client fill:#EFF6FF,stroke:#2563EB,stroke-width:2px,color:#1E3A8A;
    classDef deterministic fill:#ECFDF5,stroke:#059669,stroke-width:2px,color:#064E3B;
    classDef logic fill:#FAF5FF,stroke:#7C3AED,stroke-width:2px,color:#4C1D95;
    classDef output fill:#F8FAFC,stroke:#475569,stroke-width:2px,color:#0F172A;

    subgraph INGRESS ["1. PORTFOLIO & COMPLIANCE DATA INGESTION"]
        UI["Streamlit Cloud Interface<br/><b>BAC, PV, EV, AC Baselines & System Security Controls</b>"]:::client
    end

    subgraph CPU_GATE ["2. DETERMINISTIC CPU EVM & ADHICS AUDIT ENGINE"]
        direction TB
        EVM["<b>Earned Value Management Math (CPU)</b><br/>Computes CPI, SPI, Cost/Schedule Variance & EAC"]:::deterministic
        ADHICS["<b>ADHICS Compliance Gate</b><br/>Validates Sovereign Residency, Encryption & Audit Controls"]:::deterministic
        SCHEMA["<b>Pydantic v2 Portfolio Contract</b><br/>Structured Risk & Variance Scorecard"]:::deterministic
        EVM --> SCHEMA
        ADHICS --> SCHEMA
    end

    subgraph COGNITIVE ["3. COGNITIVE PMO INTERVENTION SYNTHESIS"]
        LLM["<b>Google Gemini Engine (gemini-3.8-flash)</b><br/>Diagnoses Root-Cause Delivery Friction<br/>Formulates Corrective Action & Remediation Plan"]:::logic
    end

    subgraph DELIVERABLE ["4. GOVERNANCE DELIVERABLE"]
        MEMO["<b>Executive Steering Committee Brief</b><br/>Integrated EVM & Compliance Status Dossier"]:::output
    end

    UI --> EVM
    UI --> ADHICS
    SCHEMA -->|Verified KPIs & Compliance Flags| LLM
    LLM --> MEMO
```

---

### Core EVM Formulas Enforced on CPU
$$\text{CPI} = \frac{\text{EV}}{\text{AC}}, \quad \text{SPI} = \frac{\text{EV}}{\text{PV}}, \quad \text{EAC} = \frac{\text{BAC}}{\text{CPI}}$$

---

### Technology Stack
* **Runtime & UI:** Python 3.12, Streamlit Community Cloud
* **Validation & Analytics:** Pydantic v2, Pandas
* **Cognitive Synthesis:** Google GenAI SDK (`gemini-3.8-flash`)

### Author & Architect
**Rohit Kumar, PMP, CEng, CEA, FSEr (TÜV)**  
Cross-Technology Technical Architect | Mission-Critical Infrastructure & Applied AI Solutions  
[LinkedIn](https://www.linkedin.com/in/rohitg41) | [Live Application](https://rohit-kumar-health-sentry.streamlit.app)

---

### Enterprise Advisory & Custom Architecture
Available for technical consulting, custom agentic workflow development, and private enterprise deployments.  
**Connect:** [LinkedIn](https://www.linkedin.com/in/rohitg41) | **Email:** `grohit41@gmail.com`

---

### Intellectual Property & Licensing
**Copyright © 2026 Rohit Kumar. All Rights Reserved.**  
This repository and its source code are published solely for technical portfolio evaluation and architectural demonstration. Unauthorized copying, redistribution, or commercial deployment is prohibited without prior written consent.
