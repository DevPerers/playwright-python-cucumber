from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to(self, url: str, timeout=60000):
        self.page.goto(url, wait_until="domcontentloaded", timeout=timeout)
        self.page.wait_for_load_state("load", timeout=timeout)    

    def wait_for_page_ready(self, timeout=60000):
        self.page.wait_for_load_state("domcontentloaded", timeout=timeout)
        self.page.wait_for_load_state("load", timeout=timeout)

    def get_ready_locator(self, selector, timeout=60000):
        locator = self.page.locator(selector)
        expect(locator).to_be_visible(timeout=timeout)
        expect(locator).to_be_enabled(timeout=timeout)
        return locator

    def fill_when_ready( self, selector: str, value: str, timeout=60000):
        locator = self.get_ready_locator(selector, timeout)
        locator.fill(value)

    def click_when_ready(self, selector: str, timeout=60000):
        locator = self.get_ready_locator(selector, timeout)
        locator.click(timeout=timeout, force=True)

    def get_text(self, selector: str, timeout=60000):
        locator = self.page.locator(selector)
        expect(locator).to_be_visible(timeout=timeout)
        return locator.inner_text()
