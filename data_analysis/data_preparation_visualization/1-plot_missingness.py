#!/usr/bin/env python3
"""Visualize missing values in a DataFrame."""
import matplotlib.pyplot as plt
import numpy as np


def plot_missingness(df):
    """Show missing records at their row and column positions."""
    plt.figure(figsize=(12, 8))
    for i, column in enumerate(df.columns):
        missing_rows = np.where(df[column].isna())[0]
        if len(missing_rows):
            plt.scatter(missing_rows, np.full(len(missing_rows), i),
                        marker='|')
    plt.yticks(np.arange(len(df.columns)), df.columns)
    plt.tight_layout()
    plt.show()
