from crewai import Agent
from BillTools import search_web_tool, sentiment_analysis_tool
from crewai import LLM
from dotenv import load_dotenv, find_dotenv
import os
# Load environment variables
load_dotenv(find_dotenv(), override=True)

# Initialize LLM
llm = LLM(os.getenv("MODEL", "azure/gpt-4o"))
# llm = LLM(os.getenv("MODEL", "gemini/gemini-1.5-flash"))

# Bill Analysis Agent: Provides detailed analysis of the legislative bill.
analysis_agent = Agent(
    role="Bill Analysis Expert",
    goal="Provides a detailed analysis of legislative bills, including structure, intent, and potential implications.",
    backstory="An expert in legislative processes and government policy.",
    tools=[search_web_tool],
    verbose=True,
    max_iter=5,
    llm=llm,
    allow_delegation=False,
)

# Bill Summarizer: Generates concise summaries highlighting the bill's key points.
summary_agent = Agent(
    role="Bill Summarizer",
    goal="Generates concise summaries of legislative bills, highlighting main objectives and key points.",
    backstory="A specialist in distilling complex legislative documents into clear summaries.",
    tools=[],
    verbose=True,
    max_iter=5,
    llm=llm,
    allow_delegation=False,
)

# Bill Impact Evaluator: Assesses the potential impact and sentiment of the legislative bill.
sentiment_agent = Agent(
    role="Bill Impact Evaluator",
    goal="Evaluates the potential impact and sentiment of a legislative bill, including economic, social, and political effects.",
    backstory="An expert in public policy and legislative impact analysis.",
    tools=[sentiment_analysis_tool],
    verbose=True,
    max_iter=5,
    llm=llm,
    allow_delegation=False,
)
