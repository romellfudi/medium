
import uvicorn
from mcp.server.fastmcp import FastMCP
from starlette.applications import Starlette
from starlette.routing import Mount, Host

from mcp_exchange_server_sse import mcp as exchange_mcp
from mcp_websearch_server_sse import mcp as websearch_mcp
from mcp_context_sse import mcp as context_mcp
import argparse

# Default host and port
DEFAULT_HOST = "0.0.0.0"
DEFAULT_PORT = 8000

# Set up argument parser
parser = argparse.ArgumentParser(description="Run the MCP Exchange Server")
parser.add_argument("--host", default=DEFAULT_HOST, help="Host address to run the server")
parser.add_argument("--port", type=int, default=DEFAULT_PORT, help="Port number to run the server")
args = parser.parse_args()

host = args.host
port = args.port

app = Starlette(
    routes=[
        Mount("/exchange", app=exchange_mcp.sse_app(mount_path="/")),
        Mount("/websearch", app=websearch_mcp.sse_app(mount_path="/")),
        Mount("/", app=context_mcp.sse_app(mount_path="/")),
    ]
)

if __name__ == "__main__":
    uvicorn.run(app=app, host=host, port=port)