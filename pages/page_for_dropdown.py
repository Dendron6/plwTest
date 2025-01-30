from playwright.sync_api import Page, Locator, expect

class LocatorsForDropdown:
    def __init__(self, page: Page):
        self.page = page
        self.dropdown = page.locator('select[id="dropdown"]')
        
    def navigate(self, base_url: str) -> None:
        self.page.goto(f"{base_url}/dropdown")

    def select_option(self, option: str) -> None:
        self.dropdown.select_option(value=option)
        
    def expect_option_selected_to_be_selected(self, option: str) -> None:
        expect(self.dropdown.locator(f'[value="{option}"]')).to_have_attribute("selected", "selected")