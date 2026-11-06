#!/usr/bin/env python3
"""Split a DataFrame into stratified training and testing sets."""
from sklearn import model_selection


def split_data(df, target='Churn', test_size=0.2, random_state=42):
    """Return train/test features and targets with stratification."""
    X = df.drop(columns=[target])
    y = df[target]
    return model_selection.train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
