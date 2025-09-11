import asyncio

from config import azure_config
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.mcp import MCPServerSSE
from pydantic_ai.providers.azure import AzureProvider
from rich import print
from dataclasses import dataclass

model = OpenAIModel(azure_config.model_name,
    provider=AzureProvider(
        azure_endpoint=azure_config.base_url,
        api_version=azure_config.api_version,
        api_key=azure_config.api_key,
    ),)

host = "http://localhost:8000"
# host = "https://mcp-server-hub-f0h3e4g2hsatgfa7.canadacentral-01.azurewebsites.net"
exchange_server = MCPServerSSE(url=f'{host}/exchange/sse')
duckduckgo_server = MCPServerSSE(url=f'{host}/websearch/sse')
context_server = MCPServerSSE(url=f'{host}/sse')

@dataclass
class CustomContext():
    data: dict

agent = Agent(
    model,
    name="MultiTask Agent",
    output_type=str,
    # deps_type=CustomContext,
    toolsets=[
        duckduckgo_server,
        exchange_server,
        context_server,
    ],
)

async def main():
    async with agent: 
        inquery = "What is the current exchange rate of USD to EUR and JPY to PEN?"
        print(f"\nQuery: '{inquery}'")
        result = await agent.run(inquery)
        print(result.output)
        # ###################################
        inquery = "Can you explain Google A2A and Anthropic MCP in detail?"
        print(f"\nQuery: '{inquery}'")
        result = await agent.run(inquery)
        print(result.output)
        # ###################################
        inquery = "What is the context of the user with ID 1234?"
        print(f"\nQuery: '{inquery}'")
        result = await agent.run(inquery,
                                 deps=CustomContext(data={"id": "1234"})
                                 )
        print(result.output)
        ####################################
        inquery = "What is the current weather in Toronto in fahrenheit?, how do you convert celsius to fahrenheit?"
        print(f"\nQuery: '{inquery}'")
        result = await agent.run(inquery)
        print(result.output)
        ####################################
    
if __name__ == "__main__":
    asyncio.run(main())