#!/usr/bin/env python3
"""Plot correlations between numeric DataFrame columns."""
import seaborn as sns
import matplotlib.pyplot as plt


def plot_correlation_heatmap(df):
    """Display an annotated correlation heatmap."""
    plt.figure(figsize=(6, 5))
    correlation = df.select_dtypes(include='number').corr()
    sns.heatmap(correlation, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.tight_layout()
    plt.show()
    return None
