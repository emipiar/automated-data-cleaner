import pandas as pd
import logging


def load_csv(path: str) -> pd.DataFrame:
    logging.info(f"Loading CSV file from {path}")
    """
    Loads a CSV file and returns a pandas DataFrame.
    """
    try:
        df = pd.read_csv(path)
        logging.info("CSV file loaded successfully")
        return df
    except Exception as e:
        logging.error(f"Error loading CSV file: {e}")
        raise RuntimeError(f"Error loading CSV file: {e}")