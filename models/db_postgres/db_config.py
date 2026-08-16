import os
from urllib.parse import urlparse

from dotenv import load_dotenv

load_dotenv()


def get_database_credentials():
    """Return validated PostgreSQL credentials from the environment."""
    db_url = os.getenv("DATABASE_URL")

    if db_url:
        parsed = urlparse(db_url)
        credentials = {
            "host": parsed.hostname,
            "port": str(parsed.port or 5432),
            "user": parsed.username,
            "password": parsed.password,
            "dbname": parsed.path.lstrip("/"),
        }
    else:
        credentials = {
            "host": os.getenv("DB_HOST", "localhost"),
            "port": os.getenv("DB_PORT", "5432"),
            "user": os.getenv("DB_USER"),
            "password": os.getenv("DB_PASSWORD"),
            "dbname": os.getenv("DB_NAME"),
        }

    missing = [
        key for key in ("host", "port", "user", "password", "dbname")
        if not credentials.get(key)
    ]
    if missing:
        raise ValueError(
            "Missing database configuration: "
            + ", ".join(missing)
            + ". Set DATABASE_URL or the DB_* environment variables."
        )

    return credentials
