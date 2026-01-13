import sqlite3
import logging
import os

DB_PATH = "data/processed/clean_data.db"


def get_connection():
    os.makedirs("data/processed", exist_ok=True)
    return sqlite3.connect(DB_PATH)


def save_to_sqlite(df, table_name="clean_data"):
    logging.info(f"Saving DataFrame to SQLite database at {DB_PATH}, table: {table_name}")
    conn = get_connection()
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
    logging.info("DataFrame saved successfully")
"""
Explication:
📌 Lo que hace:
Crea la carpeta si no existe
Crea la base de datos automáticamente
Guarda el DataFrame como tabla SQL
"""
def save_metadata(metadata, table_name="metadata"):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            key TEXT PRIMARY KEY,
            value TEXT
        )
    """)

    for key, value in metadata.items():
        cursor.execute(
            f"INSERT OR REPLACE INTO {table_name} (key, value) VALUES (?, ?)",
            (key, str(value))
        )

    conn.commit()
    conn.close()
    logging.info("Metadata saved successfully")