from pathlib import Path

# Base paths
BASE_DIR = Path(__file__).resolve().parent.parent

# Database
DB_PATH = BASE_DIR / "data" / "processed" / "clean_data.db"
CLEAN_TABLE = "clean_data"
METADATA_TABLE = "metadata"

# Reports
REPORTS_DIR = BASE_DIR / "reports"
REPORT_FILE = REPORTS_DIR / "summary.txt"

# Logging
LOG_LEVEL = "INFO"
