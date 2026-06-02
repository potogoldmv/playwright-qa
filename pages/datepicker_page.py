from pages.locators.datepicker_locators import DatePickerLocators


class DatePickerPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://formy-project.herokuapp.com/datepicker")

    def pick_date(self, value):
        self.page.fill(DatePickerLocators.DATE_INPUT, value)