#!/usr/bin/env python3
"""Retrieve feature importances from a trained random forest."""

import numpy as np


def feature_importance(rf):
    """Return feature importances and indices sorted in ascending order."""
    importances = rf.feature_importances_
    indices = np.argsort(importances)
    return importances, indices
