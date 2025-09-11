from openai import OpenAI
from rich import print
from config import corp_config
import asyncio
from pydantic_ai.providers.openai import OpenAIProvider
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai import Agent, ImageUrl, BinaryContent, AudioUrl, VideoUrl, DocumentUrl
from pydantic_graph import End
from pydantic_ai.models.openai import OpenAIChatModel, OpenAIChatModelSettings
import httpx

client = OpenAI(api_key=corp_config.api_key, base_url=corp_config.base_url)
 
model = OpenAIChatModel('vertex_ai/gemini-2.5-pro',
    provider=OpenAIProvider(
        base_url=corp_config.base_url,
        api_key=corp_config.api_key,
    ),)
settings = OpenAIChatModelSettings(
    openai_reasoning_effort='low',
    openai_reasoning_summary='detailed',
)

from pydantic_ai.models.google import GoogleModel, GoogleModelSettings

settings = GoogleModelSettings(google_thinking_config={'include_thoughts': True})
reasoning_agent = Agent(model,
                        instructions='You are a highly logical and methodical problem solver.',
                        model_settings=settings
)
prompt_reasoning = """
First, restate the question in a few sentences to show you understand it.
Then solve it step by step with your reasoning.
Finally, give your direct answer.
 
Question: Alice has N brothers and M sisters. How many sisters does each of her brothers have?
""" 

# async def main():
#     result = await reasoning_agent.run(prompt_reasoning) 
#     print("----")
#     print("Result:")
#     print(result.new_messages_json())
#     print("----")
#     print("Output:")
#     print(result.output) 
# if __name__ == "__main__":
#     asyncio.run(main())

# async def main():
#     nodes = []
#     async with reasoning_agent.iter(prompt_reasoning) as agent_run:
#         async for node in agent_run:
#             # Each node represents a step in the agent's execution
#             nodes.append(node)
#     print(nodes)
# if __name__ == "__main__":
#     asyncio.run(main())

# async def main():
#     async with reasoning_agent.iter(prompt_reasoning) as agent_run:
#         node = agent_run.next_node
#         all_nodes = [node]
#         while not isinstance(node, End):  
#             node = await agent_run.next(node)  
#             print(node)
#             all_nodes.append(node)  
#         print(all_nodes)
# # if __name__ == "__main__":
# #     asyncio.run(main())
    
# app = reasoning_agent.to_cli_sync()

############################################
############################################
############################################

model = OpenAIChatModel('vertex_ai/gemini-2.5-flash-lite',
    provider=OpenAIProvider(
        base_url=corp_config.base_url,
        api_key=corp_config.api_key,
    ),)
gemini_agent = Agent(model=model, instructions="Use a string format supported by 'from rich import print', just return the answer, no script",)
############################################
# result = gemini_agent.run_sync(
#   [
#       'What company is this logo from?',
#       ImageUrl(url='https://iili.io/3Hs4FMg.png'),
#   ]
# )
# print(result.output)

############################################
# image_response = httpx.get('https://iili.io/3Hs4FMg.png')  # Pydantic logo

# result = gemini_agent.run_sync(
#     [
#         'What company is this logo from?',
#         BinaryContent(data=image_response.content, media_type='image/png'),
#     ]
# )
# print(result.output)

# chat_history = result.all_messages()
# result = gemini_agent.run_sync('Describe me the colors', message_history=chat_history)
# print(result.output)

############################################
# result = gemini_agent.run_sync(
#     [
#         'What is the main content of this document?',
#         DocumentUrl(url='https://storage.googleapis.com/cloud-samples-data/generative-ai/pdf/2403.05530.pdf'),
#     ]
# )
# print(result.output)

############################################
# import tempfile
# import requests
# from pathlib import Path
# url = "https://storage.googleapis.com/cloud-samples-data/generative-ai/pdf/2403.05530.pdf"

# with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp_file:
#     print("Downloading PDF to temporary file:", tmp_file.name)
#     response = requests.get(url)
#     tmp_file.write(response.content)
#     temp_path = tmp_file.name
#     print("PDF downloaded successfully.")
    
# pdf_path = Path(temp_path)
# result = gemini_agent.run_sync(
#     [
#         'Tell me a title for this document',
#         BinaryContent(data=pdf_path.read_bytes(), media_type='application/pdf'),
#     ]
# )
# print(result.output)
# result2 = gemini_agent.run_sync(
#   'What is the main content of this document?', message_history=result.all_messages()
# )
# print(result2.output)

############################################
result = gemini_agent.run_sync(
    [
        'What is the main content of this mp3?',
        AudioUrl(url='https://raw.githubusercontent.com/exaile/exaile-test-files/refs/heads/master/tone.mp3'),
    ]
)
print(result.output)
print(result.usage())
result2 = gemini_agent.run_sync("Tell me how long is the audio?", message_history=result.all_messages())
print(result2.output)

############################################
# result = gemini_agent.run_sync(
#     [
#         'What is the main content of this mp4?',
#         VideoUrl(url='http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerFun.mp4'),
#     ]
# )
# print(result.output)
# import tempfile
# import requests
# from pathlib import Path
# url = "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerFun.mp4"

# with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as tmp_file:
#   print("Downloading MP4 to temporary file:", tmp_file.name)
#   with requests.get(url, stream=True) as response:
#     for chunk in response.iter_content(chunk_size=8192*10):
#       print(".", end="", flush=True)
#       tmp_file.write(chunk)
#   temp_path = tmp_file.name
#   print("MP4 downloaded successfully.")

# mp4_path = Path(temp_path)
# result = gemini_agent.run_sync(
#     [
#         'What is the main content of this mp4?',
#         BinaryContent(data=mp4_path.read_bytes(), media_type='video/mp4'),
#     ]
# )
# print(result.output)