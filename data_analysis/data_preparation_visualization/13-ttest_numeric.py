#!/usr/bin/env python3
"""Run Welch's t-tests on numeric features grouped by churn."""
from scipy import stats


def ttest_numeric(df):
    """Return p-values comparing churned and retained customers."""
    results = {}
    for col in df.select_dtypes(include='number').columns:
        yes = df.loc[df['Churn'] == 'Yes', col].dropna()
        no = df.loc[df['Churn'] == 'No', col].dropna()
        results[col] = stats.ttest_ind(yes, no, equal_var=False).pvalue
    return results
