import argparse
import os
"""
Estos los tengo aquí para recordar que antes de crear el paquete _init_.py, llamaba los módulos así:
from loader import load_csv
from cleaner import clean_data
"""
from src.database import save_to_sqlite
from src.cleaner import clean_data
from src.loader import load_csv


def main():
    parser = argparse.ArgumentParser(
        description="CLI tool to analyze and clean CSV files"
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to the input CSV file"
    )

    args = parser.parse_args()
    input_path = args.input

    if not os.path.exists(input_path):
        print(f"❌ File not found: {input_path}")
        return

    print(f"📂 Loading file: {input_path}")

    df = load_csv(input_path)

    #Basic info
    print("✅ File loaded successfully")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")
    print("\nPreview:")
    print(df.head())

    #Quality data
    print("\n📊 Data Quality Report")

    null_counts = df.isnull().sum()
    total_nulls = null_counts.sum()

    print(f"Total missing values: {total_nulls}")

    duplicate_rows = df.duplicated().sum()
    print(f"Duplicate rows: {duplicate_rows}")

    #Clean data
    print("\n🧹 Cleaning data...")

    cleaned_df = clean_data(df)

    print("✅ Data cleaned")
    print(f"Rows after cleaning: {cleaned_df.shape[0]}")

    #BD
    save_to_sqlite(cleaned_df)
    print("Data saved to SQLite database successfully")



if __name__ == "__main__":
    main()
