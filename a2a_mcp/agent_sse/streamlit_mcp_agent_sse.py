import streamlit as st
import asyncio
import streamlit as st
from mcp_agent_sse import agent, CustomContext

st.title("Streamlit Chat Application")

# Streamlit chat interface
if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to handle user input and display responses
async def handle_input(user_input):
    async with agent:
        result = await agent.run(user_input)
        return result.output

# Streamlit app layout
user_input = st.chat_input("Enter your query:")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = asyncio.run(handle_input(user_input))
    st.session_state.messages.append({"role": "assistant", "content": response})

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
