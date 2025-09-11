# python mcp_websearch_server_sse.py --port 8000
from mcp.server.fastmcp import FastMCP
from ddgs import DDGS
from rich import print
import asyncio
import argparse

# Default host and port
DEFAULT_HOST = "0.0.0.0"
DEFAULT_PORT = 8000

# Argument parser setup
parser = argparse.ArgumentParser(description="Run the Web Search Tool server.")
parser.add_argument("--host", default=DEFAULT_HOST, help="Host to run the server on.")
parser.add_argument("--port", type=int, default=DEFAULT_PORT, help="Port to run the server on.")
args = parser.parse_args()

host = args.host
port = args.port

mcp = FastMCP("Web Search Tool", host=host, port=port)
ddg = DDGS()

@mcp.tool()
async def duckduckgo_search_tool(
    query: str,
    region: str = "wt-wt",
    safesearch: str = "moderate",
    timelimit: str | None = None,
    backend: str = "auto",
    max_results: int | None = 5
) -> str:
    """Search DuckDuckGo for the given query and return the results.
    Args:
        query (str): A concise query string.
        region (str): The region to search in. Default is "wt-wt".
        safesearch (str): The safesearch level. Default is "moderate".
        timelimit (str | None): The time limit for the search. Default is None.
        backend (str): The backend to use. Default is "auto".
        max_results (int | None): The maximum number of results to return. Default is 5.
    """
    print(f"Received query: '{query}' in duckduckgo_search_tool")
    results = ddg.text(
        query,
        region=region,
        safesearch=safesearch,
        timelimit=timelimit,
        backend=backend,
        max_results=max_results
    )
    content = '\n\n'.join([result['title'] + ":" + result['body'] for result in results])
    return content


if __name__ == "__main__":
    tools = asyncio.run(mcp.list_tools())
    print("Available tools:", tools)
    print(f"Running on host {host} and port {port}")
    mcp.run(transport="sse")
    # Add MCP server after initializing the FastMCP server
    # "my-mcp-server-web-search": {
    #     "url": "http://localhost:8009/sse"
    #   }