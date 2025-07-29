import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set headless=True to run without UI
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

def test_open_google(browser):
    browser.goto("http://www.uzvis.org/login")
    assert "Kurnool Public Services" in browser.title()