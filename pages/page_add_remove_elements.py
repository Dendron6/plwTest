# playwright show-trace tracing_logs/test_check_add_remove_elements[chromium]_20250224_163746
from playwright.sync_api import Page

class AddRemoveElementsPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_button = page.locator('button[onclick="addElement()"]')
        self.delete_buttons = page.locator('button[onclick="deleteElement()"]')

    def navigate(self, base_url: str) -> None:
        self.page.goto(f"{base_url}/add_remove_elements/")

    def add_element(self, quantity: int) -> None:
        for _ in range(quantity):
            self.add_button.click()

    def delete_element(self, quantity: int) -> None:
        for _ in range(quantity):
            self.delete_buttons.locator('nth=0').click()

