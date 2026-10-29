#!/usr/bin/env python3
"""Scrape products from a static category page using Selenium."""

import time
from selenium import webdriver


def scrape_products(url):
    """Return product details from all thumbnail cards on the page."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        time.sleep(2)

        products = []
        for card in driver.find_elements("css selector", "div.thumbnail"):
            title = card.find_element(
                "css selector", "a.title"
            ).get_attribute("title")
            price = card.find_element("css selector", "h4.price").text
            description = card.find_element(
                "css selector", "p.description"
            ).text
            rating = card.find_element(
                "css selector", ".ratings p[data-rating]"
            ).get_attribute("data-rating")

            products.append({
                "title": title,
                "price": price,
                "description": description,
                "rating": int(rating)
            })

        return products
    finally:
        driver.quit()


scrape_products_list = scrape_products
