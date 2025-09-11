import streamlit as st
from StudyAgents import tutor_agent, quiz_agent, planner_agent
from StudyTasks import study_plan_task, summary_task, quiz_task
from crewai import Crew, Process

# Streamlit App Title
st.title("📚 AI-Powered Study Assistant")

st.markdown("""
🤖 **Enhance Your Learning with AI!**  
Enter your subject details below, and our AI assistant will generate a study plan, summarize content, and create quizzes to help you learn effectively! 
""")

# User Inputs
subject = st.text_input("📖 Subject", "Machine Learning")
study_hours = st.slider("⏳ Available Study Hours per Week", 1, 40, 10)
difficulty = st.selectbox("⚡ Difficulty Level", ["Beginner", "Intermediate", "Advanced"])
topic_text = st.text_area("📄 Paste Text to Summarize")

# Button to run CrewAI
if st.button("🚀 Generate Study Plan & Quiz"):
    if not subject or not study_hours or not difficulty:
        st.error("⚠️ Please fill in all fields before proceeding.")
    else:
        st.write("⏳ AI is preparing your study resources... Please wait.")

        # Initialize Tasks
        plan_task = study_plan_task(planner_agent, subject, study_hours, difficulty)
        summary = summary_task(tutor_agent, topic_text)
        quiz = quiz_task(quiz_agent, subject, difficulty)

        # Define Crew
        crew = Crew(
            agents=[tutor_agent, quiz_agent, planner_agent],
            tasks=[plan_task, summary, quiz],
            process=Process.sequential,
            full_output=True,
            verbose=True,
        )

        # Run Crew AI
        result = crew.kickoff()

        # Display Results
        st.subheader("✅ Your AI-Powered Study Resources")
        st.markdown(result)

        # Download Option
        study_resources_text = str(result)
        st.download_button(
            label="📥 Download Study Resources",
            data=study_resources_text,
            file_name=f"Study_Resources_{subject}.txt",
            mime="text/plain"
        )
