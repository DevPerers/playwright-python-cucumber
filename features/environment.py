import os
import allure
from playwright.sync_api import sync_playwright

def before_all(context):
    # Check if HEADLESS environment variable is set to "false"
    is_headless = os.getenv("HEADLESS", "true").lower() == "true"
    
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=is_headless)

def before_scenario(context, scenario):
    context.page = context.browser.new_page()

def after_scenario(context, scenario):
    # Capture screenshot on failure for Allure report
    if scenario.status == "failed":
        screenshot = context.page.screenshot(full_page=True)
        allure.attach(
            screenshot,
            name="Failure Screenshot",
            attachment_type=allure.attachment_type.PNG
        )
    context.page.close()

def after_all(context):
    # Safely close browser if it was initialized
    if hasattr(context, "browser"):
        context.browser.close()
    if hasattr(context, "playwright"):
        context.playwright.stop()