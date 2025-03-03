from playwright.sync_api import Page, expect
from pages.page_for_checkboxes import CheckboxPage

def test_checkbox_functionality(page: Page, base_url: str):
    # Initialize the page object
    checkbox_page = CheckboxPage(page)

    # Navigate to the checkboxes page
    checkbox_page.navigate(base_url)

    # Verify there are 2 checkboxes
    expect(checkbox_page.checkboxes).to_have_count(2)

    # By default, first checkbox is unchecked and second is checked
    expect(checkbox_page.get_first_checkbox()).not_to_be_checked()
    expect(checkbox_page.get_second_checkbox()).to_be_checked()

    # Click the first checkbox and verify it's checked
    checkbox_page.get_first_checkbox().check()
    expect(checkbox_page.get_first_checkbox()).to_be_checked()

    # Uncheck the second checkbox and verify it's unchecked
    checkbox_page.get_second_checkbox().uncheck()
    expect(checkbox_page.get_second_checkbox()).not_to_be_checked()

    # Verify we can toggle checkboxes multiple times
    checkbox_page.get_first_checkbox().uncheck()
    expect(checkbox_page.get_first_checkbox()).not_to_be_checked()

    checkbox_page.get_second_checkbox().check()
    expect(checkbox_page.get_second_checkbox()).to_be_checked()
