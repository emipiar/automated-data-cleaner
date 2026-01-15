import sqlite3
import logging
from src.database import get_connection
from src.config import REPORT_FILE



def generate_report(table_name="clean_data"):
    logging.info(f"Generating report for table: {table_name}")
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


def save_report(report, path=REPORT_FILE):
    logging.info(f"Saving report to {path}")
    with open(path, "w") as f:
        f.write(report)
    logging.info("Report saved successfully")
