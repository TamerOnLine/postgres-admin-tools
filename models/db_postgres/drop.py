import os
import sys

import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from models.db_postgres.db_config import get_database_credentials


def drop_database():
    """Drop the configured PostgreSQL database after explicit confirmation."""
    creds = get_database_credentials()
    dbname = creds["dbname"]

    confirmation = input(f"Type the database name '{dbname}' to permanently delete it: ")
    if confirmation != dbname:
        print("Database deletion cancelled.")
        return

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
                if not cursor.fetchone():
                    print(f"Database '{dbname}' does not exist.")
                    return

                cursor.execute(
                    """
                    SELECT pg_terminate_backend(pid)
                    FROM pg_stat_activity
                    WHERE datname = %s AND pid <> pg_backend_pid()
                    """,
                    (dbname,),
                )
                cursor.execute(sql.SQL("DROP DATABASE {}").format(sql.Identifier(dbname)))
                print(f"Dropped database: {dbname}")
    except psycopg2.Error as exc:
        print(f"Error while dropping database: {exc}")


if __name__ == "__main__":
    drop_database()
