import os

def create_obsidian_vault(company_name, financials_data, qualitative_insights, risk_matrix, scenario_analysis):
    """
    Creates a folder structured for Obsidian containing interconnected Markdown files.
    This demonstrates the 'Second Brain' concept for the Generative AI for Business course.
    """
    # 1. Klasör yapısını oluşturuyoruz
    vault_folder = f"Obsidian_Vault_{company_name}"
    os.makedirs(vault_folder, exist_ok=True)
    
    # -------------------------------------------------------------
    # FILE 1: Company Overview & Main Hub (Giriş ve Ana Merkez)
    # -------------------------------------------------------------
    hub_content = f"""# 🏢 {company_name} - 360 Degree Company Dashboard
    
## 🎯 Investment Thesis & Overview
Welcome to the automated investment research vault for **{company_name}**. This 'Second Brain' synthesizes multi-year annual reports to guide investment decisions.

### 🔍 Explore Central Analysis Areas:
*   📊 **Financial Performance & KPIs:** [[Financial_Analysis]]
*   🛡️ **Strategic Frameworks & Competitive Landscape:** [[Strategic_Analysis]]
*   ⚠️ **Risk Management & Early Signals:** [[Risk_and_Signals]]
*   🔮 **Future Outlook & Portfolio Categorization:** [[Investment_Thesis]]

---
*Generated automatically via Python & Gemini 3.1 Pro for the Generative AI for Business Course.*
"""
    
    # -------------------------------------------------------------
    # FILE 2: Financial Analysis (Sayısal Analiz)
    # -------------------------------------------------------------
    financial_content = f"""# 📊 Financial Analysis & KPIs - {company_name}
    
## 📈 Financial Health (Calculated via Deterministic Python Math)
To ensure 100% precision and avoid AI hallucinations, the following core metrics were calculated directly from the official balance sheets using Python.

### 🔢 Core Metrics:
{financials_data}

### 💡 Contextual Insights:
*   **Why it matters:** These metrics directly influence our rating in the [[Investment_Thesis]].
*   **Risk Linkage:** If the liquidity metrics drop below thresholds, it triggers the alert systems defined in [[Risk_and_Signals]].

Back to Dashboard: [[{company_name}_Overview]]
"""

    # -------------------------------------------------------------
    # FILE 3: Strategic Analysis (Porter's 5 Forces)
    # -------------------------------------------------------------
    strategic_content = f"""# 🛡️ Strategic Analysis & Market Outlook - {company_name}

## 🥊 Porter's Five Forces Analysis (AI-Generated Context)
{qualitative_insights}

## ⛓️ Supply Chain & Stakeholder Risks
*   **Customer Concentration:** High dependency on key tech accounts.
*   **Supplier Power:** Mitigated by multi-sourcing strategy detailed in the annual reports.

See how these strategic dynamics impact our overall risk rating: [[Risk_and_Signals]]
"""

    # -------------------------------------------------------------
    # FILE 4: Risk and Early Warning Signals (Risk Analizi)
    # -------------------------------------------------------------
    risk_content = f"""# ⚠️ Risk Analysis & Early Warning Indicators - {company_name}

## 🔍 Key Structural Risks
{risk_matrix}

## 🚨 Early Signals & Predictors (Frühindikatoren)
For every major risk identified above, junior analysts must track these operational signals:
1.  **Signal A (Financial):** If Gross Margin decreases by >2% quarter-over-quarter ➔ Check [[Financial_Analysis]].
2.  **Signal B (Market):** Competitor product launch in the core small-cap segment ➔ Check [[Strategic_Analysis]].

See our final portfolio evaluation: [[Investment_Thesis]]
"""

    # -------------------------------------------------------------
    # FILE 5: Final Investment Thesis & Scenarios (Yatırım Tezi)
    # -------------------------------------------------------------
    thesis_content = f"""# 🔮 Investment Thesis & Scenario Analysis - {company_name}

## 🎭 Future Scenarios
{scenario_analysis}

## 🗳️ Portfolio Categorization (The Final Verdict)
Based on the alignment of [[Financial_Analysis]] and [[Strategic_Analysis]], this company is categorized under:

### 🟩 [ ] GOOD LIST (Attractive & Worth Deep-Dive)
### 🟨 [ ] OKAY LIST (Interesting, but has open questions)
### 🟥 [ ] BAD LIST (Structural problems / unfavorable risk-reward)

Back to Main Hub: [[{company_name}_Overview]]
"""

    # Dosyaları diske yazıyoruz
    files = {
        f"{company_name}_Overview.md": hub_content,
        "Financial_Analysis.md": financial_content,
        "Strategic_Analysis.md": strategic_content,
        "Risk_and_Signals.md": risk_content,
        "Investment_Thesis.md": thesis_content,
    }
    
    for filename, content in files.items():
        with open(os.path.join(vault_folder, filename), "w", encoding="utf-8") as f:
            f.write(content)
            
    print(f"🎉 Success! Obsidian Vault created at: ./{vault_folder}")

# --- KODU TEST ETMEK İÇİN GEÇİCİ VERİLER ---
if __name__ == "__main__":
    # Yapay zekadan gelecek olan sahte verileri simüle ediyoruz
    create_obsidian_vault(
        company_name="TechCorp_SmallCap",
        financials_data="- Revenue Growth: 14.5%\n- Current Ratio: 1.82 (Healthy)\n- Net Margin: 12.3%",
        qualitative_insights="### Threat of New Entrants: Low\n### Bargaining Power of Buyers: High",
        risk_matrix="- Supply Chain Bottlenecks\n- Regulatory shifts in EU",
        scenario_analysis="### Bull Case: Revenue doubles via EU expansion\n### Bear Case: Raw material costs spike by 20%"
    )
