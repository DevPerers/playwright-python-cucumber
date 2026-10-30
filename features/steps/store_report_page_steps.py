"""Steps of the Store Report features (Cypress: storeReportPageFromExplorer / storeReportPageFromUrl).

Both variants share this file; `context.use_iframe` selects iframe (Explorer) or direct (URL) rendering.
"""
from behave import given, when, then

from config.config import Config
from config.constants import (
    PRODUCT_DETAILS_PAGE_LABELS,
    PRODUCT_DETAILS_PAGE_PRODUCT_PROPERTIES,
    REPORTING_CONFIGURATIONS_BUTTONS,
    REPORTING_CONFIGURATIONS_TABLES,
    STORE_REPORT,
)
from pages.base_page import BasePage
from pages.product_details_page import ProductDetailsPage
from pages.products_and_brands_page import ProductsAndBrands
from pages.reporting_configurations import ReportingConfigurations
from pages.store_report_page import StoreReportPage
from utils.test_data import load_test_data

test_data = load_test_data("storeReportTestData")
product_page_test_data = load_test_data("productsAndBrandsTestData")


def store_report_page(context):
    return StoreReportPage(context.page, context.use_iframe)


def product_details_page(context):
    return ProductDetailsPage(context.page, context.use_iframe)


def reporting_configurations(context):
    return ReportingConfigurations(context.page)


def products_and_brands(context):
    return ProductsAndBrands(context.page)


# --- shared helpers ---------------------------------------------------------
def add_kpis_to_store_report_table(context):
    configurations = reporting_configurations(context)
    for kpi_name, client_name in (
        (test_data["liveKpiName"], test_data["liveKpiClientName"]),
        (test_data["regularKpiName"], test_data["regularKpiClientName"]),
    ):
        configurations.set_kpi(
            kpi_name,
            client_name,
            REPORTING_CONFIGURATIONS_TABLES["storeReportTable"],
            REPORTING_CONFIGURATIONS_BUTTONS["storeReportKpiButton"],
        )


def open_live_report(context, session_uid):
    BasePage(context.page).go_to_new_live_mobile_report_page_with_session_uid(test_data["project"], session_uid)


def open_store_report_menu(context):
    page = store_report_page(context)
    page.click_three_dots_menu_in_report()
    page.click_store_report_menu_item()


def verify_store_report_page(context):
    page = store_report_page(context)
    page.click_store_report_menu_item()
    page.verify_store_report_page_title()
    page.verify_store_name_and_sales_rep_name()
    page.verify_store_report_date_and_time()
    page.verify_store_report_back_button()
    page.verify_store_report_category_filter_container()


def verify_store_report_menu_item_shown(context):
    page = store_report_page(context)
    page.click_three_dots_menu_in_report()
    page.verify_store_report_menu_item_display()


def verify_store_report_menu_item_not_shown(context):
    page = store_report_page(context)
    page.click_three_dots_menu_in_report()
    page.verify_store_report_menu_item_not_display()


def get_status_product_counts(context):
    page = store_report_page(context)
    page.get_products_count(STORE_REPORT["all"], "allCount", context.aliases)
    page.get_products_count(STORE_REPORT["present"], "presentCount", context.aliases)
    page.get_products_count(STORE_REPORT["missing"], "missingCount", context.aliases)


def verify_status_product_counts(context):
    page = store_report_page(context)
    page.verify_products_count(STORE_REPORT["all"], "allCount", context.aliases)
    page.verify_products_count(STORE_REPORT["present"], "presentCount", context.aliases)
    page.verify_products_count(STORE_REPORT["missing"], "missingCount", context.aliases)


def get_category_product_counts(context):
    page = store_report_page(context)
    category = test_data["categoryName"]
    page.get_category_products_count(STORE_REPORT["all"], category, "allCategoryCount", context.aliases)
    page.get_category_products_count(STORE_REPORT["present"], category, "presentCategoryCount", context.aliases)
    page.get_category_products_count(STORE_REPORT["missing"], category, "missingCategoryCount", context.aliases)


def verify_category_product_counts(context):
    page = store_report_page(context)
    category = test_data["categoryName"]
    page.verify_category_product_count(STORE_REPORT["all"], category, "allCategoryCount", context.aliases)
    page.verify_category_product_count(STORE_REPORT["present"], category, "presentCategoryCount", context.aliases)
    page.verify_category_product_count(STORE_REPORT["missing"], category, "missingCategoryCount", context.aliases)


def verify_product_details(context):
    page = store_report_page(context)
    details = product_details_page(context)
    page.go_to_product_details_page()
    page.verify_product_details_page_header()
    page.verify_product_image()
    page.verify_product_status()
    details.verify_product_title(context.aliases)
    details.verify_product_barcode_image()
    details.verify_product_details_page_labels(0, PRODUCT_DETAILS_PAGE_LABELS["brand"])
    details.verify_product_details_page_labels(1, PRODUCT_DETAILS_PAGE_LABELS["content"])
    details.verify_product_details_page_labels(2, PRODUCT_DETAILS_PAGE_LABELS["size"])
    details.verify_product_details_page_labels(3, PRODUCT_DETAILS_PAGE_LABELS["category"])
    details.verify_product_details_page_labels(4, PRODUCT_DETAILS_PAGE_LABELS["eanCode"])
    details.verify_product_details_page_icons()
    for alias, product_property in (
        ("brand", "brand"),
        ("content", "content"),
        ("size", "size"),
        ("category", "category"),
        ("eanCodeInDetails", "eanCode"),
    ):
        details.verify_prodcut_properties_values_and_get_values(
            PRODUCT_DETAILS_PAGE_PRODUCT_PROPERTIES[product_property], alias, context.aliases
        )


def verify_product_in_products_and_brands(context):
    page = products_and_brands(context)
    page.clear_selected_category()
    page.filter_product_by_product_local_name(product_page_test_data["storeReportProductUrl"], context.aliases)
    page.verify_store_report_product_properties_with_product_details_page(context.aliases)


def verify_pdf_downloaded(context):
    store_report_page(context).verify_download_pdf_file_exists(context.aliases["pdf_path"])


def verify_pdf_product_names(context):
    store_report_page(context).verify_pdf_file_product_names(context.aliases["pdf_path"])


def generate_and_download_pdf(context):
    page = store_report_page(context)
    page.click_generate_button()
    context.aliases["pdf_path"] = page.click_download_pdf_button()


def select_storage_field(context, storage_field):
    page = products_and_brands(context)
    page.select_storage_field_values(storage_field)
    page.click_product_barcode_settings_save_button()


def get_barcode_value(context, barcode_value):
    product_details_page(context).get_barcode(test_data["productNameForBarcode"], barcode_value, context.aliases)


def verify_barcode_in_products_and_brands(context, barcode_value):
    page = products_and_brands(context)
    page.clear_selected_category()
    page.filter_product_by_product_local_name(product_page_test_data["storeReportBarcode"], context.aliases)
    page.verify_product_barcode_values(barcode_value, context.aliases)


def get_oos_reason_product_names(context):
    page = store_report_page(context)
    page.get_oos_reason_product_name(STORE_REPORT["all"], test_data["oosReason"], "allProductName", context.aliases)
    page.get_oos_reason_product_name(
        STORE_REPORT["missing"], test_data["oosReason"], "missingProductName", context.aliases
    )


def verify_oos_reason_product_names(context):
    page = store_report_page(context)
    page.verify_oos_reason_product_name(STORE_REPORT["all"], test_data["oosReason"], "allProductName", context.aliases)
    page.verify_oos_reason_product_name(
        STORE_REPORT["missing"], test_data["oosReason"], "missingProductName", context.aliases
    )


def verify_no_present_products_and_message(context):
    page = store_report_page(context)
    page.verify_no_present_products()
    page.verify_no_present_products_message()


def verify_hidden_products_in_disable_mode(context):
    page = store_report_page(context)
    for name in (test_data["hideProductName"], test_data["hideProductName2"], test_data["hideProductName3"]):
        page.verify_multiple_selected_products_hidden(name)


def verify_hidden_product_not_in_pdf(context):
    store_report_page(context).verify_pdf_file_hidden_product_name(context.aliases["pdf_path"])


def verify_hidden_products_not_in_pdf(context):
    store_report_page(context).verify_hidden_product_names_in_pdf(context.aliases["pdf_path"])


def verify_grouping_option_selected(context, group_by):
    page = store_report_page(context)
    page.click_three_dots_item_in_store_report()
    page.verify_configured_grouping_option_has_selected(group_by)


def verify_group_by_headers(context, menu_option):
    page = store_report_page(context)
    if menu_option == "OOS Reason":
        page.verify_oos_reason_group_headers_contain_no_oos_reason_and_oos_reason()
    elif menu_option == "Status":
        page.verify_status_group_headers_contain_present_and_missing()
    elif menu_option == "Ungrouped":
        page.verify_products_un_grouped()
    else:
        raise ValueError(f"Unsupported menuOption: {menu_option}")


# --- steps shared by both features' Background / settings flows -------------
@when('I see that the title is "{page_title}"')
@when('I can see the title "{page_title}"')
def step_impl(context, page_title):
    store_report_page(context).check_page_title_contains(page_title)


@when('I delete all the KPIs from the store report table')
@when('I delete all KPIs from the store report table')
def step_impl(context):
    reporting_configurations(context).delete_all_kpis()


@when('I add the KPIs to the Store Report table')
@when('I add KPIs to the Store Report table')
def step_impl(context):
    add_kpis_to_store_report_table(context)


@when('I check "{checkbox_name}" checkbox & save the changes, if it is unchecked')
@when('I check "{checkbox_name}" checkbox if it is unchecked & save the changes')
def step_impl(context, checkbox_name):
    reporting_configurations(context).set_checkbox(checkbox_name, True)


@when('I uncheck "{checkbox_name}" checkbox & save the changes, if it is checked')
@when('I uncheck "{checkbox_name}" checkbox if it is checked & save the changes')
def step_impl(context, checkbox_name):
    reporting_configurations(context).set_checkbox(checkbox_name, False)


@when('I check that "{checkbox_name}" checkbox is checked')
@then('I verify "{checkbox_name}" checkbox is checked')
def step_impl(context, checkbox_name):
    reporting_configurations(context).verify_checkbox_is_checked(checkbox_name)


@when('I check that "{checkbox_name}" checkbox is unchecked')
@when('I verify "{checkbox_name}" checkbox is unchecked')
@then('I verify "{checkbox_name}" checkbox is unchecked')
def step_impl(context, checkbox_name):
    reporting_configurations(context).verify_checkbox_is_unchecked(checkbox_name)


# --- visit / report navigation ----------------------------------------------
@when('I navigate to the Visit Viewer page')
def step_impl(context):
    store_report_page(context).search_by_visit_id(test_data["visitID"])


@when('I navigate to Visit Viewer page')
def step_impl(context):
    store_report_page(context).search_by_visit_id(test_data["secondVisitID"])


@when('I navigate to Visit Viewer page to see the Mobile Report')
def step_impl(context):
    store_report_page(context).search_by_visit_id(test_data["sessionUidForLongPress"])


@when('I navigate to the live mobile report through URL')
def step_impl(context):
    open_live_report(context, test_data["sessionUidForStoreReport"])


@when('I go to the live mobile report through URL to check the hide and show functionality by long press')
def step_impl(context):
    open_live_report(context, test_data["sessionUidForLongPress"])


@when('I go to the live mobile report through URL')
def step_impl(context):
    open_live_report(context, test_data["storeReportSessionUid"])


# --- Store Report menu item / page ------------------------------------------
@then('I verify that showing the Store Report menu item in three dots menu')
@then('I verify showing the Store Report menu item in three dots menu')
def step_impl(context):
    verify_store_report_menu_item_shown(context)


@then('I verify that the Store Report Page')
@then('I verify the Store Report Page')
def step_impl(context):
    verify_store_report_page(context)


@then('I verify that not showing the Store Report menu item in three dots menu')
@then('I verify not showing the Store Report menu item in three dots menu')
def step_impl(context):
    verify_store_report_menu_item_not_shown(context)


@when('I go to Store Report page')
@when('I go to the Store Report page')
def step_impl(context):
    open_store_report_menu(context)


# --- product count ----------------------------------------------------------
@when('I check the status of the product count')
@when('I check the status product count')
def step_impl(context):
    get_status_product_counts(context)


@then('I verify the status product count')
@then('I verify status product count')
def step_impl(context):
    verify_status_product_counts(context)


@when('I filter product by category and get the product count')
@when('I filter the product by category and get the product count')
def step_impl(context):
    get_category_product_counts(context)


@then('I verify that the category filtered product count')
@then('I verify the category filtered product count')
def step_impl(context):
    verify_category_product_counts(context)


# --- product details --------------------------------------------------------
@when('I go to product details page and verify the values')
@then('I go to the product details page and verify the values')
def step_impl(context):
    verify_product_details(context)


@then('I proceed to the product page and verify the store report product details are equal to the product details in the Product and Brands app')
@then('I navigate to the product page and verify the store report product details are equal to the product details in the Product and Brands app')
def step_impl(context):
    verify_product_in_products_and_brands(context)


# --- back button / popup ----------------------------------------------------
@when('I click on back button and verify the pop up window')
@then('I click on the back button and verify the pop up window')
def step_impl(context):
    store_report_page(context).click_back_button_and_verify_popup_window()


@when('I click the Cancel button and verify')
@then('I click Cancel button and verify')
def step_impl(context):
    store_report_page(context).click_cancel_button_and_verify()


@when('I click the Close button and verify')
@then('I click Close button and verify')
def step_impl(context):
    store_report_page(context).click_close_button_and_verify()


# --- PDF --------------------------------------------------------------------
@when('I click on the Generate button option')
@when('I click on the Generate button')
def step_impl(context):
    store_report_page(context).click_generate_button()


@when('I click on the Download PDF button option')
@when('I click on the Download PDF button')
def step_impl(context):
    context.aliases["pdf_path"] = store_report_page(context).click_download_pdf_button()


@then('I verify that the pdf file is in the download folder and verify the header')
@then('I verify the pdf file is in the download folder and verify the header')
def step_impl(context):
    verify_pdf_downloaded(context)


@then('I verify that the products names in the PDF file')
@then('I verify the products names in the PDF file')
def step_impl(context):
    verify_pdf_product_names(context)


@when('I download pdf')
@when('I download the pdf')
def step_impl(context):
    generate_and_download_pdf(context)


# --- OOS reason -------------------------------------------------------------
@when('I filter the Store Report products by OOS Reason and get the product name')
@when('I filter the products by OOS Reason and get the product name')
def step_impl(context):
    get_oos_reason_product_names(context)


@then('I verify the OOS Reason filtered products names in the All and Missing tabs')
@then('I verify the OOS Reason filtered product name')
def step_impl(context):
    verify_oos_reason_product_names(context)


@when('I filter products by OOS Reason')
@when('I filter the products by OOS Reason')
def step_impl(context):
    store_report_page(context).go_to_oos_reason_filter_container(test_data["oosReason"])


@when('I go to the Present tab')
@when('I go to Present tab')
def step_impl(context):
    store_report_page(context).get_store_report_status_filter_container(STORE_REPORT["present"])


@then('I verify the no present product in the present tab and verify message for the selected OOS Reason')
@then('I verify no present product in the present tab and verify message for the selected OOS Reason')
def step_impl(context):
    verify_no_present_products_and_message(context)


# --- product barcode settings -----------------------------------------------
@when('I click the edit button in the product barcode settings')
@when('I click edit button in the product barcode settings')
def step_impl(context):
    products_and_brands(context).click_product_barcode_settings_edit_button()


@when('I select the "{storage_field}" and click save button')
@when('I select "{storage_field}" and click save button')
def step_impl(context, storage_field):
    select_storage_field(context, storage_field)


@when('I verify the "{storage_field}" is selected in the product barcode settings')
@when('I verify "{storage_field}" is selected in the product barcode settings')
def step_impl(context, storage_field):
    products_and_brands(context).verify_product_barcode_settings_value(storage_field)


@when('I get the "{barcode_value}" value')
@when('I get "{barcode_value}" value')
def step_impl(context, barcode_value):
    get_barcode_value(context, barcode_value)


@then('I verify "{barcode_value}" is equal to the Product and Brands app')
@then('I verify the "{barcode_value}" is equal to the Product and Brands app')
def step_impl(context, barcode_value):
    verify_barcode_in_products_and_brands(context, barcode_value)


# --- hide / show a single product -------------------------------------------
@when('I swipe product to the left side')
@when('I swipe the product to the left side')
def step_impl(context):
    store_report_page(context).swipe_product(1, STORE_REPORT["hide"])


@when('I click the HIDE button')
@when('I click on the HIDE button')
def step_impl(context):
    store_report_page(context).click_slider_buttons(STORE_REPORT["hide"])


@when('I verify the hide product is in disable mode')
@when('I verify hide product is in disable mode')
def step_impl(context):
    store_report_page(context).verify_hide_product_in_disable_mode()


@then('I verify hidden product is not available in product list')
@then('I verify hidden product is not available in the product list')
def step_impl(context):
    verify_hidden_product_not_in_pdf(context)


@when('I swipe the product to right side')
@when('I swipe the product to the right side')
def step_impl(context):
    store_report_page(context).swipe_product(0, STORE_REPORT["show"])


@when('I click the SHOW button')
@when('I click on the SHOW button')
def step_impl(context):
    store_report_page(context).click_slider_buttons(STORE_REPORT["show"])


@then('I verify the hidden product is in enable mode')
@then('I verify hidden product is in enable mode')
def step_impl(context):
    store_report_page(context).verify_hide_product_is_in_enable_mode()


# --- hide / show multiple products ------------------------------------------
@when('I long press the product name and select products')
@when('I long press the product name and select multiple products')
def step_impl(context):
    store_report_page(context).long_press_product_name_and_select_multiple_products()


@when('I check the selected products count')
@when('I verify the selected products count')
def step_impl(context):
    store_report_page(context).verify_multiple_selected_products_count()


@when('I click on the HIDE button for hide selected three products')
@when('I click on the HIDE button for hide the multiple products')
def step_impl(context):
    store_report_page(context).click_multi_select_show_hide_buttons(STORE_REPORT["hide"])


@when('I verify the hidden products are in disable mode')
@when('I verify the hide products are in disable mode')
def step_impl(context):
    verify_hidden_products_in_disable_mode(context)


@when('I verify hidden products are not available in the product list')
@when('I verify the hidden products are not available in the product list')
def step_impl(context):
    verify_hidden_products_not_in_pdf(context)


@when('I click on the SHOW button to show the hidden products')
@when('I click on the SHOW button to show multiple products')
def step_impl(context):
    store_report_page(context).click_multi_select_show_hide_buttons(STORE_REPORT["show"])


@then('I verify the hidden products are in enable mode')
@then('I verify hidden products are in enable mode')
def step_impl(context):
    store_report_page(context).verify_hidden_products_not_exists()


# --- grouping ---------------------------------------------------------------
@when('I add the "{group_by}" value to the Default Store Report Grouping drop-down and save the changes')
@when('I add a "{group_by}" value to the Default Store Report Grouping drop-down and save the changes')
def step_impl(context, group_by):
    reporting_configurations(context).select_default_store_report_grouping_dropdown_options(group_by)


@when('I verify that the "{group_by}" product grouping option is selected in the grouping options menu')
@when('I verify that "{group_by}" product grouping option is selected in the grouping options menu')
def step_impl(context, group_by):
    verify_grouping_option_selected(context, group_by)


@then('I verify the Group By headers for the "{menu_option}"')
@then('I verify the Group By headers for "{menu_option}"')
def step_impl(context, menu_option):
    verify_group_by_headers(context, menu_option)
