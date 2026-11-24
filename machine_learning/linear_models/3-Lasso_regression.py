#!/usr/bin/env python3
"""Module for creating a Lasso regression model."""

from sklearn import linear_model


def lasso_regression(random_state):
    """Return an untrained Lasso model with the given random state."""
    return linear_model.Lasso(random_state=random_state)
