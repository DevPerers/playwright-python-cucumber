import os
import allure
from playwright.sync_api import sync_playwright

from utils.browser import new_browser_context

def before_all(context):
    # Check if HEADLESS environment variable is set to "false"
    is_headless = os.getenv("HEADLESS", "true").lower() == "true"

    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=is_headless)

def before_feature(context, feature):
    # Features ported from "...FromExplorer" render the mobile report inside an iframe,
    # "...FromUrl" features open the report directly (Cypress: new HomePage(true/false))
    context.use_iframe = "from_explorer" in feature.tags

def before_scenario(context, scenario):
    # Cypress `cy.wrap(...).as(alias)` equivalent: values shared between steps of a scenario
    context.aliases = {}
    new_browser_context(context)

def after_scenario(context, scenario):
    # Capture screenshot on failure for Allure report
    if scenario.status == "failed":
        screenshot = context.page.screenshot(full_page=True)
        allure.attach(
            screenshot,
            name="Failure Screenshot",
            attachment_type=allure.attachment_type.PNG
        )
    context.browser_context.close()

def after_all(context):
    # Safely close browser if it was initialized
    if hasattr(context, "browser"):
        context.browser.close()
    if hasattr(context, "playwright"):
        context.playwright.stop()
