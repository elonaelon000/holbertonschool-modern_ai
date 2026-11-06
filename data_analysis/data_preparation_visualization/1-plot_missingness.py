#!/usr/bin/env python3
"""Plot locations of missing values in a DataFrame."""
import matplotlib.pyplot as plt
import numpy as np


def plot_missingness(df):
    """Display missing entries by row index and column name."""
    plt.figure(figsize=(12, 8))
    missing_rows, missing_cols = np.where(df.isna().to_numpy())
    plt.scatter(missing_rows, missing_cols, marker='|')
    plt.yticks(np.arange(len(df.columns)), df.columns)
    plt.xlabel('Row Index')
    plt.ylabel('Columns')
    plt.title('Missing Values in DataFrame')
    plt.xlim(0, max(len(df) - 1, 1))
    plt.ylim(-0.5, len(df.columns) - 0.5)
    plt.tight_layout()
    plt.show()
