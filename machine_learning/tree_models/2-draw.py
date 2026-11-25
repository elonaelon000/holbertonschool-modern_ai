#!/usr/bin/env python3
"""Display the decision rules of a trained tree."""

from sklearn import tree


def draw(clf, feature_names, class_names):
    """Print the decision tree structure with feature and class names."""
    rules = tree.export_text(
        clf,
        feature_names=list(feature_names),
        class_names=list(class_names)
    )
    print(rules, end="")
