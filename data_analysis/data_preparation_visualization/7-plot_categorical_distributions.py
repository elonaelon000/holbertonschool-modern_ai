#!/usr/bin/env python3
"""Plot categorical feature distributions."""
import matplotlib.pyplot as plt


def plot_categorical_distributions(df, columns_to_plot=None):
    """Plot distributions of categorical columns."""
    if columns_to_plot is None:
        columns_to_plot = (df.select_dtypes(include=['object'])
                           .columns.drop('Churn', errors='ignore').tolist())
    else:
        columns_to_plot = list(columns_to_plot)

    n_cols = 3
    n_rows = (len(columns_to_plot) + 2) // 3
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5 * n_rows))
    axes = axes.flatten()

    for i, col in enumerate(columns_to_plot):
        counts = df[col].value_counts()
        axes[i].bar(counts.index, counts.values)
        axes[i].set_title(col)
        axes[i].tick_params(axis='x', labelrotation=45)

    for i in range(len(columns_to_plot), len(axes)):
        axes[i].set_visible(False)

    plt.tight_layout()
    plt.savefig('Task_7.png')
    plt.show()
    return None
