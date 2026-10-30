import re
from datetime import datetime

from playwright.sync_api import expect

from config.constants import RECENT_VISITS_LABELS
from pages.mobile_reports_iframe_base_page import MobileReportsIframeBasePage
from utils.test_data import load_test_data

test_data = load_test_data("recentVisitsPageTestData")


def contains(text: str):
    return re.compile(re.escape(text))


def exact(text: str):
    return re.compile(f"^{re.escape(text)}$")


class RecentVisitsPage(MobileReportsIframeBasePage):
    def __init__(self, page, use_iframe: bool):
        super().__init__(page, use_iframe)

    def check_page_title_contains(self, page_title: str):
        expect(self.page).to_have_title(page_title)

    def get_visit_id_search_field(self):
        return self.page.locator('.input-with-icon > input[placeholder="Visit ID"]')

    def get_explorer_visits_search_button(self):
        return self.page.locator(".input-with-icon > .button")

    def get_three_dots_menu_in_report(self):
        return self.root().locator('[src="ellipsis"]')

    def get_three_dots_menu_item_in_report(self):
        return self.root().locator(".menu-item")

    def get_recent_visits_page_header_title(self):
        return self.root().locator(".header-title")

    def get_recent_visits_page_title_text(self):
        return self.root().locator(".recent-visits-title-text")

    def get_recent_visits_link(self):
        return self.root().locator(".recent-visit-link")

    def get_recent_visit_user(self):
        return self.root().locator(".recent-visit-user")

    def get_visit_type_label(self):
        return self.root().locator(".visit-type")

    def get_visit_type(self):
        return self.root().locator(".visit-type > span")

    def get_visit_date_label(self):
        return self.root().locator(".visit-date")

    def get_visit_date(self):
        return self.root().locator(".visit-date > span")

    def get_recent_visits_cards_arrows(self):
        return self.root().locator(".trax-icon-arrow-small-right")

    def get_recent_visits_filter_button(self):
        return self.root().locator(".trax-icon-filter-empty")

    def get_recent_visits_filter_dropdown_button(self):
        return self.root().locator(".trax-ng-select")

    def get_recent_visits_filtered_user(self):
        return self.root().locator(".ng-option")

    def get_filter_box_applied_value(self):
        return self.root().locator(".ng-value-label")

    def get_filter_box_applied_value_clear_button(self):
        return self.root().locator(".ng-value-icon")

    def get_filter_box_applied_value_clear_all_button(self):
        return self.root().locator(".ng-clear-wrapper")

    def get_visit_summary_sub_header_user_and_store_names_section(self):
        return self.root().locator(".visit-summary-subheader-section")

    def get_visit_summary_sub_header_date_and_time_section(self):
        return self.root().locator(".visit-summary-subheader > div:nth-child(2)")

    @staticmethod
    def _texts(locator):
        expect(locator.first).to_be_attached()
        return locator.evaluate_all("elements => elements.map(element => element.textContent)")

    def click_three_dots_menu_in_report(self):
        self.get_three_dots_menu_in_report().click()

    def verify_recent_visits_menu_item_display(self):
        menu_item = self.get_three_dots_menu_item_in_report().filter(
            has_text=contains(RECENT_VISITS_LABELS["recentVisits"])
        )
        expect(menu_item.first).to_be_visible()

    def click_recent_visits_menu_item(self):
        self.get_three_dots_menu_item_in_report().filter(
            has_text=contains(RECENT_VISITS_LABELS["recentVisits"])
        ).first.click()

    def verify_recent_visits_page_title(self):
        title = self.get_recent_visits_page_header_title().filter(
            has_text=contains(RECENT_VISITS_LABELS["recentVisits"])
        )
        expect(title).not_to_have_count(0)

    def verify_recent_visits_page_title_text(self):
        expect(self.get_recent_visits_page_title_text()).to_have_text(
            exact(f" Showing {test_data['visitsCount']} visits ")
        )

    def verify_recent_visit_users(self):
        users = self.get_recent_visit_user()
        expect(users.filter(has_text=contains(test_data["userName1"]))).not_to_have_count(0)
        expect(users.filter(has_text=contains(test_data["userName2"]))).not_to_have_count(0)

    def verify_recent_visits_links_count(self):
        expect(self.get_recent_visits_link()).to_have_count(test_data["visitsCount"])

    def verify_visit_type_labels(self):
        for text in self._texts(self.get_visit_type_label()):
            assert RECENT_VISITS_LABELS["visitType"] in text

    def verify_visit_types(self):
        for text in self._texts(self.get_visit_type()):
            assert text == test_data["visitTypeStandardVisit"]

    def verify_visit_date_labels(self):
        for text in self._texts(self.get_visit_date_label()):
            assert RECENT_VISITS_LABELS["date"] in text

    def verify_visit_date(self):
        expect(self.get_visit_date().first).to_have_text(exact(test_data["dateAndTime1"]))

    def verify_recent_visit_date_and_time_sorting(self):
        dates = [datetime.strptime(text, "%b %d, %Y %I:%M %p") for text in self._texts(self.get_visit_date())]
        assert dates == sorted(dates, reverse=True), "Date and times are sorted"

    def verify_recent_visits_cards_arrows(self):
        expect(self.get_recent_visits_cards_arrows().first).to_be_visible()

    def verify_recent_visits_filter_button(self):
        expect(self.get_recent_visits_filter_button()).to_be_visible()

    def filter_recent_visits_by_single_user(self, user_name: str):
        self.get_recent_visits_filter_button().click()
        dropdown = self.get_recent_visits_filter_dropdown_button()
        dropdown.click()
        dropdown.press_sequentially(user_name)
        self.get_recent_visits_filtered_user().click()

    def verify_filter_box_applied_value(self):
        expect(self.get_filter_box_applied_value()).to_have_text(exact(test_data["userName1"]))

    def verify_filtered_recent_visits(self):
        expect(self.get_recent_visits_link()).to_have_count(test_data["filteredVisitsCountForUser1"])
        users = self.get_recent_visit_user()
        expect(users.filter(has_text=contains(test_data["userName1"]))).not_to_have_count(0)
        expect(users.filter(has_text=contains(test_data["userName2"]))).to_have_count(0)

    def _verify_filter_box_cleared(self):
        dropdown = self.get_recent_visits_filter_dropdown_button().first
        expect(dropdown).not_to_have_class(re.compile("ng-value-label"))
        expect(dropdown).not_to_have_class(re.compile("ng-value-icon"))

    def verify_filter_box_applied_value_clear_button(self):
        clear_button = self.get_filter_box_applied_value_clear_button()
        expect(clear_button).to_be_visible()
        clear_button.click()
        self._verify_filter_box_cleared()
        self.get_recent_visits_filter_button().click()

    def filter_recent_visits_by_multiple_users(self):
        self.get_recent_visits_filter_button().click()
        self.get_recent_visits_filter_dropdown_button().click()
        users = self.get_recent_visits_filtered_user()
        expect(users.first).to_be_visible()
        for user in users.element_handles():
            user.click()

    def verify_filter_box_applied_multiple_values(self):
        values = self.get_filter_box_applied_value()
        expect(values.filter(has_text=contains(test_data["userName1"]))).not_to_have_count(0)
        expect(values.filter(has_text=contains(test_data["userName2"]))).not_to_have_count(0)

    def verify_filter_box_applied_value_multiple_clear_buttons(self):
        clear_buttons = self.get_filter_box_applied_value_clear_button()
        expect(clear_buttons).to_have_count(2)
        for index in range(2):
            expect(clear_buttons.nth(index)).to_be_visible()

    def verify_filter_box_applied_value_clear_all_button(self):
        clear_all_button = self.get_filter_box_applied_value_clear_all_button()
        expect(clear_all_button).to_be_visible()
        clear_all_button.click()
        self._verify_filter_box_cleared()
        self.verify_recent_visit_users()

    def verify_recent_visit_link_navigation(self):
        self.get_recent_visits_link().nth(2).click()
        expect(self.get_visit_summary_sub_header_user_and_store_names_section()).to_have_text(
            exact(f"{test_data['storeName']} • {test_data['userName2']}")
        )
        expect(self.get_visit_summary_sub_header_date_and_time_section()).to_have_text(
            exact(test_data["dateAndTime2"])
        )
