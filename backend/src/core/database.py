#database.py connect to postgres

import os
from sqlalchemy import create_engine
from dotenv import load_dotenv


#databae connection
def get_db_engine():
  load_dotenv(override = True)
  
  # Grab secrets securely from environment variables
  user = os.getenv('DB_USER')
  password = os.getenv('DB_PASSWORD')
  host = os.getenv('DB_HOST', 'localhost')
  port = os.getenv('DB_PORT', '5432')
  dbname = os.getenv('DB_NAME', 'financial_db')

  # Create and return the SQLAlchemy engine connection object
  engine = create_engine(
      f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}'
  )

  return engine