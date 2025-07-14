Multi-Agent Toolbox 🤖

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-00ADD8?style=for-the-badge&logo=LangChain&logoColor=white)](https://python.langchain.com/)
[![Groq](https://img.shields.io/badge/Groq-00FF00?style=for-the-badge&logo=Groq&logoColor=black)](https://groq.com/)

Transform your queries into actionable insights with AI-powered agents! This Streamlit application leverages LangChain and Groq to create specialized agents that handle weather forecasts and mathematical calculations.

## Features ✨

- **Weather Forecasting Agent**: Get real-time weather information for any city worldwide
- **Mathematical Calculation Agent**: Perform complex calculations and solve equations
- **Modern Streamlit UI**: Beautiful gradient design with responsive cards and animations
- **Multi-Server Architecture**: Independent agents for different domains
- **Error-Resistant Workflow**: Comprehensive error handling and user feedback
- **Responsive Design**: Works seamlessly on desktop and mobile devices

   
## Requirements 📋
Python 3.9+

Streamlit

LangChain

LangGraph

FastMCP

Groq API Key

OpenWeather API Key

## Configuration
The system uses specialized agents with distinct configurations:

Math Agent: Runs locally through Python, executing math operations with step-by-step explanations

Weather Agent: Connects to OpenWeather API via HTTP to fetch real-time forecasts

Agent Controller: Manages communication between agents using LangGraph

API Integration: Requires Groq API (for Llama3 AI model) and OpenWeather API keys stored in .env file

## How It Works
User Query Processing:

Users submit natural language queries through the Streamlit web interface

The system analyzes whether the query requires math calculation, weather data, or both

## Agent Execution:

Math queries route to the local math server that performs calculations

Weather queries call the weather server which fetches live data from OpenWeather

## Response Generation:

Math operations return detailed step-by-step solutions

Weather forecasts provide temperature and conditions

Combined queries show conversion processes between units

Results display in a formatted UI with visual feedback

Error Handling:

System catches API failures, math errors (like division by zero), and invalid inputs

User-friendly error messages explain issues clearly

