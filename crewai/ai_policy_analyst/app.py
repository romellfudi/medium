import streamlit as st
from PolicyAgents import analysis_agent, comparison_agent, summary_agent
from PolicyTasks import analyze_policy_task, compare_policies_task, summarize_policy_task
from crewai import Crew, Process

# wide page
st.set_page_config(layout="wide")

# Streamlit App Title
st.title("📜 AI-Powered Policy Analyst")

st.markdown("""
🏛️ **Analyze, Compare & Summarize Government Policy Statements (GPS) with AI**  
Upload or paste policy documents, and our AI will provide insights, comparisons, and summaries.
""")

# User Inputs
policy_text = st.text_area("📄 Paste a Policy Document", value="""
National Renewable Energy Policy (2025-2035)
📜 Government of Greenlandia

Introduction
The National Renewable Energy Policy (NREP) aims to transition Greenlandia towards a sustainable energy future by reducing fossil fuel dependency and increasing the adoption of renewable energy sources. This policy sets the framework for investments, regulations, and incentives supporting clean energy development over the next decade.

Objectives
Increase Renewable Energy Adoption: Ensure that by 2035, at least 70% of the national energy supply comes from renewable sources.
Encourage Private Investments: Offer tax incentives and subsidies to companies investing in solar, wind, and hydropower projects.
Improve Energy Infrastructure: Modernize and expand the national grid to accommodate decentralized renewable energy generation.
Reduce Carbon Emissions: Achieve a 50% reduction in greenhouse gas emissions compared to 2020 levels.
Support Research & Innovation: Fund universities and research institutions to develop efficient energy storage and distribution technologies.
Implementation Plan
Phase 1 (2025-2028): Launch pilot projects for solar and wind farms in key regions.
Phase 2 (2029-2032): Implement nationwide subsidies for renewable energy adoption in households and businesses.
Phase 3 (2033-2035): Establish energy storage systems and ensure grid stability for 100% renewable transition.
Expected Impact
✅ Creation of 500,000 green jobs.
✅ Reduction in energy costs for consumers by 20%.
✅ Improvement in air quality and environmental sustainability.

""".strip())
policy_text_2 = st.text_area("📄 (Optional) Paste a Second Policy for Comparison", value="""
Economic Stimulus and Job Recovery Act (2025-2028)
📜 Government of Greenlandia

Introduction
The Economic Stimulus and Job Recovery Act (ESJRA) is designed to accelerate economic recovery following the global recession. This policy provides direct financial support, business grants, and workforce training programs to revitalize key industries.

Objectives
Boost Employment: Create 2 million new jobs through infrastructure, technology, and green energy projects.
Support Small Businesses: Offer zero-interest loans and tax relief to small and medium enterprises (SMEs) affected by economic downturns.
Enhance Workforce Training: Provide upskilling programs in high-demand industries such as technology, healthcare, and renewable energy.
Increase Consumer Spending: Distribute direct financial aid to low-income households to stimulate market demand.
Encourage Foreign Investment: Introduce policy incentives to attract multinational corporations and boost economic activity.
Implementation Plan
Phase 1 (2025-2026): Immediate financial relief for businesses and citizens, including tax breaks and stimulus checks.
Phase 2 (2026-2027): Expansion of infrastructure projects to create jobs in transportation, energy, and construction sectors.
Phase 3 (2027-2028): Establish long-term economic growth strategies through digital transformation and trade partnerships.
Expected Impact
✅ Reduction in unemployment rate from 8% to 4%.
✅ Increase in GDP growth rate by 3.5% annually.
✅ Strengthened economic resilience against future downturns.

""".strip())

# Button to run AI analysis
if st.button("🚀 Analyze Policy"):
    if not policy_text:
        st.error("⚠️ Please provide at least one policy document.")
    else:
        st.write("⏳ AI is processing the policy document... Please wait.")

        # Initialize Tasks
        analysis_task = analyze_policy_task(analysis_agent, policy_text)
        summary_task = summarize_policy_task(summary_agent, policy_text)
        tasks = [analysis_task, summary_task]
        
        if policy_text_2:
            compare_task = compare_policies_task(comparison_agent, policy_text, policy_text_2)
            tasks.append(compare_task)

        # Define Crew
        crew = Crew(
            agents=[analysis_agent, comparison_agent, summary_agent],
            tasks=tasks,
            process=Process.sequential,
            full_output=True,
            verbose=True,
        )

        # Run Crew AI
        result = crew.kickoff()

        # Display Results
        st.subheader("✅ AI Policy Analysis Results")
        st.markdown(result)

        # Download Option
        policy_analysis_text = str(result)
        st.download_button(
            label="📥 Download Analysis Report",
            data=policy_analysis_text,
            file_name="Policy_Analysis_Report.txt",
            mime="text/plain"
        )