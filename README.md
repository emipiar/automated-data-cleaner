# 🧹 Automated Data Cleaner
CLI tool to clean and analyze CSV data using Python and SQLite

Automated Data Cleaner is a **Python CLI tool** designed to automatically load, clean, store, and report on CSV datasets.
It provides a simple command-line interface with flexible flags to control each step of the data processing pipeline.

This project was built with **modularity, clarity, and best practices** in mind, making it suitable as a learning project or a portfolio piece.

---

## 🚀 Features

* Load CSV files into Pandas DataFrames
* Automatically clean data (nulls, duplicates, basic normalization)
* Save cleaned data into a SQLite database
* Generate summary reports from the database
* Fully configurable via CLI flags
* Centralized logging system

---

## 📁 Project Structure

automated-data-cleaner/
│
├── src/
│   ├── cli.py          # Command-line interface
│   ├── loader.py       # CSV loading logic
│   ├── cleaner.py      # Data cleaning logic
│   ├── database.py     # SQLite database handling
│   ├── report.py       # Report generation
│   ├── logger.py       # Logging configuration
│
├── data/
│   ├── raw/            # Raw input CSV files
│   └── processed/      # Generated SQLite database
│
├── reports/            # Generated reports
├── tests/              # Unit tests
├── pytest.ini
└── README.md

---

## 🛠 Requirements

* Python **3.10+**
* pip

### Python Dependencies

pip install pandas

(Standard library modules used: `argparse`, `logging`, `sqlite3`)

---

## ▶️ Usage

All commands must be executed from the **project root directory**.

### 1️⃣ Full pipeline (load → clean → save → report)

```
python -m src.cli --input data/raw/example.csv
```

---

### 2️⃣ Skip data cleaning

```
python -m src.cli --input data/raw/example.csv --no-clean
```

---

### 3️⃣ Skip database export

```
python -m src.cli --input data/raw/example.csv --no-db
```

---

### 4️⃣ Skip report generation

```
python -m src.cli --input data/raw/example.csv --no-report
```

---

### 5️⃣ Generate report from existing database only

```
python -m src.cli --report-only
```

---

### 6️⃣ View help

```
python -m src.cli --help
```

---

## 📊 Output

* **SQLite database:**

  * `data/processed/clean_data.db`
* **Report file:**

  * `reports/summary.txt`

---

## 🧪 Testing

Run unit tests using:

```
pytest
```

---

## 🧠 Design Notes

* Each responsibility is isolated into its own module
* CLI logic is separated from business logic
* Logging provides traceability for every major step
* SQLite was chosen for simplicity and portability

---

## 📌 Project Status

✅ Version **1.0** — Complete and functional

Future improvements may include:

* Advanced data validation rules
* Multiple output formats (CSV, JSON)
* Configuration via `.env` file
* Packaging as an installable CLI tool

---

## 👤 Author

**Erika Ipia**
Data & Software Engineering Enthusiast

---

⭐ If you find this project useful, feel free to star the repository!
