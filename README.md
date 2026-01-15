# Automated Data Cleaner & Analyzer

A Python-based Command Line Interface (CLI) tool designed to automate the cleaning, analysis, and reporting of CSV datasets. The project demonstrates practical use of Python, Pandas, SQLite, logging, testing, and clean architecture principles.

---

## 🚀 Features

* Load CSV files from the command line
* Clean data automatically (handle nulls and duplicates)
* Save cleaned data into a SQLite database
* Store metadata about each execution
* Generate summary reports from the database
* Flexible CLI flags to control execution flow
* Structured logging for traceability
* Unit tests with pytest
* Centralized configuration for easy maintenance

---

## 📁 Project Structure

```
automated-data-cleaner/
├── src/
│   ├── cli.py          # CLI entry point and orchestration logic
│   ├── loader.py       # CSV loading logic
│   ├── cleaner.py      # Data cleaning logic
│   ├── database.py     # SQLite persistence and metadata handling
│   ├── report.py       # Report generation
│   ├── logger.py       # Logging configuration
│   ├── config.py       # Centralized configuration
│
├── data/
│   ├── raw/            # Input CSV files
│   └── processed/      # SQLite database output
│
├── reports/            # Generated reports
├── tests/              # Unit tests (pytest)
├── README.md
└── requirements.txt
```

---

## ⚙️ Configuration

All configurable values (paths, database names, table names, report locations, logging level) are centralized in:

```
src/config.py
```

This design makes the project easy to maintain, portable across operating systems, and extensible for future improvements.

---

## 🖥️ Usage

Run all commands from the **root of the project**.

### 1️⃣ Clean CSV, save to database, and generate report

```
python -m src.cli --input data/raw/example.csv
```

### 2️⃣ Skip saving to database

```
python -m src.cli --input data/raw/example.csv --no-db
```

### 3️⃣ Skip report generation

```
python -m src.cli --input data/raw/example.csv --no-report
```

### 4️⃣ Generate report only (from existing database)

```
python -m src.cli --report-only
```

### 5️⃣ View all available flags

```
python -m src.cli --help
```

---

## 🧪 Testing

Run the test suite with:

```
pytest
```

All core components (CLI behavior, loader, cleaner) are covered by unit tests.

---

## 🧠 Design Philosophy

* **Separation of concerns**: Each module has a single responsibility
* **CLI as orchestrator**: The CLI decides *what* runs, modules decide *how*
* **Configuration over hardcoding**: Centralized settings via `config.py`
* **Observability**: Logging is treated as a first-class feature
* **Testability**: Logic is designed to be testable and verifiable

---

## 🎯 Project Status

✅ Functional and complete

This project was intentionally scoped to remain focused and realistic while demonstrating professional Python development practices. Future enhancements may include performance benchmarking, environment-based configuration, and extended reporting.

✅ Version **1.0** — Complete and functional
---

## 📌 Author Notes

This project was built as a portfolio piece to strengthen skills in Python, SQL, automation, and software design. It is suitable for technical discussions and interviews.

---

## 🧠 Design Notes

* Each responsibility is isolated into its own module
* CLI logic is separated from business logic
* Logging provides traceability for every major step
* SQLite was chosen for simplicity and portability

---
---

## 👤 Author

**Erika Ipia**
Data & Software Engineering Enthusiast

---

⭐ If you find this project useful, feel free to star the repository!
