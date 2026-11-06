#!/usr/bin/env python3
"""Create service count and tenure group features."""
import pandas as pd


def create_features(df):
    """Engineer features and drop their source columns."""
    services = ['MultipleLines', 'InternetService', 'OnlineSecurity',
                'OnlineBackup', 'DeviceProtection', 'TechSupport',
                'StreamingTV', 'StreamingMovies']
    df = df.copy()
    subscribed = df[services].eq('Yes')
    subscribed['InternetService'] = df['InternetService'].isin(
        ['DSL', 'Fiber optic'])
    df['NumServices'] = subscribed.sum(axis=1)
    df['TenureGroup'] = pd.cut(
        df['tenure'], bins=[0, 12, 24, 48, 60, float('inf')],
        labels=['0-12', '13-24', '25-48', '49-60', '60+'])
    return df.drop(columns=services + ['tenure'])
