from behave import step

from config.constants import (
    ACTIONS_PAGE_GROUPING_OPTIONS,
    ACTIONS_PAGE_USER_FEEDBACK_BUTTONS,
    REPORTING_CONFIGURATIONS_BUTTONS,
    REPORTING_CONFIGURATIONS_TABLES,
    REPORTING_CONFIGURATIONS_TABS,
)
from pages.actions_page import ActionsPage
from pages.base_page import BasePage
from pages.products_and_brands_page import ProductsAndBrands
from pages.reporting_configurations import ReportingConfigurations
from utils.test_data import load_test_data

test_data = load_test_data("actionsPageTestData")
reporting_configurations_test_data = load_test_data("reportingConfigurationsTestData")
products_and_brands_test_data = load_test_data("productsAndBrandsTestData")


def actions_page(context) -> ActionsPage:
    if getattr(context, "actions_page", None) is None or context.actions_page.page is not context.page:
        context.actions_page = ActionsPage(context.page, context.use_iframe)
    return context.actions_page


def reporting_configurations(context) -> ReportingConfigurations:
    return ReportingConfigurations(context.page)


def steps(*texts):
    """Registers one implementation under several step texts (Explorer / URL variants)."""
    def decorator(func):
        for text in texts:
            func = step(text)(func)
        return func
    return decorator


def set_kpi(context, index):
    kpi = reporting_configurations_test_data["kpiNames"][index]
    reporting_configurations(context).set_kpi(
        kpi["kpiName"],
        kpi["kpiClientName"],
        REPORTING_CONFIGURATIONS_TABLES["actionTable"],
        REPORTING_CONFIGURATIONS_BUTTONS["actionsTableKpiButton"],
    )


# ----------------------------------------------------------------------
# Reporting configurations
# ----------------------------------------------------------------------
@step('I get the value of "{checkbox_name}" checkbox')
def step_impl(context, checkbox_name):
    reporting_configurations(context).get_show_live_report_first_checkbox_value(checkbox_name, context.aliases)


@steps('I remove all the KPIs form the KPIs Linked to Actions table',
       'I remove all KPIs form the KPIs Linked to Actions table')
def step_impl(context):
    reporting_configurations(context).delete_all_kpis()


@steps('I add KPIs if it is not added to the KPIs Linked to Actions table',
       'I add KPIs if they are not added to the KPIs Linked to Actions table')
def step_impl(context):
    for index in range(len(reporting_configurations_test_data["kpiNames"])):
        set_kpi(context, index)


@steps('I check the "{checkbox_name}" checkbox if it is unchecked & save the changes',
       'I check "{checkbox_name}" checkbox if it is unchecked & save changes',
       'I check "{checkbox_name}" checkbox if it is unchecked & save the changes')
def step_impl(context, checkbox_name):
    reporting_configurations(context).set_checkbox(checkbox_name, True)


@steps('I uncheck the "{checkbox_name}" checkbox if it is checked & save the changes',
       'I uncheck "{checkbox_name}" checkbox if it is checked & save changes',
       'I uncheck "{checkbox_name}" checkbox if it is checked & save the changes')
def step_impl(context, checkbox_name):
    reporting_configurations(context).set_checkbox(checkbox_name, False)


@steps('I navigate to Mobile Reports OOS Reasons page',
       'I navigate to the Mobile Reports OOS Reasons page')
def step_impl(context):
    reporting_configurations(context).navigate_to_tab(REPORTING_CONFIGURATIONS_TABS["oosReasons"])


@steps('I navigate to the Reporting configurations Mobile Reports General tab',
       'I navigate to Reporting configurations Mobile Reports General page tab')
def step_impl(context):
    reporting_configurations(context).navigate_to_tab(REPORTING_CONFIGURATIONS_TABS["general"])


@steps('I configure the OOS messages for User Override',
       'I configure OOS messages for User Override')
def step_impl(context):
    page = reporting_configurations(context)
    page.search_for_region_for_oos_messages()
    page.configure_oos_messages_for_override()


@steps('I add the single KPIs per live and per regular if they are not added to the KPIs Linked to Actions table',
       'I add single KPIs per live and per regular if they are not added to the KPIs Linked to Actions table')
def step_impl(context):
    set_kpi(context, 0)
    set_kpi(context, 2)


@steps('I verify the configuration of By KPI as default actions page layout dropdown value in Reporting Configurations',
       'I verify configuration of By KPI as default actions page layout dropdown value in Reporting Configurations')
def step_impl(context):
    reporting_configurations(context).verify_default_actions_page_layout_dropdown_value(context.aliases)


@steps('I configure the "{actions_grouping_option}" option for default actions page layout',
       'I configure "{actions_grouping_option}" option for default actions page layout')
def step_impl(context, actions_grouping_option):
    reporting_configurations(context).configure_value_for_default_actions_page_layout(actions_grouping_option)


# ----------------------------------------------------------------------
# Titles, navigation and Explorer search
# ----------------------------------------------------------------------
@steps('I see the title as "{page_title}"',
       'I can see the "{page_title}" title')
def step_impl(context, page_title):
    actions_page(context).check_page_title_contains(page_title)


@step('I search by the visit ID')
def step_impl(context):
    actions_page(context).search_by_visit_id(test_data["visitIdForActionsPageTest"])


@step('I navigate to live report')
def step_impl(context):
    actions_page(context).navigate_to_live_report_on_explorer(context.aliases["isShowLiveReportFirst"])


@step('I navigate to regular report')
def step_impl(context):
    actions_page(context).navigate_to_regular_report_on_explorer(context.aliases["isShowLiveReportFirst"])


@step('I navigate to live mobile report through URL')
def step_impl(context):
    BasePage(context.page).go_to_new_live_mobile_report_page_with_session_uid(test_data["project"], test_data["sessionUid"])


@step('I navigate to regular mobile report through URL')
def step_impl(context):
    BasePage(context.page).go_to_new_regular_mobile_report_page_with_session_uid(test_data["project"], test_data["sessionUid"])


@step('I navigate to regular mobile report through URL for category order test')
def step_impl(context):
    BasePage(context.page).go_to_new_regular_mobile_report_page_with_session_uid(
        test_data["project"], test_data["sessionUidForCategoryOrderTest"])


@step('I navigate to regular mobile report through URL for Submit Feedback test')
def step_impl(context):
    BasePage(context.page).go_to_new_regular_mobile_report_page_with_session_uid(
        test_data["project"], test_data["sessionUidForSubmitFeedbackTest"])


@step('I navigate to live mobile report through URL for Partial Recalculation test')
def step_impl(context):
    BasePage(context.page).go_to_new_live_mobile_report_page_with_session_uid(
        test_data["project"], test_data["sessionUidForPartialRecalculationTest"])


# ----------------------------------------------------------------------
# Actions page
# ----------------------------------------------------------------------
@steps('I click on the Actions button when actions are collapsed and see the collapsed actions',
       'I click on the Actions button when the actions are collapsed and see the collapsed actions')
def step_impl(context):
    page = actions_page(context)
    page.click_actions_button_when_actions_collapsed()
    page.verify_not_showing_expanded_oos_actions()


@steps('I click on Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions',
       'I click on the Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions')
def step_impl(context):
    page = actions_page(context)
    page.click_actions_button(True)
    page.verify_showing_expanded_oos_actions()


@steps('I click on Actions button when there are no actions on the Report',
       'I click on the Actions button when there are no actions on the Report')
def step_impl(context):
    actions_page(context).click_actions_button(False)


@steps('I verify the actions count on pending tab count badge',
       'I verify the actions count on the pending tab count badge')
def step_impl(context):
    context.aliases["savedCount"] = actions_page(context).verify_actions_count(0)


@steps('I verify the actions count on handled tab count badge',
       'I verify the actions count on the handled tab count badge')
def step_impl(context):
    context.aliases["savedCount"] = actions_page(context).verify_actions_count(1)


@steps('I click on Back Arrow in the Actions page',
       'I click on the Back Arrow in the Actions page')
def step_impl(context):
    actions_page(context).click_back_arrow()


@steps('I verify the actions count on Actions button',
       'I verify the actions count on the Actions button')
def step_impl(context):
    actions_page(context).verify_actions_count_in_actions_button(context.aliases["savedCount"])


@steps('I refresh the page',
       'I reload the page')
def step_impl(context):
    actions_page(context).page_reload()


@steps('I navigate to the Handled tab',
       'I navigate to Handled tab')
def step_impl(context):
    actions_page(context).navigate_to_handled_tab()


@steps('I slide an SKU and click on OOS Reason button',
       'I slide an SKU and click on the OOS Reason button')
def step_impl(context):
    page = actions_page(context)
    page.slide_sku()
    page.click_oos_reason_button()


@steps('I verify the Override messages is not shwon for the OOS Reason',
       'I verify the Override messages is not shwon for OOS Reason')
def step_impl(context):
    actions_page(context).verify_not_showing_override_message_for_oos()


@steps('I navigate to the category KPI page',
       'I navigate to category KPI page')
def step_impl(context):
    actions_page(context).click_category_kpi_item()


@steps('I verify showing only the By KPI actions grouping options in actions page',
       'I verify showing only the By KPI actions grouping options in the actions page')
def step_impl(context):
    page = actions_page(context)
    page.click_three_dots_grouping_menu_in_actions_page()
    page.verify_not_showing_actions_grouping_option_in_actions_page(ACTIONS_PAGE_GROUPING_OPTIONS["noGrouping"])
    page.verify_not_showing_actions_grouping_option_in_actions_page(ACTIONS_PAGE_GROUPING_OPTIONS["byCategory"])
    page.verify_showing_actions_grouping_option_in_actions_page(ACTIONS_PAGE_GROUPING_OPTIONS["byKpi"])
    page.verify_not_showing_actions_grouping_option_in_actions_page(ACTIONS_PAGE_GROUPING_OPTIONS["byBrand"])


@steps('I verify showing all the actions grouping options in actions page',
       'I verify showing all the actions grouping options in the actions page')
def step_impl(context):
    page = actions_page(context)
    page.click_three_dots_grouping_menu_in_actions_page()
    for option in ("noGrouping", "byCategory", "byKpi", "byBrand"):
        page.verify_showing_actions_grouping_option_in_actions_page(ACTIONS_PAGE_GROUPING_OPTIONS[option])


@steps('I verify that the "{grouping_option}" actions grouping option has selected in grouping options menu',
       'I verify that the "{grouping_option}" actions grouping option has selected in the grouping options menu')
def step_impl(context, grouping_option):
    actions_page(context).verify_configured_grouping_option_has_selected(grouping_option)


@steps('I verify that SKUs have ungrouped',
       'I verify that the SKUs have ungrouped')
def step_impl(context):
    actions_page(context).verify_skus_have_ungrouped()


@steps('I verify that SKUs have grouped By Category in the actions page',
       'I verify that the SKUs have grouped By Category in the actions page')
def step_impl(context):
    actions_page(context).verify_skus_have_grouped_by_category()


@step('I verify that SKUs have grouped By KPI in the actions page')
def step_impl(context):
    actions_page(context).verify_skus_have_grouped_by_kpi(test_data["liveKpiName1"])


@step('I verify that the SKUs have grouped By KPI in the actions page')
def step_impl(context):
    actions_page(context).verify_skus_have_grouped_by_kpi(test_data["regularKpiName1"])


@steps('I verify that the SKUs have grouped By Brand in actions page',
       'I verify that the SKUs have grouped By Brand in the actions page')
def step_impl(context):
    actions_page(context).verify_skus_have_grouped_by_brand()


# ----------------------------------------------------------------------
# OOS reason handling (URL feature)
# ----------------------------------------------------------------------
@step('I verify configured OOS messages in Reporting Configurations OOS messages page')
def step_impl(context):
    page = reporting_configurations(context)
    page.search_for_region_for_oos_messages()
    page.verify_configured_oos_messages()


@step('I configure default OOS message in Reporting Configurations OOS messages page')
def step_impl(context):
    reporting_configurations(context).configure_default_oos_message()


@step('I click on an SKU, navigate to the product details page, click on the OOS Reason button and handle the SKU')
def step_impl(context):
    page = actions_page(context)
    page.click_sku(test_data["skuNameForOosActionsHandling"])
    page.click_oos_reason_button_on_product_details_page()
    page.verify_showing_default_oos_reason(reporting_configurations_test_data["oosMessage1"])
    page.click_done_button()


@step('I verify that the SKU is handled')
def step_impl(context):
    page = actions_page(context)
    page.click_back_arrow_on_product_details_page()
    page.navigate_to_handled_tab()
    page.verify_sku_is_in_handled(test_data["skuNameForOosActionsHandling"])
    page.verify_oos_reason_of_the_handled_sku(reporting_configurations_test_data["oosMessage1"])


@step('I edit the OOS Reason of the handle SKU by product details page')
def step_impl(context):
    page = actions_page(context)
    page.click_sku(test_data["skuNameForOosActionsHandling"])
    page.click_edit_oos_reason_button_on_product_details_page()
    page.select_oos_reason(reporting_configurations_test_data["oosMessage2"])
    page.click_done_button()


@step('I verify the edited OOS Reason of the SKU')
def step_impl(context):
    page = actions_page(context)
    page.click_back_arrow_on_product_details_page()
    page.navigate_to_handled_tab()
    page.verify_sku_is_in_handled(test_data["skuNameForOosActionsHandling"])
    page.verify_oos_reason_of_the_handled_sku(reporting_configurations_test_data["oosMessage2"])


@step('I remove the OOS Reason of the handled SKU by product details page')
def step_impl(context):
    page = actions_page(context)
    page.click_sku(test_data["skuNameForOosActionsHandling"])
    page.click_edit_oos_reason_button_on_product_details_page()
    page.remove_selected_oos_reason()
    page.click_done_button()


@step('I verify the OOS Reason has removed and the SKU moved to the pending tab again')
def step_impl(context):
    page = actions_page(context)
    page.verify_oos_reason_button_on_product_details_page()
    page.click_back_arrow_on_product_details_page()
    page.verify_sku_has_moved_to_pending_tab(test_data["skuNameForOosActionsHandling"])


@step('I verify the SKU is not in the handled tab after OOS Reason removing')
def step_impl(context):
    page = actions_page(context)
    page.navigate_to_handled_tab()
    page.verify_sku_is_not_in_handled_tab(test_data["skuNameForOosActionsHandling"])


@step('I add single regular KPI if it is not added to the KPIs Linked to Actions table for category order test')
def step_impl(context):
    set_kpi(context, 3)


@step('I configure category order in category order table')
def step_impl(context):
    reporting_configurations(context).configure_category_order_for_actions_page()


@step('I click on the Actions button when the actions are collapsed and see the collapsed actions for category order test')
def step_impl(context):
    actions_page(context).click_actions_button_when_actions_collapsed()


@step('I verify category order in actions page')
def step_impl(context):
    actions_page(context).verify_category_order_in_actions_page()


@step('I verify whether the Submit Feedback button is visible on the Pending page of the Actions page')
def step_impl(context):
    actions_page(context).verify_submit_feedback_button_is_visible()


@step('I verify whether the Submit Feedback button is visible on the Handled page of the Actions page')
def step_impl(context):
    actions_page(context).verify_submit_feedback_button_is_visible()


@step('I verify Submit Feedback')
def step_impl(context):
    page = actions_page(context)
    page.verify_submit_feedback_popup()
    page.verify_submit_feedback_cancel()
    page.submit_feedback()
    page.verify_recalculated_text_on_report_header()
    page.verify_recalculated_right_mark_on_report_header()
    page.verify_recalculated_date_and_time()
    page.verify_color_of_recalculated_text_and_date_and_time()


@step('I verify whether the Submit Feedback button is not visible on the Pending page of the Actions page')
def step_impl(context):
    actions_page(context).verify_submit_feedback_button_is_not_visible()


@step('I verify whether the Submit Feedback button is not visible on the Handled page of the Actions page')
def step_impl(context):
    actions_page(context).verify_submit_feedback_button_is_not_visible()


@step('I verify display date and time for the provided user feedback')
def step_impl(context):
    page = actions_page(context)
    page.verify_user_feedback_date_and_time()
    page.verify_display_calender_icon_of_user_feedback_date_and_time()


@step('I verify not display date and time for the provided user feedback')
def step_impl(context):
    page = actions_page(context)
    page.verify_not_display_user_feedback_date_and_time()
    page.verify_not_display_calender_icon_of_user_feedback_date_and_time()


@step('I navigate to the product details page by clicking on an SKU')
def step_impl(context):
    actions_page(context).click_sku(test_data["skuNameForOosActionsHandling"])


@step('I verify that the OOS Reason button is displayed on product details page')
def step_impl(context):
    actions_page(context).verify_displaying_oos_reason_button_on_product_details_page()


@step('I configure time for OOS time based fraud prevention & save the changes')
def step_impl(context):
    page = reporting_configurations(context)
    page.configure_time_for_oos_time_based_fraud_prevention(reporting_configurations_test_data["timeForOosTimeBasedFraudPrevention"])
    page.save_changes_on_mobile_reports_general_page()


@step('I verify that the OOS Reason button is not displayed on product details page')
def step_impl(context):
    actions_page(context).verify_not_displaying_oos_reason_button_on_product_details_page()


@step('I add single live KPI if it is not added to the KPIs Linked to Actions table for partial recalculation test')
def step_impl(context):
    set_kpi(context, 0)


@step('I verify displaying of the invalid barcode icon for particular SKU in the Handled page of the Actions page')
def step_impl(context):
    actions_page(context).verify_displaying_of_invalid_barcode_icon()


@step('I verify Partial Recalculation when having invalid barcode for user feedback')
def step_impl(context):
    page = actions_page(context)
    page.verify_submit_feedback_popup()
    page.verify_submit_feedback_cancel()
    page.submit_feedback()
    page.verify_partially_recalculated_text_on_report_header()
    page.verify_partially_recalculated_attention_mark_on_report_header()
    page.verify_recalculated_date_and_time()
    page.verify_color_of_partially_recalculated_text_and_date_and_time()


@step('I see the page title as "{page_header}"')
def step_impl(context, page_header):
    actions_page(context).verify_page_title(page_header)


@step('I verify the Product Details page layout and content')
def step_impl(context):
    page = actions_page(context)
    page.verify_product_image()
    page.verify_product_barcode_image()
    context.aliases["eanCode"] = page.verify_product_barcode()
    context.aliases["productTitle"] = page.verify_product_title()


@step('I navigate to the product page and verify that the Actions page product details are equal to the product details in the Products and Brands app')
def step_impl(context):
    page = ProductsAndBrands(context.page)
    page.clear_selected_category()
    page.filter_product_by_product_local_name(
        products_and_brands_test_data["productUrlToProductPageForActionsPageProductDetailsTest"], context.aliases)
    page.verify_product_properties_with_actions_page_product_details_page(context.aliases)


# ----------------------------------------------------------------------
# Multiple selection
# ----------------------------------------------------------------------
@step('I long press on SKUs')
def step_impl(context):
    actions_page(context).long_press_product_name_and_select_multiple_products()


@step('I verify displaying of the Bulk Edit icon')
def step_impl(context):
    actions_page(context).verify_displaying_of_bulk_edit_icon()


@step('I verify the count of multiple selected products')
def step_impl(context):
    page = actions_page(context)
    page.verify_multiple_selected_product_count()
    page.verify_displaying_of_multiple_selected_products_count()


@step('I verify the close button of multiple selected products')
def step_impl(context):
    page = actions_page(context)
    page.verify_close_button_of_multiple_selected_products()
    page.click_close_button_of_multiple_selected_products()
    page.verify_not_displaying_of_bulk_edit_icon()


@step('I verify the All button of multiple selected products')
def step_impl(context):
    page = actions_page(context)
    page.long_press_product_name_and_select_multiple_products()
    page.verify_all_button_of_multiple_selected_products()
    page.click_all_button_label_of_multiple_selected_products()
    page.verify_all_skus_are_selected()


@step('I handle the multiple selected SKUs by clicking on the OOS Reason button')
def step_impl(context):
    page = actions_page(context)
    page.click_close_button_of_multiple_selected_products()
    page.long_press_product_name_and_select_multiple_products()
    page.click_oos_reason_button_of_multiple_selected_products()
    page.verify_showing_default_oos_reason(reporting_configurations_test_data["oosMessage1"])
    page.click_done_button_for_oos_handling_by_multi_selection()


@step('I verify that the SKUs are handled')
def step_impl(context):
    page = actions_page(context)
    page.navigate_to_handled_tab()
    page.verify_handling_of_multiple_selected_products_by_oos_reason()
    page.verify_oos_reason_of_the_handled_sku(reporting_configurations_test_data["oosMessage1"])


@step('I edit the OOS Reason of the handled SKUs by multiple selecting')
def step_impl(context):
    page = actions_page(context)
    page.navigate_to_handled_tab()
    page.long_press_product_name_and_select_multiple_products()
    page.click_oos_reason_button_of_multiple_selected_products()
    page.select_oos_reason(reporting_configurations_test_data["oosMessage2"])
    page.click_done_button_for_oos_handling_by_multi_selection()


@step('I verify the edited OOS Reason of the multiple handled SKUs')
def step_impl(context):
    actions_page(context).verify_oos_reason_of_the_handled_sku(reporting_configurations_test_data["oosMessage2"])


@step('I remove the OOS Reason of the handled SKUs by multiple selecting')
def step_impl(context):
    page = actions_page(context)
    page.long_press_product_name_and_select_multiple_products()
    page.click_oos_reason_button_of_multiple_selected_products()
    page.remove_selected_oos_reason()
    page.click_done_button_for_oos_removing_by_multi_selection()


@step('I verify the OOS Reason has removed and the SKUs are moved to the pending tab again')
def step_impl(context):
    page = actions_page(context)
    page.navigate_to_pending_tab()
    page.verify_multiple_skus_have_moved_to_pending_tab(test_data["skuNamesForOosMultipleActionsHandling"])


@step('I verify that the SKUs are not in the handled tab after OOS Reason removing')
def step_impl(context):
    page = actions_page(context)
    page.navigate_to_handled_tab()
    page.verify_multiple_skus_are_not_in_handled_tab(test_data["skuNamesForOosMultipleActionsHandling"])


# ----------------------------------------------------------------------
# OOS Reason button text
# ----------------------------------------------------------------------
@step('I enter text for the OOS Reason Button Text and save the changes')
def step_impl(context):
    page = reporting_configurations(context)
    page.enter_text_for_oos_reason_button_text(reporting_configurations_test_data["textForOosReasonButton"])
    page.save_changes_on_mobile_reports_general_page()


@step('I remove text for the OOS Reason Button Text and save the changes')
def step_impl(context):
    page = reporting_configurations(context)
    page.remove_text_for_oos_reason_button_text()
    page.save_changes_on_mobile_reports_general_page()


@step('I navigate to the product details page by clicking on an SKU for OOS Reason Button Text test')
def step_impl(context):
    actions_page(context).click_sku(test_data["skuNameForOosReasonButtonTextTest"])


@step('I verify that the renamed OOS Reason button is displayed on product details page')
def step_impl(context):
    actions_page(context).verify_displaying_renamed_oos_reason_button_on_product_details_page(
        test_data["renamedOosReasonButtonNameForMultipleSelectionAndProductDetailsPage"])


@step('I navigate back to the Actions page from the product details page')
def step_impl(context):
    actions_page(context).click_on_back_arrow()


@step('I verify that the renamed OOS Reason button is displayed for sliding')
def step_impl(context):
    page = actions_page(context)
    page.slide_sku()
    page.verify_displaying_renamed_oos_reason_button_for_sliding(test_data["renamedOosReasonButtonNameForSliding"])


@step('I verify that the renamed OOS Reason button is displayed for multiple selection')
def step_impl(context):
    actions_page(context).verify_displaying_renamed_oos_reason_button_for_multiple_selection(
        test_data["renamedOosReasonButtonNameForMultipleSelectionAndProductDetailsPage"])


@step('I verify that the renamed Edit OOS Reason button is displayed on product details page')
def step_impl(context):
    actions_page(context).verify_displaying_renamed_oos_reason_button_on_product_details_page(
        test_data["renamedEditOosReasonButtonNameForProductDetailsPage"])


@step('I verify that the renamed Edit OOS Reason button is displayed for sliding')
def step_impl(context):
    page = actions_page(context)
    page.slide_sku()
    page.verify_displaying_renamed_oos_reason_button_for_sliding(test_data["renamedEditOosReasonButtonNameForSliding"])


@step('I verify that the renamed Edit OOS Reason button is displayed for multiple selection')
def step_impl(context):
    actions_page(context).verify_displaying_renamed_oos_reason_button_for_multiple_selection(
        test_data["renamedEditOosReasonButtonNameForMultipleSelection"])


@step('I verify that the default OOS Reason button is displayed on product details page')
def step_impl(context):
    actions_page(context).verify_displaying_renamed_oos_reason_button_on_product_details_page(
        ACTIONS_PAGE_USER_FEEDBACK_BUTTONS["oosReason"])


@step('I verify that the default OOS Reason button is displayed for sliding')
def step_impl(context):
    page = actions_page(context)
    page.slide_sku()
    page.verify_displaying_renamed_oos_reason_button_for_sliding(ACTIONS_PAGE_USER_FEEDBACK_BUTTONS["oosReasonForSliding"])


@step('I verify that the default OOS Reason button is displayed for multiple selection')
def step_impl(context):
    actions_page(context).verify_displaying_renamed_oos_reason_button_for_multiple_selection(
        ACTIONS_PAGE_USER_FEEDBACK_BUTTONS["oosReason"])


@step('I verify that the default Edit OOS Reason button is displayed on product details page')
def step_impl(context):
    actions_page(context).verify_displaying_renamed_oos_reason_button_on_product_details_page(
        ACTIONS_PAGE_USER_FEEDBACK_BUTTONS["editOosReason"])


@step('I verify that the default Edit OOS Reason button is displayed for sliding')
def step_impl(context):
    page = actions_page(context)
    page.slide_sku()
    page.verify_displaying_renamed_edit_oos_reason_button_for_sliding(ACTIONS_PAGE_USER_FEEDBACK_BUTTONS["editOosReasonForSliding"])


@step('I verify that the default Edit OOS Reason button is displayed for multiple selection')
def step_impl(context):
    actions_page(context).verify_displaying_renamed_oos_reason_button_for_multiple_selection(
        ACTIONS_PAGE_USER_FEEDBACK_BUTTONS["oosReason"])
