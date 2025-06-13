import sys
import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Add parent directory to path to allow importing db_postgres when run directly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db_postgres.db_config import get_database_credentials

def create_database_if_not_exists():
    """
    Creates a PostgreSQL database if it does not already exist.

    Retrieves database connection credentials, connects to the default 'postgres'
    database, checks if the target database exists, and creates it if necessary.

    Raises:
        Exception: If an error occurs during connection or SQL execution.
    """
    creds = get_database_credentials()
    dbname = creds["dbname"]
    user = creds["user"]
    password = creds["password"]
    host = creds["host"]
    port = creds["port"]

    try:
        conn = psycopg2.connect(
            dbname='postgres', user=user, password=password, host=host, port=port
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()

        cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", (dbname,))
        exists = cursor.fetchone()

        if not exists:
            cursor.execute(f'CREATE DATABASE "{dbname}"')
            print(f"Created database: {dbname}")
        else:
            print(f"Database '{dbname}' already exists.")

        cursor.close()
        conn.close()

    except Exception as e:
        print("Error creating database:", e)

if __name__ == '__main__':
    create_database_if_not_exists()
