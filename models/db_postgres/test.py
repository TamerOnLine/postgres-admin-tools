from sqlalchemy import create_engine, text

url = "postgresql://postgres:12345@localhost:5432/tamer"
engine = create_engine(url)

with engine.connect() as conn:
    result = conn.execute(text("SELECT tablename FROM pg_tables WHERE schemaname='public';"))
    for row in result:
        print(row)
