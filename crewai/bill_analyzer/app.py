import streamlit as st
from BillAgents import analysis_agent, summary_agent, sentiment_agent
from BillTasks import analyze_bill_task, summarize_bill_task, impact_task
from crewai import Crew, Process
import re

st.set_page_config(page_title="AI-Powered Bill Analyzer", page_icon="📜", layout="wide")
st.title("📜 AI-Powered Bill Analyzer")

st.markdown("""
🏛️ **Analyze Legislative Bills with AI**  
Paste the text of a legislative bill and let our AI-powered tools provide:
- An in-depth analysis of its structure, intent, and implications  
- A concise summary highlighting key points  
- An evaluation of its potential economic, social, and political impact  
""")
st.markdown("""[bill1](https://www.congress.gov/119/bills/hr210/BILLS-119hr210ih.pdf)
            [bill2](https://www.congress.gov/119/bills/hr1816/BILLS-119hr1816ih.pdf)
            [bill3](https://www.congress.gov/119/bills/hr1804/BILLS-119hr1804ih.pdf)""")
bill_text = st.text_area("📄 Paste the Legislative Bill Text")
if st.button("🚀 Analyze Bill"):
    if not bill_text:
        st.error("⚠️ Please provide the text of a legislative bill.")
    else:
        st.write("⏳ AI is processing the legislative bill... Please wait.")

        # Initialize Tasks
        analysis_task = analyze_bill_task(analysis_agent, bill_text)
        summary_task = summarize_bill_task(summary_agent, bill_text)
        impact_analysis = impact_task(sentiment_agent, bill_text)

        tasks = [analysis_task, summary_task, impact_analysis]

        # Define Crew with agents and tasks
        crew = Crew(
            agents=[analysis_agent, summary_agent, sentiment_agent],
            tasks=tasks,
            process=Process.sequential,
            full_output=True,
            verbose=True,
        )
        result = str(crew.kickoff())

        # Display Results
        st.subheader("✅ Bill Analysis Results")
        if result.startswith("```"):
            result = re.sub(r"```(?:\w+\n)?(.*?)```", r"\1", result, flags=re.DOTALL).strip()
        st.markdown(result)

        # Download Option
        bill_analysis_text = result
        st.download_button(
            label="📥 Download Analysis Report",
            data=bill_analysis_text,
            file_name="Bill_Analysis_Report.txt",
            mime="text/plain"
        )
