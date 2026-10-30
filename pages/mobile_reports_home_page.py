from contextlib import ExitStack
from decimal import Decimal, ROUND_HALF_UP

from playwright.sync_api import Locator, expect

from config.constants import DELTA_COLORS, MOBILE_REPORT_HEADER_TITLES, RECENT_VISITS_LABELS
from pages.mobile_reports_iframe_base_page import MobileReportsIframeBasePage


def _to_number(text: str) -> float:
    """JS Number(): blank string is 0, unparsable text is NaN."""
    text = text.strip()
    if not text:
        return 0.0
    try:
        return float(text)
    except ValueError:
        return float("nan")


def _to_fixed_2(value: float) -> str:
    """JS Number.prototype.toFixed(2): ties round away from zero."""
    if value != value:
        return "NaN"
    return str(Decimal(value).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


class MobileReportsHomePage(MobileReportsIframeBasePage):
    def __init__(self, page, use_iframe: bool):
        super().__init__(page, use_iframe)

    def check_page_title_contains(self, page_title: str):
        expect(self.page).to_have_title(page_title)

    def get_visit_status(self) -> Locator:
        return self.page.locator('div[class="explorer-viewer-sub-header-bottom-left"]>span:nth-child(7) div')

    def get_visit_id_search_field(self) -> Locator:
        return self.page.locator('input[placeholder="Search ID Num"]')

    def get_explorer_visits_search_button(self) -> Locator:
        return self.page.locator(".trax-icons-search")

    def get_mobile_report_header_title(self) -> Locator:
        return self.root().locator(".header-title")

    def get_old_mobile_report_header_title(self) -> Locator:
        return self.root().locator(".mobile-reports-header-title")

    def get_kpi_circle_titles(self) -> Locator:
        return self.root().locator('[id="kpi-title"]')

    def get_kpi_circle_value(self) -> Locator:
        return self.root().locator("circle-progress > svg > text > tspan:nth-child(1)")

    def get_kpi_delta_value(self) -> Locator:
        return self.root().locator('[id="circle-subtitle"]')

    def get_three_dots_menu_in_report(self) -> Locator:
        return self.root().locator('[src="ellipsis"]')

    def get_three_dots_menu_item_in_report(self) -> Locator:
        return self.root().locator(".menu-item")

    def get_recent_visitslink(self, recent_visit_url: str) -> Locator:
        return self.root().locator(f'[href="{recent_visit_url}"]')

    def verify_visit_completion(self):
        expect(self.get_visit_status().first).to_contain_text("Completed")

    def verify_report_header_title(self, report_header_title: str):
        expect(self.get_mobile_report_header_title().first).to_contain_text(report_header_title)

    def verify_old_report_header_title(self, report_header_title: str):
        expect(self.get_old_mobile_report_header_title().first).to_contain_text(report_header_title)

    def save_kpi_circle_title_values_in_mobile_report(self, index: int, alias: str, aliases: dict):
        aliases[alias] = self.get_kpi_circle_titles().nth(index).text_content()

    def save_kpi_circle_values(self, index: int, kpi_circle_value: str, aliases: dict):
        aliases[kpi_circle_value] = self.get_kpi_circle_value().nth(index).text_content()

    def save_kpi_delta_values(self, index: int, kpi_delta_value: str, aliases: dict):
        aliases[kpi_delta_value] = self.get_kpi_delta_value().nth(index).text_content()

    def click_three_dots_menu_in_report(self):
        self.get_three_dots_menu_in_report().click()

    def click_recent_visits_menu_item(self):
        self.get_three_dots_menu_item_in_report().filter(has_text=RECENT_VISITS_LABELS["recentVisits"]).first.click()

    def navigate_to_recent_visit(self, recent_visit_url: str):
        self.get_recent_visitslink(recent_visit_url).click()

    def save_kpi_circle_values_of_previous_visit(
        self, index: int, kpi_circle_value_of_previous_visit: str, aliases: dict
    ):
        aliases[kpi_circle_value_of_previous_visit] = self.get_kpi_circle_value().nth(index).text_content()

    def verify_delta_values(
        self,
        kpi_circle_value_of_current_visit: str,
        kpi_circle_value_of_previous_visit: str,
        kpi_delta_value: str,
        aliases: dict,
    ):
        current_circle_value = _to_number(aliases[kpi_circle_value_of_current_visit])
        previous_circle_value = _to_number(aliases[kpi_circle_value_of_previous_visit])
        delta_value_should_be = _to_fixed_2(current_circle_value - previous_circle_value)

        delta_value = aliases[kpi_delta_value].replace("+", "", 1).replace("%", "", 1)
        delta_value_of_current_visit = _to_fixed_2(_to_number(delta_value))
        assert delta_value_of_current_visit == delta_value_should_be

    def get_kpi_circle_area(self, kpi_name: str) -> Locator:
        return self.root().locator("trx-kpi-circle").get_by_text(kpi_name).first.locator("xpath=..")

    def get_kpi_circle(self, kpi_name: str) -> Locator:
        return self.get_kpi_circle_area(kpi_name).locator("path")

    def get_kpi_circle_value_and_percentage_icon(self, kpi_name: str) -> Locator:
        return self.get_kpi_circle_area(kpi_name).locator("tspan:nth-child(1), tspan:nth-child(2)")

    def verify_kpi_circle_color(self, kpi_name: str, color: str):
        expect(self.get_kpi_circle(kpi_name).first).to_have_attribute("stroke", color)

    def verify_kpi_value_color(self, kpi_name: str, color: str):
        expect(self.get_kpi_circle_value_and_percentage_icon(kpi_name).first).to_have_attribute("fill", color)

    def get_trax_user_icon(self) -> Locator:
        return self.page.locator(".trax-tst-usr-icon")

    def get_trax_logout_button(self) -> Locator:
        return self.page.locator(".trax-tst-logout-link")

    def get_login_form(self) -> Locator:
        return self.page.locator('form[id="login-form"]')

    def get_login_title(self) -> Locator:
        return self.page.locator(".title")

    def get_username_placeholder(self) -> Locator:
        return self.page.locator('[placeholder="Username"]')

    def get_password_placeholder(self) -> Locator:
        return self.page.locator('[placeholder="Password"]')

    def get_login_button(self) -> Locator:
        return self.page.locator('[id="login-button"]')

    def get_mobile_report_through_url(self) -> Locator:
        return self.root().locator("trx-visit-summary")

    def get_mobile_report_header(self) -> Locator:
        return self.root().locator(".visit-summary-header")

    def click_trax_user_icon(self):
        self.get_trax_user_icon().click()

    def click_trax_logout_button(self):
        self.get_trax_logout_button().click()

    def _navigate_and_check_responses(self, url_parts: list, navigate_fn, expected_status: int):
        """cy.intercept + cy.wait: wait for a GET response per URL part while navigating."""
        with ExitStack() as stack:
            response_infos = [
                stack.enter_context(
                    self.page.expect_response(
                        lambda response, part=url_part: response.request.method == "GET" and part in response.url,
                        timeout=60000,
                    )
                )
                for url_part in url_parts
            ]
            navigate_fn()
        for url_part, response_info in zip(url_parts, response_infos):
            assert response_info.value.status == expected_status, f"{url_part} returned {response_info.value.status}"

    def verify_user_is_inaccessible_to_report(self, navigate_fn, project_name: str):
        self._navigate_and_check_responses(
            [f"/user-management/api/projects/{project_name}/authorize", "/user-management/api/my-user"],
            navigate_fn,
            401,
        )

    def verify_user_is_redirected_to_login_page(self):
        expect(self.get_login_form()).to_be_visible()
        expect(self.get_login_title()).to_be_visible()
        expect(self.get_login_title()).to_contain_text("Login to")
        expect(self.get_username_placeholder()).to_be_visible()
        expect(self.get_password_placeholder()).to_be_visible()
        expect(self.get_login_button()).to_be_visible()

    def verify_user_is_accessible_to_report(self, navigate_fn, project_name: str, session_uid: str):
        self._navigate_and_check_responses(
            [
                f"/user-management/api/projects/{project_name}/authorize",
                "/user-management/api/my-user",
                f"/explorer/api/projects/{project_name}/visit/{session_uid}?apiPrefix=explorer",
            ],
            navigate_fn,
            200,
        )

    def verify_displaying_of_mobile_report(self):
        expect(self.get_mobile_report_through_url()).to_be_visible()
        expect(self.get_mobile_report_header()).to_be_visible()
        expect(self.get_mobile_report_header()).to_contain_text(MOBILE_REPORT_HEADER_TITLES["regularReportHeaderTitle"])

    def verify_not_displaying_of_mobile_report(self):
        expect(self.get_mobile_report_through_url()).to_have_count(0)

    def verify_kpi_circle_title(self, expected_kpi_circle_title: str):
        expect(self.get_kpi_circle_titles().nth(1)).to_have_text(expected_kpi_circle_title)

    def verify_delta_color_in_mobile_report(self, kpi_index: int, delta_coloring_method: str):
        delta_coloring_method = str(delta_coloring_method).strip()
        delta_value_element = self.get_kpi_delta_value().nth(kpi_index)
        delta_value_text = delta_value_element.text_content().strip()
        delta_value = _to_number(delta_value_text.replace("%", "", 1).replace("+", "", 1))

        expected_color = ""
        if delta_coloring_method == "Positive":
            expected_color = DELTA_COLORS["positiveDeltaColor"] if delta_value > 0 else DELTA_COLORS["negativeDeltaColor"]
        elif delta_coloring_method == "Negative":
            expected_color = DELTA_COLORS["positiveDeltaColor"] if delta_value < 0 else DELTA_COLORS["negativeDeltaColor"]
        expect(delta_value_element).to_have_css("color", expected_color)
