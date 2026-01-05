import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the DataFrame by:
    - removing duplicate rows
    - handling missing values
    """
    cleaned_df = df.copy()

    # Remove duplicates
    cleaned_df = cleaned_df.drop_duplicates()

    # Handle missing values
    for column in cleaned_df.columns:
        if cleaned_df[column].dtype in ["int64", "float64"]:
            cleaned_df = cleaned_df.dropna(subset=[column])
        else:
            cleaned_df[column] = cleaned_df[column].fillna("UNKNOWN")

    return cleaned_df

