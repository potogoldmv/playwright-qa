from playwright.sync_api import sync_playwright
from pages.switch_page import SwitchPage


def test_switch():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        sw = SwitchPage(page)
        sw.open()

        new_page = sw.open_new_tab()
        new_page.wait_for_load_state()

        sw.trigger_alert()

        browser.close()