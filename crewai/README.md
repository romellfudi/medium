# README

## Overview

This Jupyter Notebook, `L-1_crewai.ipynb`, demonstrates the use of the CrewAI library to create and manage AI agents and tasks. The notebook includes the following key components:

- **Installation of Required Packages**: Ensures all necessary packages are installed.
- **Environment Setup**: Loads environment variables using `dotenv`.
- **LLM Integration**: Utilizes the `crewai` library to interact with a language model for generating responses.
- **Tool Definition**: Defines a web search tool using `crewai_tools`.
- **Agent Creation**: Sets up different agents with specific roles such as Senior Researcher and Content Writer.
- **Task Definition**: Creates tasks for each agent to gather and compile information.
- **Execution of Tasks**: Runs the tasks sequentially to generate a comprehensive output, including a blog post.

## Key Components

### Installation of Required Packages

The notebook begins by uninstalling any existing installations of `crewai` and `crewai_tools` packages.

```python
!pip install -qq crewai crewai_tools