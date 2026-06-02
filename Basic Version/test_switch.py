from playwright.sync_api import sync_playwright

def test_switch_window():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://formy-project.herokuapp.com/switch-window")

        with context.expect_page() as new_page_info:
            page.click("#new-tab-button")

        new_page = new_page_info.value
        new_page.wait_for_load_state()

        page.on("dialog", lambda d: d.accept())
        page.click("#alert-button")

        browser.close()