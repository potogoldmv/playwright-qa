class FormPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://formy-project.herokuapp.com/form")

    def fill_first_name(self, value):
        self.page.fill("#first-name", value)

    def fill_last_name(self, value):
        self.page.fill("#last-name", value)

    def fill_job_title(self, value):
        self.page.fill("#job-title", value)

    def fill_date(self, value):
        self.page.fill("#datepicker", value)

    def select_radio(self):
        self.page.click("#radio-button-2")

    def check_checkbox(self):
        self.page.click("#checkbox-1")

    def select_experience(self, value):
        self.page.select_option("#select-menu", value)

    def submit(self):
        self.page.click("a.btn.btn-lg.btn-primary")