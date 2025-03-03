from playwright.sync_api import Page
from pages.page_select_options import SelectOptions

def test_checkbox_functionality(page: Page, base_url: str):
    # Initialize the page object
    select_options = SelectOptions(page)

    # Navigate to the select options page
    select_options.navigate()


    select_options.select_multiple_options(['volvo', 'saab', 'audi'])

    page.pause()

