import pandas as pd
from src.loader import load_csv


def test_load_csv():
    df = load_csv("data/raw/example.csv")
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
"""
Verifica que carga, que devuelve un DataFrame y que no está vacío.
"""