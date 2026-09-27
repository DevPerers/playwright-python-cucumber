from pages.base_page import BasePage
from playwright.sync_api import expect

class HomePage(BasePage):
    APP_NAME_SPAN = ".application-name.trax-tst-app-name"

    def is_logout_visible(self) -> bool:
        return self.page.is_visible(self.LOGOUT_BUTTON)

    def verify_is_on_home_page(self):
        self.wait_for_page_ready()
        element = self.page.locator(self.APP_NAME_SPAN)
        expect(element).to_be_visible(timeout=10000)
        expect(element).to_have_text("Homepage ")
