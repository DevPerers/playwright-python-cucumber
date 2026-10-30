from behave import step

from config.constants import PRODUCT_DETAILS_PAGE_LABELS, PRODUCT_DETAILS_PAGE_PRODUCT_PROPERTIES
from pages.base_page import BasePage
from pages.product_details_page import ProductDetailsPage
from pages.products_and_brands_page import ProductsAndBrands
from utils.test_data import load_test_data

TEST_DATA = load_test_data("productDetailsPageTestData")
PRODUCTS_AND_BRANDS_TEST_DATA = load_test_data("productsAndBrandsTestData")


def get_product_details_page(context):
    return ProductDetailsPage(context.page, context.use_iframe)


def verify_product_details_page_layout_and_get_values(context):
    product_details_page = get_product_details_page(context)
    aliases = context.aliases
    product_details_page.verify_product_image()
    product_details_page.verify_product_barcode_image()
    product_details_page.verify_product_barcode(aliases)
    product_details_page.verify_product_title(aliases)
    product_details_page.verify_product_details_page_labels(0, PRODUCT_DETAILS_PAGE_LABELS["brand"])
    product_details_page.verify_product_details_page_labels(1, PRODUCT_DETAILS_PAGE_LABELS["content"])
    product_details_page.verify_product_details_page_labels(2, PRODUCT_DETAILS_PAGE_LABELS["size"])
    product_details_page.verify_product_details_page_labels(3, PRODUCT_DETAILS_PAGE_LABELS["category"])
    product_details_page.verify_product_details_page_labels(4, PRODUCT_DETAILS_PAGE_LABELS["eanCode"])
    product_details_page.verify_product_details_page_icons()
    if not context.use_iframe:
        product_details_page.verify_product_details_page_content_icon()
    properties = PRODUCT_DETAILS_PAGE_PRODUCT_PROPERTIES
    product_details_page.verify_prodcut_properties_values_and_get_values(properties["brand"], "brand", aliases)
    product_details_page.verify_prodcut_properties_values_and_get_values(properties["content"], "content", aliases)
    product_details_page.verify_prodcut_properties_values_and_get_values(properties["size"], "size", aliases)
    product_details_page.verify_prodcut_properties_values_and_get_values(properties["category"], "category", aliases)
    product_details_page.verify_prodcut_properties_values_and_get_values(
        properties["eanCode"], "eanCodeInDetails", aliases
    )


def verify_product_details_against_products_and_brands(context):
    products_and_brands = ProductsAndBrands(context.page)
    products_and_brands.clear_selected_category()
    products_and_brands.filter_product_by_product_local_name(
        PRODUCTS_AND_BRANDS_TEST_DATA["productUrlToProductPage"], context.aliases
    )
    products_and_brands.verify_product_properties_with_product_details_page(context.aliases)


@step('I can see that the "{page_title}" title')
def step_impl(context, page_title):
    get_product_details_page(context).check_page_title_contains(page_title)


@step('I search by giving visit ID')
def step_impl(context):
    get_product_details_page(context).search_by_visit_id(TEST_DATA["visitId"])


@step('I proceed to Product Details page')
def step_impl(context):
    product_details_page = get_product_details_page(context)
    product_details_page.navigate_to_kpi_details_page()
    product_details_page.navigate_to_product_details_page()


@step('I verify that the "{page_header}" page title')
def step_impl(context, page_header):
    get_product_details_page(context).verify_page_title(page_header)


@step('I verify that the layout of the Product Details page and verify the product properties values')
def step_impl(context):
    verify_product_details_page_layout_and_get_values(context)


@step('I navigate to product page and verify the mobile report product details are equal to the product details in the Product and Brands app')
def step_impl(context):
    verify_product_details_against_products_and_brands(context)


@step('I proceed to regular mobile report through URL')
def step_impl(context):
    BasePage(context.page).go_to_new_regular_mobile_report_page_with_session_uid(
        TEST_DATA["project"], TEST_DATA["sessionUid"]
    )


@step('I navigate to Product Details page')
def step_impl(context):
    product_details_page = get_product_details_page(context)
    product_details_page.navigate_to_kpi_details_page()
    product_details_page.navigate_to_product_details_page()


@step('I verify that the page title is "{page_header}"')
def step_impl(context, page_header):
    get_product_details_page(context).verify_page_title(page_header)


@step('I verify the layout of the Product Details page and verify the product properties values')
def step_impl(context):
    verify_product_details_page_layout_and_get_values(context)


@step('I navigate to the product page and verify the mobile report product details are equal to the product details in the Product and Brands app')
def step_impl(context):
    verify_product_details_against_products_and_brands(context)
