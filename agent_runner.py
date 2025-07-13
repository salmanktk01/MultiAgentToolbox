import os
import asyncio
from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq


load_dotenv()
GROQ_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_KEY:
    raise ValueError("GROQ_API_KEY not set in .env")

config = {
    "math": {
        "command": "python",
        "args": ["math_server.py"],
        "transport": "stdio"
    },
    "weather": {
        "url": "http://localhost:8000/mcp/",
        "transport": "streamable_http"
    }
}

async def run_agent_query(user_prompt: str):
    client = MultiServerMCPClient(config)
    tools = await client.get_tools()

    llm = ChatGroq(groq_api_key=GROQ_KEY, model="llama3-70b-8192")

    agent = create_react_agent(llm, tools)

    response = await agent.ainvoke({"messages": [{"role": "user", "content": user_prompt}]})
    return response