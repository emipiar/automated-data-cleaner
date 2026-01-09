import pandas as pd
from src.cleaner import clean_data


def test_clean_data_removes_nulls_and_duplicates():
    data = {
        "name": ["Ana", "Luis", "Ana", None],
        "age": [25, 30, 25, 40]
    }

    df = pd.DataFrame(data)
    cleaned = clean_data(df)

    assert cleaned.isnull().sum().sum() == 0
    assert cleaned.duplicated().sum() == 0
