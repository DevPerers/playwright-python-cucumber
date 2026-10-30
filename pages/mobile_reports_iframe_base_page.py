from playwright.sync_api import Locator, Page

from pages.base_page import BasePage


class MobileReportsIframeBasePage(BasePage):
    """Base page for the mobile report, which is rendered inside an iframe when
    opened from the Explorer and directly in the page when opened by URL.

    `root()` returns the scope that report elements must be searched in: the iframe
    content when `use_iframe` is true, otherwise the whole page. Both expose
    `.locator(...)`.
    """

    IFRAME_SELECTOR = "iframe.mobile-reports-online-iframe"

    def __init__(self, page: Page, use_iframe: bool):
        super().__init__(page)
        self.use_iframe = use_iframe

    def get_mobile_report_iframe(self) -> Locator:
        return self.page.locator(self.IFRAME_SELECTOR) if self.use_iframe else self.page.locator("body")

    def root(self):
        """Scope in which the mobile report content lives (FrameLocator or Page)."""
        return self.page.frame_locator(self.IFRAME_SELECTOR) if self.use_iframe else self.page

    def get_mobile_report_iframe_body(self) -> Locator:
        return self.root().locator("body")

    def search_by_visit_id(self, visit_id: str):
        search_input = self.page.locator('input[placeholder="Visit ID"]')
        with self.page.expect_response(
            lambda response: response.url.endswith(
                "/static/traxus/micro-frontends/web-components-icons/ellipsis.icon.svg"
            )
        ) as response_info:
            search_input.click()
            search_input.press_sequentially(visit_id)
            search_input.press("Enter")
        assert response_info.value.status == 200
