# 🛠️ PostgreSQL Admin Tools

![Build Status](https://github.com/TamerOnLine/postgres-admin-tools/actions/workflows/python-app.yml/badge.svg)

A lightweight admin interface and CLI toolkit for PostgreSQL, built with **Flask**, **SQLAlchemy**, and **psycopg2**.

> Manage your databases and tables with ease – via web or terminal.

---

## 📥 Clone the Repository
To get started, clone this repository to your local machine using Git:

```bash
git clone https://github.com/TamerOnLine/postgres-admin-tools.git
cd postgres-admin-tools
```
- Make sure you have Git installed.
- [You can download it from](https://git-scm.com).
<div align="center">
  <img src="screenshots/github.png" alt="models definitions" width="600"/>
</div>
<sub>📸 Cloning the repository via Git command line </sub>

---

## 📦 Features

- 🔐 Secure user system with Flask-Login (default admin: `admin/12345`)
- ⚙️ Create or drop PostgreSQL databases
- 🧱 Manage tables (create / migrate / drop) via SQLAlchemy
- 💾 Full database backup & restore using `pg_dump` / `psql`
- 🧩 Easy environment config via `.env` file
- 🌐 Flask-based web UI ready out of the box

---

## 🎬 Demo


<div align="center">
  <img src="screenshots/demo.gif" alt="PostgreSQL Admin Tools demo" width="600"/>
</div>
<sub>📽️ Quick demo of the PostgreSQL Admin Tools in action</sub>


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
.\env\Scripts\Activate
```
<div align="center">
  <img src="screenshots/venv.png" alt="models definitions" width="600"/>
</div>
<sub>📸 Virtual environment activated successfully</sub>

---

```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```
<div align="center">
  <img src="screenshots/pip_install.png" alt="models definitions" width="600"/>
</div>
<sub>📸 Installing dependencies using pip </sub>

---

### Create Database

```bash
py .\models\db_postgres\create.py
```
<div align="center">
  <img src="screenshots/create.png" alt="models definitions" width="600"/>
</div> 
<sub>📸 Creating PostgreSQL database</sub>

---

### Drop Database

```bash
py .\models\db_postgres\drop.py
```
<div align="center">
  <img src="screenshots/drop.png" alt="models definitions" width="600"/>
</div>
<sub>📸 Dropping the database safely</sub>

---

### Drop Tables

```bash
py .\models\db_postgres\drop_table.py
```
<div align="center">
  <img src="screenshots/drop_table.png" alt="models definitions" width="600"/>
</div>
<sub>📸 Dropping selected or all tables</sub>

---

### Manage Tables

```bash
py .\models\db_postgres\manage_tables.py
```
<div align="center">
  <img src="screenshots/manage_tables.png" alt="models definitions" width="600"/>
</div>
<sub>📸 CLI interface to manage tables (create or sync)</sub>

---

### Backup Database

```bash
py .\models\db_postgres\BACKUP.py
```
<div align="center">
  <img src="screenshots/BACKUP.png" alt="models definitions" width="600"/>
</div>
<sub>📸 Generating SQL backup file using `pg_dump`</sub>

---

### Restore Database

```bash
py .\models\db_postgres\RESTORE.py
```
<div align="center">
  <img src="screenshots/RESTORE.png" alt="models definitions" width="600"/>
</div>
<sub>📸 Restoring database from SQL file</sub>

---

## 🛡️ User System

The system automatically creates a **default admin user** on first run if no user with username `admin` is found.
- **Username**: `admin`  
- **Password**: `12345`

To manually trigger this, run the following command:

```bash
py .\models\models_definitions.py
```
You can modify this logic in [`models/models_definitions.py`](models/models_definitions.py).
<div align="center">
  <img src="screenshots/models_definitions.png" alt="models definitions" width="600"/>
</div> 
<sub>📸 Creating default admin user if not exists</sub>

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