# 💼 PostgreSQL Database Manager

A Python-based utility for managing PostgreSQL databases. This tool offers operations to create, drop, and manage tables as well as handle database connections using environment configurations.

---

## 🎯 Features

* Create a PostgreSQL database if it doesn't exist.
* Drop an existing database (including terminating active connections).
* Drop specific tables or all tables in the database.
* Manage tables: either recreate all or create only the missing ones.
* Uses `DATABASE_URL` environment variable for connection configuration.

---

## 🛠️ Tech Stack

* Python
* PostgreSQL
* SQLAlchemy
* psycopg2
* python-dotenv

---

## 🛆 Installation

```bash
git clone https://your-repo-url
cd your-repo-directory
pip install -r requirements.txt
```

Create a `.env` file with the following content:

```
DATABASE_URL=postgresql://username:password@localhost:5432/dbname
```

---

## 🚀 Usage

### Create Database

```bash
python db_postgres/create.py
```

### Drop Database

```bash
python db_postgres/drop.py
```

### Drop Tables

```bash
python db_postgres/drop_table.py
```

### Manage Tables

```bash
python db_postgres/manage_tables.py
```

---

## ⚙️ Configuration

The tool reads the PostgreSQL connection string from a `.env` file via the `DATABASE_URL` variable.

---

## 📂 Project Structure

```
.
├── models.txt
├── models_definitions.py
├── README.md
├── __init__.py
└── db_postgres/
    ├── create.py
    ├── db_config.py
    ├── drop.py
    ├── drop_table.py
    ├── manage_tables.py
    └── __init__.py
```

---

## 🧾 License

MIT License

---

## 👨‍💼 Author

* **Your Name** - \[[your.email@example.com](mailto:your.email@example.com) or GitHub profile]
