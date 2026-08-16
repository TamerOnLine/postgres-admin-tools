import os
import subprocess
from datetime import datetime

from db_config import get_database_credentials

COMMON_PG_DUMP_PATHS = [
    r"C:\Program Files\PostgreSQL\17\bin\pg_dump.exe",
    r"C:\Program Files\PostgreSQL\15\bin\pg_dump.exe",
    r"C:\Program Files\PostgreSQL\14\bin\pg_dump.exe",
    r"C:\Program Files\PostgreSQL\13\bin\pg_dump.exe",
    r"C:\Program Files\PostgreSQL\12\bin\pg_dump.exe",
]


def find_pg_dump():
    for path in COMMON_PG_DUMP_PATHS:
        if os.path.exists(path):
            return path
    return "pg_dump"


def create_backup():
    """Create a timestamped PostgreSQL backup."""
    pg_dump_path = find_pg_dump()
    creds = get_database_credentials()

    backup_folder = "./backups"
    os.makedirs(backup_folder, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_filename = f"{creds['dbname']}_backup_{timestamp}.sql"
    backup_path = os.path.join(backup_folder, backup_filename)

    dump_command = [
        pg_dump_path,
        "-h", creds["host"],
        "-p", creds["port"],
        "-U", creds["user"],
        "-d", creds["dbname"],
        "-f", backup_path,
    ]
    process_env = os.environ.copy()
    process_env["PGPASSWORD"] = creds["password"]

    try:
        print(f"Starting backup for database '{creds['dbname']}'...")
        subprocess.run(dump_command, check=True, env=process_env)
        print(f"Backup successfully saved to: {backup_path}")
    except subprocess.CalledProcessError as exc:
        print(f"Backup failed: {exc}")
    except FileNotFoundError:
        print("pg_dump executable was not found.")


if __name__ == "__main__":
    create_backup()
