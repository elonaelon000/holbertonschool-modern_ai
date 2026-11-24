#!/usr/bin/env python3
"""Module for creating a logistic regression classifier."""

from sklearn import linear_model


def Logistic_Regression_Model(random_state):
    """Return an untrained logistic regression model."""
    return linear_model.LogisticRegression(random_state=random_state)
