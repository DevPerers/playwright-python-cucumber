from behave import step, when, then

from pages.base_page import BasePage
from pages.reporting_configurations import ReportingConfigurations
from pages.view_images_page import ViewImagesPage
from utils.test_data import load_test_data

test_data = load_test_data("viewImagesPageTestData")


def view_images_page(context):
    return ViewImagesPage(context.page, context.use_iframe)


@when('I get the value of "{checkbox_name}" checkbox in Reporting Configurations')
def step_impl(context, checkbox_name):
    reporting_configurations = ReportingConfigurations(context.page)
    context.aliases["isShowLiveReportFirst"] = reporting_configurations.get_show_live_report_first_checkbox_value(
        checkbox_name
    )


@when('I see the title "{page_title}"')
def step_impl(context, page_title):
    view_images_page(context).check_page_title_contains(page_title)


@when('I search by visit ID')
def step_impl(context):
    view_images_page(context).search_by_visit_id(test_data["visitId"])


@when('I navigate to regular report for View Images Page test')
def step_impl(context):
    view_images_page(context).navigate_to_regular_report_on_explorer(context.aliases["isShowLiveReportFirst"])


@when('I navigate to the regular mobile report through URL')
def step_impl(context):
    BasePage(context.page).go_to_new_regular_mobile_report_page_with_session_uid(
        test_data["project"], test_data["sessionUid"]
    )


@when('I navigate to the View Images page')
@when('I navigate to View Images page')
def step_impl(context):
    page = view_images_page(context)
    page.click_three_dots_menu_in_report()
    page.click_view_images_menu_item()


@then('I verify "{page_header}" page title')
@then('I verify the "{page_header}" page title')
def step_impl(context, page_header):
    view_images_page(context).verify_page_title(page_header)


@then('I verify that the layout of View Images Page Scene Cards')
@then('I verify the layout of View Images Page Scene Cards')
def step_impl(context):
    page = view_images_page(context)
    page.verify_scene_card_titles_sorting()

    for index, scene_name in enumerate(test_data["viewImagesPageSceneCardSceneNames"]):
        page.verify_scene_cards_titles(index, scene_name)

    page.open_view_images_page_scene_cards()
    page.verify_scene_card_thumbnails()

    for index, scene_id in enumerate(test_data["viewImagesPageSceneIds"]):
        page.verify_scene_card_scene_ids(index, scene_id)

    for index, scene_name in enumerate(test_data["viewImagesPageSceneCardSceneNames"]):
        page.verify_scene_card_scene_names(index, scene_name)

    for index, image_count in enumerate(test_data["viewImagesPageImageCounts"]):
        page.verify_number_of_images_on_scene_cards(index, image_count)

    page.verify_image_icon_after_number_of_images()
    page.verify_image_scene_statuses()
    page.verify_approved_icon_after_scene_statuses()


@step('I navigate to Product Tagging page')
@step('I navigate to the Product Tagging page')
def step_impl(context):
    view_images_page(context).navigate_to_product_tagging_page()


@then('I verify that the layout of the Product Tagging page')
@then('I verify the layout of the Product Tagging page')
def step_impl(context):
    page = view_images_page(context)
    page.verify_product_tagging_page_image_visibility()
    page.verify_product_tagging_page_show_tags_button()
    page.verify_not_showing_image_tags()
    page.click_product_tagging_page_show_tags_button()

    for pop_up in test_data["productTaggingPageImageTagsPopUps"]:
        page.verify_product_tagging_page_image_tags(pop_up["Index"], pop_up["Url"], pop_up["Text"])
