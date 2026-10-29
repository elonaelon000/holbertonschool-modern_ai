#!/usr/bin/env python3
"""Collect unique product cards from a JavaScript infinite-scroll page."""

import time
from selenium import webdriver


def scroll_and_scrape(url, scroll_pause=2.0):
    """Scroll through the page and return unique product dictionaries."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_experimental_option(
        "prefs", {"profile.managed_default_content_settings.images": 2}
    )
    options.page_load_strategy = "eager"

    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        height_script = (
            "return Math.max(document.body.scrollHeight, "
            "document.documentElement.scrollHeight);"
        )
        previous_height = driver.execute_script(height_script)

        while True:
            driver.execute_script(
                "window.scrollTo(0, Math.max(document.body.scrollHeight, "
                "document.documentElement.scrollHeight));"
            )

            # Check for newly appended products instead of wasting the
            # entire pause when the next batch is already available.
            deadline = time.monotonic() + scroll_pause
            while True:
                current_height = driver.execute_script(height_script)
                if current_height > previous_height:
                    break
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    break
                time.sleep(min(0.15, remaining))

            if current_height <= previous_height:
                break
            previous_height = current_height

        # Find all matching elements at once to minimize WebDriver calls.
        titles = driver.find_elements("css selector", "div.thumbnail a.title")
        prices = driver.find_elements("css selector", "div.thumbnail h4.price")
        descriptions = driver.find_elements(
            "css selector", "div.thumbnail p.description"
        )
        rating_groups = driver.find_elements(
            "css selector", "div.thumbnail .ratings"
        )

        products = []
        seen = set()
        for title_element, price_element, desc_element, rating_group in zip(
            titles, prices, descriptions, rating_groups
        ):
            title = title_element.get_attribute("title")
            price = price_element.text.strip()
            key = (title, price)
            if key in seen:
                continue
            seen.add(key)

            products.append({
                "title": title,
                "price": price,
                "description": desc_element.text.strip(),
                "rating": len(rating_group.find_elements(
                    "css selector", "p.ws-icon.ws-icon-star"
                )),
            })

        return products
    finally:
        driver.quit()
