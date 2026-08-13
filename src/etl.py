#etl.py: Fetches from yfinance $\rightarrow$ Cleans $\rightarrow$ Saves to Postgres $\rightarrow$ Checks threshold & sends WhatsApp if triggered $\rightarrow$ Scheduled via crontab
from datetime import datetime 
import pandas as pd
from sqlalchemy import create_engine
import yfinance as yf

def fetch_bitcoin_price():
    btc = yf.Ticker("BTC-USD")
    price = btc.fast_info["lastPrice"]
    return price
