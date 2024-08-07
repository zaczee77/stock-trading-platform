from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
import requests

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# In-memory database for stocks
stocks_db = {}

# Define the Stock model
class Stock(BaseModel):
    symbol: str
    price: float

@app.get("/")
def read_root():
    return {"message": "Welcome to the Stock Trading Platform API"}

@app.post("/stocks/")
def create_stock(stock: Stock):
    stocks_db[stock.symbol] = stock.price
    return stock

@app.get("/stocks/")
def read_stocks():
    return stocks_db

@app.get("/update-real-time-stocks/")
def update_real_time_stocks():
    # Example API endpoint to get real-time stock data (replace with actual API URL)
    real_time_api_url = "https://api.example.com/stocks"  # Replace with your real-time stock API URL

    try:
        response = requests.get(real_time_api_url)
        response.raise_for_status()
        data = response.json()
        
        for item in data:
            symbol = item['symbol']
            price = item['price']
            stocks_db[symbol] = price

        return {"message": "Stock data updated successfully"}
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching stock data: {e}")
