# python mcp_exchange_server_sse.py
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp import Context
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
host = args.host
port = args.port

mcp = FastMCP("User Tool", host=host, port=port)

@mcp.tool()
async def fetch_user_context(id_user: str, ctx: Context) -> str:
    # """Use the user context to provide information about a person.
    # Args:
    #     id_user (str): The ID of the person.
    #     context (Context): The context provided by the user.
    # """
    print(f"Received query: '{id_user}' in fetch_user_context")
    print(f"Extra: {ctx.model_extra}")
    print(f"request_context: {ctx.request_context}")
    print(f"Context json: {ctx.model_json_schema()}")
    # print(ctx.model_dump())
    # await ctx.info("XXXX")
    # await ctx.log("Logging information")
    print("--------")
    # context.fastmcp.list_tools
    return f"John Doe is a software engineer with 10 years of experience in Python and JavaScript. He is currently working at XYZ Corp as a senior developer. He has a passion for open-source projects and enjoys contributing to the community."

# @mcp.resource("resource://{city}/weather")
@mcp.tool()
async def get_weather(city: str) -> str:
    # data = await fetch_weather(city)
    data = "23°C, Sunny"
    print(f"Received query: '{city}' in get_weather")
    print(data)
    return f"Weather for {city}: {data}"

if __name__ == "__main__":
    tools = asyncio.run(mcp.list_tools())
    print("Available tools:", tools)
    print(f"Running on host {host} and port {port}")
    mcp.run(transport="sse")
    # Add MCP server after initializing the FastMCP server
    # "my-mcp-server-exchange": {
    #     "url": "http://localhost:8000/sse"
    #   }