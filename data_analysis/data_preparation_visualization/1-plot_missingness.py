#!/usr/bin/env python3
"""Visualize missing values in a DataFrame."""
import matplotlib.pyplot as plt
import numpy as np


def plot_missingness(df):
    """Plot each missing value as a vertical bar."""
    plt.figure(figsize=(12, 8))
    missing_rows, missing_cols = np.where(df.isna().to_numpy())
    plt.scatter(missing_rows, missing_cols, marker='|')
    plt.yticks(np.arange(len(df.columns)), df.columns)
    plt.tight_layout()
    plt.show()
