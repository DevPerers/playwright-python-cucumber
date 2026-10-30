import re
import time
from datetime import datetime

from playwright.sync_api import Locator, Page, expect

from config.constants import (
    ACTIONS_PAGE_USER_FEEDBACK_BUTTONS,
    RECALCULATION_POP_UP,
    RECALCULATION_SECTION_COLORS,
    RECALCULATION_STATUSES,
    URL_SEGMENTS,
)
from pages.mobile_reports_iframe_base_page import MobileReportsIframeBasePage
from utils.test_data import load_test_data

test_data = load_test_data("actionsPageTestData")
reporting_configurations_test_data = load_test_data("reportingConfigurationsTestData")

TIMESTAMP_FORMAT = re.compile(r"^[A-Z][a-z]{2}\s\d{1,2},\s\d{4}\s\d{1,2}:\d{2}\s(AM|PM)$")


def contains_text(text: str):
    """Case sensitive substring match, like Cypress `.contains()` (Playwright `has_text` strings are case insensitive)."""
    return re.compile(re.escape(text))


class ActionsPage(MobileReportsIframeBasePage):
    def __init__(self, page: Page, use_iframe: bool):
        super().__init__(page, use_iframe)
        self.feedback_submitted_at = None

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------
    def _find(self, selector: str) -> Locator:
        return self.get_mobile_report_iframe_body().locator(selector)

    def _contains(self, selector: str, text: str) -> Locator:
        return self._find(selector).filter(has_text=contains_text(text)).first

    @staticmethod
    def _expect_text_contains(locator: Locator, text: str):
        expect(locator.filter(has_text=contains_text(text)).first).to_be_attached()

    @staticmethod
    def _expect_text_not_contains(locator: Locator, text: str):
        expect(locator.first).to_be_attached()
        expect(locator.filter(has_text=contains_text(text))).to_have_count(0)

    def _retry(self, assertion, timeout=5000):
        deadline = time.monotonic() + timeout / 1000
        while True:
            try:
                return assertion()
            except AssertionError:
                if time.monotonic() > deadline:
                    raise
                self.page.wait_for_timeout(250)

    def _joined_text(self, locator: Locator) -> str:
        expect(locator.first).to_be_attached()
        return "".join(locator.all_text_contents())

    # ------------------------------------------------------------------
    # Locators
    # ------------------------------------------------------------------
    def check_page_title_contains(self, page_title: str):
        expect(self.page).to_have_title(page_title)

    def get_visit_id_search_field(self) -> Locator:
        return self.page.locator('.input-with-icon > input[placeholder="Visit ID"]')

    def get_explorer_visits_search_button(self) -> Locator:
        return self.page.locator(".input-with-icon > .button")

    def get_mobile_report_header_title(self) -> Locator:
        return self._find(".header-title")

    def get_three_dots_menu_in_report(self) -> Locator:
        return self._find('[src="ellipsis"]')

    def get_three_dots_menu_item_in_report(self) -> Locator:
        return self._find(".menu-item")

    def get_actions_button(self) -> Locator:
        return self._contains(".trax-btn", "ACTIONS")

    def get_actions_group_header_title_on_actions_page(self) -> Locator:
        return self._find(".action-group-header > h2")

    def get_actions_list_on_actions_page(self) -> Locator:
        return self._find(".action-list-container")

    def get_action_item_on_actions_page(self) -> Locator:
        return self._find("trx-action-item")

    def get_count_badge_on_actions_page(self) -> Locator:
        return self._find(".count-badge")

    def get_back_arrow_on_actions_page(self) -> Locator:
        return self._find(".back-arrow")

    def get_handled_tab(self) -> Locator:
        return self._contains(".action-list-tabs-container-tab", "Handled")

    def get_sku_slider(self) -> Locator:
        return self._find(".slider-container")

    def get_oos_reason_button(self) -> Locator:
        return self._find(".oos")

    def get_oos_pop_up_message(self) -> Locator:
        return self._find(".pop-up-body")

    def get_category_kpi_item(self) -> Locator:
        return self._find(".category-item")

    def get_three_dots_grouping_menu_in_actions_page(self) -> Locator:
        return self._find(".grouping-menu")

    def get_three_dots_grouping_menu_item_in_actions_page(self) -> Locator:
        return self._find(".menu-item")

    def get_title_above_card_in_actions_page(self) -> Locator:
        return self._find(".title-above-card > h2")

    def get_oos_button_on_product_details_page(self) -> Locator:
        return self._contains(".trax-btn", "OOS REASON")

    def get_user_feedback_button_container_on_product_details_page(self) -> Locator:
        return self._find(".action-page-btn-container")

    def get_edit_oos_reason_button_on_product_details_page(self) -> Locator:
        return self._contains(".trax-btn", "EDIT OOS REASON")

    def get_selected_oos_reason_on_oos_pop_up(self) -> Locator:
        return self._find(".trax-icon-radiobutton-filled")

    def get_oos_reason_on_oos_pop_up(self) -> Locator:
        return self._find(".pop-up-body-message")

    def get_done_button_on_oos_pop_up(self) -> Locator:
        return self._contains(".trax-btn", "DONE")

    def get_back_arrow_on_product_details_page(self) -> Locator:
        return self._find(".back-arrow")

    def get_handled_sku_on_actions_page(self) -> Locator:
        return self._find(".handled")

    def get_oos_reason_of_the_handled_sku(self) -> Locator:
        return self._find(".action-sku-oos-reason")

    def get_submit_feedback_button(self) -> Locator:
        return self._contains(".trax-btn", "SUBMIT FEEDBACK")

    def get_recalculation_popup(self) -> Locator:
        return self._find(".recalc-popup")

    def get_recalculation_popup_image(self) -> Locator:
        return self._find(f'[src="{test_data["submitFeedbackPopUpImageUrl"]}"]')

    def get_recalculation_popup_button(self) -> Locator:
        return self._find(".recalc-btn")

    def get_recalculated_or_partially_recalculated_text_and_date_and_time_on_report_header(self) -> Locator:
        return self._find(".recalc-section-item")

    def get_recalculated_right_mark_on_report_header(self) -> Locator:
        return self._find(".trax-icon-approve")

    def get_actions_page_recalculation_button_container(self) -> Locator:
        return self._find(".actions-recalc-button-container")

    def get_user_feedback_submitted_date_and_time(self) -> Locator:
        return self._find(".action-sku-oos-date")

    def get_calender_icon_of_user_feedback_submitted_date_and_time(self) -> Locator:
        return self._find('.action-sku-oos-date > svg-icon[src="calendar"]')

    def get_invalid_barcode_icon(self) -> Locator:
        return self._find(".invalid-barcode")

    def get_partially_recalculated_section_of_report_header(self) -> Locator:
        return self._find(".visit-summary-header-recalc-section.yellow")

    def get_recalculated_section_of_report_header(self) -> Locator:
        return self._find(".visit-summary-header-recalc-section")

    def get_partially_recalculated_attention_mark_on_report_header(self) -> Locator:
        return self._find(".trax-icon-attention-fill-red")

    # ------------------------------------------------------------------
    # Explorer / report navigation
    # ------------------------------------------------------------------
    def search_by_visit_id(self, visit_id: str):
        search_field = self.get_visit_id_search_field()
        search_field.click()
        search_field.press_sequentially(visit_id)
        self.get_explorer_visits_search_button().click()

    def navigate_to_live_report_on_explorer(self, is_show_live_report_first: bool):
        if is_show_live_report_first:
            self._expect_text_contains(self.get_mobile_report_header_title(), "Live Summary")
        else:
            self._expect_text_contains(self.get_mobile_report_header_title(), "Visit Summary")
            self.get_three_dots_menu_in_report().click()
            self._contains(".menu-item", "Live Summary").click()

    def navigate_to_regular_report_on_explorer(self, is_show_live_report_first: bool):
        if not is_show_live_report_first:
            self._expect_text_contains(self.get_mobile_report_header_title(), "Visit Summary")
        else:
            self._expect_text_contains(self.get_mobile_report_header_title(), "Live Summary")
            self.get_three_dots_menu_in_report().click()
            self._contains(".menu-item", "Visit Summary").click()

    @staticmethod
    def get_expected_date_string(override_date: datetime = None, feedback_submitted_at: datetime = None) -> str:
        expected_date = override_date or feedback_submitted_at or datetime.now()
        return f"{expected_date.strftime('%b')} {expected_date.day}, {expected_date.year}"

    def _expected_date_string(self) -> str:
        return self.get_expected_date_string(feedback_submitted_at=self.feedback_submitted_at)

    def _click_and_wait_for_response(self, click, method: str, path: str):
        with self.page.expect_response(lambda r: r.request.method == method and path in r.url):
            click()

    def click_actions_button(self, is_actions_available: bool):
        if is_actions_available:
            path = "/mobile-reports/api/projects/autoqa1-int/pnb/barcode-storage-field"
        else:
            path = "/mobile-reports-new/assets/images/no-data.svg"
        self._click_and_wait_for_response(self.get_actions_button().click, "GET", path)

    def verify_actions_count(self, nth_element: int) -> str:
        """Returns the badge text (Cypress alias `savedCount`)."""
        badge = self.get_count_badge_on_actions_page().nth(nth_element)
        actions_list = self.get_actions_list_on_actions_page()
        expect(actions_list.first).to_be_attached()
        if "No actions found for this visit" in (actions_list.text_content() or ""):
            expect(badge).to_contain_text("0")
        else:
            expect(badge).to_contain_text(str(self.get_action_item_on_actions_page().count()))
        return badge.text_content()

    def click_back_arrow(self):
        self.get_back_arrow_on_actions_page().click()

    def verify_actions_count_in_actions_button(self, saved_count: str):
        expect(self.get_actions_button()).to_contain_text(saved_count)

    def page_reload(self):
        self.page.reload()

    def navigate_to_handled_tab(self):
        self.get_handled_tab().click()

    def slide_sku(self):
        """Cypress `.invoke('show')` (jQuery show) on the first SKU slider."""
        self.get_sku_slider().first.evaluate(
            "el => { el.style.display = ''; if (getComputedStyle(el).display === 'none') el.style.display = 'block'; }"
        )

    def click_oos_reason_button(self):
        self.get_oos_reason_button().first.click()

    def verify_not_showing_override_message_for_oos(self):
        message = reporting_configurations_test_data["oosMessageForOverride"]
        expect(self.get_oos_pop_up_message().first).to_be_attached()
        expect(self.get_oos_pop_up_message().filter(has_text=contains_text(message))).to_have_count(0)

    def verify_showing_expanded_oos_actions(self):
        expect(self.get_action_item_on_actions_page().first).to_be_visible()

    def click_actions_button_when_actions_collapsed(self):
        self._click_and_wait_for_response(
            self.get_actions_button().click,
            "GET",
            "/static/traxus/micro-frontends/web-components-icons/arrow-small-down.icon.svg",
        )

    def verify_not_showing_expanded_oos_actions(self):
        expect(self.get_actions_list_on_actions_page().first).not_to_have_class(re.compile(r"(^|\s)action-item-card(\s|$)"))
        kpi_name = reporting_configurations_test_data["kpiNames"][0]["kpiClientName"]
        self._expect_text_contains(self.get_actions_group_header_title_on_actions_page(), kpi_name)

    def click_category_kpi_item(self):
        self.get_category_kpi_item().first.click()

    def click_three_dots_grouping_menu_in_actions_page(self):
        self.get_three_dots_grouping_menu_in_actions_page().click()

    def verify_showing_actions_grouping_option_in_actions_page(self, grouping_option: str):
        self._expect_text_contains(self.get_three_dots_grouping_menu_item_in_actions_page(), grouping_option)

    def verify_not_showing_actions_grouping_option_in_actions_page(self, grouping_option: str):
        self._expect_text_not_contains(self.get_three_dots_grouping_menu_item_in_actions_page(), grouping_option)

    def verify_configured_grouping_option_has_selected(self, actions_page_grouping_option: str):
        item = self._contains(".menu-item", actions_page_grouping_option)
        expect(item.locator(":scope > .trax-icon-approve").first).to_be_attached()

    def verify_skus_have_ungrouped(self):
        expect(self.get_actions_list_on_actions_page().first).to_have_class(re.compile(r"(^|\s)ungrouped(\s|$)"))

    def verify_skus_have_grouped_by_category(self):
        self._expect_text_contains(self.get_title_above_card_in_actions_page(), test_data["category"])

    def verify_skus_have_grouped_by_kpi(self, kpi_name: str):
        self._expect_text_contains(self.get_title_above_card_in_actions_page(), kpi_name)

    def verify_skus_have_grouped_by_brand(self):
        self._expect_text_contains(self.get_title_above_card_in_actions_page(), test_data["brandName1"])
        self._expect_text_contains(self.get_title_above_card_in_actions_page(), test_data["brandName2"])

    # ------------------------------------------------------------------
    # Product details page / OOS handling
    # ------------------------------------------------------------------
    def click_sku(self, sku_name_for_oos_actions_handling: str):
        self.get_action_item_on_actions_page().filter(has_text=contains_text(sku_name_for_oos_actions_handling)).first.click()

    def click_oos_reason_button_on_product_details_page(self):
        button = self.get_oos_button_on_product_details_page()
        expect(button).to_be_visible()
        button.click()

    def verify_showing_default_oos_reason(self, oos_message: str):
        parent = self.get_selected_oos_reason_on_oos_pop_up().first.locator("xpath=..")
        expect(parent).to_contain_text(oos_message)

    def _click_done_button(self):
        done_button = self.get_done_button_on_oos_pop_up()
        done_button.scroll_into_view_if_needed()
        expect(done_button).to_be_visible()
        done_button.click()

    def click_done_button(self):
        self._click_done_button()

    def click_done_button_for_oos_handling_by_multi_selection(self):
        self._click_and_wait_for_response(
            self._click_done_button, "POST", f"/mobile-reports/api/projects/{test_data['project']}/oos-actions"
        )

    def click_done_button_for_oos_removing_by_multi_selection(self):
        self._click_and_wait_for_response(
            self._click_done_button, "DELETE", f"/mobile-reports/api/projects/{test_data['project']}/oos-actions"
        )

    def click_back_arrow_on_product_details_page(self):
        arrow = self.get_back_arrow_on_product_details_page()
        expect(arrow.first).to_be_visible()
        arrow.click()

    def verify_sku_is_in_handled(self, sku_name_for_oos_actions_handling: str):
        expect(self.get_handled_sku_on_actions_page().first).to_be_visible()
        self._expect_text_contains(self.get_handled_sku_on_actions_page(), sku_name_for_oos_actions_handling)

    def verify_oos_reason_of_the_handled_sku(self, oos_message: str):
        expect(self.get_oos_reason_of_the_handled_sku().first).to_be_visible()
        self._expect_text_contains(self.get_oos_reason_of_the_handled_sku(), oos_message)

    def click_edit_oos_reason_button_on_product_details_page(self):
        button = self.get_edit_oos_reason_button_on_product_details_page()
        expect(button).to_be_visible()
        button.click()

    def select_oos_reason(self, oos_message: str):
        self.get_oos_reason_on_oos_pop_up().filter(has_text=contains_text(oos_message)).first.click()

    def remove_selected_oos_reason(self):
        self.get_selected_oos_reason_on_oos_pop_up().click()

    def verify_oos_reason_button_on_product_details_page(self):
        expect(self.get_oos_button_on_product_details_page()).to_be_visible()

    def verify_sku_has_moved_to_pending_tab(self, sku_name_for_oos_actions_handling: str):
        self._expect_text_contains(self.get_action_item_on_actions_page(), sku_name_for_oos_actions_handling)

    def verify_sku_is_not_in_handled_tab(self, sku_name_for_oos_actions_handling: str):
        self._expect_text_not_contains(self.get_actions_list_on_actions_page(), sku_name_for_oos_actions_handling)

    def verify_category_order_in_actions_page(self):
        titles = self.get_title_above_card_in_actions_page()
        for index, category in enumerate(test_data["categoryOrder"]):
            self._retry(lambda: self._assert_equal(titles.nth(index).text_content(), category["categoryName"]))

    @staticmethod
    def _assert_equal(actual, expected):
        assert actual == expected, f"expected {expected!r} but got {actual!r}"

    # ------------------------------------------------------------------
    # Submit feedback / recalculation
    # ------------------------------------------------------------------
    def verify_submit_feedback_button_is_visible(self):
        expect(self.get_submit_feedback_button()).to_be_visible()

    def verify_submit_feedback_popup(self):
        self.get_submit_feedback_button().click()
        popup = self.get_recalculation_popup()
        expect(popup).to_be_visible()
        for key in ("thankYou", "popUpMessageSubLine1", "popUpMessageSubLine2", "popUpMessageSubLine3"):
            expect(popup).to_contain_text(RECALCULATION_POP_UP[key])
        expect(self.get_recalculation_popup_image().first).to_be_visible()

    def verify_submit_feedback_cancel(self):
        self._contains(".recalc-btn", "CANCEL").click(force=True)
        expect(self.get_recalculation_popup()).to_have_count(0)

    def submit_feedback(self):
        self.get_submit_feedback_button().click()
        self._contains(".recalc-btn", "SUBMIT").click(force=True)
        self.feedback_submitted_at = datetime.now()

    def verify_recalculated_text_on_report_header(self):
        header_items = self.get_recalculated_or_partially_recalculated_text_and_date_and_time_on_report_header()
        expect(header_items.first).to_contain_text(RECALCULATION_STATUSES["recalculated"])

    def verify_color_of_recalculated_text_and_date_and_time(self):
        expect(self.get_recalculated_section_of_report_header().first).to_have_css(
            "color", RECALCULATION_SECTION_COLORS["recalculated"]
        )

    def verify_recalculated_right_mark_on_report_header(self):
        expect(self.get_recalculated_right_mark_on_report_header().first).to_be_visible()

    def verify_submit_feedback_button_is_not_visible(self):
        expect(self.get_actions_page_recalculation_button_container()).to_have_count(0)

    def _verify_timestamp_text(self, locator: Locator):
        trimmed_text = (locator.text_content() or "").strip()
        expected_date_string = self._expected_date_string()
        assert TIMESTAMP_FORMAT.match(trimmed_text), (
            f"Text \"{trimmed_text}\" does not match format 'MMM D, YYYY h:mm AM/PM'"
        )
        assert expected_date_string in trimmed_text, (
            f'Header timestamp "{trimmed_text}" does not contain expected date "{expected_date_string}"'
        )

    def verify_recalculated_date_and_time(self):
        locator = self.get_recalculated_or_partially_recalculated_text_and_date_and_time_on_report_header().nth(1)
        expect(locator).to_be_attached()
        self._retry(lambda: self._verify_timestamp_text(locator))

    def verify_user_feedback_date_and_time(self):
        locator = self.get_user_feedback_submitted_date_and_time().first
        expect(locator).to_be_attached()
        self._retry(lambda: self._verify_timestamp_text(locator))

    def verify_display_calender_icon_of_user_feedback_date_and_time(self):
        expect(self.get_calender_icon_of_user_feedback_submitted_date_and_time().first).to_be_attached()

    def verify_not_display_user_feedback_date_and_time(self):
        expect(self._find("trx-action-item.action-sku-oos-date")).to_have_count(0)

    def verify_not_display_calender_icon_of_user_feedback_date_and_time(self):
        expect(self._find('trx-action-item .action-sku-oos-date > svg-icon[src="calendar"]')).to_have_count(0)

    def verify_displaying_oos_reason_button_on_product_details_page(self):
        expect(self.get_oos_button_on_product_details_page()).to_be_visible()

    def verify_not_displaying_oos_reason_button_on_product_details_page(self):
        container = self.get_user_feedback_button_container_on_product_details_page()
        expect(container.first).to_be_attached()
        expect(container.filter(has_text=contains_text(ACTIONS_PAGE_USER_FEEDBACK_BUTTONS["oosReason"]))).to_have_count(0)

    def verify_displaying_of_invalid_barcode_icon(self):
        expect(self.get_invalid_barcode_icon().first).to_be_visible()

    def verify_partially_recalculated_text_on_report_header(self):
        header_items = self.get_recalculated_or_partially_recalculated_text_and_date_and_time_on_report_header()
        expect(header_items.first).to_contain_text(RECALCULATION_STATUSES["partiallyRecalculated"])

    def verify_color_of_partially_recalculated_text_and_date_and_time(self):
        expect(self.get_partially_recalculated_section_of_report_header().first).to_have_css(
            "color", RECALCULATION_SECTION_COLORS["partiallyRecalculated"]
        )

    def verify_partially_recalculated_attention_mark_on_report_header(self):
        expect(self.get_partially_recalculated_attention_mark_on_report_header().first).to_be_visible()

    # ------------------------------------------------------------------
    # Product details page content
    # ------------------------------------------------------------------
    def get_page_title(self) -> Locator:
        return self._find(".header-title")

    def get_product_image(self) -> Locator:
        image_url = (
            URL_SEGMENTS["product_details_page_prodcut_image_url_segment"]
            + test_data["projectForProductImageUrl"]
            + test_data["productImageUrl"]
        )
        return self._find(f'[src="{image_url}"]')

    def get_product_barcode(self) -> Locator:
        return self._find(".barcode")

    def get_product_title(self) -> Locator:
        return self._find(".action-page-content-title")

    def verify_page_title(self, page_header: str):
        title = self.get_page_title()
        self._retry(lambda: self._assert_equal(self._joined_text(title).strip(), page_header))

    def verify_product_image(self):
        expect(self.get_product_image().first).to_be_visible()

    def verify_product_barcode_image(self):
        expect(self.get_product_barcode().locator('[xmlns="http://www.w3.org/2000/svg"]').first).to_be_visible()

    def verify_product_barcode(self) -> str:
        """Returns the trimmed EAN code (Cypress alias `eanCode`)."""
        barcode = self.get_product_barcode().first
        expect(barcode).to_be_visible()
        return barcode.text_content().strip()

    def verify_product_title(self) -> str:
        """Returns the trimmed product title (Cypress alias `productTitle`)."""
        title = self.get_product_title().first
        expect(title).to_be_visible()
        return title.text_content().strip()

    # ------------------------------------------------------------------
    # Multiple selection
    # ------------------------------------------------------------------
    def long_press_product_name_and_select_multiple_products(self):
        sku_names = test_data["skuNamesForOosMultipleActionsHandling"]
        items = self.get_action_item_on_actions_page()
        items.filter(has_text=contains_text(sku_names[0])).first.dispatch_event("pointerdown", {"button": 0})
        self.page.wait_for_timeout(500)  # long press doesn't work without a wait
        for sku_name in sku_names[1:]:
            items.filter(has_text=contains_text(sku_name)).first.click(force=True)

    def get_bulk_edit_icon(self) -> Locator:
        return self._find(".bulk-edit-icon")

    def verify_displaying_of_bulk_edit_icon(self):
        expect(self.get_bulk_edit_icon().first).to_be_visible()

    def get_multiple_selected_products(self) -> Locator:
        return self._find(".trax-icon-approved-filled")

    def verify_multiple_selected_product_count(self):
        expect(self.get_multiple_selected_products()).to_have_count(len(test_data["skuNamesForOosMultipleActionsHandling"]))

    def get_multiple_selected_products_count(self) -> Locator:
        return self._find("div > .bulk-count-text")

    def verify_displaying_of_multiple_selected_products_count(self):
        counter = self.get_multiple_selected_products_count()
        expected_count = len(test_data["skuNamesForOosMultipleActionsHandling"])

        def check():
            match = re.search(r"(\d+)\s+(.*)", self._joined_text(counter))
            selected_count = int(match.group(1)) if match else 0
            selected_text = match.group(2).strip() if match else ""
            self._assert_equal(selected_count, expected_count)
            self._assert_equal(selected_text, "selected")

        self._retry(check)

    def get_close_button_of_multiple_selected_products(self) -> Locator:
        return self._find(".trax-icon-close-small")

    def verify_close_button_of_multiple_selected_products(self):
        expect(self.get_close_button_of_multiple_selected_products().first).to_be_visible()

    def click_close_button_of_multiple_selected_products(self):
        self.get_close_button_of_multiple_selected_products().click()

    def verify_not_displaying_of_bulk_edit_icon(self):
        expect(self.get_bulk_edit_icon()).to_have_count(0)

    def get_all_button_label_of_multiple_selected_products(self) -> Locator:
        return self._contains(".bulk-select-text", "All")

    def get_all_button_of_multiple_selected_products(self) -> Locator:
        return self.get_all_button_label_of_multiple_selected_products().locator("xpath=..").locator(
            ".trax-icon-deactivate-filled"
        )

    def verify_all_button_of_multiple_selected_products(self):
        expect(self.get_all_button_label_of_multiple_selected_products()).to_be_visible()
        expect(self.get_all_button_of_multiple_selected_products().first).to_be_visible()

    def click_all_button_label_of_multiple_selected_products(self):
        self.get_all_button_label_of_multiple_selected_products().click()

    def verify_all_skus_are_selected(self):
        items = self.get_action_item_on_actions_page()
        selected = self.get_multiple_selected_products()
        expect(items.first).to_be_attached()
        self._retry(lambda: self._assert_equal(items.count(), selected.count() - 3))

    def get_oos_reason_button_of_multiple_selected_products(self) -> Locator:
        return self._find(".oos-button")

    def click_oos_reason_button_of_multiple_selected_products(self):
        button = self.get_oos_reason_button_of_multiple_selected_products()
        expect(button.first).to_be_visible()
        button.click()

    def verify_handling_of_multiple_selected_products_by_oos_reason(self):
        expect(self.get_handled_sku_on_actions_page().first).to_be_visible()
        for sku_name in test_data["skuNamesForOosMultipleActionsHandling"]:
            self._expect_text_contains(self.get_handled_sku_on_actions_page(), sku_name)

    def get_pending_tab(self) -> Locator:
        return self._contains(".action-list-tabs-container-tab", "Pending")

    def navigate_to_pending_tab(self):
        self.get_pending_tab().click()
        # the page is not loaded properly without a wait and there is no request to wait for
        self.page.wait_for_timeout(500)

    def verify_multiple_skus_have_moved_to_pending_tab(self, sku_names_for_oos_actions_handling):
        sku_names = [sku_names_for_oos_actions_handling] if isinstance(sku_names_for_oos_actions_handling, str) else sku_names_for_oos_actions_handling
        for sku_name in sku_names:
            self._expect_text_contains(self.get_action_item_on_actions_page(), sku_name)

    def verify_multiple_skus_are_not_in_handled_tab(self, sku_names_for_oos_actions_handling):
        sku_names = [sku_names_for_oos_actions_handling] if isinstance(sku_names_for_oos_actions_handling, str) else sku_names_for_oos_actions_handling
        for sku_name in sku_names:
            self._expect_text_not_contains(self.get_actions_list_on_actions_page(), sku_name)

    # ------------------------------------------------------------------
    # Renamed OOS reason buttons
    # ------------------------------------------------------------------
    def get_renamed_oos_reason_button_on_product_details_page(self, renamed_oos_reason_button_name: str) -> Locator:
        return self._contains(".trax-btn", renamed_oos_reason_button_name)

    def verify_displaying_renamed_oos_reason_button_on_product_details_page(self, renamed_oos_reason_button_name: str):
        expect(self.get_renamed_oos_reason_button_on_product_details_page(renamed_oos_reason_button_name)).to_be_visible()

    def verify_displaying_renamed_oos_reason_button_for_sliding(self, renamed_oos_reason_button_name: str):
        button = self.get_oos_reason_button().first
        expect(button).to_be_visible()
        expect(button).to_contain_text(renamed_oos_reason_button_name)

    def get_back_arrow_on_mobile_report(self) -> Locator:
        return self._find(".back-arrow")

    def click_on_back_arrow(self):
        self.get_back_arrow_on_mobile_report().click()

    def verify_displaying_renamed_oos_reason_button_for_multiple_selection(self, renamed_oos_reason_button_name: str):
        button = self.get_oos_reason_button_of_multiple_selected_products().first
        expect(button).to_be_visible()
        expect(button).to_contain_text(renamed_oos_reason_button_name)

    def verify_displaying_renamed_edit_oos_reason_button_for_sliding(self, renamed_edit_oos_reason_button_name: str):
        button = self.get_oos_reason_button().first
        expect(button).to_be_visible()

        def check():
            text = re.sub(r"\s+", " ", (button.text_content() or "").replace("&nbsp;", "")).strip()
            assert renamed_edit_oos_reason_button_name in text, f"{renamed_edit_oos_reason_button_name!r} not in {text!r}"

        self._retry(check)


MobileReportActionsPage = ActionsPage
