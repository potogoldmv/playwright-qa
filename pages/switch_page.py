class SwitchPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto("https://formy-project.herokuapp.com/switch-window")

    def open_new_tab(self):
        with self.page.context.expect_page() as new_page_info:
            self.page.click("#new-tab-button")
        return new_page_info.value

    def trigger_alert(self):
        self.page.on("dialog", lambda d: d.accept())
        self.page.click("#alert-button")