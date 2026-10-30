from behave import step

from pages.kpi_details_page import KpiDetailsPage
from pages.reporting_configurations import ReportingConfigurations
from utils.test_data import load_test_data

TEST_DATA = load_test_data("kpiDetailsPageTestData")
REPORTING_CONFIG_TEST_DATA = load_test_data("reportingConfigurationsTestData")


def get_kpi_details_page(context):
    return KpiDetailsPage(context.page, context.use_iframe)


@step('I see the title as "{page_title}" in Reporting configurations')
def step_impl(context, page_title):
    get_kpi_details_page(context).check_page_title_contains(page_title)


@step('I set "{checkbox_name}" checkbox in Reporting Configurations to {to_be_checked:boolean} & save the changes')
def step_impl(context, checkbox_name, to_be_checked):
    ReportingConfigurations(context.page).set_checkbox(checkbox_name, to_be_checked)


@step('I verify "{checkbox_name}" checkbox is checked in Reporting Configurations')
def step_impl(context, checkbox_name):
    ReportingConfigurations(context.page).verify_checkbox_is_checked(checkbox_name)


@step('I search by live first visit ID for KPI reference image test')
def step_impl(context):
    get_kpi_details_page(context).search_by_visit_id(TEST_DATA["visitIdForReferenceImageTest"])


@step('I add reference images to the KPI')
def step_impl(context):
    reporting_configurations = ReportingConfigurations(context.page)
    reporting_configurations.search_by_kpi(REPORTING_CONFIG_TEST_DATA["kpiCircleForReferenceImageTest"])
    reporting_configurations.add_kpi_reference_images()


@step('I navigate to KPI details page')
def step_impl(context):
    get_kpi_details_page(context).navigate_to_kpi_details_page(TEST_DATA["kpiCircleForReferenceImageTest"])


@step('I verify showing KPI reference image button in KPI details page')
def step_impl(context):
    get_kpi_details_page(context).verify_showing_kpi_reference_image_button()


@step('I verify KPI reference images page')
def step_impl(context):
    kpi_details_page = get_kpi_details_page(context)
    kpi_details_page.click_kpi_reference_image_button()
    kpi_details_page.verify_showing_kpi_reference_image()
    kpi_details_page.verify_showing_kpi_reference_image_text()


@step('I remove all the reference images for the KPI')
def step_impl(context):
    reporting_configurations = ReportingConfigurations(context.page)
    reporting_configurations.search_by_kpi(REPORTING_CONFIG_TEST_DATA["kpiCircleForReferenceImageTest"])
    reporting_configurations.delete_all_kpi_reference_images()


@step('I verify not showing KPI reference image button in KPI details page')
def step_impl(context):
    get_kpi_details_page(context).verify_not_showing_kpi_reference_image_button()


@step('I navigate to the regular report')
def step_impl(context):
    get_kpi_details_page(context).navigate_to_regular_report()


@step('I navigate to KPI details page for the KPI entities sorting test')
def step_impl(context):
    get_kpi_details_page(context).navigate_to_kpi_details_page(TEST_DATA["kpiCircleForKpiEntitiesSortingTest"])


@step('I search by live first visit ID for KPI entities sorting test')
def step_impl(context):
    get_kpi_details_page(context).search_by_visit_id(TEST_DATA["visitIdForKpiEntitiesSortingTest"])


@step('I capture KPI entity names and entity headers in the KPI details page')
def step_impl(context):
    kpi_details_page = get_kpi_details_page(context)
    kpi_details_page.capture_kpi_entity_names(context.aliases)
    kpi_details_page.capture_kpi_entity_column_headers(context.aliases)


@step('I verify KPI entities sorting menu options as per the KPI entity names and headers in the KPI details page')
def step_impl(context):
    kpi_details_page = get_kpi_details_page(context)
    kpi_details_page.verify_kpi_entities_names_showing_in_sorting_menu(context.aliases)
    kpi_details_page.verify_kpi_entity_header_in_sorting_menu(context.aliases)


@step('I sort KPI entities in ascending order')
def step_impl(context):
    get_kpi_details_page(context).sort_kpi_entities_by_selecting_sorting_option(TEST_DATA["kpiSortingMenuOption"])


@step('I verify sorting of KPI entities in ascending order')
def step_impl(context):
    kpi_details_page = get_kpi_details_page(context)
    kpi_details_page.verify_kpi_entities_sorted_in_ascending_order()
    kpi_details_page.verify_right_sign_of_selected_sorting_option()
    kpi_details_page.verify_upside_arrow_icon_for_ascending_order()


@step('I sort KPI entities in descending order')
def step_impl(context):
    get_kpi_details_page(context).sort_kpi_entities_by_selecting_sorting_option(TEST_DATA["kpiSortingMenuOption"])


@step('I verify sorting of KPI entities in descending order')
def step_impl(context):
    kpi_details_page = get_kpi_details_page(context)
    kpi_details_page.verify_kpi_entities_sorted_in_descending_order()
    kpi_details_page.verify_right_sign_of_selected_sorting_option()
    kpi_details_page.verify_downside_arrow_icon_for_descending_order()
