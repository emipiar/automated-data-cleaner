import pandas as pd


def load_csv(path: str) -> pd.DataFrame:
    """
    Loads a CSV file and returns a pandas DataFrame.
    """
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        raise RuntimeError(f"Error loading CSV file: {e}")
