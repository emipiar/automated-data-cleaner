import sqlite3
from src.database import get_connection


def generate_report(table_name="clean_data"):
    conn = get_connection()
    cursor = conn.cursor()

    # Total rows
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    total_rows = cursor.fetchone()[0]

    # Total columns
    cursor.execute(f"PRAGMA table_info({table_name})")
    total_columns = len(cursor.fetchall())

    report = f"""
Report Summary
--------------
Total rows: {total_rows}
Total columns: {total_columns}
"""

    conn.close()
    return report


def save_report(report, path="reports/summary.txt"):
    with open(path, "w") as f:
        f.write(report)
