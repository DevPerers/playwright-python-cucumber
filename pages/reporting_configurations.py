import re

from playwright.sync_api import Locator, expect

from config.constants import COLOR_THRESHOLD_COLORS_AND_BUTTON, DEFAULT_ACTIONS_PAGE_LAYOUT_DROPDOWN_VALUES
from pages.base_page import BasePage
from utils.test_data import image_path, load_test_data

TEST_DATA = load_test_data("reportingConfigurationsTestData")
NO_AVAILABLE_DATA = "No Available Data"
SHOW_ELEMENT_SCRIPT = "element => { element.style.display = 'block'; }"


def _parent(locator: Locator) -> Locator:
    return locator.locator("xpath=..")


def _clear_and_type(locator: Locator, value: str):
    locator.click()
    locator.clear()
    locator.press_sequentially(value)


class ReportingConfigurations(BasePage):

    def get_checkbox(self, checkbox_name: str):
        return self.page.locator("trax-checkbox").get_by_text(checkbox_name).first

    def get_save_button(self):
        return self.page.locator(".save-button")

    def get_save_confirm_pop_up_save_button(self):
        return self.page.locator(".xsuite-popup-button", has_text="Save").first

    def get_save_success_xsuite_pop_up_ok_button(self):
        return self.page.locator(".xsuite-popup-button", has_text="OK").first

    def get_kpis_linked_to_table(self, index: int):
        return self.page.locator("xsuite-table").nth(index)

    def get_kpis_linked_to_actions_table(self):
        return self.page.locator("xsuite-table").nth(1)

    def get_kpis_linked_to_store_table(self):
        return self.page.locator("xsuite-table").nth(0)

    def get_add_kpi_button_of_kpis_linked_to_tables(self, add_kpi: int):
        return self.page.locator(".xsuite-button-input").nth(add_kpi)

    def get_kpi_search_box_of_kpi_catalog(self):
        return self.page.locator(".search-box ")

    def get_apply_button_of_kpi_catalog(self):
        return self.page.locator(".xsuite-button", has_text="APPLY").first

    def get_kpi_select_check_box_of_kpi_catalog(self):
        return self.page.locator(".trax-tst-kpi-catalog-item-multi-select-toggle")

    def get_save_success_xsuite_pop_up_button(self):
        return self.page.locator(".xsuite-popup-button")

    def get_time_based_fraud_prevention_for_oos_reason_input_box(self):
        return self.page.locator('[ng-if="ctrl.fraudPreventionTimeOosFeatureFlag"]').locator('input[type="number"]')

    def get_time_based_fraud_prevention_for_oos_reason_check_box(self, checkbox_name: str):
        return self.page.locator("trax-checkbox").get_by_text(checkbox_name).first

    def get_region_search_box_for_oos(self):
        return self.page.locator(".xsuite-list-search-input")

    def get_selected_oos_region(self):
        return self.page.locator(".xsuite-list-item-selected")

    def get_oos_reasons_page_checkbox(self):
        return self.page.locator(".xsuite-checkbox > div")

    def get_oos_reasons_page_save_button(self):
        return self.page.locator(".button-name", has_text="SAVE").first

    def get_save_success_xsuite_pop_up_ok_button_of_oos_reasons_page(self):
        return self.page.locator(".xsuite-button", has_text="Ok").first

    def get_reporting_configurations_tabs(self):
        return self.page.locator(".tab")

    def get_kpi_page_kpi_search_box(self):
        return self.page.locator(".xsuite-list-search-input")

    def get_kpi_page_kpi_list_item(self):
        return self.page.locator(".kpis-list-item")

    def get_kpi_page_kpi_order(self):
        return self.page.locator('[ng-model="ctrl.chosenKpi.display_order"]')

    def get_default_actions_page_layout_dropdown(self):
        return self.page.locator("trax-dropdown-single").nth(1)

    def get_default_actions_page_layout_dropdown_value(self):
        return self.page.locator(".dropdown").nth(2)

    def get_default_actions_page_layout_dropdown_options(self):
        return self.page.locator(".item")

    def get_category_order_input_cells(self):
        return self.page.locator('xsuite-table[options="ctrl.categoryTableColumns"] input[type="number"]')

    def get_kpi_reference_image_file_upload_input(self):
        return self.page.locator('input[type="file"]')

    def get_kpi_reference_image_text_input(self):
        return self.page.locator('input[type="text"]').nth(3)

    def get_kpis_page_save_button(self):
        return self.page.locator(".button-name", has_text="SAVE").first

    def get_kpis_page_save_popup_ok_button(self):
        return self.page.locator(".xsuite-popup-button", has_text="OK").first

    def get_kpi_reference_image_remove_icon(self):
        return self.page.locator(".trax-icons-remove")

    def get_kpi_title_input_field(self):
        return self.page.locator('input[placeholder="title..."]')

    def check_page_title_contains(self, page_title: str):
        expect(self.page).to_have_title(page_title)

    def set_checkbox(self, checkbox_name: str, to_be_checked: bool):
        parent = _parent(self.get_checkbox(checkbox_name))
        is_checked = parent.get_attribute("checked") == "checked"
        if is_checked != to_be_checked:
            self.get_checkbox(checkbox_name).click()
            self.get_save_button().click()
            self.get_save_success_xsuite_pop_up_ok_button().click(force=True)
        self.page.reload()

    def verify_checkbox_is_checked(self, checkbox_name: str):
        expect(_parent(self.get_checkbox(checkbox_name))).to_have_attribute("checked", re.compile(".*"))

    def verify_checkbox_is_unchecked(self, checkbox_name: str):
        expect(_parent(self.get_checkbox(checkbox_name))).not_to_have_attribute("checked", re.compile(".*"))

    def _remove_all_remove_icons(self):
        for remove_icon in self.get_kpi_reference_image_remove_icon().all():
            remove_icon.evaluate(SHOW_ELEMENT_SCRIPT)
            remove_icon.click(force=True)

    def delete_all_kpis(self):
        table = self.get_kpis_linked_to_actions_table()
        if NO_AVAILABLE_DATA not in table.text_content():
            self._remove_all_remove_icons()
            self.get_save_button().click()
            self.get_save_confirm_pop_up_save_button().click(force=True)
            self.get_save_success_xsuite_pop_up_ok_button().click(force=True)

    def delete_store_report_kpi(self):
        table = self.get_kpis_linked_to_store_table()
        if NO_AVAILABLE_DATA not in table.text_content():
            self._remove_all_remove_icons()
            self.get_save_button().click()
            self.get_save_success_xsuite_pop_up_ok_button().click(force=True)

    def set_kpi(self, kpi_name: str, kpi_client_name: str, index: int, add_kpi: int):
        table = self.get_kpis_linked_to_table(index)
        if kpi_name not in table.text_content():
            self.get_add_kpi_button_of_kpis_linked_to_tables(add_kpi).click()
            search_box = self.get_kpi_search_box_of_kpi_catalog()
            search_box.click(force=True)
            search_box.press_sequentially(kpi_client_name)
            # Unable to click on the filtered KPI without a wait; there are no api calls to wait for here
            self.page.wait_for_timeout(1000)
            self.get_kpi_select_check_box_of_kpi_catalog().first.click()
            self.get_apply_button_of_kpi_catalog().click(force=True)
            self.get_save_button().click()
            self.get_save_success_xsuite_pop_up_ok_button().click(force=True)

    def get_show_live_report_first_checkbox_value(self, checkbox_name: str, aliases: dict = None) -> bool:
        is_checked = _parent(self.get_checkbox(checkbox_name)).get_attribute("checked") == "checked"
        if aliases is not None:
            aliases["isShowLiveReportFirst"] = is_checked
        return is_checked

    def navigate_to_tab(self, tab: str):
        self.get_reporting_configurations_tabs().filter(has_text=tab).first.click()

    def search_for_region_for_oos_messages(self):
        region = TEST_DATA["regionForOosReasons"]
        search_box = self.get_region_search_box_for_oos()
        search_box.click()
        search_box.press_sequentially(region)
        expect(self.get_selected_oos_region()).to_contain_text(region)

    def verify_configured_oos_messages(self):
        expect(self.page.locator(f'[nice-title="{TEST_DATA["oosMessage1"]}"]')).to_be_visible()
        expect(self.page.locator(f'[nice-title="{TEST_DATA["oosMessage2"]}"]')).to_be_visible()

    @staticmethod
    def _has_class(locator: Locator, class_name: str) -> bool:
        return class_name in (locator.get_attribute("class") or "").split()

    def configure_default_oos_message(self):
        checkbox = self.get_oos_reasons_page_checkbox().nth(2)
        if self._has_class(checkbox, "ng-hide"):
            checkbox.click(force=True)
            self.get_oos_reasons_page_save_button().click(force=True)
            self.get_save_success_xsuite_pop_up_ok_button_of_oos_reasons_page().click(force=True)

    def configure_oos_messages_for_override(self):
        checkbox = self.get_oos_reasons_page_checkbox().nth(1)
        if self._has_class(checkbox, "ng-hide"):
            parent = _parent(checkbox)
            expect(parent).to_be_visible()
            parent.click()
            self.get_oos_reasons_page_save_button().click(force=True)
            self.get_save_success_xsuite_pop_up_ok_button_of_oos_reasons_page().click(force=True)

    @staticmethod
    def _resolve_alias(value: str, aliases: dict = None) -> str:
        """Cypress `cy.get('@alias')` for names given as '@alias'; plain values are returned as they are."""
        if value.startswith("@") and aliases is not None:
            return aliases[value[1:]]
        return value

    def get_kpi_order_values(self, kpi_name: str, kpi_order_value: str, aliases: dict = None) -> str:
        kpi = str(self._resolve_alias(kpi_name, aliases))
        _clear_and_type(self.get_kpi_page_kpi_search_box(), kpi)
        kpi_item = (
            _parent(_parent(self.get_kpi_page_kpi_list_item().get_by_text("store level kpi").first))
            .locator("xpath=./*")
            .nth(1)
            .get_by_text(kpi)
            .first
        )
        kpi_item.dblclick(force=True)
        order_value = self.get_kpi_page_kpi_order().evaluate("element => element.value")
        if aliases is not None:
            aliases[kpi_order_value] = order_value
        return order_value

    def verify_kpi_order_with_kpi_order_in_mobile_report(self, aliases: dict = None):
        kpi_order_values = [aliases[alias["kpiOrderValue"]] for alias in TEST_DATA["kpiOrderValueAliases"]]
        print(kpi_order_values, "unsorted KPI order values")
        sorted_kpi_order_values = sorted(kpi_order_values)
        print(sorted_kpi_order_values, "sorted list KPI order values")
        return sorted_kpi_order_values

    def verify_default_actions_page_layout_dropdown_value(self, aliases: dict = None):
        expected = DEFAULT_ACTIONS_PAGE_LAYOUT_DROPDOWN_VALUES["actionsGroupingOption3"]
        dropdown_value = self.get_default_actions_page_layout_dropdown_value()
        if aliases is not None:
            aliases["defaultActionsPageLayoutDropdownValue"] = dropdown_value.text_content().strip()
        expect(dropdown_value).to_have_text(expected)

    def configure_value_for_default_actions_page_layout(self, actions_grouping_option: str):
        self.get_default_actions_page_layout_dropdown().click()
        self.get_default_actions_page_layout_dropdown_options().filter(has_text=actions_grouping_option).first.click()
        self.get_save_button().click()
        self.get_save_success_xsuite_pop_up_ok_button().click(force=True)

    def configure_category_order_for_actions_page(self):
        for category in TEST_DATA["categoryOrder"]:
            cell = self.get_category_order_input_cells().nth(category["inputIndex"])
            cell.clear()
            cell.press_sequentially(str(category["order"]))
        self.get_save_button().click()
        self.get_save_success_xsuite_pop_up_ok_button().click(force=True)

    def search_by_kpi(self, kpi_name: str):
        _clear_and_type(self.get_kpi_page_kpi_search_box(), kpi_name)
        kpi_item = (
            _parent(_parent(self.get_kpi_page_kpi_list_item().get_by_text("circle with table").first))
            .locator("xpath=./*")
            .get_by_text(kpi_name)
            .first
        )
        kpi_item.dblclick(force=True)

    def add_kpi_reference_images(self):
        with self.page.expect_response(
            lambda response: "expand-mini-wrap.svg" in response.url and response.request.method == "GET"
        ) as response_info:
            self.get_kpi_reference_image_file_upload_input().set_input_files(str(image_path("kpiReferenceImage1.jpg")))
        assert response_info.value.status == 200
        self.get_kpi_reference_image_text_input().press_sequentially(TEST_DATA["kpiReferenceImageText"])
        self.save_changes_on_kpis_page()

    def save_changes_on_kpis_page(self):
        self.get_kpis_page_save_button().click(force=True)
        self.get_kpis_page_save_popup_ok_button().click(force=True)

    def delete_all_kpi_reference_images(self):
        for remove_icon in self.get_kpi_reference_image_remove_icon().all():
            remove_icon.evaluate(SHOW_ELEMENT_SCRIPT)
            remove_icon.click()
        self.save_changes_on_kpis_page()

    def get_circle_value_radio_button(self, radio_button_name: str):
        return (
            self.page.locator(".xsuite-radio-wrapper")
            .locator(".radio-option", has_text=radio_button_name)
            .first.locator("xpath=preceding-sibling::*[1][self::xsuite-radio-button]")
        )

    def get_color_thresholds_toggle_button(self):
        return self.page.locator('trax-switch[ng-checked="$ctrl.colorThresholdSwitch.value"]')

    def get_color_cell_of_thresholds_table_with_default_color(self):
        default_color = COLOR_THRESHOLD_COLORS_AND_BUTTON["thresholdColors"][0]
        return self.page.locator(".xsuite-table-cell", has_text=default_color).first.locator("xsuite-table-on-top-cell")

    def get_color_dropdown_of_color_thresholds_table(self):
        return self.page.locator(".xsuite-dropdown-selections")

    def get_color_dropdown_option_of_color_thresholds_table(self):
        return self.page.locator(".xsuite-dropdown-drawer-item-name")

    def get_add_threshold_button(self):
        return self.page.locator(".button-name", has_text=COLOR_THRESHOLD_COLORS_AND_BUTTON["addThresholdButton"]).first

    def get_threshold_of_radio_button(self, radio_button_name: str):
        return self.page.locator(
            'xsuite-radio-button[ng-repeat*="thresholdTypeOfItems"]', has_text=radio_button_name
        ).first.locator(".xsuite-radio-selector-inner")

    def get_color_threshold_value_cell(self):
        return self.page.locator("color-threshold-picker").locator('input[type="text"]')

    def search_for_kpi(self, kpi_name: str):
        _clear_and_type(self.get_kpi_page_kpi_search_box(), kpi_name)
        self.get_kpi_page_kpi_list_item().filter(has_text=kpi_name).first.dblclick(force=True)

    def enable_or_disable_color_thresholds(self):
        self.get_color_thresholds_toggle_button().click(force=True)

    def verify_threshold_of_radio_button_is_selected(self, radio_button_name: str):
        expect(self.get_threshold_of_radio_button(radio_button_name)).to_have_attribute("style", "opacity: 1;")

    def open_color_dropdown_of_thresholds_table(self):
        self.get_color_cell_of_thresholds_table_with_default_color().click(force=True)
        default_color = COLOR_THRESHOLD_COLORS_AND_BUTTON["thresholdColors"][0]
        color_option = self.get_color_dropdown_of_color_thresholds_table().get_by_text(default_color).first
        expect(color_option).to_be_visible()
        color_option.click(force=True)

    def _configure_threshold_cell(self, index: int, value: str, color: str):
        cell = self.get_color_threshold_value_cell().nth(index)
        cell.click()
        cell.clear()
        cell.press_sequentially(value)
        self.open_color_dropdown_of_thresholds_table()
        self.get_color_dropdown_option_of_color_thresholds_table().filter(has_text=color).first.click(force=True)

    def configure_first_threshold_value_and_color(self, index: int, value: str, color: str):
        self._configure_threshold_cell(index, value, color)

    def configure_threshold_value_and_color(self, index: int, value: str, color: str):
        self.get_add_threshold_button().click(force=True)
        self._configure_threshold_cell(index, value, color)

    def configure_circle_value_radio_button(self, radio_button_name: str):
        radio_button = self.get_circle_value_radio_button(radio_button_name)
        opacity = radio_button.locator(".xsuite-radio-selector-inner").evaluate(
            "element => getComputedStyle(element).opacity"
        )
        if opacity == "0":
            radio_button.click(force=True)

    def select_threshold_of_radio_button(self, radio_button_name: str):
        self.get_threshold_of_radio_button(radio_button_name).click(force=True)

    def configure_time_for_oos_time_based_fraud_prevention(self, time: str):
        input_box = self.get_time_based_fraud_prevention_for_oos_reason_input_box()
        input_box.clear()
        input_box.press_sequentially(time)

    def save_changes_on_mobile_reports_general_page(self):
        self.get_save_button().click()
        self.get_save_success_xsuite_pop_up_ok_button().click(force=True)

    def rename_kpi_circle_title(self, renamed_kpi_circle_title: str):
        title_input = self.get_kpi_title_input_field()
        title_input.clear()
        title_input.press_sequentially(renamed_kpi_circle_title)

    def get_kengine_kpi_attributes_table(self):
        return self.page.locator(".k-engine-table")

    def retrieve_delta_coloring_method_for_kpi(self, kpi_name: str, aliases: dict = None) -> str:
        kpi_cell = self.get_kengine_kpi_attributes_table().locator(f'[nice-title="{kpi_name}"]')
        row = _parent(_parent(_parent(_parent(kpi_cell))))
        text = row.locator(".xsuite-dropdown-in-table-single").nth(3).text_content()
        delta_coloring_method = text.strip()
        if aliases is not None:
            aliases["deltaColoringMethod"] = delta_coloring_method
        return delta_coloring_method

    def get_default_store_report_grouping_dropdown(self):
        return self.page.locator("trax-dropdown-single").nth(0)

    def get_default_store_report_grouping_dropdown_options(self):
        return self.page.locator(".item")

    def select_default_store_report_grouping_dropdown_options(self, group_by: str):
        self.get_default_store_report_grouping_dropdown().click()
        self.get_default_store_report_grouping_dropdown_options().filter(has_text=group_by).first.click(force=True)
        self.get_save_button().click()
        self.get_save_success_xsuite_pop_up_ok_button().click(force=True)

    def verify_default_store_report_grouping_dropdown_value(self, group_by: str):
        expect(self.get_default_store_report_grouping_dropdown().locator(".text")).to_have_text(group_by)

    def get_input_for_oos_reason_button_text(self):
        return self.page.locator(".oos-reason-text-wrapper").locator("input")

    def enter_text_for_oos_reason_button_text(self, text_for_oos_reason_button: str):
        input_box = self.get_input_for_oos_reason_button_text()
        input_box.clear()
        input_box.press_sequentially(text_for_oos_reason_button)

    def remove_text_for_oos_reason_button_text(self):
        self.get_input_for_oos_reason_button_text().clear()
