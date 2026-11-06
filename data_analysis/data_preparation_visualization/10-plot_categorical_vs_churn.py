#!/usr/bin/env python3
"""Plot churn rate by categorical feature."""
import matplotlib.pyplot as plt


def plot_categorical_vs_churn(df, col):
    """Display the proportion of churned customers per category."""
    churn_rate = df.groupby(col)['Churn'].apply(lambda x: (x == 'Yes').mean())
    plt.figure(figsize=(12, 8))
    churn_rate.plot(kind='bar')
    plt.title(f'Churn Rate by {col}')
    plt.ylabel('Churn Rate')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    return None
