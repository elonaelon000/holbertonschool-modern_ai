#!/usr/bin/env python3
"""Scrape quotes from all API pages."""

import json

fetch_html = __import__('0-fetch_html').fetch_html


def scrape_via_api(base_url):
    """Return all quotes from the paginated quotes API."""
    quotes = []
    page = 1

    while True:
        url = f"{base_url.rstrip('/')}/api/quotes?page={page}"
        data = json.loads(fetch_html(url))

        for quote in data["quotes"]:
            quotes.append({
                "text": quote["text"],
                "author": quote["author"]["name"],
                "tags": quote["tags"]
            })

        if not data["has_next"]:
            break

        page += 1

    return quotes
