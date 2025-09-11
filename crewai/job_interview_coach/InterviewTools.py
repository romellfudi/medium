# from crewai_tools import WebsiteSearchTool
from crewai.tools import tool
from langchain_community.tools import DuckDuckGoSearchResults

# Web search tool using DuckDuckGo
@tool
def search_web_tool(query: str):
    """
    Searches the web and returns results.
    """
    search_tool = DuckDuckGoSearchResults(num_results=10, verbose=True)
    return search_tool.run(query)

# AI-powered response evaluation tool
@tool
def evaluate_response_tool(response: str):
    """
    Evaluates an interview response and provides feedback.
    """
    evaluation = f"Assessment of response: {response}\nStrengths: Clear articulation, relevant examples.\nAreas to Improve: Add more details on impact."
    return evaluation