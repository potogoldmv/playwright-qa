class ButtonsPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://formy-project.herokuapp.com/buttons")

    def click_primary(self):
        self.page.click(".btn.btn-lg.btn-primary")