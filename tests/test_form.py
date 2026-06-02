from playwright.sync_api import sync_playwright
from pages.form_page import FormPage
from utils.ai_data import generate_form_data


def test_form():
    data = generate_form_data()

    print("\n Ai picks", data)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        form = FormPage(page)
        form.open()
        #ai picks
        form.fill_first_name(data["first_name"])
        form.fill_last_name(data["last_name"])
        form.fill_job_title(data["job_title"])
        form.fill_date(data["date"])
        #manual picks
        form.select_radio()
        form.check_checkbox()
        form.select_experience("2")

        form.submit()

        browser.close()