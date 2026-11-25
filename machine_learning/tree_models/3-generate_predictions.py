#!/usr/bin/env python3
"""Generate predictions from a trained tree-based classifier."""


def generate_predictions(clf, X):
    """Return the predicted class labels for the input features."""
    return clf.predict(X)
