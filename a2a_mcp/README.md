![AI A2A Project Logo](banner.gif)

# AI A2A Project

This project is an AI-driven assistant designed to optimize user tasks and time management using various agents. The agents interact with different services like Azure, ArXiv, and DuckDuckGo to provide actionable insights and suggestions.

## Project Structure

- **Agents**: Each agent is responsible for specific tasks, such as web searching, exchange rate retrieval, and ArXiv paper summarization.
- **Configuration**: The project uses configuration files (`config.py`, `config.yaml`, `.env`) to manage settings and credentials.

## Files

- `arxiv_agent.py`: Handles searches on ArXiv for research papers.
- `exchange_agent.py`: Retrieves the latest currency exchange rates.
- `web_search_agent.py`: Performs web searches using DuckDuckGo.
- `orchestrator.py`: Coordinates the actions of different agents based on user queries.
- `main.py`: Initializes the Spanish Agent for math calculations.
- `test_agent.py`: Tests the functionality of agents.
- `config.py`: Contains configuration classes for Azure, MongoDB, and other services.
- `config.yaml`: Stores prompt configurations for agents.
- `.env`: Contains environment variables for API keys and other credentials.
- `.gitignore`: Specifies files and directories to be ignored by Git.

## Setup

1. **Install Dependencies**: Ensure you have Python and the required libraries installed.
2. **Environment Variables**: Set up the `.env` file with your credentials.
3. **Run Agents**: Use `uvicorn` to run agents on specified ports.

## Usage

- **Agents**: Each agent can be run independently to perform its designated task.
- **Orchestrator**: Use the orchestrator to coordinate multiple agents for complex queries.

## Running the cases

Case 1:

### run hub

The `mcp_server_hub.py` script sets up and runs the MCP Exchange Server using `uvicorn`. It includes argument parsing for host and port configuration.

```bash
python mcp_server_hub.py
```

### test agent

The `mcp_agent_sse.py` script initializes an agent using the OpenAI model with Azure as the provider. It connects to the MCP Server SSE for exchange services.

```bash
python mcp_agent_sse.py
```

Case 2:

### start the agents servers

The `web_search_agent.py` script sets up a web search agent using DuckDuckGo. It utilizes the OpenAI model with Azure as the provider and includes a tool for executing code.

```bash
uvicorn web_search_agent:app --host 0.0.0.0 --port 8001 --reload
```

The `arxiv_agent.py` script configures an agent to search ArXiv for research papers. It uses the OpenAI model with Azure as the provider.

```bash
uvicorn arxiv_agent:app --host 0.0.0.0 --port 8002 --reload
```

The `exchange_agent.py` script sets up an agent to retrieve currency exchange rates. It uses the OpenAI model with Azure as the provider and includes a function for performing mathematical calculations.

```bash
uvicorn exchange_agent:app --host 0.0.0.0 --port 8003 --reload
```

### Test orchestrator

The `orchestrator.py` script coordinates the actions of different agents using the A2AClient. It sends messages and manages tasks asynchronously.

```bash
python orchestrator.py
```

Case 3:

### Run main application

The `main.py` script initializes the Spanish Agent for math calculations using the OpenAI model with Azure as the provider.

```bash
uvicorn main:app --host 0.0.0.0 --port 8004 --reload
```

### Test agent

The `test_agent.py` script tests the functionality of agents using the A2AClient. It sends messages and manages tasks asynchronously.

```bash
python test_agent.py
```
