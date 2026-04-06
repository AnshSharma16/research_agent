# routes/research.py
from fastapi import APIRouter, Query
from services.news_service import fetch_news
from services.llm_service import summarize, analyze_sentiment
from utils.formatter import format_articles, format_response

router = APIRouter()

@router.get("/research")
async def research(q: str = Query("AI")):
    raw_articles = await fetch_news(q)
    articles = format_articles(raw_articles)
    summary = summarize(q, articles)
    sentiments = analyze_sentiment( articles)


    return format_response(q,articles, summary, sentiments)