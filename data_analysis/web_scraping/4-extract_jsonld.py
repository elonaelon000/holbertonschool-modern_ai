#!/usr/bin/env python3
"""Extract Quote objects from embedded JSON-LD scripts."""

import json
from bs4 import BeautifulSoup

fetch_html = __import__('0-fetch_html').fetch_html


def extract_jsonld(url):
    """Return quotes described by JSON-LD on the page."""
    soup = BeautifulSoup(fetch_html(url), "html.parser")
    quotes = []

    for script in soup.find_all("script", type="application/ld+json"):
        if not script.string:
            continue
        data = json.loads(script.string)
        objects = data if isinstance(data, list) else [data]

        for obj in objects:
            if not isinstance(obj, dict):
                continue
            if obj.get("@type") != "Quote":
                continue

            tags = obj.get("keywords", [])
            if isinstance(tags, str):
                tags = [tag.strip() for tag in tags.split(",") if tag.strip()]
            elif tags is None:
                tags = []

            quotes.append({
                "text": obj.get("text"),
                "author": obj.get("author", {}).get("name"),
                "tags": tags
            })

    return quotes
