from playwright.sync_api import sync_playwright

def test_handle_child_window():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://demoqa.com/browser-windows")

        # Listen for popup event
        with context.expect_page() as popup_info:
            page.click("button#windowButton")  # Opens new tab
        child_page = popup_info.value

        # Wait for child page to load
        child_page.wait_for_load_state()

        # Interact with child window
        assert child_page.locator("h1").inner_text() == "This is a sample page"

        print(child_page.locator("h1").inner_text())
        browser.close()