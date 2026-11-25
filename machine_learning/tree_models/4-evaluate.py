#!/usr/bin/env python3
"""Evaluate the performance of a classifier."""

from sklearn import metrics


def evaluate(true_labels, predicted_labels, class_names):
    """Return a classification report for the predicted labels."""
    return metrics.classification_report(
        true_labels,
        predicted_labels,
        target_names=class_names
    )
