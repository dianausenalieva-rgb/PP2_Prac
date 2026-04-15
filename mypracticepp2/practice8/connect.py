import psycopg2
from config import load_config

def create_connection():
    try:
        config = load_config()

        conn = psycopg2.connect(
            host=config['host'],
            database=config['database'],
            user=config['user'],
            password=config['password'],
            port=5432
        )

        print("Connected to PostgreSQL")
        return conn

    except Exception as error:
        print("Connection error:", error)
        return None


if __name__ == "__main__":
    create_connection()