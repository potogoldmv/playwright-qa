from playwright.sync_api import sync_playwright
from pages.datepicker_page import DatePickerPage


def test_datepicker():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        dp = DatePickerPage(page)
        dp.open()

        dp.pick_date("05/29/2026")

        browser.close()