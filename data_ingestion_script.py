import pandas as pd
import os 
from sqlalchemy import create_engine
import logging
from datetime import datetime

# --- Configuration ---
CSV_FILE = "healthcare_dataset.csv"
DB_FILE = "Healthcare_Db.db"
TABLE_NAME = "healthcare_data"
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "ingestion.log")

# --- Set up logging ---
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S",
    filemode="a"
)

'''Function to load the csv file as dataframe and ingest it into database '''
def ingest_csv_to_sqlite(csv_file, db_file, table_name):
    try:
        # Read CSV
        df = pd.read_csv(csv_file)
        logging.info(f"Loaded CSV file '{csv_file}' with {len(df)} rows.")

        # Connect to SQLite using SQLAlchemy
        engine = create_engine(f"sqlite:///{db_file}")
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        logging.info(f"Successfully ingested data into '{db_file}' table '{table_name}'.")

    except Exception as e:
        logging.error(f"Failed to ingest CSV: {e}")

if __name__ == "__main__":
    ingest_csv_to_sqlite(CSV_FILE, DB_FILE, TABLE_NAME)
    