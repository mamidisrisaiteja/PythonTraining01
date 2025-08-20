from playwright.sync_api import sync_playwright

def test_alerts():
    # Start Playwright in synchronous mode
    with sync_playwright() as p:
        # Launch Chromium browser in non-headless mode (visible UI)
        browser = p.chromium.launch(headless=False)

        # Create a new browser page (tab)
        page = browser.new_page()

        # Navigate to the demo page containing JavaScript alerts
        page.goto("https://the-internet.herokuapp.com/javascript_alerts")

        # === Handle Simple Alert (JS alert) ===
        # Register a one-time listener for the alert dialog
        page.once("dialog", lambda dialog: (
            print(f" Alert text: {dialog.message}"),  # Log alert message
            dialog.accept()  # Accept the alert (click OK)
        ))
        # Trigger the alert by clicking the button
        page.click("text=Click for JS Alert")

        # === Handle Confirm Alert (JS confirm) ===
        # Register a one-time listener for the confirm dialog
        page.once("dialog", lambda dialog: (
            print(f" Confirm text: {dialog.message}"),  # Log confirm message
            dialog.dismiss()  # Dismiss the confirm (click Cancel)
            # Use dialog.accept() to simulate clicking OK instead
        ))
        # Trigger the confirm dialog
        page.click("text=Click for JS Confirm")

        # === Handle Prompt Alert (JS prompt) ===
        # Register a one-time listener for the prompt dialog
        page.once("dialog", lambda dialog: (
            print(f"Prompt text: {dialog.message}"),  # Log prompt message
            dialog.accept("Anusha")  # Accept prompt and send input text
        ))
        # Trigger the prompt dialog
        page.click("text=Click for JS Prompt")

        # Close the browser after all interactions
        browser.close()

# Run the test function
test_alerts()