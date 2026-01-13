import argparse
import logging
import sys
import os
from src.loader import load_csv
from src.cleaner import clean_data
from src.logger import setup_logger
from src.database import save_metadata
from src.database import save_to_sqlite
from src.report import generate_report, save_report
from pathlib import Path
from src.database import DB_PATH



def main():
    setup_logger()
    logging.info("CLI started")

    try:
        parser = argparse.ArgumentParser(
            description="Automated Data Cleaner CLI"
        )

        parser.add_argument("--input", help="Path to input CSV file")
        parser.add_argument("--no-clean", action="store_true", help="Skip data cleaning")
        parser.add_argument("--no-db", action="store_true", help="Skip saving cleaned data to SQLite")
        parser.add_argument("--no-report", action="store_true", help="Skip report generation")
        parser.add_argument("--report-only", action="store_true", help="Generate report using existing database")

        args = parser.parse_args()

        if args.report_only:
            logging.info("Generating report from existing database")

            if not Path(DB_PATH).exists():
                logging.error("Database not found. Cannot generate report.")
                raise SystemExit(1)
            
            report = generate_report()
            save_report(report)
            logging.info("Report generated from database")
            return


        if not args.input:
            logging.error("Input CSV file is required unless --report-only is used")
            sys.exit(1)

        # Input validation
        if not os.path.exists(args.input):
            logging.error(f"Input file does not exist: {args.input}")
            sys.exit(1)

        if not os.path.isfile(args.input):
            logging.error(f"Input path is not a file: {args.input}")
            sys.exit(1)

        if not args.input.lower().endswith(".csv"):
            logging.error("Input file must be a CSV")
            sys.exit(1)

        if os.path.getsize(args.input) == 0:
            logging.error("Input CSV file is empty")
            sys.exit(1)
        
        ### Load CSV   
        df = load_csv(args.input)
        logging.info(f"CSV loaded from {args.input}")

        original_rows = len(df)
        
        if not args.no_clean:
            df = clean_data(df)
            logging.info("Data cleaning applied")
        else:
            logging.info("Data cleaning skipped")

        cleaned_rows = len(df)

        metadata = {
            "original_rows": original_rows,
            "cleaned_rows": cleaned_rows,
            "rows_removed": original_rows - cleaned_rows,
            "removal_percentage": round(
                (original_rows - cleaned_rows) / original_rows * 100, 2
            ) if original_rows > 0 else 0
        }

        if not args.no_db:
            save_to_sqlite(df)
            save_metadata(metadata)
            logging.info("Data and metadata saved to SQLite database")
        else:
            logging.info("Database export skipped")

        ######
        db_path = "data/processed/clean_data.db"
        ######
        if not os.path.exists(db_path):
            logging.error("Database not found. Run the tool without --report-only first.")
            sys.exit(1)

        if not args.no_report:
            report = generate_report()
            save_report(report)
            logging.info("Report generated successfully")
        else:
            logging.info("Report generation skipped")

        logging.info("Processing completed successfully")

    except Exception as e:
        logging.error(f"Fatal error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
