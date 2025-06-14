import os
from urllib.parse import urlparse
from dotenv import load_dotenv

load_dotenv()

def get_database_credentials():
    db_url = os.getenv("DATABASE_URL")

    # لو DATABASE_URL موجود، نستخدمه
    if db_url:
        parsed = urlparse(db_url)
        return {
            "host": parsed.hostname,
            "port": str(parsed.port or 5432),
            "user": parsed.username,
            "password": parsed.password,
            "dbname": parsed.path.lstrip('/')
        }

    # لو مش موجود، نرجع للمتغيرات المفصولة
    dbname = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "5432")

    if not all([dbname, user, password]):
        raise ValueError("❌ تأكد من وجود إما DATABASE_URL أو DB_NAME, DB_USER, DB_PASSWORD في ملف .env")

    return {
        "host": host,
        "port": str(port),
        "user": user,
        "password": password,
        "dbname": dbname
    }
