#!/usr/bin/env python3
"""Handle missing values in the TotalCharges column."""


def clean_total_charges(df, method='drop'):
    """Clean missing TotalCharges using drop, median, or imputation."""
    df = df.copy()
    if method == 'drop':
        return df.dropna(subset=['TotalCharges'])
    if method == 'median':
        df['TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].median())
    elif method == 'impute':
        df['TotalCharges'] = df['TotalCharges'].fillna(
            df['MonthlyCharges'] * df['tenure']
        )
    else:
        raise ValueError("method must be 'drop', 'median', or 'impute'")
    return df
