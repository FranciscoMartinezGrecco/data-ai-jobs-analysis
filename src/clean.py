"""
clean.py — Data loading and cleaning pipeline.

Handles loading raw CSV data, mapping coded values to readable labels,
removing duplicates, and saving processed output.
"""

import pandas as pd
import os


# Mapping dictionaries for coded columns
EXPERIENCE_MAP = {
    'EN': 'Entry-Level',
    'MI': 'Mid-Level',
    'SE': 'Senior',
    'EX': 'Executive'
}

EMPLOYMENT_MAP = {
    'FT': 'Full-Time',
    'PT': 'Part-Time',
    'CT': 'Contract',
    'FL': 'Freelance'
}

COMPANY_SIZE_MAP = {
    'S': 'Small',
    'M': 'Medium',
    'L': 'Large'
}


def load_raw_data(filepath: str) -> pd.DataFrame:
    """Load raw CSV and return DataFrame."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Dataset not found at {filepath}")
    df = pd.read_csv(filepath)
    print(f"Loaded {df.shape[0]} rows × {df.shape[1]} columns")
    return df


def clean_salaries_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the salaries DataFrame:
    - Drop duplicates
    - Drop unnecessary index column if present
    - Map coded values to readable labels
    - Keep only USD salary for consistency
    """
    df = df.copy()

    # Drop the unnamed index column if it exists
    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])

    # Remove duplicate rows
    n_before = len(df)
    df = df.drop_duplicates()
    n_removed = n_before - len(df)
    if n_removed > 0:
        print(f"Removed {n_removed} duplicate rows")

    # Map coded values to labels
    df['experience_level'] = df['experience_level'].map(EXPERIENCE_MAP)
    df['employment_type'] = df['employment_type'].map(EMPLOYMENT_MAP)
    df['company_size'] = df['company_size'].map(COMPANY_SIZE_MAP)

    print(f"Cleaned dataset: {df.shape[0]} rows × {df.shape[1]} columns")
    return df


def save_processed(df: pd.DataFrame, filepath: str) -> None:
    """Save processed DataFrame to CSV."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    df.to_csv(filepath, index=False)
    print(f"Saved processed data to {filepath}")
