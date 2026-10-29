#!/usr/bin/env python3
"""Log in to Quotes to Scrape and collect quotes."""

import requests
from bs4 import BeautifulSoup


def login_and_scrape(login_url, user, pwd):
    """Log in with a session, then return quotes from the home page."""
    with requests.Session() as session:
        login_response = session.get(login_url)
        login_response.raise_for_status()

        soup = BeautifulSoup(login_response.text, "html.parser")
        token = soup.find("input", attrs={"name": "csrf_token"})
        csrf_token = token["value"]

        payload = {
            "username": user,
            "password": pwd,
            "csrf_token": csrf_token
        }
        response = session.post(login_url, data=payload)
        response.raise_for_status()

        quotes_response = session.get("https://quotes.toscrape.com/")
        quotes_response.raise_for_status()
        soup = BeautifulSoup(quotes_response.text, "html.parser")

        quotes = []
        for block in soup.select("div.quote"):
            text = block.select_one("span.text").get_text(strip=True)
            author = block.select_one("small.author").get_text(strip=True)
            tags = [
                tag.get_text(strip=True)
                for tag in block.select("a.tag")
            ]
            quotes.append({
                "text": text,
                "author": author,
                "tags": tags
            })

        return quotes
