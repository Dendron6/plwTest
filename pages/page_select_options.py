from playwright.sync_api import Page

class SelectOptions:
    def __init__(self, page: Page):
        self.page = page
        self.dropdown = page.locator('select[id="dropdown"]')

    def navigate(self) -> None:
        self.page.goto("https://demoqa.com/select-menu")

    def select_multiple_options(self, list: str) -> None:
        self.page.select_option('select#cars', list)

