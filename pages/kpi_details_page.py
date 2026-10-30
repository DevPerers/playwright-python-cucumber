from playwright.sync_api import expect

from pages.mobile_reports_iframe_base_page import MobileReportsIframeBasePage
from utils.test_data import load_test_data

TEST_DATA = load_test_data("kpiDetailsPageTestData")


class KpiDetailsPage(MobileReportsIframeBasePage):

    def check_page_title_contains(self, page_title: str):
        expect(self.page).to_have_title(page_title)

    def get_visit_id_search_field(self):
        return self.page.locator('.input-with-icon > input[placeholder="Visit ID"]')

    def get_explorer_visits_search_button(self):
        return self.page.locator(".input-with-icon > .button")

    def get_kpi_circle_titles(self):
        return self.get_mobile_report_iframe_body().locator('[id="kpi-title"]')

    def get_kpi_circle(self):
        return self.get_mobile_report_iframe_body().locator("trx-kpi-circle")

    def get_kpi_reference_image_button(self):
        return self.get_mobile_report_iframe_body().locator(".reference-images-button")

    def get_kpi_reference_image(self):
        return self.get_mobile_report_iframe_body().locator(f'[src="{TEST_DATA["kpiReferenceImageUrl"]}"]')

    def get_kpi_reference_image_text(self):
        return self.get_mobile_report_iframe_body().locator(".image-title")

    def search_by_visit_id(self, visit_id: str):
        search_field = self.get_visit_id_search_field()
        search_field.click()
        search_field.press_sequentially(visit_id)
        self.get_explorer_visits_search_button().click()

    def navigate_to_kpi_details_page(self, kpi_circle_name: str):
        self.get_kpi_circle().filter(has_text=kpi_circle_name).first.click()

    def verify_showing_kpi_reference_image_button(self):
        expect(self.get_kpi_reference_image_button()).to_be_visible()

    def click_kpi_reference_image_button(self):
        self.get_kpi_reference_image_button().click()

    def verify_showing_kpi_reference_image(self):
        expect(self.get_kpi_reference_image()).to_be_visible()

    def verify_showing_kpi_reference_image_text(self):
        expect(self.get_kpi_reference_image_text()).to_have_text(TEST_DATA["kpiReferenceImageText"])

    def verify_not_showing_kpi_reference_image_button(self):
        expect(self.get_mobile_report_iframe_body()).not_to_contain_text(".reference-images-button")
        expect(self.get_kpi_reference_image_button()).to_have_count(0)

    def get_kpi_entity_names(self):
        return self.get_mobile_report_iframe_body().locator(".kpi-data-name")

    def get_kpi_entities_sorting_menu_button(self):
        return self.get_mobile_report_iframe_body().locator(".trax-icon-ellipsis")

    def get_kpi_entities_sorting_menu_items(self):
        return self.get_mobile_report_iframe_body().locator(".menu-item-left-side")

    def get_live_regular_report_switch_button(self):
        return self.get_mobile_report_iframe_body().locator(".visit-summary-header > .trax-icon-ellipsis")

    def get_navigating_menu_button_to_regular_report(self):
        return self.get_mobile_report_iframe_body().locator(".menu-item").filter(has_text="Visit Summary").first

    def get_column_headers_of_kpi_entities(self):
        return self.get_mobile_report_iframe_body().locator(".first-column-header")

    def get_kpi_entity_values(self):
        return self.get_mobile_report_iframe_body().locator('[data-column="3"] > .kpi-data-value')

    def get_right_sign_of_selected_sorting_option(self):
        return self.get_mobile_report_iframe_body().locator(".trax-icon-approve")

    def get_upside_arrow_icon_for_ascending_order(self):
        return self.get_mobile_report_iframe_body().locator(".menu-item > .icon-container > .trax-icon-arrow-small-up")

    def get_downside_arrow_icon_for_descending_order(self):
        return self.get_mobile_report_iframe_body().locator(
            ".menu-item > .icon-container > .trax-icon-arrow-small-down"
        )

    def navigate_to_regular_report(self):
        self.get_live_regular_report_switch_button().click()
        self.get_navigating_menu_button_to_regular_report().click()

    def capture_kpi_entity_names(self, aliases: dict = None) -> list:
        entity_names = self.get_kpi_entity_names()
        entity_names.first.wait_for()
        names = [name.strip() for name in entity_names.all_text_contents()]
        if aliases is not None:
            aliases["kpiEntityNames"] = names
        return names

    def capture_kpi_entity_column_headers(self, aliases: dict = None) -> str:
        headers = self.get_column_headers_of_kpi_entities()
        headers.first.wait_for()
        text = "".join(headers.all_text_contents())
        if aliases is not None:
            aliases["kpiEntityHeaders"] = text
        return text

    def click_kpi_entities_sorting_menu_button(self):
        self.get_kpi_entities_sorting_menu_button().click()

    def verify_kpi_entities_names_showing_in_sorting_menu(self, aliases: dict):
        self.click_kpi_entities_sorting_menu_button()
        menu_items = self.get_kpi_entities_sorting_menu_items()
        menu_items.first.wait_for()
        item_texts = menu_items.all_text_contents()
        kpi_entity_names = aliases["kpiEntityNames"]
        max_comparisons = min(len(kpi_entity_names), len(item_texts) - 1)
        for i in range(max_comparisons):
            assert item_texts[i + 1].strip() == kpi_entity_names[i]

    def verify_kpi_entity_header_in_sorting_menu(self, aliases: dict):
        first_menu_item = self.get_kpi_entities_sorting_menu_items().first
        expect(first_menu_item).to_be_attached()
        assert first_menu_item.text_content().strip() == aliases["kpiEntityHeaders"].strip()

    def sort_kpi_entities_by_selecting_sorting_option(self, option_name: str):
        self.get_kpi_entities_sorting_menu_items().filter(has_text=option_name).first.click()

    def _get_kpi_entity_numeric_values(self) -> list:
        values = self.get_kpi_entity_values()
        values.first.wait_for()
        return [float(text.strip().replace(",", "")) for text in values.all_text_contents()]

    def verify_kpi_entities_sorted_in_ascending_order(self):
        values = self._get_kpi_entity_numeric_values()
        assert values == sorted(values)

    def verify_right_sign_of_selected_sorting_option(self):
        self.click_kpi_entities_sorting_menu_button()
        expect(self.get_right_sign_of_selected_sorting_option()).to_be_visible()

    def verify_upside_arrow_icon_for_ascending_order(self):
        expect(self.get_upside_arrow_icon_for_ascending_order()).to_be_visible()

    def verify_kpi_entities_sorted_in_descending_order(self):
        values = self._get_kpi_entity_numeric_values()
        assert values == sorted(values, reverse=True)

    def verify_downside_arrow_icon_for_descending_order(self):
        expect(self.get_downside_arrow_icon_for_descending_order()).to_be_visible()
