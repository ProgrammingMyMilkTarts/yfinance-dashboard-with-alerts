#etl.py: Fetches from yfinance $\rightarrow$ Cleans $\rightarrow$ Saves to Postgres $\rightarrow$ Checks threshold & sends WhatsApp if triggered $\rightarrow$ Scheduled via crontab
import logging 
import random
import time
import pandas as pd
import yfinance as yf
from database import get_db_engine
import os


logging.basicConfig(level=logging.INFO)
user = os.getenv('DB_USER')
print(user)

def run_bitcoin_etl():
    logging.info("Starting Bitcoin ETl")

    #sleep a random amount of seconds so i am not picked up by bots
    time.sleep(random.uniform(1.0,5.0))

    try:
        print("Fetching data")
        btc = yf.Ticker("BTC-USD")
        df = btc.history(period = "1d")

        if df.empty:
            logging.warning("No data is found")
            return
        
        df = df.reset_index()
        df["Ticker"] = "BTC-USD"
        df = df[["Date", "Ticker", "Open", "High", "Low", "Close", "Volume"]]

        print("connecting to db")
        engine = get_db_engine()

        #df.to_sql('table_name', con=engine, if_exists='append', index=False)
        print("Pushing data to postgres...")
        df.to_sql('crypto_prices', con=engine, if_exists='append',index=False)
        print('Successfully pushed')
            
    except Exception as e:
        logging.error(f"ETL failed: {e}")

    


if __name__ == "__main__":
    run_bitcoin_etl()
