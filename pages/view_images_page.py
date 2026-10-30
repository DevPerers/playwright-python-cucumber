import re

from playwright.sync_api import expect

from config.constants import VIEW_IMAGES_LABELS
from pages.mobile_reports_iframe_base_page import MobileReportsIframeBasePage
from utils.test_data import load_test_data

test_data = load_test_data("viewImagesPageTestData")

TEXT_CONTENTS = "elements => elements.map(element => element.textContent)"


def contains(text: str):
    return re.compile(re.escape(text))


def exact(text: str):
    return re.compile(f"^{re.escape(text)}$")


def without_whitespace(text: str) -> str:
    return re.sub(r"\s", "", text)


class ViewImagesPage(MobileReportsIframeBasePage):
    def __init__(self, page, use_iframe: bool):
        super().__init__(page, use_iframe)

    def check_page_title_contains(self, page_title: str):
        expect(self.page).to_have_title(page_title)

    def get_visit_id_search_field(self):
        return self.page.locator('.input-with-icon > input[placeholder="Visit ID"]')

    def get_explorer_visits_search_button(self):
        return self.page.locator(".input-with-icon > .button")

    def get_three_dots_menu_in_report(self):
        return self.root().locator('[src="ellipsis"]')

    def get_three_dots_menu_item_in_report(self):
        return self.root().locator(".menu-item")

    def get_page_title(self):
        return self.root().locator(".header-title")

    def get_scene_cards_expand_arrow_buttons(self):
        return self.root().locator(".trax-icon-up-arrow-triangle")

    def get_view_images_page_scene_card_scene_titles(self):
        return self.root().locator(".title-above-card")

    def get_view_images_page_scene_card_thumbnails(self):
        return self.root().locator(".img-item-thumbnail")

    def get_scene_card_scene_ids(self):
        return self.root().locator(".img-item-details-scene-id")

    def get_scene_card_scene_names(self):
        return self.root().locator(".img-item-details-type")

    def get_number_of_images_on_scene_cards(self):
        return self.root().locator(".img-item-details-count > div")

    def get_image_icon_after_number_of_images(self):
        return self.root().locator(".trax-icon-image")

    def get_image_scene_statuses(self):
        return self.root().locator(".img-item-card-right")

    def get_approved_icon_after_scene_statuses(self):
        return self.root().locator(".trax-icon-approved")

    def get_product_tagging_page_image(self):
        return self.root().locator(".openseadragon-canvas")

    def get_product_tagging_page_show_tags_button_text(self):
        return self.root().locator(".trax-form-label")

    def get_product_tagging_page_show_tags_button(self):
        return self.root().locator(".form-check-input")

    def get_product_tagging_page_image_tags(self):
        return self.root().locator(".tag-image")

    def get_product_tagging_page_image_tags_pop_up_text(self):
        return self.root().locator(".tag-name-container")

    def get_mobile_report_header_title(self):
        return self.root().locator(".header-title")

    def get_tag_image_pop_up(self):
        return self.root().locator(".tag-container")

    def search_by_visit_id(self, visit_id: str):
        search_field = self.get_visit_id_search_field()
        search_field.click()
        search_field.press_sequentially(visit_id)
        self.get_explorer_visits_search_button().click()

    def navigate_to_regular_report_on_explorer(self, is_show_live_report_first: bool):
        header_title = self.get_mobile_report_header_title()
        if not is_show_live_report_first:
            expect(header_title.filter(has_text=contains("Visit Summary"))).not_to_have_count(0)
        else:
            expect(header_title.filter(has_text=contains("Live Summary"))).not_to_have_count(0)
            self.get_three_dots_menu_in_report().click()
            self.get_three_dots_menu_item_in_report().filter(has_text=contains("Visit Summary")).first.click()

    def click_three_dots_menu_in_report(self):
        self.get_three_dots_menu_in_report().click()

    def click_view_images_menu_item(self):
        self.get_three_dots_menu_item_in_report().filter(
            has_text=contains(VIEW_IMAGES_LABELS["viewImages"])
        ).first.click()

    def verify_page_title(self, page_header: str):
        title_locator = self.get_page_title()
        expect(title_locator.first).to_be_attached()
        title = "".join(title_locator.evaluate_all(TEXT_CONTENTS))
        if VIEW_IMAGES_LABELS["images"] in page_header:
            assert without_whitespace(title) == page_header
        else:
            assert page_header in title

    def verify_scene_cards_titles(self, index: int, scene_name: str):
        expect(self.get_view_images_page_scene_card_scene_titles().nth(index)).to_have_text(exact(scene_name))

    def verify_scene_card_titles_sorting(self):
        titles = self.get_view_images_page_scene_card_scene_titles()
        expect(titles.first).to_be_attached()
        unsorted_titles = titles.evaluate_all(TEXT_CONTENTS)
        assert unsorted_titles == sorted(unsorted_titles), "Scene cards titles are sorted"

    def open_view_images_page_scene_cards(self):
        arrows = self.get_scene_cards_expand_arrow_buttons()
        expect(arrows.first).to_be_visible()
        for arrow in arrows.element_handles():
            arrow.click()

    @staticmethod
    def _expect_all_visible(locator):
        expect(locator.first).to_be_visible()
        for index in range(locator.count()):
            expect(locator.nth(index)).to_be_visible()

    def verify_scene_card_thumbnails(self):
        self._expect_all_visible(self.get_view_images_page_scene_card_thumbnails())

    def verify_scene_card_scene_ids(self, index: int, scene_id: str):
        expect(self.get_scene_card_scene_ids().nth(index)).to_have_text(exact(scene_id))

    def verify_scene_card_scene_names(self, index: int, scene_name: str):
        expect(self.get_scene_card_scene_names().nth(index)).to_have_text(exact(scene_name))

    def verify_number_of_images_on_scene_cards(self, index: int, image_count: str):
        expect(self.get_number_of_images_on_scene_cards().nth(index)).to_have_text(exact(image_count))

    def verify_image_icon_after_number_of_images(self):
        self._expect_all_visible(self.get_image_icon_after_number_of_images())

    def verify_image_scene_statuses(self):
        status = self.get_image_scene_statuses().first
        expect(status).to_be_attached()
        assert without_whitespace(status.text_content()) == "Completed"

    def verify_approved_icon_after_scene_statuses(self):
        self._expect_all_visible(self.get_approved_icon_after_scene_statuses())

    def navigate_to_product_tagging_page(self):
        self.get_view_images_page_scene_card_thumbnails().first.click()

    def verify_product_tagging_page_image_visibility(self):
        expect(self.get_product_tagging_page_image()).to_be_visible()

    def verify_product_tagging_page_show_tags_button(self):
        expect(self.get_product_tagging_page_show_tags_button_text()).to_have_text(
            exact(f"Show Tags ({test_data['productTaggingPageImageTagsCount']})")
        )
        expect(self.get_product_tagging_page_show_tags_button()).to_be_visible()

    def verify_not_showing_image_tags(self):
        expect(self.get_product_tagging_page_image_tags().first).not_to_have_class(re.compile(r"\.tag-image"))

    def click_product_tagging_page_show_tags_button(self):
        self.get_product_tagging_page_show_tags_button().click()

    def verify_product_tagging_page_image_tags(self, image_tag_index: int, image_url: str, image_text: str):
        tag = self.get_product_tagging_page_image_tags().nth(image_tag_index)
        tag.click()
        expect(self.get_tag_image_pop_up()).to_be_visible()
        tag.click()
        expect(self.root().locator(f'[src="{image_url}"]').first).to_be_visible()
        pop_up_text = self.get_product_tagging_page_image_tags_pop_up_text()
        expect(pop_up_text).to_be_visible()
        expect(pop_up_text).to_have_text(exact(image_text))
        tag.click()
