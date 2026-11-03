# =====================================================================
# APPLICATION: app_digital_health_sentry.py
# PURPOSE: Autonomous Digital Health Portfolio Governance & ADHICS Sentry
# RUNTIME: Python 3.12 / Streamlit / LangChain / Pydantic / Google Gemini
# ARCHITECT: Rohit Kumar, PMP, CEng | Applied AI Practice Lead
# =====================================================================

import os
import streamlit as st
import pandas as pd
from typing import Dict, Any, List
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# ---------------------------------------------------------------------
# UI CONFIGURATION & EXECUTIVE BRANDING
# ---------------------------------------------------------------------
st.set_page_config(
    page_title="Digital Health Portfolio & ADHICS Assurance Sentry",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 Autonomous Digital Health Portfolio & ADHICS Assurance Sentry")
st.caption("Engineered by Rohit Kumar, PMP, CEng | Digital Health Transformation & Strategic PMO Governance")
st.markdown("---")

# ---------------------------------------------------------------------
# SIDEBAR CONTROLS & SECRETS GOVERNANCE
# ---------------------------------------------------------------------
with st.sidebar:
    st.header("⚙️ Governance Configuration")
    
    api_key_from_secrets = st.secrets.get("GEMINI_API_KEY", "")
    if api_key_from_secrets:
        os.environ["GEMINI_API_KEY"] = api_key_from_secrets
        st.success("API Key loaded securely from Secrets.")
    else:
        user_key = st.text_input("Enter Google Gemini API Key:", type="password")
        if user_key:
            os.environ["GEMINI_API_KEY"] = user_key
            
    st.markdown("### 📋 UAE Healthcare Governance Benchmarks")
    st.info(
        "**Regulatory & Delivery Controls:**\n"
        "- **EVM Baselines:** ANSI/PMI 99-001-2019 Practice Standards\n"
        "- **Schedule Velocity:** SPI >= 0.95 (Critical Path Alignment)\n"
        "- **Cost Efficiency:** CPI >= 0.95 (Budget Burn Ceiling)\n"
        "- **ADHICS V2.0:** Department of Health Abu Dhabi Data Residency\n"
        "- **Interoperability:** HL7 FHIR R4 Malaffi Health Information Exchange"
    )

# ---------------------------------------------------------------------
# STAGE 1: DETERMINISTIC EVM & REGULATORY AUDIT ENGINE (CPU)
# ---------------------------------------------------------------------
def audit_digital_health_portfolio(
    program_name: str,
    bac_aed: float,
    pv_aed: float,
    ev_aed: float,
    ac_aed: float,
    uae_data_residency: bool,
    fhir_r4_compliant: bool,
    aes256_encrypted: bool,
    clinical_safety_signoff: bool
) -> Dict[str, Any]:
    """
    Executes deterministic EVM math and ADHICS compliance logic checks.
    Zero-hallucination CPU layer for digital health portfolio assurance.
    """
    # 1. Earned Value Management Metrics
    cv_aed = ev_aed - ac_aed
    sv_aed = ev_aed - pv_aed
    cpi = ev_aed / ac_aed if ac_aed > 0 else 1.0
    spi = ev_aed / pv_aed if pv_aed > 0 else 1.0
    
    # 2. Forecasting
    eac_aed = bac_aed / cpi if cpi > 0 else bac_aed
    vac_aed = bac_aed - eac_aed

    # 3. Regulatory & Statutory Compliance Audit
    compliance_defects = []
    if not uae_data_residency:
        compliance_defects.append(
            "ADHICS NON-COMPLIANCE: Patient Health Information (PHI) hosted outside sovereign UAE data borders (Breach of UAE Federal Law No. 2 of 2019)."
        )
    if not fhir_r4_compliant:
        compliance_defects.append(
            "INTEROPERABILITY BREACH: Missing HL7 FHIR Release 4 standard gateway for integration into Malaffi Health Information Exchange."
        )
    if not aes256_encrypted:
        compliance_defects.append(
            "CYBERSECURITY DEFECT: Patient Data at Rest/In-Transit fails mandatory AES-256 cryptographic standard."
        )
    if not clinical_safety_signoff:
        compliance_defects.append(
            "CLINICAL GOVERNANCE RISK: Production rollout lacking formal Clinical Safety Officer (CSO) sign-off."
        )

    # 4. EVM Performance Warnings
    delivery_warnings = []
    if spi < 0.90:
        delivery_warnings.append(f"CRITICAL SCHEDULE SLIPPAGE: SPI is {spi:.3f} (< 0.90 target). Critical path clinical milestones delayed.")
    elif spi < 0.95:
        delivery_warnings.append(f"MODERATE SCHEDULE LAG: SPI is {spi:.3f} (< 0.95 target).")
        
    if cpi < 0.90:
        delivery_warnings.append(f"UNFAVORABLE BUDGET BURN: CPI is {cpi:.3f} (< 0.90 target). Projected outturn exceeds allocation.")

    evm_passed = (spi >= 0.95) and (cpi >= 0.95)
    adhics_passed = len(compliance_defects) == 0

    return {
        "program_name": program_name,
        "bac_aed": bac_aed,
        "pv_aed": pv_aed,
        "ev_aed": ev_aed,
        "ac_aed": ac_aed,
        "cv_aed": cv_aed,
        "sv_aed": sv_aed,
        "cpi": cpi,
        "spi": spi,
        "eac_aed": eac_aed,
        "vac_aed": vac_aed,
        "adhics_passed": adhics_passed,
        "evm_passed": evm_passed,
        "compliance_defects": compliance_defects,
        "delivery_warnings": delivery_warnings
    }

# ---------------------------------------------------------------------
# SAMPLE PRESET GENERATOR (ABU DHABI REGIONAL HEALTH TRANSFORMATION)
# ---------------------------------------------------------------------
def load_sample_portfolio():
    return {
        "name": "Abu Dhabi Regional Enterprise EHR & AI Diagnostics Rollout",
        "bac": 45000000.0,  # AED 45.0 Million
        "pv": 22500000.0,   # AED 22.5 Million
        "ev": 18900000.0,   # AED 18.9 Million (Schedule Lag, SPI = 0.84)
        "ac": 21000000.0,   # AED 21.0 Million (Cost Inefficiency, CPI = 0.90)
        "residency": True,  # Hosted in In-Country UAE Cloud
        "fhir": False,      # Non-compliant with Malaffi FHIR R4 (Defect)
        "aes": True,        # AES-256 Encrypted
        "clinical_signoff": True
    }

# ---------------------------------------------------------------------
# MAIN DASHBOARD INTERFACE
# ---------------------------------------------------------------------
col_left, col_right = st.columns([1, 1])

with col_left:
    st.subheader("1. Ingest Program Baselines & Regulatory Status")
    use_preset = st.checkbox("Load Sample: Abu Dhabi Enterprise Health Tech Portfolio (AED 45M)", value=True)
    
    if use_preset:
        preset = load_sample_portfolio()
        prog_name = preset["name"]
        bac = preset["bac"]
        pv = preset["pv"]
        ev = preset["ev"]
        ac = preset["ac"]
        residency_val = preset["residency"]
        fhir_val = preset["fhir"]
        aes_val = preset["aes"]
        clinical_val = preset["clinical_signoff"]
    else:
        prog_name = st.text_input("Program Name:", value="National Telehealth & Remote Care Expansion")
        c1, c2 = st.columns(2)
        with c1:
            bac = st.number_input("Budget at Completion (AED):", min_value=100000.0, max_value=500000000.0, value=30000000.0, step=1000000.0)
            pv = st.number_input("Planned Value - PV (AED):", min_value=100000.0, max_value=500000000.0, value=15000000.0, step=500000.0)
        with c2:
            ev = st.number_input("Earned Value - EV (AED):", min_value=100000.0, max_value=500000000.0, value=13500000.0, step=500000.0)
            ac = st.number_input("Actual Cost - AC (AED):", min_value=100000.0, max_value=500000000.0, value=14200000.0, step=500000.0)
            
        st.markdown("### 🔒 ADHICS & Regulatory Verification Gates")
        residency_val = st.checkbox("UAE Sovereign Data Residency (Zero Cross-Border PHI)", value=True)
        fhir_val = st.checkbox("Malaffi FHIR R4 Interoperability Gateway Certified", value=True)
        aes_val = st.checkbox("AES-256 In-Transit & At-Rest Cryptographic Standard", value=True)
        clinical_val = st.checkbox("Clinical Safety Officer (CSO) Sign-off Completed", value=True)

    # Financial & Delivery Register Preview
    st.write("### Portfolio Controls Summary")
    summary_df = pd.DataFrame([{
        "Program": prog_name,
        "Total Budget (BAC)": f"AED {bac:,.0f}",
        "Planned (PV)": f"AED {pv:,.0f}",
        "Earned (EV)": f"AED {ev:,.0f}",
        "Actual (AC)": f"AED {ac:,.0f}",
        "Data Residency": "Compliant" if residency_val else "Breach",
        "FHIR Gateway": "Compliant" if fhir_val else "Missing"
    }])
    st.dataframe(summary_df, use_container_width=True, hide_index=True)

with col_right:
    st.subheader("2. Deterministic EVM & Regulatory Audit")
    if st.button("🚀 Execute Strategic Portfolio Audit", type="primary"):
        res = audit_digital_health_portfolio(
            program_name=prog_name,
            bac_aed=bac,
            pv_aed=pv,
            ev_aed=ev,
            ac_aed=ac,
            uae_data_residency=residency_val,
            fhir_r4_compliant=fhir_val,
            aes256_encrypted=aes_val,
            clinical_safety_signoff=clinical_val
        )
        
        # Display Metric Gauges
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Schedule SPI", f"{res['spi']:.2f}", "Target >= 0.95", delta_color="normal" if res['spi'] >= 0.95 else "inverse")
        m2.metric("Cost CPI", f"{res['cpi']:.2f}", "Target >= 0.95", delta_color="normal" if res['cpi'] >= 0.95 else "inverse")
        m3.metric("Projected Outturn", f"AED {res['eac_aed']/1e6:.1f} M", f"{res['vac_aed']/1e6:.1f} M Var", delta_color="normal" if res['vac_aed'] >= 0 else "inverse")
        m4.metric("ADHICS Gate", "PASSED" if res['adhics_passed'] else "FAILED", delta_color="normal" if res['adhics_passed'] else "inverse")

        # Status Alert Banners
        if res['adhics_passed'] and res['evm_passed']:
            st.success("✅ PORTFOLIO HEALTH HEALTHY: Baselines conform to ADHICS and PMI standards.")
        else:
            if not res['adhics_passed']:
                st.error("❌ ADHICS REGULATORY COMPLIANCE VIOLATION")
                for defect in res['compliance_defects']:
                    st.warning(f"⚠️ {defect}")
            if res['delivery_warnings']:
                st.error("📉 DELIVERY VELOCITY DEFICIT DETECTED")
                for warn in res['delivery_warnings']:
                    st.warning(f"⚠️ {warn}")

        st.markdown("---")
        st.subheader("3. Executive Steering Committee Memorandum (Gemini 3.8 Flash)")
        
        if not os.environ.get("GEMINI_API_KEY"):
            st.info("💡 Enter your GEMINI_API_KEY in Streamlit Secrets or sidebar to generate the Steering Committee Memo.")
        else:
            with st.spinner("Agentic Loop Synthesizing Steering Committee Transformation Memo..."):
                llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash", temperature=0.0)
                
                memo_prompt = ChatPromptTemplate.from_messages([
                    ("system", 
                     "You are the Director of Strategy & Delivery for Digital Health in Abu Dhabi, reporting to the Executive Steering Committee. "
                     "Analyze the provided deterministic EVM calculations, delivery variances, and ADHICS compliance audit results. "
                     "Draft a formal, high-impact Executive Steering Committee Memorandum. "
                     "Structure the memorandum with: "
                     "1. Strategic Program Context & Executive Status Summary "
                     "2. EVM Delivery Assurance & Budget Variance Analysis (SPI, CPI, EAC Outturn) "
                     "3. ADHICS V2.0 Regulatory Audit & Malaffi Interoperability Gaps "
                     "4. Cross-Workstream Interdependency Assessment (Infrastructure vs. Clinical Adoption) "
                     "5. Concrete Strategic Recovery & Remediation Directives."),
                    ("human", 
                     "PROGRAM AUDIT DATA:\n{metrics}\n\n"
                     "Output an authoritative, executive-ready memorandum for health leadership.")
                ])
                
                chain = memo_prompt | llm
                response = chain.invoke({"metrics": str(res)})
                
                if isinstance(response.content, list):
                    report_text = "\n".join([str(p.get("text", p)) if isinstance(p, dict) else str(p) for p in response.content])
                else:
                    report_text = str(response.content)

                st.markdown(report_text)
                st.download_button(
                    label="📥 Download Steering Committee Memorandum",
                    data=report_text,
                    file_name="Digital_Health_Steering_Committee_Memo.md",
                    mime="text/markdown"
                )
