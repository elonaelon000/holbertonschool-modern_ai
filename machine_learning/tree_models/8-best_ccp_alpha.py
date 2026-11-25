#!/usr/bin/env python3
"""Select the best cost-complexity pruning parameter."""


def get_best_alpha(clfs, train_scores, test_scores, ccp_alphas):
    """Return the best pruning alpha and its trained classifier."""
    best_idx = max(
        range(len(clfs)),
        key=lambda i: (
            test_scores[i],
            -abs(train_scores[i] - test_scores[i]),
            ccp_alphas[i]
        )
    )
    return ccp_alphas[best_idx], clfs[best_idx]
