"""Steps shared by several features (Cypress: e2e/common/common.cy.ts)."""
from behave import given, step, when, register_type

from config.config import Config
from utils.browser import new_browser_context
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.okta_page import OktaLoginPage
from utils.auth import AuthSession


def parse_boolean(text):
    return text == "true"


# Cypress custom parameter type `{boolean}` -> use as `{flag:boolean}`
register_type(boolean=parse_boolean)
parse_boolean.pattern = r"true|false"


@given('I login to Trax successfully through Okta')
def step_impl(context):
    if AuthSession.storage_state:
        # Reuse the earlier login (cy.session): start a fresh, already authenticated context
        context.browser_context.close()
        new_browser_context(context, storage_state=AuthSession.storage_state)
        return

    login_page = LoginPage(context.page)
    login_page.go_to_home_page(Config.PROJECT_NAME)
    login_page.enter_username(Config.VALID_USERNAME)
    login_page.enter_password(Config.VALID_PASSWORD)
    login_page.click_login()

    okta_page = OktaLoginPage(context.page)
    okta_page.verify_is_on_okta_page()
    okta_page.enter_username(Config.VALID_USERNAME)
    okta_page.enter_password(Config.VALID_OKTAPASSWORD)
    okta_page.click_login()

    HomePage(context.page).verify_is_on_home_page()
    AuthSession.storage_state = context.browser_context.storage_state()


@step('I navigate to the Explorer application')
def step_impl(context):
    BasePage(context.page).go_to_explorer_visit_page(Config.PROJECT_NAME)


@step('I navigate to the Products and Brands app')
def step_impl(context):
    BasePage(context.page).go_to_products_and_brands_page(Config.PROJECT_NAME)


@step('I navigate to the Reporting configurations Explorer page')
def step_impl(context):
    BasePage(context.page).go_to_reporting_configurations_explorer_page(Config.PROJECT_NAME)


@step('I navigate to the Reporting configurations Mobile Reports General page')
def step_impl(context):
    BasePage(context.page).go_to_reporting_configurations_mobile_reports_general_page(Config.PROJECT_NAME)


@step('I navigate to the Reporting configuration Mobile Reports KPI page')
def step_impl(context):
    BasePage(context.page).go_to_reporting_configurations_mobile_reports_kpis_page(Config.PROJECT_NAME)


@step('I go the Project Settings page in the P&B app')
def step_impl(context):
    BasePage(context.page).go_to_products_and_brands_project_settings_page(Config.PROJECT_NAME)


@step('I navigate to the Reporting Configurations K-Engine KPI Attributes page')
def step_impl(context):
    BasePage(context.page).go_to_reporting_configurations_kengine_kpi_attributes_page(Config.PROJECT_NAME)
