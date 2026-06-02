from playwright.sync_api import sync_playwright
from pages.buttons_page import ButtonsPage


def test_buttons():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        btn = ButtonsPage(page)
        btn.open()

        btn.click_primary()

        browser.close()