from crewai import Agent
from InterviewTools import search_web_tool, evaluate_response_tool
from crewai import LLM
from dotenv import load_dotenv, find_dotenv
import os
load_dotenv(find_dotenv(), override=True)

# Initialize LLM
llm = LLM(os.getenv("MODEL", "azure/gpt-4o"))
# llm = LLM(os.getenv("MODEL", "gemini/gemini-1.5-flash"))

# Agents
question_agent = Agent(
    role="Interview Question Generator",
    goal="Creates job-specific interview questions based on industry trends.",
    backstory="An AI recruiter with deep knowledge of hiring practices.",
    tools=[search_web_tool],
    verbose=True,
    max_iter=5,
    llm=llm,
    allow_delegation=False,
)

feedback_agent = Agent(
    role="Response Evaluator",
    goal="Analyzes interview responses and provides constructive feedback.",
    backstory="An AI interview expert trained to assess answers with precision.",
    tools=[evaluate_response_tool],
    verbose=True,
    max_iter=5,
    llm=llm,
    allow_delegation=False,
)

coaching_agent = Agent(
    role="Interview Coach",
    goal="Provides personalized interview coaching tips.",
    backstory="An AI mentor with experience in corporate hiring and coaching.",
    tools=[search_web_tool],
    verbose=True,
    max_iter=5,
    llm=llm,
    allow_delegation=False,
)