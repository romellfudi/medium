# python mcp_exchange_server_sse.py
from mcp.server.fastmcp import FastMCP
from rich import print
import requests 
import asyncio
import argparse

# Default host and port
DEFAULT_HOST = "0.0.0.0"
DEFAULT_PORT = 8000

# Set up argument parser
parser = argparse.ArgumentParser(description="Run the MCP Exchange Server")
parser.add_argument("--host", default=DEFAULT_HOST, help="Host address to run the server")
parser.add_argument("--port", type=int, default=DEFAULT_PORT, help="Port number to run the server")

# Parse arguments
args = parser.parse_args()

mcp = FastMCP("Exchange Tool", host=args.host, port=args.port)

@mcp.tool()
def make_a_math_calculation(math_expression: str) -> float:
    """
    Performs a math calculation based on the user's input.
    Args:
        math_expression (str): The math expression to evaluate. i.e. "100 + 200 - 300 * 400 / 500"
    """
    print(f"Received math expression: '{math_expression}' in make_a_math_calculation")
    res = eval(math_expression)
    return res

@mcp.tool()
def get_latest_exchange_rates(base_currency: str):
    """
    Gets the latest exchange rates using a base currency.

    Parameters:
        base_currency (str): Base currency code (e.g., 'USD', 'EUR', 'JPY').

    Returns:
        dict: Dictionary containing the exchange rate data or an error if the currency is not supported.
    """
    print(f"Received base currency: '{base_currency}' in 'get_latest_exchange_rates'")
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency.upper()}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        return {
            "error": "Currency code not supported.",
            "details": response.json()
        }
    else:
        response.raise_for_status()  # Raises an exception for other HTTP codes


if __name__ == "__main__":
    tools = asyncio.run(mcp.list_tools())
    print("Available tools:", tools)
    print(f"Running on host {args.host} and port {args.port}")
    mcp.run(transport="sse")
    # Add MCP server after initializing the FastMCP server
    # "my-mcp-server-exchange": {
    #     "url": "http://localhost:8000/sse"
    #   }