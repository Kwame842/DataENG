import os
from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Base directory
BASE_DIR = Path(__file__).parent.parent

# Database configurations
DB_CONFIG = {
    'mysql': {
        'host': os.getenv('MYSQL_HOST', 'mysql'),
        'port': int(os.getenv('MYSQL_PORT', 3306)),
        'user': os.getenv('MYSQL_USER', 'YOUR_USER'),
        'password': os.getenv('MYSQL_PASSWORD', 'YOUR_PASSWORD'),
        'database': os.getenv('MYSQL_STAGING_DB', 'YOUR_DB')
    },
    'postgresql': {
        'host': os.getenv('POSTGRES_HOST', 'postgres'),
        'port': int(os.getenv('POSTGRES_PORT', 5432)),
        'user': os.getenv('POSTGRES_USER', 'YOUR_PG_USER'),
        'password': os.getenv('POSTGRES_PASSWORD', 'YOUR_POSTGRES_PASSWORD'),
        'database': os.getenv('POSTGRES_ANALYTICS_DB', 'YOUR_PG_DB')
    }
}

# File paths
DATA_FILE = os.path.join(BASE_DIR, 'data/Flight_Price_Dataset_of_Bangladesh.csv')
LOG_DIR = os.path.join(BASE_DIR, 'logs/pipeline')

# Airflow configurations
DEFAULT_ARGS = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Create log directory if it doesn't exist
os.makedirs(LOG_DIR, exist_ok=True)


class Settings:
    def __init__(self):
        self.BASE_DIR = BASE_DIR
        self.DB_CONFIG = DB_CONFIG
        self.DATA_FILE = DATA_FILE
        self.LOG_DIR = LOG_DIR
        self.DEFAULT_ARGS = DEFAULT_ARGS

settings = Settings()  # <- This is now importable
