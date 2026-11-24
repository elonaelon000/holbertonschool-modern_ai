#!/usr/bin/env python3
"""Module for creating support vector machine classifiers."""

from sklearn import svm


def get_SVM_model(name, random_state):
    """Return an untrained SVC with the specified kernel and seed."""
    return svm.SVC(kernel=name, random_state=random_state)
