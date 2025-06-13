import sys
import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Add project root to system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from models.db_postgres.db_config import get_database_credentials

def drop_database():
    """
    Drops a PostgreSQL database if it exists.

    Terminates any active connections to the target database, then deletes it
    using credentials obtained from the environment configuration.

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

        if exists:
            cursor.execute(
                """
                SELECT pg_terminate_backend(pid)
                FROM pg_stat_activity
                WHERE datname = %s
                """,
                (dbname,)
            )
            cursor.execute(f'DROP DATABASE "{dbname}"')
            print(f"Dropped database: {dbname}")
        else:
            print(f"Database '{dbname}' does not exist.")

        cursor.close()
        conn.close()

    except Exception as e:
        print("Error while dropping database:", e)

if __name__ == '__main__':
    drop_database()
