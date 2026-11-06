#!/usr/bin/env python3
"""Standardize numeric charge columns."""
from sklearn import preprocessing


def scale_numeric(df):
    """Scale MonthlyCharges and TotalCharges with StandardScaler."""
    df = df.copy()
    scaler = preprocessing.StandardScaler()
    columns = ['MonthlyCharges', 'TotalCharges']
    df[columns] = scaler.fit_transform(df[columns])
    return df
