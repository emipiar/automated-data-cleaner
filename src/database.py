import sqlite3
import os

DB_PATH = "data/processed/clean_data.db"


def get_connection():
    os.makedirs("data/processed", exist_ok=True)
    return sqlite3.connect(DB_PATH)


def save_to_sqlite(df, table_name="clean_data"):
    conn = get_connection()
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
"""
Explication:
📌 Lo que hace:
Crea la carpeta si no existe
Crea la base de datos automáticamente
Guarda el DataFrame como tabla SQL
"""