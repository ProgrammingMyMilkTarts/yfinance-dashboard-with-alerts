# backend/src/test_db.py
from core.database import init_db, save_crypto_price, get_latest_prices

def run_test():
    print("1. Initializing database tables...")
    init_db()  # This will create crypto_prices and alerts tables if they don't exist

    print("\n2. Inserting a test price record...")
    try:
        record = save_crypto_price(symbol="TEST-USD", price=99999.99, change_24h=5.5, volume=1000.0)
        print(f"Success! Inserted: {record}")
    except Exception as e:
        print(f"Failed to insert record: {e}")

    print("\n3. Fetching latest prices...")
    try:
        latest = get_latest_prices(["TEST-USD"])
        print(f"Success! Fetched: {latest}")
    except Exception as e:
        print(f"Failed to fetch record: {e}")

if __name__ == "__main__":
    run_test()