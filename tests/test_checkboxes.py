from playwright.sync_api import sync_playwright
from pages.checkbox_page import CheckboxPage
from utils.ai_data import generate_checkbox_data


def test_checkboxes():
    data = generate_checkbox_data()

    print("\n Ai picks:", data)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        cb = CheckboxPage(page)
        cb.open()

        if data["checkbox_1"]:
            cb.check_first()

        if data["checkbox_2"]:
            cb.check_second()

        if data["checkbox_3"]:
            cb.check_third()

        browser.close()