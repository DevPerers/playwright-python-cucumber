import re

from playwright.sync_api import expect

from config.constants import SURVEY_LABELS
from pages.mobile_reports_iframe_base_page import MobileReportsIframeBasePage
from utils.test_data import load_test_data

test_data = load_test_data("showSurveysTestData")


def contains(text: str):
    return re.compile(re.escape(text))


class ShowSurveysPage(MobileReportsIframeBasePage):
    def __init__(self, page, use_iframe: bool):
        super().__init__(page, use_iframe)

    def check_page_title_contains(self, page_title: str):
        expect(self.page).to_have_title(page_title)

    def get_visit_id_search_field(self):
        return self.page.locator('.input-with-icon > input[placeholder="Visit ID"]')

    def get_explorer_visits_search_button(self):
        return self.page.locator(".input-with-icon > .button")

    def get_visit_status(self):
        return self.page.locator('div[class="explorer-viewer-sub-header-bottom-left"]>span:nth-child(7) div')

    def get_three_dots_menu_in_report(self):
        return self.root().locator('[src="ellipsis"]')

    def get_surveys_group_container(self):
        return self.root().locator(".survey-group-header-container")

    def get_surveys_toggle_all_button(self):
        return self.root().locator(".trax-icon-down-arrow-triangle")

    def get_three_dots_menu_item_in_report(self):
        return self.root().locator(".menu-item")

    def get_show_surveys_page_title(self):
        return self.root().locator(".header-title")

    def get_surveys_content_title(self):
        return self.root().locator(".survey-content-title-container")

    def get_survey_group_questions_count(self):
        return self.root().locator(".header-count")

    def search_by_visit_id(self, visit_id: str):
        search_field = self.get_visit_id_search_field()
        search_field.click()
        search_field.press_sequentially(visit_id)
        self.get_explorer_visits_search_button().click()

    def verify_visit_completion(self):
        expect(self.get_visit_status().first).to_contain_text("Completed")

    def click_three_dots_menu_in_report(self):
        self.get_three_dots_menu_in_report().click()

    def click_visit_surveys_group_container(self):
        self.get_surveys_group_container().first.click()

    def click_scene_surveys_group_container(self):
        self.get_surveys_group_container().nth(1).click()

    def click_surveys_toggle_all_button(self):
        self.get_surveys_toggle_all_button().click()

    def _show_surveys_menu_item(self):
        return self.get_three_dots_menu_item_in_report().filter(has_text=contains(SURVEY_LABELS["showSurveys"]))

    def verify_show_surveys_menu_item_display(self):
        expect(self._show_surveys_menu_item().first).to_be_visible()

    def click_show_surveys_menu_item(self):
        self._show_surveys_menu_item().first.click()

    def verify_show_surveys_page_title(self):
        title = self.get_show_surveys_page_title().filter(has_text=contains(SURVEY_LABELS["surveys"]))
        expect(title).not_to_have_count(0)

    def verify_surveys_content_title(self):
        title = self.get_surveys_content_title().filter(has_text=contains(SURVEY_LABELS["surveys"]))
        expect(title).not_to_have_count(0)

    def verify_visit_survey_title(self, type_survey_title: str, visit_survey_title: str):
        expect(self.root().locator(type_survey_title).first).to_contain_text(contains(visit_survey_title))

    def verify_visit_survey_group_questions_and_answers_display(self):
        self.click_visit_surveys_group_container()
        expect(self.root().locator(test_data["typeQuestion"]).first).to_contain_text(
            contains(test_data["surveyQuestion"])
        )
        expect(self.root().locator(test_data["typeAnswer"]).first).to_contain_text(
            contains(test_data["visitSurveyAnswer"])
        )
        expect(self.root().locator(f'[src="{test_data["surveyImageUrl"]}"]').first).to_be_visible()
        self.click_visit_surveys_group_container()

    def verify_scene_survey_title(self, type_survey_title: str, scene_survey_title: str):
        expect(self.root().locator(type_survey_title).nth(1)).to_contain_text(contains(scene_survey_title))

    def verify_survey_group_title(self, visit_survey_group_header_title: str, scene_survey_group_header_title: str):
        titles = self.root().locator(test_data["typeSurveyGroupHeaderTitle"])
        expect(titles.first).to_contain_text(contains(visit_survey_group_header_title))
        expect(titles.nth(1)).to_contain_text(contains(scene_survey_group_header_title))

    def verify_survey_group_questions_count_display(
        self, visit_survey_group_questions_count: int, scene_survey_group_questions_count: int
    ):
        counts = self.get_survey_group_questions_count()
        expect(counts.first).to_have_text(re.compile(rf"^\s*{visit_survey_group_questions_count}(\.0+)?(\D|$)"))
        expect(counts.nth(1)).to_have_text(re.compile(rf"^\s*{scene_survey_group_questions_count}(\.0+)?(\D|$)"))
        expect(self.root().locator(".header-info").nth(1)).to_contain_text(contains(SURVEY_LABELS["questions"]))

    def verify_scene_survey_group_questions_and_answers_display(self):
        self.click_scene_surveys_group_container()
        expect(self.root().locator(test_data["typeQuestion"]).first).to_contain_text(
            contains(test_data["surveyQuestion"])
        )
        expect(self.root().locator(test_data["typeAnswer"]).first).to_contain_text(
            contains(test_data["sceneSurveyAnswer"])
        )
        self.click_scene_surveys_group_container()

    def verify_toggle_all_button(self):
        self.click_surveys_toggle_all_button()
        expect(self.root().locator(f'[src="{test_data["surveyImageUrl"]}"]').first).to_be_visible()
        self.click_surveys_toggle_all_button()
        expect(self.root().locator("body")).not_to_have_attribute(
            f'[src="{test_data["surveyImageUrl"]}"]', re.compile(".*")
        )

    def verify_show_surveys_menu_item_not_display(self):
        expect(self._show_surveys_menu_item()).to_have_count(0)
