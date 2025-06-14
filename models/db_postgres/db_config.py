import os
from urllib.parse import urlparse
from dotenv import load_dotenv

load_dotenv()

def get_database_credentials():
    """
    Retrieve database credentials from environment variables or a DATABASE_URL.

    Returns:
        dict: A dictionary containing database connection parameters:
              'host', 'port', 'user', 'password', and 'dbname'.

    Raises:
        ValueError: If required credentials are not found in the environment.
    """
    db_url = os.getenv("DATABASE_URL")

    # Use DATABASE_URL if provided
    if db_url:
        parsed = urlparse(db_url)
        return {
            "host": parsed.hostname,
            "port": str(parsed.port or 5432),
            "user": parsed.username,
            "password": parsed.password,
            "dbname": parsed.path.lstrip('/')
        }

    # Fallback to individual environment variables
    dbname = os.getenv("DB_NAME", "default_dbname")
    user = os.getenv("DB_USER", "default_user")
    password = os.getenv("DB_PASSWORD", "default_password")
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "5432")


    if not all([dbname, user, password]):
        raise ValueError("Missing database configuration. Provide either DATABASE_URL or DB_NAME, DB_USER, DB_PASSWORD in the .env file.")

    return {
        "host": host,
        "port": str(port),
        "user": user,
        "password": password,
        "dbname": dbname
    }

if __name__ == "__main__":
    creds = get_database_credentials()
    print(creds)

