import streamlit as st
from InterviewAgents import question_agent, feedback_agent, coaching_agent
from InterviewTasks import generate_questions_task, evaluate_response_task, coaching_tips_task
from crewai import Crew, Process
import re
# Streamlit App Title
st.title("🎤 AI Job Interview Coach")

st.markdown("""
💼 **Prepare for Your Next Job Interview with AI!**  
Enter the job details below, and our AI coach will generate interview questions, evaluate your answers, and provide personalized feedback. 
""")

# User Inputs
job_title = st.text_input("🏢 Job Title", "Software Engineer")
industry = st.text_input("🌎 Industry", "Technology")
response_text = st.text_area("🗣️ Paste Your Response to an Interview Question")

# Button to run CrewAI
if st.button("🚀 Start Interview Coaching"):
    if not job_title or not industry:
        st.error("⚠️ Please fill in all fields before proceeding.")
    else:
        st.write("⏳ AI is generating your interview preparation resources... Please wait.")

        # Initialize Tasks
        questions_task = generate_questions_task(question_agent, job_title, industry)
        feedback_task = evaluate_response_task(feedback_agent, response_text)
        coaching_task = coaching_tips_task(coaching_agent, job_title, industry)

        # Define Crew
        crew = Crew(
            agents=[question_agent, feedback_agent, coaching_agent],
            tasks=[questions_task, feedback_task, coaching_task],
            process=Process.sequential,
            full_output=True,
            verbose=True,
        )

        # Run Crew AI
        result = crew.kickoff()

        # Display Results
        st.subheader("✅ Your AI-Powered Interview Coaching")
        content = re.sub(r"```(?:\w+\n)?(.*?)```", r"\1", result, flags=re.DOTALL).strip().replace("$", r"\$")  

        st.markdown(content)

        # Download Option
        interview_coaching_text = str(result)
        st.download_button(
            label="📥 Download Interview Report",
            data=interview_coaching_text,
            file_name=f"Interview_Coaching_{job_title}.txt",
            mime="text/plain"
        )
