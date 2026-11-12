# =====================================================================
# APPLICATION: app_digital_health_sentry.py
# PURPOSE: Autonomous Digital Health Portfolio Governance & ADHICS Sentry
# RUNTIME: Python 3.12 / Streamlit / LangChain / Pydantic / Google Gemini
# ARCHITECT: Rohit Kumar, PMP, CEng (India), CEA, FSEr (TÜV)
# =====================================================================

import os
import streamlit as st
import pandas as pd
from typing import Dict, Any, List
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# ---------------------------------------------------------------------
# 1. PAGE CONFIGURATION & EXECUTIVE STYLING
# ---------------------------------------------------------------------
st.set_page_config(
    page_title="Digital Health Portfolio & ADHICS Assurance Sentry | Rohit Kumar",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

CUSTOM_CSS = """
<style>
    .main-header {
        font-family: 'Segoe UI', Helvetica, Arial, sans-serif;
        color: #102C57;
        font-size: 2.10rem;
        font-weight: 800;
        margin-bottom: 0px;
        letter-spacing: -0.5px;
    }
    .sub-header {
        font-family: 'Segoe UI', Helvetica, Arial, sans-serif;
        color: #0F766E;
        font-size: 1.05rem;
        font-weight: 600;
        margin-bottom: 16px;
    }
    .provenance-card {
        background-color: #F8FAFC;
        border-left: 4px solid #102C57;
        padding: 12px 18px;
        border-radius: 4px;
        margin-bottom: 16px;
        font-size: 0.88rem;
        color: #334155;
        line-height: 1.5;
    }
    .metric-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 12px 14px;
        text-align: center;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }
    .metric-value {
        font-size: 1.50rem;
        font-weight: 700;
        color: #102C57;
        margin-top: 4px;
    }
    .metric-label {
        font-size: 0.75rem;
        color: #64748B;
        text-transform: uppercase;
        font-weight: 700;
        letter-spacing: 0.5px;
    }
    .memo-card {
        background-color: #F0FDFA;
        border: 1px solid #99F6E4;
        border-left: 5px solid #0F766E;
        padding: 18px;
        border-radius: 6px;
        margin-top: 10px;
    }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ---------------------------------------------------------------------
# 2. DETERMINISTIC EVM & REGULATORY AUDIT ENGINE (CPU)
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
# 3. SAMPLE PRESET GENERATOR (ABU DHABI REGIONAL HEALTH TRANSFORMATION)
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

def build_deterministic_steering_memo(res: Dict[str, Any]) -> str:
    """Deterministic Steering Committee memo fallback when API key is omitted."""
    defects_list = res["compliance_defects"] + res["delivery_warnings"]
    findings_md = "\n".join([f"- {item}" for item in defects_list]) if defects_list else "- All PMI Earned Value and DoH ADHICS V2.0 gates satisfied."
    return f"""### 1. Strategic Program Context & Executive Status
- **Program:** {res['program_name']}
- **Earned Value Gate:** {'PASSED' if res['evm_passed'] else 'ACTION REQUIRED'} (SPI: {res['spi']:.2f} | CPI: {res['cpi']:.2f})
- **ADHICS V2.0 Gate:** {'PASSED' if res['adhics_passed'] else 'HOLD PRODUCTION CUTOVER'}

### 2. EVM Delivery Assurance & Budget Outturn
- **Baseline Budget (BAC):** AED {res['bac_aed']:,.0f} | **Planned (PV):** AED {res['pv_aed']:,.0f} | **Earned (EV):** AED {res['ev_aed']:,.0f} | **Actual (AC):** AED {res['ac_aed']:,.0f}
- **Schedule & Cost Variances:** SV = AED {res['sv_aed']:,.0f} | CV = AED {res['cv_aed']:,.0f}
- **Estimate at Completion (EAC):** AED {res['eac_aed']:,.0f} (Variance at Completion: AED {res['vac_aed']:,.0f})

### 3. Regulatory & Delivery Audit Findings
{findings_md}

### 4. Steering Committee Recovery Directives
- Mandate immediate HL7 FHIR R4 gateway certification prior to Malaffi Health Information Exchange go-live.
- Enforce bi-weekly critical-path milestone recovery tracking to restore SPI >= 0.95 and contain EAC variance.
"""

# ---------------------------------------------------------------------
# 4. MAIN DASHBOARD INTERFACE
# ---------------------------------------------------------------------
def main():
    st.markdown('<p class="main-header">🏥 DIGITAL HEALTH PORTFOLIO & ADHICS ASSURANCE SENTRY</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Strategic PMO & Sovereign Health-Data Governance | Deterministic Earned Value (EVM) & UAE ADHICS V2.0 Engine</p>', unsafe_allow_html=True)

    st.markdown("""
    <div class="provenance-card">
        <b>Lead Systems Architect:</b> Rohit Kumar, PMP, CEng (India), CEA, FSEr (TÜV)<br/>
        <b>Professional Domain:</b> Mission-Critical Infrastructure & Systems Engineering Specialist | Forensic Project Controls & Contract Governance<br/>
        <b>Contact & Channels:</b> grohit41@gmail.com | LinkedIn: ROHITG41 (linkedin.com/in/rohitg41)<br/>
        <b>Central Repository:</b> <a href="https://github.com/ROHITG41/agentic-digital-health-sentry" target="_blank">github.com/ROHITG41/agentic-digital-health-sentry</a>
    </div>
    """, unsafe_allow_html=True)

    st.info(
        "**Operational Context & Quick Guide:** This portfolio governance sentry unites ANSI/PMI Earned Value Management "
        "(SPI, CPI, EAC, VAC) with Department of Health Abu Dhabi (**ADHICS V2.0**) and Malaffi HL7 FHIR R4 compliance gates. "
        "Review the pre-loaded **AED 45M Abu Dhabi Enterprise EHR Rollout** (or uncheck the preset in the left sidebar to test custom "
        "program baselines and regulatory toggles) to generate an Executive Steering Committee Memorandum."
    )

    with st.sidebar:
        st.subheader("🔑 Engine Configuration")
        api_key_from_secrets = st.secrets.get("GEMINI_API_KEY", "")
        if api_key_from_secrets:
            os.environ["GEMINI_API_KEY"] = api_key_from_secrets
            st.success("Gemini API Key active via Vault.")
        else:
            user_key = st.text_input("Gemini API Key (Optional)", type="password", help="Leave blank to run deterministic EVM & ADHICS engine.")
            if user_key:
                os.environ["GEMINI_API_KEY"] = user_key

        st.markdown("---")
        st.subheader("⚙️ Program Baselines & Gates")
        use_preset = st.checkbox("Load Sample: Abu Dhabi EHR Portfolio (AED 45M)", value=True)

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
            prog_name = st.text_input("Program Name", value="National Telehealth & Remote Care Expansion")
            bac = st.number_input("Budget at Completion - BAC (AED)", min_value=100000.0, max_value=500000000.0, value=30000000.0, step=1000000.0)
            pv = st.number_input("Planned Value - PV (AED)", min_value=100000.0, max_value=500000000.0, value=15000000.0, step=500000.0)
            ev = st.number_input("Earned Value - EV (AED)", min_value=100000.0, max_value=500000000.0, value=13500000.0, step=500000.0)
            ac = st.number_input("Actual Cost - AC (AED)", min_value=100000.0, max_value=500000000.0, value=14200000.0, step=500000.0)

            st.markdown("**ADHICS & Regulatory Gates:**")
            residency_val = st.checkbox("UAE Sovereign Data Residency", value=True)
            fhir_val = st.checkbox("Malaffi FHIR R4 Gateway Certified", value=True)
            aes_val = st.checkbox("AES-256 Cryptographic Standard", value=True)
            clinical_val = st.checkbox("Clinical Safety Officer (CSO) Sign-off", value=True)

        st.markdown("---")
        st.subheader("📋 UAE Governance Benchmarks")
        st.caption(
            "• EVM Standard: ANSI/PMI 99-001-2019\n"
            "• Schedule Velocity: SPI >= 0.95\n"
            "• Cost Efficiency: CPI >= 0.95\n"
            "• ADHICS V2.0: UAE Sovereign Data Residency\n"
            "• Exchange: HL7 FHIR R4 (Malaffi)"
        )

    # Execute Deterministic EVM & ADHICS Audit Immediately
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

    # Top 4 Executive KPI Cards
    k1, k2, k3, k4 = st.columns(4)
    with k1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Schedule Index (SPI)</div>
            <div class="metric-value" style="color:{'#16A34A' if res['spi']>=0.95 else '#DC2626'};">
                {res['spi']:.2f} <span style="font-size:0.85rem;">(Min 0.95)</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with k2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Cost Index (CPI)</div>
            <div class="metric-value" style="color:{'#16A34A' if res['cpi']>=0.95 else '#DC2626'};">
                {res['cpi']:.2f} <span style="font-size:0.85rem;">(Min 0.95)</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with k3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Projected Outturn (EAC)</div>
            <div class="metric-value" style="color:{'#16A34A' if res['vac_aed']>=0 else '#DC2626'};">
                AED {res['eac_aed']/1e6:.1f}M <span style="font-size:0.80rem;">({res['vac_aed']/1e6:+.1f}M)</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with k4:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">ADHICS V2.0 Gate</div>
            <div class="metric-value" style="font-size:1.15rem; color:{'#16A34A' if res['adhics_passed'] else '#DC2626'};">
                {'PASSED' if res['adhics_passed'] else 'COMPLIANCE HOLD'}
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br/>", unsafe_allow_html=True)

    col_left, col_right = st.columns([1, 1.35])

    with col_left:
        st.subheader("1. Portfolio Controls & Gate Register")
        summary_df = pd.DataFrame([
            {"Control Metric": "Active Program", "Status / Value": prog_name},
            {"Control Metric": "Budget at Completion (BAC)", "Status / Value": f"AED {bac:,.0f}"},
            {"Control Metric": "Planned Value (PV)", "Status / Value": f"AED {pv:,.0f}"},
            {"Control Metric": "Earned Value (EV)", "Status / Value": f"AED {ev:,.0f}"},
            {"Control Metric": "Actual Cost (AC)", "Status / Value": f"AED {ac:,.0f}"},
            {"Control Metric": "Estimate at Completion (EAC)", "Status / Value": f"AED {res['eac_aed']:,.0f}"},
            {"Control Metric": "UAE Data Residency", "Status / Value": "Compliant" if residency_val else "Breach"},
            {"Control Metric": "Malaffi FHIR R4 Gateway", "Status / Value": "Certified" if fhir_val else "Missing"},
            {"Control Metric": "AES-256 Encryption & CSO", "Status / Value": "Verified" if (aes_val and clinical_val) else "Incomplete"}
        ])
        st.dataframe(summary_df, use_container_width=True, hide_index=True)

        if res['adhics_passed'] and res['evm_passed']:
            st.success("✅ PORTFOLIO HEALTHY: Baselines conform to ADHICS V2.0 and PMI standards.")
        else:
            if not res['adhics_passed']:
                st.error("❌ ADHICS REGULATORY COMPLIANCE VIOLATION")
                for defect in res['compliance_defects']:
                    st.warning(f"⚠️ {defect}")
            if res['delivery_warnings']:
                st.error("📉 DELIVERY VELOCITY DEFICIT DETECTED")
                for warn in res['delivery_warnings']:
                    st.warning(f"⚠️ {warn}")

    with col_right:
        st.subheader("2. Executive Steering Committee Memorandum")
        st.button("🚀 Re-Generate Steering Committee Memo", type="primary")

        if os.environ.get("GEMINI_API_KEY"):
            try:
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
            except Exception:
                report_text = build_deterministic_steering_memo(res)
        else:
            report_text = build_deterministic_steering_memo(res)

        st.markdown(f'<div class="memo-card">{report_text}</div>', unsafe_allow_html=True)
        st.markdown("<br/>", unsafe_allow_html=True)
        st.download_button(
            label="📥 Download Steering Committee Memorandum (.md)",
            data=report_text,
            file_name="Digital_Health_Steering_Committee_Memo.md",
            mime="text/markdown",
            use_container_width=True
        )

if __name__ == "__main__":
    main()

# --- EXECUTIVE PORTFOLIO FOOTER ---
st.divider()
st.markdown(
    """
    <div style="text-align: center; color: #475569; font-size: 0.85rem; padding: 10px 0;">
        <p style="margin-bottom: 4px;">
            <strong>Architect:</strong> Rohit Kumar, PMP, CEng (India), CEA, FSEr (TÜV) | 
            Mission-Critical Infrastructure &amp; Systems Engineering Specialist | Forensic Project Controls &amp; Contract Governance
        </p>
        <p style="margin-bottom: 4px;">
            <strong>Enterprise Advisory &amp; Custom Architecture:</strong> 
            Available for technical consulting &amp; custom agentic workflows &bull; 
            <a href="https://www.linkedin.com/in/rohitg41" target="_blank" style="color: #2563EB; text-decoration: none;">LinkedIn</a> | 
            <a href="mailto:grohit41@gmail.com" style="color: #2563EB; text-decoration: none;">grohit41@gmail.com</a>
        </p>
        <p style="font-size: 0.78rem; color: #64748B; margin-top: 6px;">
            <em>Dataset Note: Independent engineering demonstration validated on representative, anonymized datasets.</em><br>
            Copyright &copy; 2026 Rohit Kumar. All Rights Reserved.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)
