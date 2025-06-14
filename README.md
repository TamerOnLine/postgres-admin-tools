# 🛠️ PostgreSQL Admin Tools

![Build Status](https://github.com/TamerOnLine/postgres-admin-tools/actions/workflows/python-app.yml/badge.svg)

A lightweight admin interface and CLI toolkit for PostgreSQL, built with **Flask**, **SQLAlchemy**, and **psycopg2**.

> Manage your databases and tables with ease – via web or terminal.

---

## 📦 Features

- 🔐 Secure user system with Flask-Login (default admin: `admin/12345`)
- ⚙️ Create or drop PostgreSQL databases
- 🧱 Manage tables (create / migrate / drop) via SQLAlchemy
- 💾 Full database backup & restore using `pg_dump` / `psql`
- 🧩 Easy environment config via `.env` file
- 🌐 Flask-based web UI ready out of the box

---

## 🔧 Tech Stack

| Technology     | Description                         |
|----------------|-------------------------------------|
| Python         | Core programming language           |
| PostgreSQL     | Relational database engine          |
| SQLAlchemy     | ORM for database modeling           |
| psycopg2       | PostgreSQL driver for Python        |
| python-dotenv  | Load `.env` variables into runtime  |

---

## 🧱 Project Structure

```
postgres-admin-tools/
├── myapp.py                  # Flask app with login & DB panel
├── requirements.txt
├── LICENSE
├── README.md
└── models/
    ├── models_definitions.py # SQLAlchemy models
    └── db_postgres/
        ├── create.py         # Create DB if not exists
        ├── drop.py           # Drop DB (safe disconnect)
        ├── drop_table.py     # Drop individual/all tables
        ├── manage_tables.py  # Schema updates
        ├── BACKUP.py         # Backup to SQL file
        ├── RESTORE.py        # Restore from backup
        └── db_config.py      # Load from .env
```

---

## ⚙️ Environment Setup

Create a `.env` file in the root directory:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/your_db
SECRET_KEY=your_secret_here
```

---

## 🚀 Quick Start

### 1. Create Virtual Environment

```bash
# Windows
py -3.12 -m venv venv
.env\Scriptsctivate
```

```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

![venv](screenshots/venv.png)  
<sub>📸 Virtual environment activated successfully</sub>

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Create Database

```bash
py models/db_postgres/create.py
```

![Create](screenshots/create.png)  
<sub>📸 Creating PostgreSQL database</sub>

---

### 4. Drop Database

```bash
py models/db_postgres/drop.py
```

![Drop](screenshots/drop.png)  
<sub>📸 Dropping the database safely</sub>

---

### 5. Drop Tables

```bash
py models/db_postgres/drop_table.py
```

![Drop Table](screenshots/drop_table.png)  
<sub>📸 Dropping selected or all tables</sub>

---

### 6. Manage Tables

```bash
py models/db_postgres/manage_tables.py
```

![Manage Tables](screenshots/manage_tables.png)  
<sub>📸 CLI interface to manage tables (create or sync)</sub>

---

### 7. Backup Database

```bash
py models/db_postgres/BACKUP.py
```

![Manage Tables](screenshots/BACKUP.png)  
<sub>📸 Generating SQL backup file using `pg_dump`</sub>

---

### 8. Restore Database

```bash
py models/db_postgres/RESTORE.py
```

![Manage Tables](screenshots/RESTORE.png)  
<sub>📸 Restoring database from SQL file</sub>

---

## 🛡️ User System

The system auto-creates a default admin user on first run if not found:

- **Username**: `admin`
- **Password**: `12345`

You can modify this in `models/models_definitions.py`.

---

## 🧪 SQLite Test Mode

If `DATABASE_URL` is not set in the `.env`, the system defaults to SQLite (`sqlite:///test.db`) for quick testing.

> Note: Scripts like `create.py`, `BACKUP.py`, etc., require PostgreSQL and do not support SQLite.

---

## 📋 CLI Command Summary

| Operation             | Script              | Mode            |
|----------------------|---------------------|-----------------|
| 🏗️ Create Database     | `create.py`          | CLI             |
| ❌ Drop Database       | `drop.py`            | CLI             |
| 🧹 Drop Tables         | `drop_table.py`      | Interactive CLI |
| 🧩 Manage Tables       | `manage_tables.py`   | Interactive CLI |
| 💾 Backup Database     | `BACKUP.py`          | CLI             |
| ♻️ Restore from Backup | `RESTORE.py`         | Interactive CLI |

---

## 📄 License

This project is licensed under the MIT License.  
See the [LICENSE](./LICENSE) file for details.

---

## 👨‍💻 Author

**Tamer Hamad Faour**  
GitHub: [@TamerOnLine](https://github.com/TamerOnLine)

---