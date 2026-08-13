# #yfinance dashboard + notification etl

# etl.py: Fetches from yfinance $\rightarrow$ Cleans $\rightarrow$ Saves to Postgres $\rightarrow$ Checks threshold & sends WhatsApp if triggered $\rightarrow$ Scheduled via crontab

# app.py: Reads from Postgres $\rightarrow$ Powers your Streamlit UI for analytics and visualization

# --------What my plan is so far---------
crypto_tracker/
├── .github/
│   └── workflows/
│       └── cron_job.yml      # GitHub Actions scheduler
├── .streamlit/
│   └── secrets.toml          # Local dev only (git-ignored)
├── src/
│   ├── database.py
│   ├── etl.py
│   └── notifications.py
├── .gitignore
├── app.py                    # Streamlit UI
├── worker.py                 # The script GitHub Actions will trigger
└── requirements.txt