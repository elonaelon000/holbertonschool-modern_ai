#!/usr/bin/env python3
"""Plot the churn distribution."""
import matplotlib.pyplot as plt


def plot_churn_distribution(df):
    """Plot counts for Churn No and Yes."""
    plt.figure(figsize=(12, 8))
    counts = df['Churn'].value_counts().reindex(['No', 'Yes'], fill_value=0)
    plt.bar(counts.index, counts.values, color=['skyblue', 'salmon'])
    plt.title('Churn Distribution')
    plt.ylabel('Count')
    plt.show()
    return None
