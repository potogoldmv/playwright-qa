class CheckboxPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://formy-project.herokuapp.com/checkbox")

    def check_first(self):
        self.page.click("#checkbox-1")

    def check_second(self):
        self.page.click("#checkbox-2")

    def check_third(self):
        self.page.click("#checkbox-3")