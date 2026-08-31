Crypto dashboard & Alert Engine (Backend)

A robust, lightweight backend system designed to track core cryptocurrency market data via automated ETL pipelines, evaluate custom user price thresholds, and dispatch real-time alerts via WhatsApp and Email.

FRONT END STILL BUSY

Tech Stack & Libraries

    Language: Python 3.10+

    Database & ORM: PostgreSQL, SQLAlchemy

    Data Extraction: yfinance

    Notifications: Twilio API (WhatsApp), Python smtplib (Email)

    Environment Management: python-dotenv

Project Directory Structure
Plaintext

    backend/
    ├── src/
    │   ├── core/
    │   │   └── database.py          # SQLAlchemy engine, session management, and DB models
    │   ├── etl/
    │   │   ├── crypto_fetcher.py    # Fetches crypto data from yfinance and persists to DB
    │   │   └── price_checker.py     # Background worker evaluating active user alerts
    │   ├── api/
    │   │   ├── routes/
    │   │   │   ├── alerts.py        # Alert CRUD endpoints
    │   │   │   └── prices.py        # Price data endpoints
    │   │   └── main.py              # FastAPI application entry point
    │   ├── models/
    │   │   ├── alert.py             # Pydantic models for alert validation
    │   │   └── crypto.py            # Pydantic models for crypto data
    │   └── utils/
    │       └── notifications.py     # Dispatchers for Twilio WhatsApp and SMTP email
    ├── .env                         # Secure configuration secrets
    ├── requirements.txt             # Python dependencies
    └── README.md                    # This file

Database Schema
1. crypto_prices

Stores historical and live pricing snapshots fetched from market APIs.

    id (Integer, Primary Key)

    symbol (String, Indexed) - e.g., BTC-USD, ETH-USD, SOL-USD

    price (Float)

    change_24h (Float)

    volume (Float)

    timestamp (DateTime, Server Default: Now)

2. alerts

Manages user-defined threshold alerts and tracking states.

    id (Integer, Primary Key)

    symbol (String, Indexed)

    target_price (Float)

    condition (String) - 'above' or 'below'

    contact (String) - Phone number or email address

    notification_method (String) - 'whatsapp' or 'email'

    unsubscribe_token (String, Unique)

    is_active (Boolean)

    triggered_count (Integer)

    last_notified_at (DateTime)

Setup & Configuration
1. Environment Variables

Create a .env file in your root backend folder with the following configuration:
Code snippet


2. Python Dependencies

Install the required packages:
Bash

pip install sqlalchemy psycopg2-binary yfinance twilio python-dotenv

Execution & Automation
Running the ETL Fetcher

Pulls the latest closing prices and volumes for target coins (BTC-USD, ETH-USD, SOL-USD) and saves them to PostgreSQL:
Bash

python3 -m src.etl.crypto_fetcher

Running the Price Alert Checker

Evaluates active user alerts against the latest database records, enforces a 24-hour cooldown period to prevent message spam, and dispatches notifications:
Bash

python3 -m src.etl.price_checker

Cron Job Automation

To run the pipeline automatically in a production or local Linux environment, configure your crontab:
Bash

# Run crypto fetcher every 30 minutes
*/30 * * * * /usr/bin/python3 /path/to/backend/src/etl/crypto_fetcher.py >> /var/log/crypto_etl.log 2>&1

# Run price alert checker every 30 minutes (offset by 2 mins)
2,32 * * * * /usr/bin/python3 /path/to/backend/src/etl/price_checker.py >> /var/log/crypt
