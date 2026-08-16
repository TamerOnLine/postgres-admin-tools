# PostgreSQL Admin Tools

A Python toolkit for PostgreSQL administration with database creation, deletion, schema management, backup, and restore utilities. The repository also contains a minimal Flask application foundation built with Flask-SQLAlchemy and Flask-Login.

> [!IMPORTANT]
> This is a development and reference project, not a production-ready administration panel. Authentication routes and authorization controls are not yet implemented. Do not expose the Flask application to the public internet.

## Features

- Validated PostgreSQL configuration through environment variables
- Database creation with safely quoted identifiers
- Explicitly confirmed database deletion
- SQL backup with `pg_dump`
- Confirmed restore with `psql`
- Table creation, synchronization, and deletion utilities
- SQLAlchemy user model with password hashing
- Flask application factory
- GitHub Actions workflow

## Security changes

The project intentionally has:

- no default administrator account
- no hardcoded administrator password
- no fallback Flask secret key
- no fallback database username or password
- Debug mode disabled unless explicitly enabled
- database credentials scoped to backup and restore subprocesses
- stronger confirmation for destructive operations

## Requirements

- Python 3.10+
- PostgreSQL client tools
- `pg_dump` and `psql` available on PATH, or installed in a supported Windows PostgreSQL location

## Setup

### 1. Clone the repository

~~~bash
git clone https://github.com/TamerOnLine/postgres-admin-tools.git
cd postgres-admin-tools
~~~

### 2. Create a virtual environment

~~~bash
python -m venv .venv
~~~

Activate it:

~~~bash
# Linux or macOS
source .venv/bin/activate

# Windows PowerShell
.\.venv\Scripts\Activate.ps1
~~~

### 3. Install dependencies

~~~bash
pip install -r requirements.txt
~~~

### 4. Configure the environment

~~~bash
cp .env.example .env
~~~

Replace every placeholder in `.env`. Never commit the resulting `.env` file.

You may configure PostgreSQL with one complete URL:

~~~env
DATABASE_URL=postgresql://user:password@localhost:5432/database_name
~~~

Or with individual variables:

~~~env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=database_name
DB_USER=database_user
DB_PASSWORD=use-a-strong-password
~~~

Generate a Flask secret:

~~~bash
python -c "import secrets; print(secrets.token_hex(32))"
~~~

Store the result as `SECRET_KEY` in `.env`.

## Usage

### Create the configured database

~~~bash
python models/db_postgres/create.py
~~~

### Manage tables

~~~bash
python models/db_postgres/manage_tables.py
~~~

### Back up the database

~~~bash
python models/db_postgres/BACKUP.py
~~~

Backups are stored in the ignored local `backups/` directory.

### Restore a backup

~~~bash
python models/db_postgres/RESTORE.py
~~~

The command requires typing `RESTORE` before applying the selected SQL file.

### Delete the configured database

~~~bash
python models/db_postgres/drop.py
~~~

The command requires typing the exact configured database name before deletion.

### Run the Flask foundation

~~~bash
python myapp.py
~~~

This creates the database tables and starts the minimal application. It does not provide a completed login or administration interface.

## Project structure

~~~text
postgres-admin-tools/
├── .env.example
├── .github/workflows/
├── models/
│   ├── models_definitions.py
│   └── db_postgres/
│       ├── BACKUP.py
│       ├── RESTORE.py
│       ├── create.py
│       ├── db_config.py
│       ├── drop.py
│       ├── drop_table.py
│       └── manage_tables.py
├── myapp.py
├── requirements.txt
└── README.md
~~~

## Production readiness

Before production use, add and test:

- login, logout, and administrator provisioning workflows
- route-level authorization
- CSRF protection for web forms
- secure session-cookie settings
- dependency version locking and automated security updates
- automated tests for destructive database operations
- structured audit logging
- deployment behind TLS and a production WSGI server

## License

Released under the MIT License. See [LICENSE](LICENSE).
