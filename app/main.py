from fastapi import FastAPI
from app.esg_rag import get_esg_response
from app.webscrape import get_latest_esg_news

app = FastAPI()

@app.get("/")
def home():
    return {"message": "ESG Chatbot API is running"}

@app.get("/ask")
def ask_esg(query: str):
    response = get_esg_response(query)
    return {"response": response}

@app.get("/news")
def get_esg_news():
    news = get_latest_esg_news()
    return {"news": news}
