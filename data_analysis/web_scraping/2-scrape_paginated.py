#!/usr/bin/env python3
"""Scrape quotes across all pages by following Next links."""

from bs4 import BeautifulSoup
import time
from urllib import parse

fetch_html = __import__('0-fetch_html').fetch_html
scrape_basic = __import__('1-scrape_basic').scrape_basic


def scrape_paginated(base_url):
    """Return quotes from every page, following pagination links."""
    all_quotes = []
    current_url = base_url

    while current_url:
        all_quotes.extend(scrape_basic(current_url))
        time.sleep(0.5)

        soup = BeautifulSoup(fetch_html(current_url), "html.parser")
        next_link = soup.select_one("li.next a")

        if next_link is None:
            break

        current_url = parse.urljoin(current_url, next_link["href"])
        time.sleep(0.5)

    return all_quotes
