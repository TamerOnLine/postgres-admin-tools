import os
import subprocess
from datetime import datetime
from db_config import get_database_credentials

# Common pg_dump paths for Windows systems
COMMON_PG_DUMP_PATHS = [
    r"C:\\Program Files\\PostgreSQL\\17\\bin\\pg_dump.exe",
    r"C:\\Program Files\\PostgreSQL\\15\\bin\\pg_dump.exe",
    r"C:\\Program Files\\PostgreSQL\\14\\bin\\pg_dump.exe",
    r"C:\\Program Files\\PostgreSQL\\13\\bin\\pg_dump.exe",
    r"C:\\Program Files\\PostgreSQL\\12\\bin\\pg_dump.exe"
]

def find_pg_dump():
    """
    Search for the pg_dump executable in common installation paths.

    Returns:
        str: Path to the pg_dump executable, or 'pg_dump' if not found in predefined paths.
    """
    for path in COMMON_PG_DUMP_PATHS:
        if os.path.exists(path):
            return path
    return "pg_dump"  # Fallback to relying on system PATH


def create_backup():
    """
    Create a PostgreSQL database backup using credentials from configuration.

    The backup file is stored in a local 'backups' folder with a timestamped filename.
    """
    pg_dump_path = find_pg_dump()
    creds = get_database_credentials()

    # Create backup directory if it doesn't exist
    backup_folder = "./backups"
    os.makedirs(backup_folder, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_filename = f"{creds['dbname']}_backup_{timestamp}.sql"
    backup_path = os.path.join(backup_folder, backup_filename)

    # Set environment variable for password authentication
    os.environ["PGPASSWORD"] = creds['password']

    # Construct the pg_dump command
    dump_command = [
        pg_dump_path,
        "-h", creds['host'],
        "-p", creds['port'],
        "-U", creds['user'],
        "-d", creds['dbname'],
        "-f", backup_path
    ]

    try:
        print(f"Starting backup for database '{creds['dbname']}'...")
        subprocess.run(dump_command, check=True)
        print(f"Backup successfully saved to: {backup_path}")
    except subprocess.CalledProcessError as e:
        print("Backup failed due to a process error:")
        print(f"{e}")
    except FileNotFoundError:
        print("pg_dump executable was not found in expected locations.")


if __name__ == "__main__":
    create_backup()
