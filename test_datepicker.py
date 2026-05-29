from playwright.sync_api import sync_playwright, expect

def test_datepicker():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://formy-project.herokuapp.com/datepicker")

        date_input = page.locator("#datepicker")
        date_input.fill("05/29/2026")

        expect(date_input).to_have_value("05/29/2026")

        browser.close()