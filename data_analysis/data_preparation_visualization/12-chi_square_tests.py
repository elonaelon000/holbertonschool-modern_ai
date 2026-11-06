#!/usr/bin/env python3
"""Perform chi-square independence tests for categorical features."""
import pandas as pd
from scipy import stats


def chi_square_tests(df):
    """Return chi-square p-values for categorical features versus Churn."""
    categorical = df.select_dtypes(include=['object', 'category']).columns
    results = {}
    for col in categorical:
        if col != 'Churn':
            contingency = pd.crosstab(df[col], df['Churn'])
            results[col] = stats.chi2_contingency(contingency)[1]
    return results
