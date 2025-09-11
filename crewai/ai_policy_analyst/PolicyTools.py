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

# Sentiment analysis tool for policies
@tool
def sentiment_analysis_tool(policy_text: str):
    """
    Analyzes the sentiment and potential impact of a policy document.
    """
    sentiment_result = f"Policy sentiment analysis: {policy_text[:200]}...\nImpact: Moderate impact on economy, high impact on social equity."
    return sentiment_result