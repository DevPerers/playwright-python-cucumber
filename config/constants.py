"""Constants ported from the Cypress project (globalConstants, mobileReportsConstants,
reportingConfigurationsConstants)."""

# --- global constants -------------------------------------------------------
ENV = "int"
COMMON_PROJECT = "autoqa1-int"
OKTA_LOGIN_PAGE_TITLE = "Trax Retail Solutions LTD - Sign In"
TRAX_HOME_PAGE_TITLE = "Trax Image Recognition"

URL_SEGMENTS = {
    "base_url_int": "https://services-int.traxretail.com/trax-one/",
    "base_url_int_short": "https://services-int.traxretail.com/",
    "base_url_prod": "https://services.traxretail.com/trax-one/",
    "okta_url": "https://traxretail.okta.com/login/login.htm",
    "home_url": "/homepage",
    "kpi_act_url": "/configuration-manager/kengine/kpi-activation",
    "common_mobile_store_url": "/mobile-reports/store/",
    "sale_rep_url": "/sales-rep/",
    "hide_panel_url": "?hidepanel=true",
    "mobile_explorer_visit_url": "/explore/visit/",
    "usr_mgr_url": "/user-management/users",
    "route_view_url": "/routes/view/",
    "store_url": "/stores",
    "training_task_url": "/navigation/training-tasks-setup",
    "mobile_rpt_kpi_url": "/configuration-manager/mobilereports/kpis",
    "explorer_visit_url": "/explore/visits",
    "report_config_mobile_reports_general_url": "/configuration-manager/mobilereports/general",
    "common_new_mobile_report_url": "mobile-reports-new/reports/",
    "live_url_segment": "/live/visit-summary",
    "regular_url_segment": "/regular/visit-summary",
    "report_config_explorer_url": "/configuration-manager/explorer/general",
    "mobile_report_session_uid_url_segment": "&sessionUid=",
    "products_and_brands_url": "/products-and-brands/tree",
    "products_and_brands_project_settings_url": "/products-and-brands/project-settings",
    "product_details_page_prodcut_image_url_segment": "https://traxus.s3.amazonaws.com/",
    "reporting_configurations_kengine_kpi_attributes_url": "/configuration-manager/kengine/kpi-attributes",
}

# --- mobile reports constants ----------------------------------------------
SURVEY_LABELS = {
    "showSurveys": "Show Surveys",
    "surveys": "Surveys",
    "questions": "Questions",
}

VIEW_IMAGES_LABELS = {
    "viewImages": "View Images",
    "images": "Images",
}

STORE_REPORT = {
    "StoreReport": "Store Report",
    "all": "All",
    "present": "Present",
    "missing": "Missing",
    "productDetailsPageHeader": "Product Details",
    "productStatus": "PRESENT",
    "popupHeader": "Closing Report",
    "popupMessage": "Are you sure you want to close the report? Any applied filters and visibility settings will be lost.",
    "noPresentProductsMessage": "No present products found for this report in the selected category with the selected oos reason",
    "show": "SHOW",
    "hide": "HIDE",
    "noOosReason": "No OOS Reason",
}

RECENT_VISITS_LABELS = {
    "recentVisits": "Recent Visits",
    "visitType": "Visit Type ",
    "date": "Date ",
}

PRODUCT_DETAILS_PAGE_LABELS = {
    "productDetails": "Product Details",
    "brand": "Brand:",
    "content": "Content:",
    "size": "Size:",
    "category": "Category:",
    "eanCode": "EAN Code:",
}

PRODUCT_DETAILS_PAGE_PRODUCT_PROPERTIES = {
    "brand": "Brand",
    "content": "Content",
    "size": "Size",
    "category": "Category",
    "eanCode": "EAN Code",
}

ACTIONS_PAGE_GROUPING_OPTIONS = {
    "noGrouping": "No Grouping",
    "byCategory": "By Category",
    "byKpi": "By KPI",
    "byBrand": "By Brand",
}

RECALCULATION_POP_UP = {
    "thankYou": "Thank you",
    "popUpMessageSubLine1": "We are processing the new information.",
    "popUpMessageSubLine2": "Once validated, the handled products will be updated in your report.",
    "popUpMessageSubLine3": "When done with your actions, please end your visit.",
}

RECALCULATION_STATUSES = {
    "recalculated": "Recalculated",
    "partiallyRecalculated": "Partially Recalculated",
}

RECALCULATION_SECTION_COLORS = {
    "recalculated": "rgb(8, 131, 183)",
    "partiallyRecalculated": "rgb(249, 183, 35)",
}

KPI_CIRCLE_DEFAULT_COLOR = "#7797ab"

ACTIONS_PAGE_USER_FEEDBACK_BUTTONS = {
    "oosReason": "OOS REASON",
    "oosReasonForSliding": "OOS Reason",
    "editOosReason": "EDIT OOS REASON",
    "editOosReasonForSliding": "Edit OOS Reason",
}

MOBILE_REPORT_HEADER_TITLES = {
    "regularReportHeaderTitle": "Visit Summary",
}

DELTA_COLORS = {
    "positiveDeltaColor": "rgb(125, 187, 43)",
    "negativeDeltaColor": "rgb(255, 0, 31)",
}

# --- reporting configurations constants ------------------------------------
REPORTING_CONFIGURATIONS_APP_NAME = "Reporting Configurations"

REPORTING_CONFIGURATIONS_PAGES = {
    "mobileReports": "Mobile Reports",
}

REPORTING_CONFIGURATIONS_TABS = {
    "general": "General",
    "oosReasons": "OOS Reasons",
}

REPORTING_CONFIGURATIONS_TABLES = {
    "storeReportTable": 0,
    "actionTable": 1,
}

REPORTING_CONFIGURATIONS_BUTTONS = {
    "storeReportKpiButton": 1,
    "actionsTableKpiButton": 2,
}

DEFAULT_ACTIONS_PAGE_LAYOUT_DROPDOWN_VALUES = {
    "actionsGroupingOption1": "Ungrouped",
    "actionsGroupingOption2": "By Category",
    "actionsGroupingOption3": "By KPI",
    "actionsGroupingOption4": "By Brand",
}

COLOR_THRESHOLD_COLORS_AND_BUTTON = {
    "addThresholdButton": "ADD THRESHOLD",
    "thresholdColors": ["#BBBBBB", "#7797AB", "#B31225", "#7DBB2B", "#F9B723"],
}
