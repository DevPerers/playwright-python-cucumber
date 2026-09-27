from behave import given, when, then
from config.config import Config
from pages.login_page import LoginPage
from pages.okta_page import OktaLoginPage
from pages.home_page import HomePage

@given('the user navigates to the login page')
def step_impl(context):
    context.login_page = LoginPage(context.page)
    context.login_page.navigate_to(Config.BASE_URL)

@then('the login page should be visible')
def step_impl(context):
    context.login_page.verify_is_on_login_page()

@then('the login page UI elements are visible')
def step_impl(context):
    context.login_page.verify_login_page_ui_elements_visible()

@when('the user enters invalid credentials')
def step_impl(context):
    context.login_page.enter_username(Config.INVALID_USERNAME)
    context.login_page.enter_password(Config.INVALID_PASSWORD)    

@when('the user enters valid credentials')
def step_impl(context):
    context.login_page.enter_username(Config.VALID_USERNAME)
    context.login_page.enter_password(Config.VALID_PASSWORD)

@when('clicks the login button')
def step_impl(context):
    context.login_page.click_login()

@then('the user should see the error message as "{expected_message}"')
def step_impl(context, expected_message):
    context.login_page.verify_error_message(expected_message)

@then('the user should see the message "{expected_message}"')
def step_impl(context, expected_message):
    message = context.login_page.get_flash_message()
    assert expected_message in message, f"Expected '{expected_message}', but got '{message}'"

@then('user should see OKTA login page')
def step_impl(context):
    context.okta_page = OktaLoginPage(context.page)
    context.okta_page.verify_is_on_okta_page()

@when('the user enters valid OKTA credentials')
def step_impl(context):
    context.okta_page.enter_username(Config.VALID_USERNAME)
    context.okta_page.enter_password(Config.VALID_OKTAPASSWORD)

@when('clicks the OKTA login button')
def step_impl(context):
    context.okta_page.click_login()

@then('the homepage application header should be visible as "{expected_text}"')
def step_impl(context, expected_text):
    context.home_page = HomePage(context.page)
    context.home_page.verify_is_on_home_page()
