from playwright.sync_api import expect, TimeoutError as PlaywrightTimeoutError
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = "#input-userName"
    PASSWORD_INPUT = "#input-password"
    LOGIN_BUTTON = "#login-button"
    FLASH_MESSAGE = "#flash"
    ERROR_MESSAGE = "#error-message"
    AUTH_PAGE_URL_PATTERN = "**/auth/v4.2/authentication-code**"

    def verify_is_on_login_page(self):
        self.wait_for_page_ready()
        expect(self.page.locator(self.USERNAME_INPUT)).to_be_visible(timeout=60000)

    def verify_login_page_ui_elements_visible(self):
        self.wait_for_page_ready()
        expect(self.page.locator(self.USERNAME_INPUT)).to_be_visible(timeout=60000)
        expect(self.page.locator(self.PASSWORD_INPUT)).to_be_visible(timeout=60000)
        expect(self.page.locator(self.LOGIN_BUTTON)).to_be_visible(timeout=60000)

    def enter_username(self, username: str):
        self.fill_when_ready( self.USERNAME_INPUT, username)

    def enter_password(self, password: str):
        self.fill_when_ready( self.PASSWORD_INPUT, password)

    def click_login(self):
        # The homepage login form redirects to a second, separate auth
        # form (same field ids, values carried over) that actually
        # validates the credentials. A single click only performs the
        # redirect, so submit again once we land on that form.
        self.click_when_ready(self.LOGIN_BUTTON)
        try:
            self.page.wait_for_url(self.AUTH_PAGE_URL_PATTERN, timeout=60000)
            self.click_when_ready(self.LOGIN_BUTTON)
        except PlaywrightTimeoutError:
            pass

    def get_flash_message(self) -> str:
        return self.get_text(self.FLASH_MESSAGE)

    def verify_error_message(self, expected_message: str, timeout: int = 60000):
        error_locator = self.page.locator(self.ERROR_MESSAGE)
        expect(error_locator).to_contain_text(expected_message, timeout=timeout)
