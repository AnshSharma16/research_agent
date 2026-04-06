# utils/formatter.py

def format_articles(articles: list) -> list:
    return [
        {
            "title": article["title"],
            "description": article["description"],
            "url": article["url"]
        }
        for article in articles
    ]

def format_response(query: str, articles: list, summary: str, sentiments: str) -> dict:
    return {
        "status": "success",
        "query": query,
        "data": {
            "articles": articles,
            "summary": summary,
            "sentiments": sentiments
        }
    }