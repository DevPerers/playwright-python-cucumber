import re

from playwright.sync_api import Page, expect

from config.config import Config
from config.constants import URL_SEGMENTS


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to(self, url: str, timeout=60000):
        self.page.goto(url, wait_until="domcontentloaded", timeout=timeout)
        self.page.wait_for_load_state("load", timeout=timeout)

    def wait_for_page_ready(self, timeout=60000):
        self.page.wait_for_load_state("domcontentloaded", timeout=timeout)
        self.page.wait_for_load_state("load", timeout=timeout)

    def get_ready_locator(self, selector, timeout=60000):
        locator = self.page.locator(selector)
        expect(locator).to_be_visible(timeout=timeout)
        expect(locator).to_be_enabled(timeout=timeout)
        return locator

    def fill_when_ready( self, selector: str, value: str, timeout=60000):
        locator = self.get_ready_locator(selector, timeout)
        locator.fill(value)

    def click_when_ready(self, selector: str, timeout=60000):
        locator = self.get_ready_locator(selector, timeout)
        locator.click(timeout=timeout, force=True)

    def get_text(self, selector: str, timeout=60000):
        locator = self.page.locator(selector)
        expect(locator).to_be_visible(timeout=timeout)
        return locator.inner_text()

    # ------------------------------------------------------------------
    # URL builders (ported from the Cypress BasePage)
    # ------------------------------------------------------------------
    @staticmethod
    def _with_trailing_slash(url: str) -> str:
        return url.rstrip("/") + "/"

    def get_common_url(self, project_name: str) -> str:
        return self._with_trailing_slash(Config.TRAX_BASE_URL) + project_name

    def get_new_common_url(self) -> str:
        base_url = Config.TRAX_BASE_URL.replace("trax-one", "").rstrip("/") or URL_SEGMENTS["base_url_int_short"]
        return self._with_trailing_slash(base_url)

    def get_home_page_url(self, project_name: str) -> str:
        return self.get_common_url(project_name) + URL_SEGMENTS["home_url"]

    def get_reporting_config_page_url(self, project_name: str) -> str:
        return self.get_common_url(project_name) + URL_SEGMENTS["kpi_act_url"]

    def get_reporting_configurations_mobile_reports_general_page_url(self, project_name: str) -> str:
        return self.get_common_url(project_name) + URL_SEGMENTS["report_config_mobile_reports_general_url"]

    def get_reporting_configurations_mobile_reports_kpis_page_url(self, project_name: str) -> str:
        return self.get_common_url(project_name) + URL_SEGMENTS["mobile_rpt_kpi_url"]

    def get_reporting_configurations_explorer_page_url(self, project_name: str) -> str:
        return self.get_common_url(project_name) + URL_SEGMENTS["report_config_explorer_url"]

    def get_mobile_report_page_url(self, project_name: str, store_id: str, sale_rep_id: str) -> str:
        return (
            self.get_common_url(project_name)
            + URL_SEGMENTS["common_mobile_store_url"]
            + store_id
            + URL_SEGMENTS["sale_rep_url"]
            + sale_rep_id
            + URL_SEGMENTS["hide_panel_url"]
        )

    def get_old_mobile_report_page_url_with_session_uid(
        self, project_name: str, store_id: str, sale_rep_id: str, session_uid: str
    ) -> str:
        return (
            self.get_mobile_report_page_url(project_name, store_id, sale_rep_id)
            + URL_SEGMENTS["mobile_report_session_uid_url_segment"]
            + session_uid
        )

    def get_new_live_mobile_report_page_url_with_session_uid(self, project: str, session_uid: str) -> str:
        return (
            self.get_new_common_url()
            + URL_SEGMENTS["common_new_mobile_report_url"]
            + project
            + "/"
            + session_uid
            + URL_SEGMENTS["live_url_segment"]
        )

    def get_new_regular_mobile_report_page_url_with_session_uid(self, project: str, session_uid: str) -> str:
        return (
            self.get_new_common_url()
            + URL_SEGMENTS["common_new_mobile_report_url"]
            + project
            + "/"
            + session_uid
            + URL_SEGMENTS["regular_url_segment"]
        )

    def get_mobile_report_explore_page_url(self, project_name: str, session_id: str) -> str:
        return self.get_common_url(project_name) + URL_SEGMENTS["mobile_explorer_visit_url"] + session_id

    def get_users_page_login_url(self, project_name: str) -> str:
        return self.get_common_url(project_name) + URL_SEGMENTS["usr_mgr_url"]

    def get_data_collection_page_login_url(self, project_name: str) -> str:
        return self.get_common_url(project_name) + URL_SEGMENTS["route_view_url"]

    def get_stores_page_login_url(self, project_name: str) -> str:
        return self.get_common_url(project_name).replace("trax-one", "stores") + URL_SEGMENTS["store_url"]

    def get_training_acc(self, project_name: str) -> str:
        return self.get_common_url(project_name).replace("trax-one", "qat-training") + URL_SEGMENTS["training_task_url"]

    def get_mobile_reporting_config_page(self, project_name: str) -> str:
        return self.get_common_url(project_name) + URL_SEGMENTS["mobile_rpt_kpi_url"]

    def get_explorer_visit_page_url(self, project_name: str) -> str:
        return self.get_common_url(project_name) + URL_SEGMENTS["explorer_visit_url"]

    def get_products_and_brands_page_url(self, project_name: str) -> str:
        return self.get_common_url(project_name) + URL_SEGMENTS["products_and_brands_url"]

    def get_products_and_brands_project_settings_page(self, project_name: str) -> str:
        return self.get_common_url(project_name) + URL_SEGMENTS["products_and_brands_project_settings_url"]

    def get_reporting_configurations_kengine_kpi_attributes_page(self, project_name: str) -> str:
        return self.get_common_url(project_name) + URL_SEGMENTS["reporting_configurations_kengine_kpi_attributes_url"]

    # ------------------------------------------------------------------
    # Navigation (Cypress: goTo*)
    # ------------------------------------------------------------------
    def go_to_products_and_brands_page(self, project_name: str):
        self.navigate_to(self.get_products_and_brands_page_url(project_name))

    def go_to_explorer_visit_page(self, project_name: str):
        self.navigate_to(self.get_explorer_visit_page_url(project_name))

    def go_to_users(self, project_name: str):
        self.navigate_to(self.get_users_page_login_url(project_name))

    def go_to_training_acc(self, project_name: str):
        self.navigate_to(self.get_training_acc(project_name))

    def go_to_login_page(self, project_name: str):
        common_url = self.get_common_url(project_name)
        self.navigate_to(common_url[: common_url.rfind("/")])

    def go_to_home_page(self, project_name: str):
        self.navigate_to(self.get_home_page_url(project_name))

    def go_to_reporting_config_page(self, project_name: str):
        self.navigate_to(self.get_reporting_config_page_url(project_name))

    def go_to_reporting_configurations_mobile_reports_general_page(self, project_name: str):
        self.navigate_to(self.get_reporting_configurations_mobile_reports_general_page_url(project_name))

    def go_to_reporting_configurations_mobile_reports_kpis_page(self, project_name: str):
        self.navigate_to(self.get_reporting_configurations_mobile_reports_kpis_page_url(project_name))

    def go_to_reporting_configurations_explorer_page(self, project_name: str):
        self.navigate_to(self.get_reporting_configurations_explorer_page_url(project_name))

    def go_to_mobile_reporting_config_page(self, project_name: str):
        self.navigate_to(self.get_mobile_reporting_config_page(project_name))

    def go_to_mobile_report_page(self, project_name: str, store_id: str, sale_rep_id: str):
        self.navigate_to(self.get_mobile_report_page_url(project_name, store_id, sale_rep_id))

    def go_to_old_mobile_report_page_with_session_uid(
        self, project_name: str, store_id: str, sale_rep_id: str, session_uid: str
    ):
        self.navigate_to(
            self.get_old_mobile_report_page_url_with_session_uid(project_name, store_id, sale_rep_id, session_uid)
        )

    def go_to_new_live_mobile_report_page_with_session_uid(self, project_name: str, session_uid: str):
        self.navigate_to(self.get_new_live_mobile_report_page_url_with_session_uid(project_name, session_uid))

    def go_to_new_regular_mobile_report_page_with_session_uid(self, project_name: str, session_uid: str):
        self.navigate_to(self.get_new_regular_mobile_report_page_url_with_session_uid(project_name, session_uid))

    def go_to_mobile_report_explore(self, project_name: str, session_id: str):
        self.navigate_to(self.get_mobile_report_explore_page_url(project_name, session_id))

    def go_to_products_and_brands_project_settings_page(self, project_name: str):
        self.navigate_to(self.get_products_and_brands_project_settings_page(project_name))

    def go_to_data_collection(self, project_name: str):
        self.navigate_to(self.get_data_collection_page_login_url(project_name))

    def go_to_stores(self, project_name: str):
        self.navigate_to(self.get_stores_page_login_url(project_name))

    def go_to_reporting_configurations_kengine_kpi_attributes_page(self, project_name: str):
        self.navigate_to(self.get_reporting_configurations_kengine_kpi_attributes_page(project_name))

    # ------------------------------------------------------------------
    # Common assertions / actions
    # ------------------------------------------------------------------
    def validate_page_title(self, page_title: str):
        expect(self.page).to_have_title(page_title)

    def check_page_url(self, page_url: str):
        expect(self.page).to_have_url(page_url)

    def validate_url_contains(self, page_url: str):
        expect(self.page).to_have_url(re.compile(re.escape(page_url)))

    def refresh_page(self):
        self.page.reload()

    def search_for(self, value: str):
        self.page.locator('[placeholder="Search..."]').press_sequentially(value)

    def select_option_from_left_pane_tab_menu(self, menu_option: str):
        self.page.locator(".navigation-tab", has_text=menu_option).first.click()
