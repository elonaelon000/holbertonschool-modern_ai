#!/usr/bin/env python3
"""Train a tree-based classifier."""


def train_tree(clf, X, y):
    """Fit the classifier using input features and target labels."""
    clf.fit(X, y)
