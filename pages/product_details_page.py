from playwright.sync_api import expect

from pages.mobile_reports_iframe_base_page import MobileReportsIframeBasePage
from utils.test_data import load_test_data

TEST_DATA = load_test_data("productDetailsPageTestData")


class ProductDetailsPage(MobileReportsIframeBasePage):

    def check_page_title_contains(self, page_title: str):
        expect(self.page).to_have_title(page_title)

    def get_visit_id_search_field(self):
        return self.page.locator('.input-with-icon > input[placeholder="Visit ID"]')

    def get_explorer_visits_search_button(self):
        return self.page.locator(".input-with-icon > .button")

    def get_kpi_circle(self):
        return self.get_mobile_report_iframe_body().locator("trx-kpi-circle")

    def get_sku_container(self):
        return self.get_mobile_report_iframe_body().locator(".kpi-box")

    def get_page_title(self):
        return self.get_mobile_report_iframe_body().locator(".header-title")

    def get_product_image(self):
        return self.get_mobile_report_iframe_body().locator(f'[src="{TEST_DATA["imageUrl"]}"]')

    def get_product_barcode(self):
        return self.get_mobile_report_iframe_body().locator(".barcode")

    def get_product_title(self):
        return self.get_mobile_report_iframe_body().locator(".product-title")

    def get_product_details_page_brand_icon(self):
        return self.get_mobile_report_iframe_body().locator(".trax-icon-brand")

    def get_product_details_page_content_icon(self):
        return self.get_mobile_report_iframe_body().locator(".trax-icon-content")

    def get_product_details_page_size_icon(self):
        return self.get_mobile_report_iframe_body().locator(".trax-icon-ruler")

    def get_product_details_page_category_icon(self):
        return self.get_mobile_report_iframe_body().locator(".trax-icon-category")

    def get_product_details_page_ean_icon(self):
        return self.get_mobile_report_iframe_body().locator(".trax-icon-ean")

    def get_product_details_page_labels(self):
        return self.get_mobile_report_iframe_body().locator(".list-item-title")

    def get_product_details_list_item(self):
        return self.get_mobile_report_iframe_body().locator(".product-details-list-item-content")

    def search_by_visit_id(self, visit_id: str):
        search_field = self.get_visit_id_search_field()
        search_field.click()
        search_field.press_sequentially(visit_id)
        self.get_explorer_visits_search_button().click()

    def navigate_to_kpi_details_page(self):
        self.get_kpi_circle().filter(has_text=TEST_DATA["kpiCircle"]).first.click()

    def navigate_to_product_details_page(self):
        self.get_sku_container().first.click()

    def verify_page_title(self, page_header: str):
        expect(self.get_page_title()).to_have_text(page_header)

    def verify_product_image(self):
        expect(self.get_product_image()).to_be_visible()

    def verify_product_barcode_image(self):
        expect(self.get_product_barcode().locator(f'[xmlns="{TEST_DATA["barcode"]}"]')).to_be_visible()

    def verify_product_barcode(self, aliases: dict = None) -> str:
        barcode = self.get_product_barcode()
        expect(barcode).to_be_visible()
        ean_code = barcode.text_content().strip()
        if aliases is not None:
            aliases["eanCode"] = ean_code
        return ean_code

    def verify_product_title(self, aliases: dict = None) -> str:
        title = self.get_product_title()
        expect(title).to_be_visible()
        product_title = title.text_content().strip()
        if aliases is not None:
            aliases["productTitle"] = product_title
        return product_title

    def verify_product_details_page_labels(self, index: int, label: str):
        expect(self.get_product_details_page_labels().nth(index)).to_have_text(label, use_inner_text=False)

    def verify_product_details_page_icons(self):
        expect(self.get_product_details_page_brand_icon()).to_be_visible()
        expect(self.get_product_details_page_size_icon()).to_be_visible()
        expect(self.get_product_details_page_category_icon()).to_be_visible()
        expect(self.get_product_details_page_ean_icon()).to_be_visible()

    def verify_product_details_page_content_icon(self):
        expect(self.get_product_details_page_content_icon()).to_be_visible()

    def verify_prodcut_properties_values_and_get_values(self, property_name: str, alias: str, aliases: dict = None) -> str:
        value = (
            self.get_product_details_list_item()
            .get_by_text(property_name)
            .first.locator("xpath=..")
            .locator("xpath=./*")
            .nth(1)
        )
        expect(value).to_be_visible()
        text = value.text_content().strip()
        if aliases is not None:
            aliases[alias] = text
        return text

    def get_products_item(self):
        return self.get_mobile_report_iframe_body().locator(".store-report-slider > .store-report-item-content")

    def get_barcode(self, product_name: str, alias: str, aliases: dict = None) -> str:
        self.get_products_item().filter(has_text=product_name).first.click()
        self.verify_product_title(aliases)
        barcode = self.get_product_barcode()
        expect(barcode).to_be_visible()
        text = barcode.text_content().strip()
        if aliases is not None:
            aliases[alias] = text
        return text
