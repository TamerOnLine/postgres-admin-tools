import os
import subprocess

from db_config import get_database_credentials

PSQL_PATHS = [
    r"C:\Program Files\PostgreSQL\17\bin\psql.exe",
    r"C:\Program Files\PostgreSQL\15\bin\psql.exe",
    r"C:\Program Files\PostgreSQL\14\bin\psql.exe",
    "psql",
]


def find_psql():
    for path in PSQL_PATHS:
        if path == "psql" or os.path.exists(path):
            return path
    raise FileNotFoundError("psql executable was not found.")


def choose_backup_file(folder="./backups"):
    files = sorted(f for f in os.listdir(folder) if f.endswith(".sql"))
    if not files:
        raise FileNotFoundError("No SQL backup files were found.")

    print("Available backup files:")
    for index, filename in enumerate(files, start=1):
        print(f"{index}. {filename}")

    while True:
        try:
            choice = int(input("Select a backup file: "))
            if 1 <= choice <= len(files):
                return os.path.join(folder, files[choice - 1])
        except ValueError:
            pass
        print("Enter a valid selection.")


def restore_backup():
    """Restore a selected local SQL backup."""
    creds = get_database_credentials()
    backup_file = choose_backup_file()

    restore_command = [
        find_psql(),
        "-h", creds["host"],
        "-p", creds["port"],
        "-U", creds["user"],
        "-d", creds["dbname"],
        "-f", backup_file,
    ]
    process_env = os.environ.copy()
    process_env["PGPASSWORD"] = creds["password"]

    confirmation = input(
        f"Restore '{backup_file}' into database '{creds['dbname']}'? Type RESTORE: "
    )
    if confirmation != "RESTORE":
        print("Restore cancelled.")
        return

    try:
        subprocess.run(restore_command, check=True, env=process_env)
        print("Database restoration completed successfully.")
    except subprocess.CalledProcessError as exc:
        print(f"Restoration failed: {exc}")
    except FileNotFoundError as exc:
        print(exc)


if __name__ == "__main__":
    restore_backup()
