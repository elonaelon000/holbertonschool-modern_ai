#!/usr/bin/env python3
"""Remove duplicate rows from a DataFrame."""


def remove_duplicates(df):
    """Return a DataFrame without duplicate rows."""
    return df.drop_duplicates()
