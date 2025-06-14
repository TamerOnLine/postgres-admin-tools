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
git clone https://github.com/TamerOnLine/postgres-admin-tools.git
cd postgres-admin-tools
pip install -r requirements.txt
```

Create a `.env` file with the following content:

```
DATABASE_URL=postgresql://username:password@localhost:5432/dbname
```

---



## ⚙️ Configuration

The tool reads the PostgreSQL connection string from a `.env` file via the `DATABASE_URL` variable.

---

## 📂 Project Structure

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

## 📝 License

This project is licensed under the MIT License.  
See the [LICENSE](./LICENSE) file for details.

---

## 👨‍💻 Author

**Tamer Hamad Faour**  
GitHub: [@TamerOnLine](https://github.com/TamerOnLine)
