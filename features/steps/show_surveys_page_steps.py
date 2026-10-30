from behave import step, when, then

from pages.base_page import BasePage
from pages.reporting_configurations import ReportingConfigurations
from pages.show_surveys_page import ShowSurveysPage
from utils.test_data import load_test_data

test_data = load_test_data("showSurveysTestData")


def show_surveys_page(context):
    return ShowSurveysPage(context.page, context.use_iframe)


@then('I verify the title as "{page_title}"')
@then('I see the "{page_title}" title')
def step_impl(context, page_title):
    show_surveys_page(context).check_page_title_contains(page_title)


@when('I check the "{checkbox_name}" checkbox if it is unchecked and save the changes')
@when('I check "{checkbox_name}" checkbox if it is unchecked and save the changes')
def step_impl(context, checkbox_name):
    ReportingConfigurations(context.page).set_checkbox(checkbox_name, True)


@then('I see that the "{checkbox_name}" checkbox is checked')
@then('I see that "{checkbox_name}" checkbox is checked')
def step_impl(context, checkbox_name):
    ReportingConfigurations(context.page).verify_checkbox_is_checked(checkbox_name)


@when('I search by visit ID for surveys test')
def step_impl(context):
    show_surveys_page(context).search_by_visit_id(test_data["visitId"])


@when('I proceed to the live mobile report through URL')
def step_impl(context):
    BasePage(context.page).go_to_new_live_mobile_report_page_with_session_uid(
        test_data["project"], test_data["sessionUid"]
    )


@then('I verify that the visit is completed')
def step_impl(context):
    show_surveys_page(context).verify_visit_completion()


@then('I verify showing "{menu_item}" menu item in three dots menu')
@step('I verify showing the "{menu_item}" menu item in three dots menu')
def step_impl(context, menu_item):
    page = show_surveys_page(context)
    page.click_three_dots_menu_in_report()
    page.verify_show_surveys_menu_item_display()


@then('I verify Show Surveys Page')
@step('I verify the Show Surveys Page')
def step_impl(context):
    page = show_surveys_page(context)
    page.click_show_surveys_menu_item()
    page.verify_show_surveys_page_title()
    page.verify_surveys_content_title()
    page.verify_visit_survey_title(test_data["typeSurveyTitle"], test_data["visitSurveyTitle"])
    page.verify_visit_survey_group_questions_and_answers_display()
    page.verify_scene_survey_title(test_data["typeSurveyTitle"], test_data["sceneSurveyTitle"])
    page.verify_survey_group_title(
        test_data["visitSurveyGroupHeaderTitle"], test_data["sceneSurveyGroupHeaderTitle"]
    )
    page.verify_survey_group_questions_count_display(
        test_data["visitSurveyGroupQuestionsCount"], test_data["sceneSurveyGroupQuestionsCount"]
    )
    page.verify_scene_survey_group_questions_and_answers_display()
    page.verify_toggle_all_button()


@when('I uncheck the "{checkbox_name}" checkbox if it is checked and save the changes')
@when('I uncheck "{checkbox_name}" checkbox if it is checked and save the changes')
def step_impl(context, checkbox_name):
    ReportingConfigurations(context.page).set_checkbox(checkbox_name, False)


@then('I see that the "{checkbox_name}" checkbox is unchecked')
@then('I see "{checkbox_name}" checkbox is unchecked')
def step_impl(context, checkbox_name):
    ReportingConfigurations(context.page).verify_checkbox_is_unchecked(checkbox_name)


@then('I verify not showing "{menu_item}" menu item in three dots menu')
@step('I verify not showing the "{menu_item}" menu item in three dots menu')
def step_impl(context, menu_item):
    page = show_surveys_page(context)
    page.click_three_dots_menu_in_report()
    page.verify_show_surveys_menu_item_not_display()
