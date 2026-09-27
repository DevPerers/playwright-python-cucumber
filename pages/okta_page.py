import re
from pages.base_page import BasePage
from playwright.sync_api import expect

class OktaLoginPage(BasePage):
    USERNAME_INPUT = "#okta-signin-username"
    PASSWORD_INPUT = "#okta-signin-password"
    LOGIN_BUTTON = "#okta-signin-submit"

    def verify_is_on_okta_page(self):
        self.wait_for_page_ready()
        expect(self.page.locator(self.USERNAME_INPUT)).to_be_visible(timeout=60000)

    def enter_username(self, username: str):
        self.fill_when_ready(self.USERNAME_INPUT, username)

    def enter_password(self, password: str):
        self.fill_when_ready(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click_when_ready(self.LOGIN_BUTTON)
