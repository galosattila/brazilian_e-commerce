import pandas as pd
import sys
import os


def load_data_from_csv(file_path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError as e:
        print(f"Error: Dataset file not found: {file_path}")
        exit(1)

    return df