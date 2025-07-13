from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import requests
import os

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
if not API_KEY:
    raise ValueError("Missing OPENWEATHER_API_KEY")

mcp = FastMCP("Weather")

@mcp.tool()
def get_weather(city: str) -> str:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    r = requests.get(url, timeout=5)
    data = r.json()
    if r.status_code != 200:
        return f"Error: {data.get('message')}"
    temp = data["main"]["temp"]
    cond = data["weather"][0]["description"]
    return f"{city.title()}: {temp}°C, {cond}"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
