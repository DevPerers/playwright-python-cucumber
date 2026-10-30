import re

from playwright.sync_api import Locator, expect

from pages.base_page import BasePage

PRODUCT_COLUMN_GROUP_VISIBLE_LABEL = "Product column group toggle visibility (visible)"


class ProductsAndBrands(BasePage):

    def get_selected_category_clear_button(self):
        return self.page.locator(".selected-category > div > button")

    def get_coulmn_selector(self):
        return self.page.locator(".ag-side-button")

    def get_column_selector_list_item(self):
        return self.page.locator(".ag-virtual-list-item")

    def get_product_grid_column_header_filter_open_button(self):
        return self.page.locator(".ag-header-cell-menu-button")

    def get_product_grid_column_filter_input_field(self):
        return self.page.locator(".ag-text-field-input")

    def get_product_grid_product_link(self, product_page_url: str):
        return self.page.locator(f'[href="{product_page_url}"]')

    def get_global_product_properties_in_product_page(self):
        return self.page.locator(
            ".global-product-properties-form > form > .awesome-form-container > .awesome-form-line > .key-value > .awesome-form-value"
        )

    def get_brand_name_in_product_page(self):
        return self.page.locator('[data-cy="brand-name"]')

    def get_physical_product_attributes_in_product_page(self):
        return self.page.locator(".pa-value")

    def clear_selected_category(self):
        self.get_selected_category_clear_button().click()

    def filter_product_by_product_local_name(self, product_page_url: str, aliases: dict):
        checkbox = self.get_column_selector_list_item().get_by_text("Product").first.locator("xpath=..")
        is_checked = checkbox.get_attribute("aria-label") == PRODUCT_COLUMN_GROUP_VISIBLE_LABEL
        if not is_checked:
            self.get_coulmn_selector().click()
            self.get_column_selector_list_item().get_by_text("Product").first.click()
        self.get_product_grid_column_header_filter_open_button().nth(8).click()
        self.get_product_grid_column_filter_input_field().nth(1).press_sequentially(str(aliases["productTitle"]))
        self.get_product_grid_product_link(product_page_url).click(force=True)

    @staticmethod
    def _text(locator: Locator) -> str:
        expect(locator).to_be_attached()
        return locator.text_content()

    @staticmethod
    def _digits(text: str) -> str:
        return re.sub(r"[^0-9]", "", text)

    def _verify_ean(self, expected_ean: str):
        ean = self._text(self.get_global_product_properties_in_product_page().nth(2))
        assert ean.strip() == expected_ean

    def _verify_brand(self, expected_brand: str):
        brand = self._text(self.get_brand_name_in_product_page())
        assert brand.upper().strip() == expected_brand

    def _verify_size(self, size: str):
        attributes = self.get_physical_product_attributes_in_product_page()
        for index in (4, 3, 5):
            assert self._digits(self._text(attributes.nth(index))) in size

    def _verify_category(self, expected_category: str):
        category = self._text(self.get_global_product_properties_in_product_page().nth(3))
        assert category.upper().strip() == expected_category

    def verify_product_properties_with_product_details_page(self, aliases: dict):
        self._verify_ean(aliases["eanCode"])
        self._verify_ean(aliases["eanCodeInDetails"])
        self._verify_brand(aliases["brand"])
        content = self._text(self.get_physical_product_attributes_in_product_page().nth(1))
        assert content.strip() == aliases["content"]
        self._verify_size(aliases["size"])
        self._verify_category(aliases["category"])

    def verify_product_properties_with_actions_page_product_details_page(self, aliases: dict):
        self._verify_ean(aliases["eanCode"])

    def verify_store_report_product_properties_with_product_details_page(self, aliases: dict):
        self._verify_ean(aliases["eanCodeInDetails"])
        self._verify_brand(aliases["brand"])
        self._verify_size(aliases["size"])
        self._verify_category(aliases["category"])

    def get_product_item_code(self):
        return self.page.locator('[data-cy="item-code"]')

    def get_product_global_code(self):
        return self.page.locator('[data-cy="global-code"]')

    def get_product_barcode_settings_edit_button(self):
        return self.page.locator("[data-cy=barcode-settings-buttons]", has_text="Edit").first

    def click_product_barcode_settings_edit_button(self):
        self.get_product_barcode_settings_edit_button().click()

    def get_storage_field_drop_down(self):
        return self.page.locator("div.product-barcode-field-list-container")

    def open_storage_field_drop_down(self):
        self.get_storage_field_drop_down().click()

    def select_storage_field_values(self, storage_field: str):
        self.open_storage_field_drop_down()
        self.page.locator(".ng-dropdown-panel-items").get_by_text(storage_field).first.click()

    def get_product_barcode_settings_save_button(self):
        return self.page.locator('[data-cy="barcode-settings-buttons"]', has_text="Save").first

    def click_product_barcode_settings_save_button(self):
        self.get_product_barcode_settings_save_button().click(force=True)

    def verify_product_barcode_settings_value(self, storage_field: str):
        expect(self.get_storage_field_drop_down().get_by_text(storage_field).first).to_be_attached()

    def verify_product_barcode_values(self, barcode_value: str, aliases: dict):
        if barcode_value == "itemCode":
            item_code = self._text(self.get_product_item_code())
            assert item_code.strip() == aliases["itemCode"]
        elif barcode_value == "productGlobalCode":
            global_code = self._text(self.get_product_global_code())
            assert global_code.strip() == aliases["productGlobalCode"]
        elif barcode_value == "ean":
            self._verify_ean(aliases["ean"])
