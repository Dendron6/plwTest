import pytest
from playwright.sync_api import Page, expect
from pages.page_for_dropdown import LocatorsForDropdown

# pytest tests/test_dropdown.py -v --headed
def test_dropdown_functionality(page: Page, base_url: str):
    # Initialize the page object
    dropdown_page = LocatorsForDropdown(page)
    
    # Navigate to the dropdown page
    dropdown_page.navigate(base_url)
    
    #select option 1
    dropdown_page.select_option("1")
    # expect(page.get_by_text("Option 1")).to_be_visible()
    dropdown_page.expect_option_selected_to_be_selected("1")
    
    #select option 2
    dropdown_page.select_option("2")
    # expect(page.get_by_text("Option 2")).to_be_visible()
    dropdown_page.expect_option_selected_to_be_selected("2")
