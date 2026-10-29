#!/usr/bin/env python3
"""Fetch HTML content from a web page."""

import requests


def fetch_html(url, headers=None, timeout=10):
    """Fetch a web page and return its HTML as a string."""
    response = requests.get(url, headers=headers, timeout=timeout)
    response.raise_for_status()
    return response.text
