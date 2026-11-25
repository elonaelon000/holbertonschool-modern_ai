#!/usr/bin/env python3
"""Initialize boosting classifiers."""

from sklearn import ensemble
import xgboost as xgb
import lightgbm as lgb


def compare_boosting_classifiers(name, n_estimators, random_state):
    """Return an untrained classifier for the selected algorithm."""
    params = {
        "n_estimators": n_estimators,
        "random_state": random_state
    }

    if name == "adaboost":
        return ensemble.AdaBoostClassifier(**params)
    if name == "gradientboosting":
        return ensemble.GradientBoostingClassifier(**params)
    if name == "xgboost":
        return xgb.XGBClassifier(**params)
    if name == "lightgbm":
        return lgb.LGBMClassifier(verbose=-1, **params)

    raise ValueError(f"Unknown model name '{name}'")
