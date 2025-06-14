
# 🛠️ PostgreSQL Admin Tools

![Build Status](https://github.com/TamerOnLine/postgres-admin-tools/actions/workflows/python-app.yml/badge.svg)


A lightweight Python-based admin panel and command-line toolkit for managing PostgreSQL databases and tables using **Flask**, **SQLAlchemy**, and **psycopg2**.

---

## 📦 Features

- 🔐 User management with Flask-Login
- ⚙️ Create or drop PostgreSQL databases
- 🧱 Create all or missing tables from SQLAlchemy models
- 🧹 Drop specific or all tables interactively
- 💾 Backup and restore databases via `pg_dump` and `psql`
- 🧩 Environment-based configuration using `.env`
- 🌐 Ready for web interface with Flask

---

## 📁 Project Structure

```
tameronline-postgres-admin-tools/
├── myapp.py                  # Flask app with login & DB integration
├── requirements.txt
├── LICENSE
├── README.md
└── models/
    ├── models_definitions.py # SQLAlchemy models (User, etc.)
    ├── db_postgres/
    │   ├── create.py         # Create DB if not exists
    │   ├── drop.py           # Drop DB after terminating connections
    │   ├── drop_table.py     # Drop individual or all tables
    │   ├── manage_tables.py  # CLI to recreate or patch schema
    │   ├── BACKUP.py         # Dump DB to timestamped SQL file
    │   ├── RESTORE.py        # Restore DB from backup
    │   └── db_config.py      # Environment-based DB config
```

---

## ⚙️ Environment Setup

Create a `.env` file in the root directory:

```env
DATABASE_URL=postgresql://your_user:your_password@localhost:5432/your_db
SECRET_KEY=your_secret_here
```

---


## 🚀 Usage

### 1. تهيئة البيئة الافتراضية
```bash
py -3.12 -m venv venv
```

![venv](images/venv.png)

### 1. Create Database

```bash
python models/db_postgres/create.py
```
![Create](images/create.png)

### 2. Drop Database

```bash
python models/db_postgres/drop.py
```
![Drop](images/drop.png)

### 3. Drop Tables

```bash
python models/db_postgres/drop_table.py
```
![Drop Table](images/drop_table.png)

### 4. Manage Tables

```bash
python models/db_postgres/manage_tables.py
```
![Manage Tables](images/manage_tables.png)





### 6. إعداد ملف البيئة
![Env Setup](images/env-setup.png)

### 7. النسخ الاحتياطي لقاعدة البيانات
![Backup](images/BACKUP.png)


### 8. استعادة قاعدة البيانات
![Restore](images/RESTORE.png)

---






## 🛡️ User System

An admin user will be created automatically if it doesn't exist:

- **Username**: `admin`
- **Password**: `12345`

You can change this behavior in `models/models_definitions.py`.

---

## 🧰 Database Tools

| Operation                  | Script         | Mode            |
|---------------------------|----------------|-----------------|
| 🏗️ Create Database         | `create.py`     | CLI             |
| 🧨 Drop Database           | `drop.py`       | CLI             |
| 🧹 Drop Tables             | `drop_table.py` | Interactive CLI |
| 🧩 Manage Tables (CLI)     | `manage_tables.py` | Interactive CLI |
| 💾 Backup Database         | `BACKUP.py`     | CLI             |
| ♻️ Restore from Backup     | `RESTORE.py`    | Interactive CLI |


---


---


## 🧪 Test Mode (SQLite)

When running `models_definitions.py` directly, if `DATABASE_URL` is not defined,
the system falls back to SQLite (`sqlite:///test.db`) for quick testing.

> Note: Other scripts (like `create.py`) require a PostgreSQL connection and do not support SQLite.


---

## 📝 License

This project is licensed under the MIT License.  
See the [LICENSE](./LICENSE) file for details.

---

## 👨‍💻 Author

**Tamer Hamad Faour**  
GitHub: [@TamerOnLine](https://github.com/TamerOnLine)
