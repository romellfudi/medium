from crewai import Task

def study_plan_task(agent, subject, study_hours, difficulty):
    return Task(
        description=f"""
        Create a detailed study plan for {subject} based on {study_hours} hours per week
        and a difficulty level of {difficulty}.
        Include learning objectives, recommended resources, and a timeline.
        """,
        expected_output="A structured markdown study plan.",
        agent=agent,
        output_file='study_plan.md',
    )

def summary_task(agent, topic_text):
    return Task(
        description=f"""
        Summarize the following text in a clear and concise manner:
        {topic_text}
        Provide key takeaways and important points.
        """,
        expected_output="A summarized markdown document with key points.",
        agent=agent,
        output_file='summary.md',
    )

def quiz_task(agent, subject, difficulty):
    return Task(
        description=f"""
        Generate a set of quiz questions for {subject} at a {difficulty} level.
        Include multiple-choice and short-answer questions.
        """,
        expected_output="A markdown file with quiz questions and answers.",
        agent=agent,
        output_file='quiz.md',
    )
