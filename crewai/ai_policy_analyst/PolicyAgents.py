from crewai import Agent
from PolicyTools import search_web_tool, sentiment_analysis_tool
from crewai import LLM
from dotenv import load_dotenv, find_dotenv
import os
# Load environment variables
load_dotenv(find_dotenv(), override=True)

# Initialize LLM
llm = LLM(os.getenv("MODEL", "azure/gpt-4o"))
# llm = LLM(os.getenv("MODEL", "gemini/gemini-1.5-flash"))

# Agents
analysis_agent = Agent(
    role="Policy Analyst",
    goal="Breaks down and analyzes policy statements for impact and key points.",
    backstory="An AI expert trained in governance and legislative analysis.",
    tools=[sentiment_analysis_tool],
    verbose=True,
    max_iter=5,
    llm=llm,
    allow_delegation=False,
)

comparison_agent = Agent(
    role="Policy Comparison Expert",
    goal="Identifies key differences, similarities, and inconsistencies between policies.",
    backstory="An AI trained in comparative policy analysis.",
    tools=[search_web_tool],
    verbose=True,
    max_iter=5,
    llm=llm,
    allow_delegation=False,
)

summary_agent = Agent(
    role="Policy Summarizer",
    goal="Generates clear, concise summaries of policy statements.",
    backstory="An AI designed to extract key points from policy documents.",
    tools=[],
    verbose=True,
    max_iter=5,
    llm=llm,
    allow_delegation=False,
)
