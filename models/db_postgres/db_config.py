import os
from urllib.parse import urlparse
from dotenv import load_dotenv

load_dotenv()

def get_database_credentials():
    """
    Retrieves PostgreSQL database credentials from the environment variable 'DATABASE_URL'.

    Returns:
        dict: A dictionary containing the database name, username, password,
              host, and port required for the connection.
    """
    url = os.getenv("DATABASE_URL")
    parsed = urlparse(url)
    return {
        "dbname": parsed.path.lstrip('/'),
        "user": parsed.username,
        "password": parsed.password,
        "host": parsed.hostname or 'localhost',
        "port": parsed.port or 5432,
    }

if __name__ == '__main__':
    creds = get_database_credentials()
    print("Database Credentials:")
    for key, value in creds.items():
        print(f"{key}: {value}")
