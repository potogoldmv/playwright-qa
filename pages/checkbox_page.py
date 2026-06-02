from pages.locators.checkbox_locators import CheckboxLocators


class CheckboxPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://formy-project.herokuapp.com/checkbox")

    def check_first(self):
        self.page.check(CheckboxLocators.CHECKBOX_1)

    def check_second(self):
        self.page.check(CheckboxLocators.CHECKBOX_2)

    def check_third(self):
        self.page.check(CheckboxLocators.CHECKBOX_3)