from playwright.sync_api import sync_playwright, expect

def test_buttons():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://formy-project.herokuapp.com/buttons")

        primary = page.get_by_role("button", name="Primary")
        primary.click()

        expect(primary).to_be_visible()

        left = page.get_by_role("button", name="Left")
        left.click()

        expect(left).to_be_visible()

        browser.close()