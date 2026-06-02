from pages.locators.switch_locators import SwitchLocators


class SwitchPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://formy-project.herokuapp.com/switch-window")

    def open_new_tab(self):
        with self.page.context.expect_page() as new_page_info:
            self.page.click("#new-tab-button")

        new_page = new_page_info.value
        return new_page

    def trigger_alert(self):
        self.page.click(SwitchLocators.ALERT_BUTTON)