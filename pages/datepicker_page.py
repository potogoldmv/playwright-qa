class DatepickerPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://formy-project.herokuapp.com/datepicker")

    def select_date(self, value):
        self.page.fill("#datepicker", value)