#!/usr/bin/env python3
"""Visualize missing values in a DataFrame."""
import matplotlib.pyplot as plt
import numpy as np


def plot_missingness(df):
    """Plot missing entries by row index and column name."""
    rows, cols = np.where(df.isna().to_numpy())

    plt.figure(figsize=(12, 8))
    plt.scatter(rows, cols, marker='|')
    plt.yticks(np.arange(len(df.columns)), df.columns)
    plt.title('Missingness Plot')
    plt.tight_layout()
    plt.show()
    return None
