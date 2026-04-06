# services/llm_service.py
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_KEY = os.getenv("GEMINI_KEY")

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel("gemini-2.0-flash-lite")

def summarize(q: str, articles: list) -> str:
    prompt = f""" You are a professional researcher.Given these news articles about {q}: {articles} Summarize the key insights in 3 bullet points.  Focus on insights. Return as JSON: {{ "summary": "...", "key_points": ["...", "..."] }} """
    
    try:
        response = model.generate_content(prompt)   
        return response.text
    except Exception as e:
        return f"Summary unavailable: {str(e)}"

def analyze_sentiment(articles: list) -> list:
    descriptions = [article["description"] for article in articles]
    
    prompt = f"""
    You are a sentiment analyst.
Given these news descriptions: {descriptions}
Return a JSON array with sentiment for each description:
[
    {{"index": 0, "sentiment": "positive/negative/neutral"}},
    {{"index": 1, "sentiment": "positive/negative/neutral"}}
]
"""
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Sentiment unavailable: {str(e)}"