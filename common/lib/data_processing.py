"""
Common data processing utilities for all notebooks.
"""
import pandas as pd
import numpy as np
from typing import Optional, List


def load_csv_data(filepath: str, **kwargs) -> pd.DataFrame:
    """
    Load CSV data with common preprocessing.
    
    Args:
        filepath: Path to the CSV file
        **kwargs: Additional arguments to pass to pd.read_csv
        
    Returns:
        pd.DataFrame: Loaded dataframe
    """
    return pd.read_csv(filepath, **kwargs)


def clean_missing_values(df: pd.DataFrame, strategy: str = 'drop', fill_value=None) -> pd.DataFrame:
    """
    Handle missing values in a dataframe.
    
    Args:
        df: Input dataframe
        strategy: 'drop' to remove rows with NaN, 'fill' to fill with value
        fill_value: Value to use when strategy is 'fill'
        
    Returns:
        pd.DataFrame: Cleaned dataframe
    """
    if strategy == 'drop':
        return df.dropna()
    elif strategy == 'fill':
        return df.fillna(fill_value if fill_value is not None else 0)
    else:
        raise ValueError(f"Unknown strategy: {strategy}")


def normalize_column(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Normalize a column to 0-1 range.
    
    Args:
        df: Input dataframe
        column: Column name to normalize
        
    Returns:
        pd.DataFrame: DataFrame with normalized column
    """
    df_copy = df.copy()
    min_val = df_copy[column].min()
    max_val = df_copy[column].max()
    
    if max_val - min_val != 0:
        df_copy[column] = (df_copy[column] - min_val) / (max_val - min_val)
    
    return df_copy


def get_basic_stats(df: pd.DataFrame, columns: Optional[List[str]] = None) -> pd.DataFrame:
    """
    Get basic statistical description of dataframe.
    
    Args:
        df: Input dataframe
        columns: Specific columns to describe (None for all)
        
    Returns:
        pd.DataFrame: Statistical description
    """
    if columns:
        return df[columns].describe()
    return df.describe()
