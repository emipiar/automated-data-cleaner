import subprocess
import sys
from pathlib import Path
from tests.utils import run_cli
from pathlib import Path
from src.database import DB_PATH




def run_cli(args):
    return subprocess.run(
        [sys.executable, "-m", "src.cli"] + args,
        capture_output=True,
        text=True
    )

def test_missing_input_file():
    result = run_cli(["--input", "data/raw/no_file.csv"])
    assert result.returncode != 0
    assert "does not exist" in result.stderr.lower() or result.stdout.lower()

def test_report_only_without_db():
    #for delete it = db_path = Path("clean_data.db")
    db_path = Path(DB_PATH)


    # Asegurar entorno limpio
    if db_path.exists():
        db_path.unlink()

    result = run_cli(["--report-only"])

    assert result.returncode != 0
    assert "database" in result.stderr.lower() or "no such table" in result.stderr.lower()
"""
Archivo de pruebas para errores comunes en la CLI
"""