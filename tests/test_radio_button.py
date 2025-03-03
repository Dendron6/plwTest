from playwright.sync_api import Page
from pages.page_radio_button import RadioButton

def test_checkbox_functionality(page: Page, base_url: str):
    # Initialize the page object
    radio_button = RadioButton(page)

    # Navigate to the select options page
    radio_button.navigate()


    radio_button.select_yes_radio_button()
    radio_button.expect_text_to_be_displayed("Yes")
    # radio_button.expect_yes_radio_button_to_be_selected()

    radio_button.select_impressive_radio_button()
    radio_button.expect_text_to_be_displayed("Impressive")
    # radio_button.expect_impressive_radio_button_to_be_selected()

    page.pause()

