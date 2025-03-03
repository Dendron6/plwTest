# pytest --headed --browser firefox --browser chromium
# pytest --headed --browser firefox --browser chromium --tracing on #this allows to create report files of runs
from playwright.sync_api import Page
import pytest

# @pytest.mark.skip_browser('firefox') #will skip run in chrome if you set up more browsers
def test_title_validation(page: Page):
    page.goto("/")
    assert page.title() == "Swag Labs"

# @pytest.mark.only_browser('chromium') #will only run in chromium if you set up more browsers
def test_title_validation_inventory(page: Page):
    page.goto("/inventory.html")
    print('this is my print statement', page.inner_text('h3'))
    assert page.inner_text('h3') == "Epic sadface: You can only access '/inventory.html' when you are logged in."

# parametrize is used to run the same test with different parameters
@pytest.mark.parametrize('login, password, expected', [('standard_user', 'secret_sauce', 'logge_in'), ('locked_out_user', 'secret_sauce', 'logge_in'), ('locked_out_user', 'wrong_password', 'failed_to_login')])
def test_login(page: Page, login, password, expected):
    page.goto("/")
    page.locator('#user-name').fill(login)
    page.locator('#password').fill(password)
    page.locator('#login-button').click()
    assert page.title() == "Swag Labs"
