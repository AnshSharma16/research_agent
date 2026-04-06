# main.py
from fastapi import FastAPI
from routes.research import router as research_router

app = FastAPI()

app.include_router(research_router) 