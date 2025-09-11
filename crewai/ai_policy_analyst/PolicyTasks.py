from crewai import Task

def analyze_policy_task(agent, policy_text):
    return Task(
        description=f"""
        Analyze the following government policy document:
        {policy_text[:300]}...
        Provide insights, implications, and a breakdown of key components.
        """,
        expected_output="A structured markdown policy analysis.",
        agent=agent,
        output_file='policy_analysis.md',
    )

def compare_policies_task(agent, policy_text_1, policy_text_2):
    return Task(
        description=f"""
        Compare the following two government policies:
        Policy 1: {policy_text_1[:200]}...
        Policy 2: {policy_text_2[:200]}...
        Highlight differences, similarities, and potential conflicts.
        """,
        expected_output="A comparative markdown policy analysis.",
        agent=agent,
        output_file='policy_comparison.md',
    )

def summarize_policy_task(agent, policy_text):
    return Task(
        description=f"""
        Generate a concise summary of the following policy document:
        {policy_text[:300]}...
        Provide key points, main objectives, and a short overview.
        """,
        expected_output="A markdown document with a structured policy summary.",
        agent=agent,
        output_file='policy_summary.md',
    )
