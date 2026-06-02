from pages.locators.buttons_locators import ButtonsLocators


class ButtonsPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://formy-project.herokuapp.com/buttons")

    def click_primary(self):
        self.page.click(ButtonsLocators.PRIMARY)

    def click_success(self):
        self.page.click(ButtonsLocators.SUCCESS)