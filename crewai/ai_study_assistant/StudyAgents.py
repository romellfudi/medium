from crewai import Agent
from StudyTools import search_web_tool
from crewai import LLM
from dotenv import load_dotenv, find_dotenv
import os
# Load environment variables
load_dotenv(find_dotenv(), override=True)

# Initialize LLM
llm = LLM(os.getenv("MODEL", "azure/gpt-4o"))
# llm = LLM(os.getenv("MODEL", "gemini/gemini-1.5-flash"))

# Agents
tutor_agent = Agent(
    role="AI Study Tutor",
    goal="Provides detailed explanations and summaries of study topics.",
    backstory="An AI tutor with deep knowledge in multiple subjects, dedicated to helping students learn.",
    tools=[search_web_tool],
    verbose=True,
    max_iter=5,
    llm=llm,
    allow_delegation=False,
)

quiz_agent = Agent(
    role="Quiz Master",
    goal="Creates quizzes and flashcards to reinforce learning.",
    backstory="An AI assistant that generates challenging and fun quizzes for effective study.",
    tools=[search_web_tool],
    verbose=True,
    max_iter=5,
    llm=llm,
    allow_delegation=False,
)

planner_agent = Agent(
    role="Study Planner",
    goal="Generates structured study plans based on subject, difficulty, and available time.",
    backstory="An AI expert in educational planning who helps students stay on track.",
    tools=[search_web_tool],
    verbose=True,
    max_iter=5,
    llm=llm,
    allow_delegation=False,
)
