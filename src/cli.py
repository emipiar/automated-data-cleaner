import argparse
import logging
from src.loader import load_csv
from src.cleaner import clean_data
from src.logger import setup_logger
from src.database import save_to_sqlite
from src.report import generate_report, save_report


def main():
    # 1️⃣ Crear parser
    parser = argparse.ArgumentParser(
        description="Automated Data Cleaner CLI"
    )

    # 2️⃣ Argumentos (AQUÍ VAN LOS FLAGS)
    parser.add_argument(
        "--input",
        required=False,
        help="Path to input CSV file"
    )

    parser.add_argument(
        "--no-db",
        action="store_true",
        help="Skip saving cleaned data to SQLite"
    )

    parser.add_argument(
        "--no-report",
        action="store_true",
        help="Skip report generation"
    )

    parser.add_argument(
        "--report-only",
        action="store_true",
        help="Generate report using existing database"
    )

    # 3️⃣ Parsear argumentos
    args = parser.parse_args()

    # 4️⃣ LÓGICA DEL PROGRAMA (NO ES ARGPARSE)
    if args.report_only:
        report = generate_report()
        save_report(report)
        print("Report generated from existing database")
        return

    if not args.input:
        raise ValueError("Input CSV file is required unless --report-only is used")

    df = load_csv(args.input)
    cleaned_df = clean_data(df)

    if not args.no_db:
        save_to_sqlite(cleaned_df)
        print("Data saved to SQLite database")

    if not args.no_report:
        report = generate_report()
        save_report(report)
        print("Report generated successfully")
    
    print("Processing completed successfully")



if __name__ == "__main__":
    main()
