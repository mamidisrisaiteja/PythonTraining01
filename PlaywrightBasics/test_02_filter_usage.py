import time

from playwright.sync_api import sync_playwright
def test_add_specific_product_to_cart():
 with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")  # Example site with product cards

    # Login first (site requires it)
    page.fill("input[data-test='username']", "standard_user")
    page.fill("input[data-test='password']", "secret_sauce")
    page.click("input[data-test='login-button']")

    # Filter product cards by text
    product_card = page.locator(".inventory_item").filter(has_text="Sauce Labs Backpack")

    # Click the Add to Cart button inside the filtered card
    product_card.locator("button").click()
    time.sleep(5)