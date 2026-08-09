# #yfinance dashboard + notification etl

# etl.py: Fetches from yfinance $\rightarrow$ Cleans $\rightarrow$ Saves to Postgres $\rightarrow$ Checks threshold & sends WhatsApp if triggered $\rightarrow$ Scheduled via crontab

# app.py: Reads from Postgres $\rightarrow$ Powers your Streamlit UI for analytics and visualization