from playwright.sync_api import sync_playwright, expect

def test_form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://formy-project.herokuapp.com/form")

        page.fill("#first-name","Alex")
        page.fill("#last-name", "Alexandru")
        page.fill("#job-title", "QA Tester")

        page.check("#radio-button-2")
        page.check("#checkbox-1")

        page.select_option("#select-menu", "2")
        page.fill("#datepicker", "05/29/2026")
        page.click(".btn-primary")

        expect(page.locator(".alert")).to_contain_text("successfully")
        browser.close()