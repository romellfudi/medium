from crewai import Task

def analyze_bill_task(agent, bill_text):
    return Task(
        description=f"""
        Analyze the following legislative bill document:
        {bill_text[:300]}...
        Provide an in-depth analysis including structure, intent, and potential implications.
        """,
        expected_output="A detailed markdown analysis of the legislative bill.",
        agent=agent,
        output_file='bill_analysis.md',
    )

def summarize_bill_task(agent, bill_text):
    return Task(
        description=f"""
        Summarize the following legislative bill document:
        {bill_text[:300]}...
        Highlight the main objectives and key points.
        """,
        expected_output="A concise markdown summary of the legislative bill.",
        agent=agent,
        output_file='bill_summary.md',
    )

def impact_task(agent, bill_text):
    return Task(
        description=f"""
        Evaluate the potential impact of the following legislative bill:
        {bill_text[:300]}...
        Include economic, social, and political implications.
        """,
        expected_output="A markdown file detailing the impact analysis of the legislative bill.",
        agent=agent,
        output_file='bill_impact.md',
    )
