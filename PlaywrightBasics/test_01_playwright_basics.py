import time

from playwright.sync_api import Playwright
from playwright.sync_api import Page, expect


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

def test_locator_incorrect_login_actions(page: Page):
    page.goto("https://practice.expandtesting.com/login")
    page.get_by_label("Username").fill("practice")
    page.get_by_label("Password").fill("SuperSecretPassword")
    page.get_by_role("button",name="Login").click()
    expect(page.get_by_text("Your password is invalid!"))

def test_locator_check_box(page: Page):
        page.goto("https://practice.expandtesting.com/checkboxes")
        # page.get_by_label("Checkbox 1").click()
        # page.locator('.form-check-label').nth(0).click()
        # as there are 2 elements matching
        page.locator('label[for="checkbox1"]')


def test_locator_form_validation(page: Page):
        page.goto("https://practice.expandtesting.com/form-validation")
        page.get_by_label('Contact Name').fill("Jay")
        #Be careful in selecting text wrt name, it not what is written in the attribute "name"
        # rather it is the display label "Contact number"
        page.get_by_role('textbox',name='Contact number').fill("950-5999999")
        #Also make sure to see that the date is given in YYYY-MM-DD format
        page.locator("#validationCustom05[type='date']").fill("2025-07-30")
        time.sleep(5)
        # here also the option is 'cash on delivery' which the text that is being displayed
        page.get_by_role('combobox').select_option('cash on delivery')
        page.locator(".btn.btn-primary").click()

def test_login_fireFoxBrowser(playwright : Playwright):
    browser=playwright.firefox.launch(headless=False)
    page=browser.new_page()
    page.goto("https://practice.expandtesting.com/login")
    page.get_by_label("Username").fill("practice")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()