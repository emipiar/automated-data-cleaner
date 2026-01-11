import argparse
import logging
from src.loader import load_csv
from src.cleaner import clean_data
from src.logger import setup_logger
from src.database import save_to_sqlite
from src.report import generate_report, save_report


def main():
    setup_logger()
    logging.info("CLI started")

    parser = argparse.ArgumentParser(
        description="Automated Data Cleaner CLI"
    )

    parser.add_argument("--input", help="Path to input CSV file")
    parser.add_argument("--no-clean", action="store_true", help="Skip data cleaning")
    parser.add_argument("--no-db", action="store_true", help="Skip saving cleaned data to SQLite")
    parser.add_argument("--no-report", action="store_true", help="Skip report generation")
    parser.add_argument("--report-only", action="store_true", help="Generate report using existing database")

    args = parser.parse_args()

    # 🔹 Report-only mode
    if args.report_only:
        logging.info("Generating report from existing database")
        report = generate_report()
        save_report(report)
        logging.info("Report generated from database")
        return

    # 🔹 Normal flow requires input
    if not args.input:
        logging.error("Input CSV file is required unless --report-only is used")
        return

    df = load_csv(args.input)
    logging.info(f"CSV loaded from {args.input}")

    if not args.no_clean:
        df = clean_data(df)
        logging.info("Data cleaning applied")
    else:
        logging.info("Data cleaning skipped")

    if not args.no_db:
        save_to_sqlite(df)
        logging.info("Data saved to SQLite database")
    else:
        logging.info("Database export skipped")

    if not args.no_report:
        report = generate_report()
        save_report(report)
        logging.info("Report generated successfully")
    else:
        logging.info("Report generation skipped")

    
    logging.info("Processing completed successfully")
if __name__ == "__main__":
    main()
