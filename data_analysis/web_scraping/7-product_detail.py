#!/usr/bin/env python3
"""Scrape a single product detail page using Selenium."""

import time
from selenium import webdriver


def scrape_product_detail(url, delay=2.0):
    """Return the title, price, description, and rating for one product."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        time.sleep(delay)

        headings = driver.find_elements("css selector", ".caption h4")
        title = headings[1].text
        price = driver.find_element(
            "css selector", ".caption h4.price"
        ).text
        description = driver.find_element(
            "css selector", ".caption p.description"
        ).text

        stars = driver.find_elements(
            "css selector", ".ratings .ws-icon.ws-icon-star"
        )
        rating = len(stars)
        if rating == 0:
            rating_element = driver.find_element(
                "css selector", ".ratings [data-rating]"
            )
            rating = int(rating_element.get_attribute("data-rating"))

        return {
            "title": title,
            "price": price,
            "description": description,
            "rating": rating
        }
    finally:
        driver.quit()
