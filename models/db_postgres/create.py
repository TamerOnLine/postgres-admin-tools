import os
import sys

import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from db_postgres.db_config import get_database_credentials


def create_database_if_not_exists():
    """Create the configured PostgreSQL database when it does not exist."""
    creds = get_database_credentials()
    dbname = creds["dbname"]

    try:
        with psycopg2.connect(
            dbname="postgres",
            user=creds["user"],
            password=creds["password"],
            host=creds["host"],
            port=creds["port"],
        ) as connection:
            connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", (dbname,))
                if cursor.fetchone():
                    print(f"Database '{dbname}' already exists.")
                    return
                cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(dbname)))
                print(f"Created database: {dbname}")
    except psycopg2.Error as exc:
        print(f"Error creating database: {exc}")


if __name__ == "__main__":
    create_database_if_not_exists()
