"""
features.py — Feature engineering utilities.

Creates derived features for analysis and modeling:
remote work flags, experience rankings, company size ordinals.
"""

import pandas as pd


# Ordinal mapping for experience level
EXPERIENCE_ORDER = {
    'Entry-Level': 0,
    'Mid-Level': 1,
    'Senior': 2,
    'Executive': 3
}

COMPANY_SIZE_ORDER = {
    'Small': 0,
    'Medium': 1,
    'Large': 2
}


def add_remote_category(df: pd.DataFrame) -> pd.DataFrame:
    """Add a categorical remote work column based on remote_ratio."""
    df = df.copy()
    df['remote_category'] = df['remote_ratio'].map({
        0: 'On-site',
        50: 'Hybrid',
        100: 'Remote'
    })
    return df


def add_experience_rank(df: pd.DataFrame) -> pd.DataFrame:
    """Add numeric experience ranking for correlation analysis."""
    df = df.copy()
    df['experience_rank'] = df['experience_level'].map(EXPERIENCE_ORDER)
    return df


def add_company_size_rank(df: pd.DataFrame) -> pd.DataFrame:
    """Add numeric company size ranking."""
    df = df.copy()
    df['company_size_rank'] = df['company_size'].map(COMPANY_SIZE_ORDER)
    return df


def encode_categoricals(df: pd.DataFrame, columns: list = None) -> pd.DataFrame:
    """
    Label-encode categorical columns for modeling.
    If no columns specified, encodes all object-type columns.
    """
    df = df.copy()
    if columns is None:
        columns = df.select_dtypes(include='object').columns.tolist()

    for col in columns:
        df[f'{col}_encoded'] = df[col].astype('category').cat.codes

    print(f"Encoded {len(columns)} columns: {columns}")
    return df


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    """Apply all feature engineering steps."""
    df = add_remote_category(df)
    df = add_experience_rank(df)
    df = add_company_size_rank(df)
    print(f"Features added. New shape: {df.shape[0]} rows × {df.shape[1]} columns")
    return df
