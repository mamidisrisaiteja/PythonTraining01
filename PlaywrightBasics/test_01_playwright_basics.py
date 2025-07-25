import playwright

def test_plyw_one(playwright):
    browser = playwright.chromium.launch(headless=False)
    context= browser.new_context()
    page=context.new_page()
    page.goto("www.google.com")