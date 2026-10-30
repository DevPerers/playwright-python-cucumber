from behave import step, when, then

from config.config import Config
from config.constants import COLOR_THRESHOLD_COLORS_AND_BUTTON, KPI_CIRCLE_DEFAULT_COLOR
from pages.base_page import BasePage
from pages.mobile_reports_home_page import MobileReportsHomePage
from pages.reporting_configurations import ReportingConfigurations
from utils.test_data import load_test_data

test_data = load_test_data("mobileReportsTestData")
reporting_config_test_data = load_test_data("reportingConfigurationsTestData")
THRESHOLD_COLORS = COLOR_THRESHOLD_COLORS_AND_BUTTON["thresholdColors"]


def home_page(context):
    return MobileReportsHomePage(context.page, context.use_iframe)


def save_kpi_circle_titles(context):
    for alias in test_data["kpiNameAliases"]:
        home_page(context).save_kpi_circle_title_values_in_mobile_report(alias["id"], alias["name"], context.aliases)


def save_kpi_order_values(context):
    reporting_configurations = ReportingConfigurations(context.page)
    for alias in reporting_config_test_data["kpiOrderValueAliases"]:
        reporting_configurations.get_kpi_order_values(alias["kpiName"], alias["kpiOrderValue"], context.aliases)


def save_kpi_circle_values_of_current_visit(context):
    for value in test_data["kpiCircleValuesOfCurrentVisit"]:
        home_page(context).save_kpi_circle_values(value["id"], value["circleValueAlias"], context.aliases)


def save_kpi_delta_values_of_current_visit(context):
    for value in test_data["kpiDeltaValues"]:
        home_page(context).save_kpi_delta_values(value["id"], value["deltaValueAlias"], context.aliases)


def navigate_to_recent_visit(context, recent_visit_url):
    page = home_page(context)
    page.click_three_dots_menu_in_report()
    page.click_recent_visits_menu_item()
    page.navigate_to_recent_visit(recent_visit_url)


def save_kpi_circle_values_of_previous_visit(context):
    for index in range(len(test_data["kpiCircleValuesOfCurrentVisit"])):
        value = test_data["kpiCircleValuesOfPreviousVisit"][index]
        home_page(context).save_kpi_circle_values_of_previous_visit(
            value["id"], value["previousCircleValueAlias"], context.aliases
        )


def verify_delta_values(context):
    for index in range(len(test_data["kpiCircleValuesOfCurrentVisit"])):
        home_page(context).verify_delta_values(
            test_data["kpiCircleValuesOfCurrentVisit"][index]["circleValueAlias"],
            test_data["kpiCircleValuesOfPreviousVisit"][index]["previousCircleValueAlias"],
            test_data["kpiDeltaValues"][index]["deltaValueAlias"],
            context.aliases,
        )


def go_to_regular_report(context, session_uid):
    BasePage(context.page).go_to_new_regular_mobile_report_page_with_session_uid(test_data["project"], session_uid)


def save_first_kpi_values_of_current_visit(context, index):
    page = home_page(context)
    page.save_kpi_circle_values(
        test_data["kpiCircleValuesOfCurrentVisit"][index]["id"],
        test_data["kpiCircleValuesOfCurrentVisit"][index]["circleValueAlias"],
        context.aliases,
    )


def save_kpi_delta_value_of_current_visit(context, index):
    home_page(context).save_kpi_delta_values(
        test_data["kpiDeltaValues"][index]["id"], test_data["kpiDeltaValues"][index]["deltaValueAlias"], context.aliases
    )


def save_kpi_circle_value_of_previous_visit(context, index):
    home_page(context).save_kpi_circle_values_of_previous_visit(
        test_data["kpiCircleValuesOfPreviousVisit"][index]["id"],
        test_data["kpiCircleValuesOfPreviousVisit"][index]["previousCircleValueAlias"],
        context.aliases,
    )


def verify_delta_value_of_kpi_circle(context, index):
    home_page(context).verify_delta_values(
        test_data["kpiCircleValuesOfCurrentVisit"][index]["circleValueAlias"],
        test_data["kpiCircleValuesOfPreviousVisit"][index]["previousCircleValueAlias"],
        test_data["kpiDeltaValues"][index]["deltaValueAlias"],
        context.aliases,
    )


# --- steps shared by the FromExplorer and FromUrl variants (behaviour chosen by context.use_iframe) ---

@when('I can see the title as "{page_title}"')
def step_impl(context, page_title):
    home_page(context).check_page_title_contains(page_title)


@when('I see "{page_title}" as title')
def step_impl(context, page_title):
    home_page(context).check_page_title_contains(page_title)


@when('I set "{checkbox_name}" checkbox to {to_be_checked:boolean} & save the changes')
def step_impl(context, checkbox_name, to_be_checked):
    ReportingConfigurations(context.page).set_checkbox(checkbox_name, to_be_checked)


@when('I set the "{checkbox_name}" checkbox to {to_be_checked:boolean} & save the changes')
def step_impl(context, checkbox_name, to_be_checked):
    ReportingConfigurations(context.page).set_checkbox(checkbox_name, to_be_checked)


@then('I verify the "{checkbox_name}" checkbox is checked')
def step_impl(context, checkbox_name):
    ReportingConfigurations(context.page).verify_checkbox_is_checked(checkbox_name)


@then('I verify that the "{checkbox_name}" checkbox is checked')
def step_impl(context, checkbox_name):
    ReportingConfigurations(context.page).verify_checkbox_is_checked(checkbox_name)


@then('I verify the "{checkbox_name}" checkbox is unchecked')
def step_impl(context, checkbox_name):
    ReportingConfigurations(context.page).verify_checkbox_is_unchecked(checkbox_name)


@then('I verify that the "{checkbox_name}" checkbox is unchecked')
def step_impl(context, checkbox_name):
    ReportingConfigurations(context.page).verify_checkbox_is_unchecked(checkbox_name)


# --- FromExplorer ---

@when('I search by live first visit ID')
def step_impl(context):
    home_page(context).search_by_visit_id(test_data["liveFirstVisitId"])


@then('I verify that visit is completed')
def step_impl(context):
    home_page(context).verify_visit_completion()


@then('I see "{report_header_title}" text in the report header')
def step_impl(context, report_header_title):
    home_page(context).verify_report_header_title(report_header_title)


@when('I get the KPI circle titles')
def step_impl(context):
    save_kpi_circle_titles(context)


@when('I get the KPI order values in Reporting configuration Mobile Reports KPI page')
def step_impl(context):
    save_kpi_order_values(context)


@then('I verify the KPI order values with the KPI display order in the mobile report')
def step_impl(context):
    ReportingConfigurations(context.page).verify_kpi_order_with_kpi_order_in_mobile_report(context.aliases)


@when('I search by visit ID for delta values verifying test')
def step_impl(context):
    home_page(context).search_by_visit_id(test_data["visitIdForDeltaValuesExplorerTest"])


@when('I get the KPI circle values of the current visit')
def step_impl(context):
    save_kpi_circle_values_of_current_visit(context)


@when('I get the KPI delta values of the current visit')
def step_impl(context):
    save_kpi_delta_values_of_current_visit(context)


@when('I navigate to the recent visit')
def step_impl(context):
    navigate_to_recent_visit(context, test_data["recentVisitUrlForDeltaValuesExplorerTest"])


@when('I get the KPI circle values of the recent previous visit')
def step_impl(context):
    save_kpi_circle_values_of_previous_visit(context)


@then('I verify delta values of the KPI circles of the current visit')
def step_impl(context):
    verify_delta_values(context)


# --- FromUrl ---

@when('I navigate to the old mobile report through URL')
def step_impl(context):
    BasePage(context.page).go_to_old_mobile_report_page_with_session_uid(
        test_data["project"],
        test_data["liveFirstStoreId"],
        test_data["liveFirstSalesRepId"],
        test_data["liveFirstSessionUid"],
    )


@then('I see the "{report_header_title}" text in the report header')
def step_impl(context, report_header_title):
    home_page(context).verify_old_report_header_title(report_header_title)


@when('I navigate to regular mobile report through the URL')
def step_impl(context):
    go_to_regular_report(context, test_data["sessionUidForKpiOrderTest"])


@when('I get KPI circle titles')
def step_impl(context):
    save_kpi_circle_titles(context)


@when('I get KPI order values in Reporting configuration Mobile Reports KPI page')
def step_impl(context):
    save_kpi_order_values(context)


@then('I verify KPI order values with the KPI display order in the mobile report')
def step_impl(context):
    ReportingConfigurations(context.page).verify_kpi_order_with_kpi_order_in_mobile_report(context.aliases)


@when('I navigate to regular mobile report through the URL for delta values verifying test')
def step_impl(context):
    go_to_regular_report(context, test_data["sessionUidForDeltaValuesUrlTest"])


@when('I get KPI circle values of the current visit')
def step_impl(context):
    save_kpi_circle_values_of_current_visit(context)


@when('I get KPI delta values of the current visit')
def step_impl(context):
    save_kpi_delta_values_of_current_visit(context)


@when('I proceed to the recent visit')
def step_impl(context):
    navigate_to_recent_visit(context, test_data["recentVisitUrlForDeltaValuesUrlTest"])


@when('I get KPI circle values of the recent previous visit')
def step_impl(context):
    save_kpi_circle_values_of_previous_visit(context)


@then('I verify the delta values of the KPI circles of the current visit')
def step_impl(context):
    verify_delta_values(context)


@when('I search by a KPI for color configuration')
def step_impl(context):
    ReportingConfigurations(context.page).search_for_kpi(reporting_config_test_data["kpiNameForColorConfiguration"])


@when('I enable color thresholds for the KPI')
def step_impl(context):
    ReportingConfigurations(context.page).enable_or_disable_color_thresholds()


@when("I verify '{radio_button_name}' is selected as Threshold of radio button")
def step_impl(context, radio_button_name):
    ReportingConfigurations(context.page).verify_threshold_of_radio_button_is_selected(radio_button_name)


@when('I configure KPI color threshold values and colors for a particular KPI')
def step_impl(context):
    reporting_configurations = ReportingConfigurations(context.page)
    threshold_values = reporting_config_test_data["thresholdValues"]
    reporting_configurations.configure_first_threshold_value_and_color(
        threshold_values[0]["index"], threshold_values[0]["value"], THRESHOLD_COLORS[1]
    )
    for i in range(1, len(threshold_values)):
        reporting_configurations.configure_threshold_value_and_color(
            threshold_values[i]["index"], threshold_values[i]["value"], THRESHOLD_COLORS[i + 1]
        )


@when('I save changes for the KPI')
def step_impl(context):
    ReportingConfigurations(context.page).save_changes_on_kpis_page()


@when('I navigate to regular mobile report through the URL for KPI colors verifying test')
def step_impl(context):
    go_to_regular_report(context, test_data["sessionUidForKpiColorConfigurationTest"])


def verify_kpi_colors(context, color):
    page = home_page(context)
    page.verify_kpi_circle_color(test_data["kpiNameForColorConfiguration"], color)
    page.verify_kpi_value_color(test_data["kpiNameForColorConfiguration"], color)


@then('I verify color of KPI circle and value on the mobile report when Threshold of is Target and Result is selected as Circle Value')
def step_impl(context):
    verify_kpi_colors(context, THRESHOLD_COLORS[3])


@when("I select '{radio_button_name}' radio button as Circle Value if it is not selected")
def step_impl(context, radio_button_name):
    ReportingConfigurations(context.page).configure_circle_value_radio_button(radio_button_name)


@then('I verify color of KPI circle and value on the mobile report when Threshold of is Target and Score is selected as Circle Value')
def step_impl(context):
    verify_kpi_colors(context, THRESHOLD_COLORS[4])


@when("I select '{radio_button_name}' as Threshold of radio button")
def step_impl(context, radio_button_name):
    ReportingConfigurations(context.page).select_threshold_of_radio_button(radio_button_name)


@then('I verify color of KPI circle and value on the mobile report when Threshold of is KPI result and Result is selected as Circle Value')
def step_impl(context):
    verify_kpi_colors(context, THRESHOLD_COLORS[1])


@then('I verify color of KPI circle and value on the mobile report when Threshold of is KPI result and Score is selected as Circle Value')
def step_impl(context):
    verify_kpi_colors(context, THRESHOLD_COLORS[2])


@when('I disable color thresholds for the KPI')
def step_impl(context):
    ReportingConfigurations(context.page).enable_or_disable_color_thresholds()


@then('I verify color of KPI circle and value on the mobile report when color thresholds are disabled')
def step_impl(context):
    verify_kpi_colors(context, KPI_CIRCLE_DEFAULT_COLOR)


@when('I log out from X-Suite')
def step_impl(context):
    page = home_page(context)
    page.click_trax_user_icon()
    page.click_trax_logout_button()


@step('I navigate to Mobile Report and verify that the user has no access to the Mobile Report')
def step_impl(context):
    home_page(context).verify_user_is_inaccessible_to_report(
        lambda: go_to_regular_report(
            context, test_data["sessionUidForReportInaccessibilityVerifyingForNonLoggedInUserTest"]
        ),
        test_data["project"],
    )


@then('I verify that the user is redirected to the login page')
def step_impl(context):
    home_page(context).verify_user_is_redirected_to_login_page()


@when('I navigate to Mobile Report and verify that the user has access to the Mobile Report')
def step_impl(context):
    session_uid = test_data["sessionUidForReportInaccessibilityVerifyingForNonLoggedInUserTest"]
    home_page(context).verify_user_is_accessible_to_report(
        lambda: go_to_regular_report(context, session_uid), test_data["project"], session_uid
    )


@then('I verify that the Mobile Report is visible to the user')
def step_impl(context):
    home_page(context).verify_displaying_of_mobile_report()


@step('I verify that the Mobile Report is not visible to the user')
def step_impl(context):
    home_page(context).verify_not_displaying_of_mobile_report()


@when('I search by a KPI for KPI circle title renaming test')
def step_impl(context):
    ReportingConfigurations(context.page).search_for_kpi(reporting_config_test_data["kpiForKpiCircleTitleRenamingTest"])


@step('I rename the KPI circle title')
def step_impl(context):
    ReportingConfigurations(context.page).rename_kpi_circle_title(reporting_config_test_data["nameForKpiCircleTitleRename"])


@step('I navigate to regular mobile report through the URL for KPI circle title renaming test')
def step_impl(context):
    go_to_regular_report(context, test_data["sessionUidForKpiCircleTitleRenamingTest"])


@then('I verify that the renaming has applied to the KPI circle title on the mobile report')
def step_impl(context):
    home_page(context).verify_kpi_circle_title(reporting_config_test_data["nameForKpiCircleTitleRename"])


@when('I rename the KPI circle title back to the original name')
def step_impl(context):
    ReportingConfigurations(context.page).rename_kpi_circle_title(
        reporting_config_test_data["kpiForKpiCircleTitleRenamingTest"]
    )


@then('I verify that the original name has applied to the KPI circle title on the mobile report')
def step_impl(context):
    home_page(context).verify_kpi_circle_title(reporting_config_test_data["kpiForKpiCircleTitleRenamingTest"])


@step('I retrieve Delta Coloring Method for the KPI when KPI has positive Delta Coloring Method')
def step_impl(context):
    ReportingConfigurations(context.page).retrieve_delta_coloring_method_for_kpi(
        reporting_config_test_data["kpiForPositiveDeltaColoringMethodTest"], context.aliases
    )


@step('I retrieve Delta Coloring Method for the KPI when KPI has negative Delta Coloring Method')
def step_impl(context):
    ReportingConfigurations(context.page).retrieve_delta_coloring_method_for_kpi(
        reporting_config_test_data["kpiForNegativeDeltaColoringMethodTest"], context.aliases
    )


@step('I navigate to regular mobile report through the URL for Delta Coloring Method verifying test when positive Delta Coloring Method with positive delta value')
def step_impl(context):
    go_to_regular_report(context, test_data["sessionUidsForDeltaColoringMethodTests"][0])


@step('I navigate to regular mobile report through the URL for Delta Coloring Method verifying test when positive Delta Coloring Method with negative delta value')
def step_impl(context):
    go_to_regular_report(context, test_data["sessionUidsForDeltaColoringMethodTests"][1])


@step('I navigate to regular mobile report through the URL for Delta Coloring Method verifying test when negative Delta Coloring Method with positive delta value')
def step_impl(context):
    go_to_regular_report(context, test_data["sessionUidsForDeltaColoringMethodTests"][2])


@step('I navigate to regular mobile report through the URL for Delta Coloring Method verifying test when negative Delta Coloring Method with negative delta value')
def step_impl(context):
    go_to_regular_report(context, test_data["sessionUidsForDeltaColoringMethodTests"][3])


@step('I get KPI circle value of the first KPI of the current visit')
def step_impl(context):
    save_first_kpi_values_of_current_visit(context, 0)


@step('I get KPI delta value of the first KPI of the current visit')
def step_impl(context):
    save_kpi_delta_value_of_current_visit(context, 0)


@step('I get KPI circle value of the second KPI of the current visit')
def step_impl(context):
    save_first_kpi_values_of_current_visit(context, 1)


@step('I get KPI delta value of the second KPI of the current visit')
def step_impl(context):
    save_kpi_delta_value_of_current_visit(context, 1)


@step('I navigate to the recent visit for Delta Coloring Method test when positive Delta Coloring Method with positive delta value')
def step_impl(context):
    navigate_to_recent_visit(context, test_data["recentVisitUrlsForDeltaColoringMethodTests"][0])


@step('I navigate to the recent visit for Delta Coloring Method test when positive Delta Coloring Method with negative delta value')
def step_impl(context):
    navigate_to_recent_visit(context, test_data["recentVisitUrlsForDeltaColoringMethodTests"][1])


@step('I navigate to the recent visit for Delta Coloring Method test when negative Delta Coloring Method with positive delta value')
def step_impl(context):
    navigate_to_recent_visit(context, test_data["recentVisitUrlsForDeltaColoringMethodTests"][2])


@step('I navigate to the recent visit for Delta Coloring Method test when negative Delta Coloring Method with negative delta value')
def step_impl(context):
    navigate_to_recent_visit(context, test_data["recentVisitUrlsForDeltaColoringMethodTests"][3])


@step('I get KPI circle value of the first KPI of the recent previous visit')
def step_impl(context):
    save_kpi_circle_value_of_previous_visit(context, 0)


@step('I get KPI circle value of the second KPI of the recent previous visit')
def step_impl(context):
    save_kpi_circle_value_of_previous_visit(context, 1)


@step('I verify the delta value of the first KPI circle of the current visit')
def step_impl(context):
    verify_delta_value_of_kpi_circle(context, 0)


@step('I verify the delta value of the second KPI circle of the current visit')
def step_impl(context):
    verify_delta_value_of_kpi_circle(context, 1)


@then('I verify the delta color of the KPI circle of the current visit when KPI has positive Delta Coloring Method')
def step_impl(context):
    home_page(context).verify_delta_color_in_mobile_report(0, context.aliases["deltaColoringMethod"])


@then('I verify the delta color of the KPI circle of the current visit when KPI has negative Delta Coloring Method')
def step_impl(context):
    home_page(context).verify_delta_color_in_mobile_report(1, context.aliases["deltaColoringMethod"])
