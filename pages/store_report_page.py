import re
import time

from playwright.sync_api import Page, expect

from config.config import Config
from config.constants import STORE_REPORT
from pages.mobile_reports_iframe_base_page import MobileReportsIframeBasePage
from utils.pdf_utils import clear_downloads_folder, read_pdf, read_pdf_normalized, save_download
from utils.test_data import load_test_data

test_data = load_test_data("storeReportTestData")


class StoreReportPage(MobileReportsIframeBasePage):
    def __init__(self, page: Page, use_iframe: bool):
        super().__init__(page, use_iframe)

    def _wait_for_joined_text(self, locator, predicate, timeout=Config.DEFAULT_TIMEOUT):
        """Retry until the concatenated text of all matched elements (Cypress `invoke('text')`) satisfies predicate."""
        deadline = time.monotonic() + timeout / 1000
        text = ""
        while time.monotonic() < deadline:
            text = "".join(locator.all_text_contents())
            if predicate(text):
                return
            self.page.wait_for_timeout(200)
        raise AssertionError(f"Text did not match the expectation, last text: {text!r}")

    def check_page_title_contains(self, page_title: str):
        expect(self.page).to_have_title(page_title)

    def get_three_dots_menu_in_report(self):
        return self.root().locator('[src="ellipsis"]')

    def click_three_dots_menu_in_report(self):
        self.get_three_dots_menu_in_report().click()

    def get_three_dots_menu_item_in_store_report(self):
        return self.root().locator(".menu-item")

    def get_sub_header_in_store_report(self):
        return self.root().locator(".store-report-subheader-section")

    def get_store_report_date_and_time(self):
        return self.root().locator(".store-report-subheader > :nth-child(2)")

    def get_store_report_back_button(self):
        return self.root().locator(".back-arrow")

    def get_store_report_status_filter_container(self, status: str):
        status_filter = self.root().locator(
            ".status-filter-container > .status-filter > .status-filter-text", has_text=status
        ).first
        status_filter.click(force=True)
        return status_filter

    def get_store_report_category_filter_container(self):
        return self.root().locator(".category-filter-container")

    def verify_store_report_menu_item_display(self):
        menu_item = self.get_three_dots_menu_item_in_store_report().filter(has_text=STORE_REPORT["StoreReport"])
        expect(menu_item.first).to_be_visible()

    def click_store_report_menu_item(self):
        self.get_three_dots_menu_item_in_store_report().filter(has_text=STORE_REPORT["StoreReport"]).first.click()

    def get_store_report_page_title(self):
        return self.root().locator(".header-title")

    def get_products_item(self):
        return self.root().locator("div .store-report-slider > .store-report-item-content")

    def get_product_count(self):
        return self.root().locator(".selected > .count-badge")

    def get_product_image(self):
        return self.root().locator(f'[src="{test_data["productImage"]}"]')

    def get_product_barcode(self):
        return self.root().locator(".barcode")

    def get_product_name(self):
        return self.root().locator("div > .product-name")

    def go_to_category_filter_container(self, category: str):
        self.get_store_report_category_filter_container().filter(has_text=category).first.click()

    def verify_store_report_page_title(self):
        self._wait_for_joined_text(
            self.get_store_report_page_title(),
            lambda text: re.sub(r"\s", " ", text) == STORE_REPORT["StoreReport"],
        )

    def verify_store_name_and_sales_rep_name(self):
        self._wait_for_joined_text(
            self.get_sub_header_in_store_report(), lambda text: text == test_data["storeReportSubHeader"]
        )

    def verify_store_report_date_and_time(self):
        self._wait_for_joined_text(
            self.get_store_report_date_and_time(), lambda text: text == test_data["reportDateAndTime"]
        )

    def verify_store_report_back_button(self):
        expect(self.get_store_report_back_button().first).to_be_visible()

    def verify_store_report_status_filter_container(self, status: str):
        expect(self.get_store_report_status_filter_container(status)).to_be_visible()

    def verify_store_report_category_filter_container(self):
        expect(self.get_store_report_category_filter_container().first).to_be_visible()

    def verify_store_report_menu_item_not_display(self):
        menu_item = self.get_three_dots_menu_item_in_store_report().filter(has_text=STORE_REPORT["StoreReport"])
        expect(menu_item).to_have_count(0)

    def get_products_count(self, status: str, status_count: str, aliases: dict):
        self.get_store_report_status_filter_container(status)
        expect(self.get_products_item().first).to_be_attached()
        count = self.get_products_item().count()
        product_count = self.get_product_count().first
        expect(product_count).to_contain_text(str(count))
        aliases[status_count] = product_count.text_content()

    def verify_products_count(self, status: str, status_count: str, aliases: dict):
        self.get_store_report_status_filter_container(status)
        expect(self.get_product_count().first).to_contain_text(aliases[status_count])

    def get_category_products_count(self, status: str, category: str, category_count: str, aliases: dict):
        self.get_store_report_status_filter_container(status)
        self.go_to_category_filter_container(category)
        expect(self.get_products_item().first).to_be_attached()
        count = self.get_products_item().count()
        product_count = self.get_product_count().first
        expect(product_count).to_contain_text(str(count))
        aliases[category_count] = product_count.text_content()
        self.go_to_category_filter_container(category)

    def verify_category_product_count(self, status: str, category: str, category_count: str, aliases: dict):
        self.get_store_report_status_filter_container(status)
        self.go_to_category_filter_container(category)
        expect(self.get_product_count().first).to_contain_text(aliases[category_count])
        self.go_to_category_filter_container(category)

    def go_to_product_details_page(self):
        self.get_products_item().first.click()

    def verify_product_details_page_header(self):
        self._wait_for_joined_text(
            self.get_store_report_page_title(),
            lambda text: text.strip() == STORE_REPORT["productDetailsPageHeader"],
        )

    def verify_product_image(self):
        expect(self.get_product_image().first).to_be_visible()

    def get_product_status_text(self):
        return self.root().locator(".product-presence-status")

    def verify_product_status(self):
        self._wait_for_joined_text(
            self.get_product_status_text(), lambda text: text.strip() == STORE_REPORT["productStatus"]
        )

    def get_closing_report_popup_window(self):
        return self.root().locator(".popup")

    def get_cancel_button(self):
        return self.root().locator(".trax-btn").filter(has_text="CANCEL").first

    def get_close_button(self):
        return self.root().locator(".close-btn")

    def click_back_button_and_verify_popup_window(self):
        self.get_store_report_back_button().click()
        popup = self.get_closing_report_popup_window()
        expect(popup).to_contain_text(STORE_REPORT["popupHeader"])
        expect(popup).to_contain_text(STORE_REPORT["popupMessage"])

    def click_cancel_button_and_verify(self):
        self.get_cancel_button().click()
        self.verify_store_report_page_title()

    def click_close_button_and_verify(self):
        self.get_store_report_back_button().click()
        self.get_close_button().click()
        expect(self.get_store_report_back_button()).to_have_count(0)

    def get_generate_button(self):
        return self.root().locator(".generate-btn")

    def click_generate_button(self):
        self.get_generate_button().click()

    def get_download_pdf_button(self):
        return self.root().locator(".trax-btn").filter(has_text="DOWNLOAD PDF").first

    def click_download_pdf_button(self):
        """Click DOWNLOAD PDF, save the file in downloads/ and return its path."""
        clear_downloads_folder()
        with self.page.expect_download() as download_info:
            self.get_download_pdf_button().click()
        return save_download(download_info.value)

    def verify_download_pdf_file_exists(self, pdf_path):
        assert pdf_path.exists(), f"PDF file {pdf_path} does not exist"
        assert "Store Report" in read_pdf(pdf_path)

    def verify_pdf_file_product_names(self, pdf_path):
        expect(self.get_product_name().first).to_be_attached()
        product_names = [(name or " ").strip() for name in self.get_product_name().all_text_contents()]
        pdf_text = read_pdf_normalized(pdf_path)
        for product_name in product_names:
            assert product_name in pdf_text, f'Product name "{product_name}" is found in the PDF'

    def get_store_report_oos_reason_filter_container(self):
        return self.root().locator(".oos-reason-filter-container")

    def go_to_oos_reason_filter_container(self, oos_reason: str):
        self.get_store_report_oos_reason_filter_container().filter(has_text=oos_reason).first.click()

    def get_oos_reason_product_name(self, status: str, oos_reason: str, product_name: str, aliases: dict):
        self.get_store_report_status_filter_container(status)
        self.go_to_oos_reason_filter_container(oos_reason)
        element = self.get_products_item().get_by_text(test_data["oosReasonProductName"]).first
        expect(element).to_be_attached()
        aliases[product_name] = element.text_content()
        self.go_to_oos_reason_filter_container(oos_reason)

    def verify_oos_reason_product_name(self, status: str, oos_reason: str, product_name: str, aliases: dict):
        self.get_store_report_status_filter_container(status)
        self.go_to_oos_reason_filter_container(oos_reason)
        expect(self.get_products_item().first).to_be_attached()
        assert aliases[product_name] == test_data["oosReasonProductName"]
        self.go_to_oos_reason_filter_container(oos_reason)

    def get_store_report_slider(self):
        return self.root().locator(".slide-btn-container")

    def swipe_product(self, index: int, button_text: str):
        expect(self.get_products_item().get_by_text(test_data["hideProductName"]).first).to_be_attached()
        slider = self.get_store_report_slider().nth(index)
        slider.evaluate("element => element.style.display = 'block'")
        expect(slider).to_contain_text(button_text)

    def get_slider_buttons(self, button_text: str):
        return self.root().locator(".slider-btn").filter(has_text=button_text).first

    def click_slider_buttons(self, button_text: str):
        self.get_slider_buttons(button_text).click()

    def get_hide_product_name(self):
        return self.root().locator(".store-report-slider > .hidden-product")

    def verify_hide_product_in_disable_mode(self):
        expect(self.get_hide_product_name().first).to_contain_text(test_data["hideProductName"])

    def verify_pdf_file_hidden_product_name(self, pdf_path):
        pdf_text = read_pdf_normalized(pdf_path)
        assert test_data["hideProductName"] not in pdf_text, "Hidden product should not appear in PDF"

    def verify_hide_product_is_in_enable_mode(self):
        expect(self.get_hide_product_name()).to_have_count(0)

    def verify_no_present_products(self):
        expect(self.get_products_item()).to_have_count(0)

    def get_no_present_products_messsage(self):
        return self.root().locator("div.empty-container-no-content-text")

    def verify_no_present_products_message(self):
        self._wait_for_joined_text(
            self.get_no_present_products_messsage(),
            lambda text: text.strip() == STORE_REPORT["noPresentProductsMessage"],
        )

    def long_press_product_name_and_select_multiple_products(self):
        products = self.get_products_item()
        products.get_by_text(test_data["hideProductName"]).first.dispatch_event("pointerdown", {"button": 0})
        self.page.wait_for_timeout(500)  # long press doesn't work without a wait
        products.get_by_text(test_data["hideProductName2"]).first.click(force=True)
        products.get_by_text(test_data["hideProductName3"]).first.click(force=True)

    def get_multi_select_show_hide_buttons(self, button_text: str):
        return self.root().locator(".action-button-container").filter(has_text=button_text).first

    def click_multi_select_show_hide_buttons(self, button_text: str):
        self.get_multi_select_show_hide_buttons(button_text).click()

    def verify_multiple_selected_products_hidden(self, hidden_product_name: str):
        expect(self.get_hide_product_name().first).to_contain_text(hidden_product_name)

    def get_multiple_selected_products_count(self):
        return self.root().locator("div > .bulk-count-text")

    def verify_multiple_selected_products_count(self):
        self._wait_for_joined_text(
            self.get_multiple_selected_products_count(),
            lambda text: text.strip() == test_data["multipleProductsCount"],
        )

    def verify_hidden_product_names_in_pdf(self, pdf_path):
        assert pdf_path.exists(), f"PDF file {pdf_path} does not exist"
        pdf_text = read_pdf_normalized(pdf_path)
        for product_name in (test_data["hideProductName"], test_data["hideProductName2"], test_data["hideProductName3"]):
            assert product_name not in pdf_text, "Hidden products should not appear in PDF"

    def verify_hidden_products_not_exists(self):
        expect(self.get_hide_product_name()).to_have_count(0)

    def get_three_dots_item_in_store_report(self):
        return self.root().locator(".column-title-container >.trax-icon-ellipsis")

    def click_three_dots_item_in_store_report(self):
        self.get_three_dots_item_in_store_report().click()

    def verify_configured_grouping_option_has_selected(self, group_by: str):
        menu_item = self.get_three_dots_menu_item_in_store_report().filter(has_text=group_by).first
        expect(menu_item.locator(".trax-icon-approve").first).to_be_attached()

    def get_store_report_group_headers(self):
        return self.root().locator(".store-report-group-header")

    def verify_status_group_headers_contain_present_and_missing(self):
        headers = self.get_store_report_group_headers()
        self._wait_for_joined_text(headers, lambda text: STORE_REPORT["present"] in text)
        self._wait_for_joined_text(headers, lambda text: STORE_REPORT["missing"] in text)

    def verify_oos_reason_group_headers_contain_no_oos_reason_and_oos_reason(self):
        headers = self.get_store_report_group_headers()
        self._wait_for_joined_text(headers, lambda text: STORE_REPORT["noOosReason"] in text)
        self._wait_for_joined_text(headers, lambda text: test_data["oosReason"] in text)

    def verify_products_un_grouped(self):
        expect(self.get_store_report_group_headers()).to_have_count(0)
