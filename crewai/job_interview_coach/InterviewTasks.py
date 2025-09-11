from crewai import Task

def generate_questions_task(agent, job_title, industry):
    return Task(
        description=f"""
        Generate a list of common and advanced interview questions for a {job_title}
        role in the {industry} industry.
        """,
        expected_output="A markdown file with job-specific interview questions.",
        agent=agent,
        output_file='interview_questions.md',
    )

def evaluate_response_task(agent, response_text):
    return Task(
        description=f"""
        Evaluate the following interview response:
        {response_text}
        Provide strengths, weaknesses, and suggestions for improvement.
        """,
        expected_output="A markdown file with interview feedback.",
        agent=agent,
        output_file='response_feedback.md',
    )

def coaching_tips_task(agent, job_title, industry):
    return Task(
        description=f"""
        Provide personalized coaching tips for acing a {job_title} interview
        in the {industry} industry. Include best practices, common mistakes, and
        techniques for success.
        """,
        expected_output="A markdown document with structured interview coaching tips.",
        agent=agent,
        output_file='coaching_tips.md',
    )
