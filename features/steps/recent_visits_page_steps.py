from behave import when, then

from pages.base_page import BasePage
from pages.recent_visits_page import RecentVisitsPage
from utils.test_data import load_test_data

test_data = load_test_data("recentVisitsPageTestData")


def recent_visits_page(context):
    return RecentVisitsPage(context.page, context.use_iframe)


@when('I see that the "{page_title}" title')
def step_impl(context, page_title):
    recent_visits_page(context).check_page_title_contains(page_title)


@when('I search by giving a visit ID')
def step_impl(context):
    recent_visits_page(context).search_by_visit_id(test_data["visitId"])


@when('I proceed to the regular mobile report through URL')
def step_impl(context):
    BasePage(context.page).go_to_new_regular_mobile_report_page_with_session_uid(
        test_data["project"], test_data["sessionUid"]
    )


@then('I verify that showing the Recent Visits menu item in three dots menu')
@then('I verify showing the Recent Visits menu item in three dots menu')
def step_impl(context):
    page = recent_visits_page(context)
    page.click_three_dots_menu_in_report()
    page.verify_recent_visits_menu_item_display()


@when('I proceed to Recent Visits page')
@when('I navigate to Recent Visits page')
def step_impl(context):
    recent_visits_page(context).click_recent_visits_menu_item()


@then('I verify that the Recent Visits page layout')
@then('I verify the Recent Visits page layout')
def step_impl(context):
    page = recent_visits_page(context)
    page.verify_recent_visits_page_title()
    page.verify_recent_visits_page_title_text()
    page.verify_recent_visit_users()
    page.verify_recent_visits_links_count()
    page.verify_visit_type_labels()
    page.verify_visit_types()
    page.verify_visit_date_labels()
    page.verify_visit_date()
    page.verify_recent_visit_date_and_time_sorting()
    page.verify_recent_visits_cards_arrows()
    page.verify_recent_visits_filter_button()


@when('I filter that the the Recent Visits page by single user filtering')
@when('I filter the the Recent Visits page by single user filtering')
def step_impl(context):
    recent_visits_page(context).filter_recent_visits_by_single_user(test_data["userName1"])


@then('I verify that the Recent Visits page single user filtering and clearing the filter')
@then('I verify the Recent Visits page single user filtering and clearing the filter')
def step_impl(context):
    page = recent_visits_page(context)
    page.verify_filter_box_applied_value()
    page.verify_filtered_recent_visits()
    page.verify_filter_box_applied_value_clear_button()


@when('I filter the Recent Visits page by multiple user filtering')
@when('I filter the the Recent Visits page by multiple user filtering')
def step_impl(context):
    recent_visits_page(context).filter_recent_visits_by_multiple_users()


@then('I verify that the Recent Visits page multiple user filtering and clearing the filter')
@then('I verify the Recent Visits page multiple user filtering and clearing the filter')
def step_impl(context):
    page = recent_visits_page(context)
    page.verify_filter_box_applied_multiple_values()
    page.verify_filter_box_applied_value_multiple_clear_buttons()
    page.verify_filter_box_applied_value_clear_all_button()


@then('I verify that the navigation to recent visits')
@then('I verify the navigation to recent visits')
def step_impl(context):
    recent_visits_page(context).verify_recent_visit_link_navigation()
