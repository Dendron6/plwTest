from playwright.sync_api import Page, expect

class RadioButton:
    def __init__(self, page: Page):
        self.page = page
        self.yesRadioButton =  page.get_by_text("Yes")
        self.impressiveRadioButton = page.get_by_text("Impressive")
        self.noRadioButton = page.locator('#noRadio')
        self.page.locator(".text-success")

    def navigate(self) -> None:
        self.page.goto("https://demoqa.com/radio-button")

    def select_yes_radio_button(self) -> None:
        self.yesRadioButton.click()

    def select_impressive_radio_button(self) -> None:
        self.impressiveRadioButton.click()

    def select_no_radio_button(self) -> None:
        self.noRadioButton.click()

    def expect_yes_radio_button_to_be_selected(self) -> None:
        expect(self.yesRadioButton).to_be_checked()

    def expect_impressive_radio_button_to_be_selected(self) -> None:
        expect(self.impressiveRadioButton).to_be_checked()

    def expect_text_to_be_displayed(self, text: str) -> None:
        expect(self.page.locator(".text-success")).to_have_text(text)
