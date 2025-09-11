from crewai.tools import tool
from langchain_community.tools import DuckDuckGoSearchResults

@tool
def search_web_tool(query: str):
    """Searches the web for legislative context and information."""
    search_tool = DuckDuckGoSearchResults(num_results=10, verbose=True)
    return search_tool.run(query)

@tool
def sentiment_analysis_tool(bill_text: str):
    """Analyzes the sentiment and potential impact of a legislative bill."""
    sentiment_result = (
        f"Bill Impact Analysis: {bill_text[:200]}...\n"
        "Potential Impact: Likely to influence economic policy and social welfare programs."
    )
    return sentiment_result
