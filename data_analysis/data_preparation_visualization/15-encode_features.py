#!/usr/bin/env python3
"""Encode customer churn features for machine learning."""
import pandas as pd
from sklearn import preprocessing


def encode_features(df):
    """Return encoded data and fitted target, binary, and tenure encoders."""
    df = df.copy()
    churn_le = preprocessing.LabelEncoder()
    df['Churn'] = churn_le.fit_transform(df['Churn'])

    binary_cols = ['Partner', 'Dependents', 'PaperlessBilling', 'SeniorCitizen']
    binary_oe = preprocessing.OrdinalEncoder(categories=[['No', 'Yes']])
    for col in binary_cols:
        df[[col]] = binary_oe.fit_transform(df[[col]]).astype(int)

    tenure_oe = preprocessing.OrdinalEncoder()
    df[['TenureGroup']] = tenure_oe.fit_transform(
        df[['TenureGroup']].astype(str)
    ).astype(int)

    df = pd.get_dummies(df, columns=['Contract', 'PaymentMethod'],
                        drop_first=True, dtype=int)
    numeric_cols = df.select_dtypes(include='number').columns
    df = df[numeric_cols]
    return df, churn_le, binary_oe, tenure_oe
