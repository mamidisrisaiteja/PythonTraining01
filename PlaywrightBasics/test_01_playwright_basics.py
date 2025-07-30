import time

from playwright.sync_api import Page

def test_playwright_one(playwright):
    # - Launches a Chromium browser instance with the GUI visible (headless=False = headed mode).
    # - Useful for debugging or watching the test run in real-time.
    browser=playwright.chromium.launch(headless=False)
    # - Creates an isolated browser context — like an incognito session.
    # - No shared cookies, localStorage, or history; perfect for a clean test environment.
    context=browser.new_context()
    # - Opens a new browser tab within that isolated context.
    # - This is where your test actions will happen.
    page=context.new_page()
    # - Navigates the tab to Google’s homepage.
    # - You can follow this with actions like searching, validating UI elements, or taking screenshots.
    page.goto("https://www.google.com/")


def test_playwright_two(page :Page):
    page.goto("https://www.google.com/")

def test_locator_login_elements(page: Page):
    page.goto("https://practice.expandtesting.com/login")
    page.get_by_label("Username").fill("practice")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button",name="Login").click()


def test_locator_check_box(page: Page):
        page.goto("https://practice.expandtesting.com/checkboxes")
        # page.get_by_label("Checkbox 1").click()
        # page.locator('.form-check-label').nth(0).click()
        page.locator('label[for="checkbox1"]')
