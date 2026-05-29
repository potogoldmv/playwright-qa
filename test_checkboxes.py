from playwright.sync_api import sync_playwright, expect

def test_checkboxes():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://formy-project.herokuapp.com/checkbox")

        checkbox = page.locator("#checkbox-1")
        checkbox.check()

        expect(checkbox).to_be_checked()

        browser.close()