#!/usr/bin/env python3
"""Scrape unique products from a JavaScript infinite-scroll page."""

import time
from selenium import webdriver


def scroll_and_scrape(url, scroll_pause=2.0):
    """Scroll to load products, then return unique product dictionaries."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        time.sleep(scroll_pause)

        previous_height = 0
        while True:
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )
            time.sleep(scroll_pause)
            current_height = driver.execute_script(
                "return document.body.scrollHeight"
            )
            if current_height == previous_height:
                break
            previous_height = current_height

        products = []
        seen = set()
        for card in driver.find_elements("css selector", "div.thumbnail"):
            title = card.find_element(
                "css selector", "a.title"
            ).get_attribute("title")
            price = card.find_element("css selector", "h4.price").text
            if (title, price) in seen:
                continue

            description = card.find_element(
                "css selector", "p.description"
            ).text
            rating = len(card.find_elements(
                "css selector", ".ratings .ws-icon.ws-icon-star"
            ))
            if rating == 0:
                ratings = card.find_elements(
                    "css selector", ".ratings [data-rating]"
                )
                if ratings:
                    rating = int(ratings[0].get_attribute("data-rating"))

            seen.add((title, price))
            products.append({
                "title": title,
                "price": price,
                "description": description,
                "rating": rating
            })

        return products
    finally:
        driver.quit()
