import os
import subprocess
from db_config import get_database_credentials

# Common psql paths for Windows systems
PSQL_PATHS = [
    r"C:\\Program Files\\PostgreSQL\\17\\bin\\psql.exe",
    r"C:\\Program Files\\PostgreSQL\\15\\bin\\psql.exe",
    r"C:\\Program Files\\PostgreSQL\\14\\bin\\psql.exe",
    "psql"  # Fallback if psql is in the system PATH
]

def find_psql():
    """
    Search for the psql executable in common installation paths.

    Returns:
        str: Path to the psql executable.

    Raises:
        FileNotFoundError: If no valid psql executable is found.
    """
    for path in PSQL_PATHS:
        if os.path.exists(path):
            return path
    raise FileNotFoundError("psql executable was not found in the expected locations.")


def choose_backup_file(folder="./backups"):
    """
    Prompt the user to select a backup file from a specified folder.

    Args:
        folder (str): Path to the folder containing backup files.

    Returns:
        str: Full path to the selected backup file.

    Raises:
        FileNotFoundError: If no .sql backup files are found in the folder.
    """
    files = [f for f in os.listdir(folder) if f.endswith(".sql")]
    if not files:
        raise FileNotFoundError("No backup files found in the specified folder.")

    print("Available backup files:")
    for idx, file in enumerate(files):
        print(f"{idx + 1}. {file}")

    while True:
        try:
            choice = int(input("Enter the number of the backup file to restore: "))
            if 1 <= choice <= len(files):
                return os.path.join(folder, files[choice - 1])
            else:
                print("Invalid selection. Please choose a valid number.")
        except ValueError:
            print("Input must be a valid integer.")


def restore_backup():
    """
    Restore a PostgreSQL database from a selected backup file using psql.
    """
    creds = get_database_credentials()
    psql_path = find_psql()
    backup_folder = "./backups"
    backup_file = choose_backup_file(backup_folder)

    os.environ["PGPASSWORD"] = creds["password"]

    restore_command = [
        psql_path,
        "-h", creds["host"],
        "-p", creds["port"],
        "-U", creds["user"],
        "-d", creds["dbname"],
        "-f", backup_file
    ]

    try:
        print(f"Restoring from backup file: {backup_file}")
        subprocess.run(restore_command, check=True)
        print("Database restoration completed successfully.")
    except subprocess.CalledProcessError as e:
        print("Restoration failed with a subprocess error:")
        print(e)
    except FileNotFoundError as e:
        print(e)


if __name__ == "__main__":
    restore_backup()
