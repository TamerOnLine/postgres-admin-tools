import sys
import os
from sqlalchemy import create_engine, MetaData

# Add models directory to import paths
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db_postgres.db_config import get_database_credentials

def drop_tables():
    """
    Drops specific or all tables in a PostgreSQL database based on user input.

    Prompts the user to select a table to drop or to drop all tables. Uses SQLAlchemy
    to reflect the database schema and delete selected tables.

    Raises:
        Exception: If any error occurs during table deletion.
    """
    creds = get_database_credentials()
    url = (
        f"postgresql://{creds['user']}:{creds['password']}@{creds['host']}:{creds['port']}/{creds['dbname']}"
    )
    engine = create_engine(url)
    metadata = MetaData()
    metadata.reflect(bind=engine)

    tables = list(metadata.tables.keys())
    print("Current Tables:")
    print("0) Delete all tables")
    for i, table_name in enumerate(tables, start=1):
        print(f"{i}) {table_name}")

    choice = input("Enter the number of the table you want to delete (or 0 to delete all): ").strip()

    try:
        choice = int(choice)
        if choice == 0:
            confirm = input("Are you sure you want to delete ALL tables? (y/n): ")
            if confirm.lower() == 'y':
                metadata.drop_all(bind=engine)
                print("All tables have been deleted.")
            else:
                print("Operation cancelled.")
        elif 1 <= choice <= len(tables):
            table_name = tables[choice - 1]
            metadata.tables[table_name].drop(engine)
            print(f"Table '{table_name}' has been deleted.")
        else:
            print("Invalid choice.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    drop_tables()
