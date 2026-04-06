# services/news_service.py
import httpx
import os
from dotenv import load_dotenv

load_dotenv()
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")

async def fetch_news(q: str) -> list:
    url = f"https://newsapi.org/v2/everything?q={q}&apiKey={NEWSAPI_KEY}"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
    
    return data["articles"]