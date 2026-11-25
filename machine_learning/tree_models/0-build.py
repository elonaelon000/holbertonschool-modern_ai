#!/usr/bin/env python3
"""Build a decision tree classifier."""

from sklearn import tree


def build_decision_tree(min_samples_leaf, min_samples_split, random_state):
    """Create and return a decision tree classifier."""
    model = tree.DecisionTreeClassifier(
        criterion="gini",
        max_depth=None,
        min_samples_leaf=min_samples_leaf,
        min_samples_split=min_samples_split,
        random_state=random_state
    )
    return model
