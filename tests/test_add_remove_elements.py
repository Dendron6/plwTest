from playwright.sync_api import Page, expect
from pages.page_add_remove_elements import AddRemoveElementsPage

# pytest tests/test_add_remove_elements.py -v --headed
def test_check_add_remove_elements(page: Page, base_url: str):
    # Initialize the page object
    checkbox_page = AddRemoveElementsPage(page)

    # Navigate to the checkboxes page
    checkbox_page.navigate(base_url)

    # Add 10 elements
    checkbox_page.add_element(10)

    # Verify there are 10 elements
    expect(checkbox_page.delete_buttons).to_have_count(10)

     # Delete 10 elements
    checkbox_page.delete_element(10)

    # Verify there are 0 elements
    expect(checkbox_page.delete_buttons).to_have_count(0)
