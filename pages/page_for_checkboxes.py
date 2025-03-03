from playwright.sync_api import Page, Locator

class CheckboxPage:
    def __init__(self, page: Page):
        self.page = page
        self.checkboxes = page.locator('input[type="checkbox"]')

    def navigate(self, base_url: str) -> None:
        self.page.goto(f"{base_url}/checkboxes")

    def get_first_checkbox(self) -> Locator:
        return self.checkboxes.nth(0)

    def get_second_checkbox(self) -> Locator:
        return self.checkboxes.nth(1)

    def get_checkbox_count(self) -> int:
        return self.checkboxes.count()
