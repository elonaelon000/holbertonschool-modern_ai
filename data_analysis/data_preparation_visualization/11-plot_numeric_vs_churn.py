#!/usr/bin/env python3
"""Visualize numeric feature distributions grouped by churn."""
import matplotlib.pyplot as plt
import seaborn as sns


def plot_numeric_vs_churn(df, col):
    """Plot overlapping histograms for churn categories."""
    plt.figure(figsize=(12, 8))
    sns.histplot(data=df, x=col, hue='Churn', bins=30)
    plt.title(f'{col} Distribution by Churn')
    plt.xlabel(col)
    plt.tight_layout()
    plt.show()
    return None
