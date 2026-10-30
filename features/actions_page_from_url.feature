@from_url
Feature: Mobile Reports Actions Page Feature

  This contains the Mobile Reports Actions Page feature

  Background: Login to Trax and navigate to Reporting Configuration Mobile Reports General page & remove all KPIs linked to actions
    Given I login to Trax successfully through Okta
    When  I navigate to the Reporting configurations Mobile Reports General page
    And   I can see the "Mobile Reports" title
    And   I remove all KPIs form the KPIs Linked to Actions table

  @commented_out_in_cypress
  Scenario: Configure KPIs to actions & verify showing actions in mobile report according to Collapse OOS Action Groups checkbox
    When  I add KPIs if they are not added to the KPIs Linked to Actions table
    And   I check "Collapse OOS Action Groups" checkbox if it is unchecked & save changes
    And   I navigate to live mobile report through URL
    And   I click on the Actions button when the actions are collapsed and see the collapsed actions
    And   I navigate to the Reporting configurations Mobile Reports General page
    And   I uncheck "Collapse OOS Action Groups" checkbox if it is checked & save changes
    And   I navigate to live mobile report through URL
    And   I click on the Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions

  @commented_out_in_cypress
  Scenario: Configure KPIs to actions & navigate to mobile report & navigate to Actions page & verify the actions count on the report when there are actions
    When  I add KPIs if they are not added to the KPIs Linked to Actions table
    And   I uncheck "Collapse OOS Action Groups" checkbox if it is checked & save changes
    And   I navigate to live mobile report through URL
    And   I click on the Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions
    And   I verify the actions count on the pending tab count badge
    And   I click on the Back Arrow in the Actions page
    And   I verify the actions count on the Actions button
    And   I reload the page
    And   I click on the Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions
    And   I navigate to Handled tab
    Then  I verify the actions count on the handled tab count badge

  @commented_out_in_cypress
  Scenario: Navigate to mobile report & navigate to Actions page and verify Actions count on the report when there are no actions in the report
    When  I navigate to live mobile report through URL
    And   I click on the Actions button when there are no actions on the Report
    And   I verify the actions count on the pending tab count badge
    And   I click on the Back Arrow in the Actions page
    And   I verify the actions count on the Actions button
    And   I reload the page
    And   I click on the Actions button when there are no actions on the Report
    And   I navigate to Handled tab
    Then  I verify the actions count on the handled tab count badge

  @commented_out_in_cypress
  Scenario: Configure KPIs to Actions, disable fraud prevention for OOS Reason, configure OOS & Override messages on Reporting Configurations & verify not showing the Override messages for OOS Reason on mobile report
    When  I add KPIs if they are not added to the KPIs Linked to Actions table
    And   I navigate to the Mobile Reports OOS Reasons page
    And   I configure OOS messages for User Override
    And   I navigate to Reporting configurations Mobile Reports General page tab
    And   I uncheck "Enable time based fraud prevention for OOS reason" checkbox if it is checked & save changes
    And   I uncheck "Collapse OOS Action Groups" checkbox if it is checked & save changes
    And   I navigate to live mobile report through URL
    And   I click on the Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions
    And   I slide an SKU and click on the OOS Reason button
    Then  I verify the Override messages is not shwon for OOS Reason

  @commented_out_in_cypress
  Scenario: Configure KPIs to actions & navigate to Explorer Visit Viewer Page & navigate to Category KPI page & verify the actions count on the actions page when there are actions
    When  I add KPIs if they are not added to the KPIs Linked to Actions table
    And   I uncheck "Collapse OOS Action Groups" checkbox if it is checked & save changes
    And   I navigate to regular mobile report through URL
    And   I navigate to category KPI page
    And   I click on the Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions
    And   I verify the actions count on the pending tab count badge
    And   I click on the Back Arrow in the Actions page
    And   I verify the actions count on the Actions button
    And   I reload the page
    And   I click on the Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions
    And   I navigate to Handled tab
    Then  I verify the actions count on the handled tab count badge

  @commented_out_in_cypress
  Scenario: Navigate to mobile report & navigate to Category KPI page & verify Actions count on the report when there are no actions in the report
    When  I navigate to regular mobile report through URL
    And   I click on the Actions button when there are no actions on the Report
    And   I verify the actions count on the pending tab count badge
    And   I click on the Back Arrow in the Actions page
    And   I verify the actions count on the Actions button
    And   I reload the page
    And   I click on the Actions button when there are no actions on the Report
    And   I navigate to Handled tab
    Then  I verify the actions count on the handled tab count badge

  @commented_out_in_cypress
  Scenario: Configure single KPI per live and per regular to actions, configure Ungrouped as default actions page layout & verify the actions are ungrouped in actions page of mobile report
    When  I add single KPIs per live and per regular if they are not added to the KPIs Linked to Actions table
    And   I configure "Ungrouped" option for default actions page layout
    And   I uncheck "Collapse OOS Action Groups" checkbox if it is checked & save changes
    And   I navigate to regular mobile report through URL
    And   I click on the Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions
    Then  I verify showing all the actions grouping options in the actions page
    And   I verify that the "No Grouping" actions grouping option has selected in the grouping options menu
    And   I verify that the SKUs have ungrouped

  @commented_out_in_cypress
  Scenario: Configure single KPI per live and per regular to actions, configure By Category as default actions page layout & verify showing the actions By Category in the actions page of mobile report
    When  I add single KPIs per live and per regular if they are not added to the KPIs Linked to Actions table
    And   I configure "By Category" option for default actions page layout
    And   I uncheck "Collapse OOS Action Groups" checkbox if it is checked & save changes
    And   I navigate to regular mobile report through URL
    And   I click on the Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions
    Then  I verify showing all the actions grouping options in the actions page
    And   I verify that the "By Category" actions grouping option has selected in the grouping options menu
    And   I verify that the SKUs have grouped By Category in the actions page

  @commented_out_in_cypress
  Scenario: Configure single KPI per live and per regular to actions, configure By KPI as default actions page layout & verify showing the actions By KPI in the actions page of mobile report
    When  I add single KPIs per live and per regular if they are not added to the KPIs Linked to Actions table
    And   I configure "By KPI" option for default actions page layout
    And   I uncheck "Collapse OOS Action Groups" checkbox if it is checked & save changes
    And   I navigate to regular mobile report through URL
    And   I click on the Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions
    Then  I verify showing all the actions grouping options in the actions page
    And   I verify that the "By KPI" actions grouping option has selected in the grouping options menu
    And   I verify that the SKUs have grouped By KPI in the actions page

  @commented_out_in_cypress
  Scenario: Configure single KPI per live and per regular to actions, configure By Brand as default actions page layout & verify showing the actions By Brand in the actions page of mobile report
    When  I add single KPIs per live and per regular if they are not added to the KPIs Linked to Actions table
    And   I configure "By Brand" option for default actions page layout
    And   I uncheck "Collapse OOS Action Groups" checkbox if it is checked & save changes
    And   I navigate to live mobile report through URL
    And   I click on the Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions
    Then  I verify showing all the actions grouping options in the actions page
    And   I verify that the "By Brand" actions grouping option has selected in the grouping options menu
    And   I verify that the SKUs have grouped By Brand in the actions page

  @commented_out_in_cypress
  Scenario: Configure multiple KPIs per live and per regular to actions & navigate to mobile report & navigate to Actions page & verify showing the actions By KPI in the report
    When  I add KPIs if they are not added to the KPIs Linked to Actions table
    And   I verify configuration of By KPI as default actions page layout dropdown value in Reporting Configurations
    And   I uncheck "Collapse OOS Action Groups" checkbox if it is checked & save changes
    And   I navigate to regular mobile report through URL
    And   I click on the Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions
    Then  I verify showing only the By KPI actions grouping options in the actions page

  @commented_out_in_cypress
  Scenario: Configure KPIs to Actions, disable fraud prevention for OOS Reason, configure OOS & Override messages on Reporting Configurations & verify handling actions by OOS Reason on mobile report
    When  I add KPIs if it is not added to the KPIs Linked to Actions table
    And   I navigate to the Mobile Reports OOS Reasons page
    And   I verify configured OOS messages in Reporting Configurations OOS messages page
    And   I configure default OOS message in Reporting Configurations OOS messages page
    And   I navigate to Reporting configurations Mobile Reports General page tab
    And   I uncheck "Enable time based fraud prevention for OOS reason" checkbox if it is checked & save the changes
    And   I uncheck "Collapse OOS Action Groups" checkbox if it is checked & save the changes
    And   I navigate to live mobile report through URL
    And   I click on the Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions
    And   I click on an SKU, navigate to the product details page, click on the OOS Reason button and handle the SKU
    And   I verify that the SKU is handled
    And   I edit the OOS Reason of the handle SKU by product details page
    And   I verify the edited OOS Reason of the SKU
    And   I remove the OOS Reason of the handled SKU by product details page
    And   I verify the OOS Reason has removed and the SKU moved to the pending tab again
    Then  I verify the SKU is not in the handled tab after OOS Reason removing

  @commented_out_in_cypress
  Scenario: Configure KPIs to Actions, enable displaying the date and time for user feedback, configure OOS messages & verify handled date & time for OOS actions on mobile report
    When  I add KPIs if it is not added to the KPIs Linked to Actions table
    And   I navigate to the Mobile Reports OOS Reasons page
    And   I verify configured OOS messages in Reporting Configurations OOS messages page
    And   I configure default OOS message in Reporting Configurations OOS messages page
    And   I navigate to Reporting configurations Mobile Reports General page tab
    And   I check "Enable displaying the date and time of the provided user feedback" checkbox if it is unchecked & save the changes
    And   I uncheck "Collapse OOS Action Groups" checkbox if it is checked & save the changes
    And   I navigate to live mobile report through URL
    And   I click on the Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions
    And   I click on an SKU, navigate to the product details page, click on the OOS Reason button and handle the SKU
    And   I verify that the SKU is handled
    Then  I verify display date and time for the provided user feedback
    And   I remove the OOS Reason of the handled SKU by product details page

  @commented_out_in_cypress
  Scenario: Configure KPIs to Actions, disable displaying the date and time for user feedback, configure OOS messages & verify not showing handled date & time for OOS actions on mobile report
    When  I add KPIs if it is not added to the KPIs Linked to Actions table
    And   I navigate to the Mobile Reports OOS Reasons page
    And   I verify configured OOS messages in Reporting Configurations OOS messages page
    And   I configure default OOS message in Reporting Configurations OOS messages page
    And   I navigate to Reporting configurations Mobile Reports General page tab
    And   I uncheck "Enable displaying the date and time of the provided user feedback" checkbox if it is checked & save the changes
    And   I uncheck "Collapse OOS Action Groups" checkbox if it is checked & save the changes
    And   I navigate to live mobile report through URL
    And   I click on the Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions
    And   I click on an SKU, navigate to the product details page, click on the OOS Reason button and handle the SKU
    And   I verify that the SKU is handled
    Then  I verify not display date and time for the provided user feedback
    And   I remove the OOS Reason of the handled SKU by product details page

  @commented_out_in_cypress
  Scenario: Configure single regular KPI to actions & verify the category order of actions in the actions page of mobile report
    When  I add single regular KPI if it is not added to the KPIs Linked to Actions table for category order test
    And   I configure "By Category" option for default actions page layout
    And   I check "Collapse OOS Action Groups" checkbox if it is unchecked & save changes
    And   I configure category order in category order table
    And   I navigate to regular mobile report through URL for category order test
    And   I click on the Actions button when the actions are collapsed and see the collapsed actions for category order test
    Then  I verify category order in actions page

  @commented_out_in_cypress
  Scenario: Configure single regular KPI to actions, check Allow Recalculation checkbox, verify showing Submit Feedback button in the actions page of mobile report & verify recalculation
    When  I add single regular KPI if it is not added to the KPIs Linked to Actions table for category order test
    And   I check "Allow Recalculation" checkbox if it is unchecked & save the changes
    And   I navigate to regular mobile report through URL for Submit Feedback test
    And   I click on the Actions button when the actions are collapsed and see the collapsed actions for category order test
    Then  I verify whether the Submit Feedback button is visible on the Pending page of the Actions page
    And   I navigate to Handled tab
    And   I verify whether the Submit Feedback button is visible on the Handled page of the Actions page
    And   I verify Submit Feedback

  @commented_out_in_cypress
  Scenario: Configure single regular KPI to actions, uncheck Allow Recalculation checkbox & verify not showing Submit Feedback button in the actions page of mobile report
    When  I add single regular KPI if it is not added to the KPIs Linked to Actions table for category order test
    And   I uncheck "Allow Recalculation" checkbox if it is checked & save the changes
    And   I navigate to regular mobile report through URL for Submit Feedback test
    And   I click on the Actions button when the actions are collapsed and see the collapsed actions for category order test
    Then  I verify whether the Submit Feedback button is not visible on the Pending page of the Actions page
    And   I navigate to Handled tab
    And   I verify whether the Submit Feedback button is not visible on the Handled page of the Actions page

  @commented_out_in_cypress
  @flaky
  Scenario: Configure single live KPI to actions, check Allow Recalculation checkbox, verify showing Submit Feedback button in the actions page of mobile report & verify Partial Recalculation
    When  I add single live KPI if it is not added to the KPIs Linked to Actions table for partial recalculation test
    And   I uncheck "Collapse OOS Action Groups" checkbox if it is checked & save the changes
    And   I check "Allow Recalculation" checkbox if it is unchecked & save the changes
    And   I navigate to live mobile report through URL for Partial Recalculation test
    And   I click on the Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions
    Then  I verify whether the Submit Feedback button is visible on the Pending page of the Actions page
    And   I navigate to Handled tab
    And   I verify displaying of the invalid barcode icon for particular SKU in the Handled page of the Actions page
    And   I verify whether the Submit Feedback button is visible on the Handled page of the Actions page
    And   I verify Partial Recalculation when having invalid barcode for user feedback

  @commented_out_in_cypress
  Scenario: Configure KPIs to Actions, disable time based fraud prevention for OOS Reason, configure OOS messages on Reporting Configurations & verify displaying OOS Reason button on mobile report
    When  I add KPIs if it is not added to the KPIs Linked to Actions table
    And   I navigate to the Mobile Reports OOS Reasons page
    And   I verify configured OOS messages in Reporting Configurations OOS messages page
    And   I navigate to Reporting configurations Mobile Reports General page tab
    And   I uncheck "Enable time based fraud prevention for OOS reason" checkbox if it is checked & save the changes
    And   I uncheck "Collapse OOS Action Groups" checkbox if it is checked & save the changes
    And   I navigate to live mobile report through URL
    And   I click on the Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions
    And   I navigate to the product details page by clicking on an SKU
    Then  I verify that the OOS Reason button is displayed on product details page

  @commented_out_in_cypress
  @flaky
  Scenario: Configure KPIs to Actions, enable time based fraud prevention for OOS Reason, configure OOS messages on Reporting Configurations & verify not displaying OOS Reason button on mobile report
    When  I add KPIs if it is not added to the KPIs Linked to Actions table
    And   I navigate to the Mobile Reports OOS Reasons page
    And   I verify configured OOS messages in Reporting Configurations OOS messages page
    And   I navigate to Reporting configurations Mobile Reports General page tab
    And   I check "Enable time based fraud prevention for OOS reason" checkbox if it is unchecked & save the changes
    And   I configure time for OOS time based fraud prevention & save the changes
    And   I uncheck "Collapse OOS Action Groups" checkbox if it is checked & save the changes
    And   I navigate to live mobile report through URL
    And   I click on the Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions
    And   I navigate to the product details page by clicking on an SKU
    Then  I verify that the OOS Reason button is not displayed on product details page

  @commented_out_in_cypress
  Scenario: Navigate to Product Details page of the Actions page and verify the page layout and product details according to the Products and Brands app
    When  I add KPIs if they are not added to the KPIs Linked to Actions table
    And   I navigate to live mobile report through URL
    And   I click on the Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions
    And   I navigate to the product details page by clicking on an SKU
    Then  I see the page title as "Product Details"
    And   I verify the Product Details page layout and content
    And   I navigate to the Products and Brands app
    And   I navigate to the product page and verify that the Actions page product details are equal to the product details in the Products and Brands app

  @commented_out_in_cypress
  Scenario: Configure KPIs to Actions, disable fraud prevention for OOS Reason, configure OOS & Override messages on Reporting Configurations & verify handling actions by OOS Reason, editing OOS Reason and removing OOS Reason with multiple selection on mobile report
    When  I add KPIs if it is not added to the KPIs Linked to Actions table
    And   I navigate to the Mobile Reports OOS Reasons page
    And   I verify configured OOS messages in Reporting Configurations OOS messages page
    And   I configure default OOS message in Reporting Configurations OOS messages page
    And   I navigate to Reporting configurations Mobile Reports General page tab
    And   I uncheck "Enable time based fraud prevention for OOS reason" checkbox if it is checked & save the changes
    And   I uncheck "Collapse OOS Action Groups" checkbox if it is checked & save the changes
    And   I navigate to live mobile report through URL
    And   I click on the Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions
    And   I long press on SKUs
    And   I verify displaying of the Bulk Edit icon
    And   I verify the count of multiple selected products
    And   I verify the close button of multiple selected products
    And   I verify the All button of multiple selected products
    And   I handle the multiple selected SKUs by clicking on the OOS Reason button
    And   I verify that the SKUs are handled
    And   I navigate to live mobile report through URL
    And   I click on the Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions
    And   I navigate to Handled tab
    And   I edit the OOS Reason of the handled SKUs by multiple selecting
    And   I verify the edited OOS Reason of the multiple handled SKUs
    And   I navigate to live mobile report through URL
    And   I click on the Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions
    And   I navigate to Handled tab
    And   I remove the OOS Reason of the handled SKUs by multiple selecting
    And   I verify the OOS Reason has removed and the SKUs are moved to the pending tab again
    Then  I verify that the SKUs are not in the handled tab after OOS Reason removing

  @commented_out_in_cypress
  Scenario: Configure KPIs to Actions, disable time based fraud prevention for OOS Reason, configure OOS messages on Reporting Configurations, configure OOS Reason Button text & verify displaying renamed OOS Reason button on mobile report
    When  I add KPIs if it is not added to the KPIs Linked to Actions table
    And   I navigate to the Mobile Reports OOS Reasons page
    And   I verify configured OOS messages in Reporting Configurations OOS messages page
    And   I navigate to Reporting configurations Mobile Reports General page tab
    And   I uncheck "Enable time based fraud prevention for OOS reason" checkbox if it is checked & save the changes
    And   I uncheck "Collapse OOS Action Groups" checkbox if it is checked & save the changes
    And   I enter text for the OOS Reason Button Text and save the changes
    And   I navigate to live mobile report through URL
    And   I click on the Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions
    And   I navigate to the product details page by clicking on an SKU for OOS Reason Button Text test
    And   I verify that the renamed OOS Reason button is displayed on product details page
    And   I navigate back to the Actions page from the product details page
    And   I verify that the renamed OOS Reason button is displayed for sliding
    And   I navigate to live mobile report through URL
    And   I click on the Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions
    And   I long press on SKUs
    Then  I verify that the renamed OOS Reason button is displayed for multiple selection
    And   I navigate to the Reporting configurations Mobile Reports General page
    And   I remove text for the OOS Reason Button Text and save the changes

  @commented_out_in_cypress
  Scenario: Configure KPIs to Actions, disable time based fraud prevention for OOS Reason, configure OOS messages on Reporting Configurations, remove OOS Reason Button text & verify displaying default OOS Reason button on mobile report
    When  I add KPIs if it is not added to the KPIs Linked to Actions table
    And   I navigate to the Mobile Reports OOS Reasons page
    And   I verify configured OOS messages in Reporting Configurations OOS messages page
    And   I navigate to Reporting configurations Mobile Reports General page tab
    And   I uncheck "Enable time based fraud prevention for OOS reason" checkbox if it is checked & save the changes
    And   I uncheck "Collapse OOS Action Groups" checkbox if it is checked & save the changes
    And   I navigate to live mobile report through URL
    And   I click on the Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions
    And   I navigate to the product details page by clicking on an SKU for OOS Reason Button Text test
    And   I verify that the default OOS Reason button is displayed on product details page
    And   I navigate back to the Actions page from the product details page
    And   I verify that the default OOS Reason button is displayed for sliding
    And   I navigate to live mobile report through URL
    And   I click on the Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions
    And   I long press on SKUs
    Then  I verify that the default OOS Reason button is displayed for multiple selection

  @commented_out_in_cypress
  Scenario: Configure KPIs to Actions, disable time based fraud prevention for OOS Reason, configure OOS messages on Reporting Configurations, configure OOS Reason Button text & verify displaying renamed Edit OOS Reason button on mobile report
    When  I add KPIs if it is not added to the KPIs Linked to Actions table
    And   I navigate to the Mobile Reports OOS Reasons page
    And   I verify configured OOS messages in Reporting Configurations OOS messages page
    And   I navigate to Reporting configurations Mobile Reports General page tab
    And   I uncheck "Enable time based fraud prevention for OOS reason" checkbox if it is checked & save the changes
    And   I uncheck "Collapse OOS Action Groups" checkbox if it is checked & save the changes
    And   I enter text for the OOS Reason Button Text and save the changes
    And   I navigate to live mobile report through URL
    And   I click on the Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions
    And   I long press on SKUs
    And   I handle the multiple selected SKUs by clicking on the OOS Reason button
    And   I navigate to Handled tab
    And   I navigate to the product details page by clicking on an SKU for OOS Reason Button Text test
    And   I verify that the renamed Edit OOS Reason button is displayed on product details page
    And   I navigate back to the Actions page from the product details page
    And   I navigate to Handled tab
    And   I verify that the renamed Edit OOS Reason button is displayed for sliding
    And   I navigate to live mobile report through URL
    And   I click on the Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions
    And   I navigate to Handled tab
    And   I long press on SKUs
    And   I verify that the renamed Edit OOS Reason button is displayed for multiple selection
    And   I navigate to live mobile report through URL
    And   I click on the Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions
    And   I navigate to Handled tab
    And   I remove the OOS Reason of the handled SKUs by multiple selecting
    And   I verify the OOS Reason has removed and the SKUs are moved to the pending tab again
    Then  I verify that the SKUs are not in the handled tab after OOS Reason removing
    And   I navigate to the Reporting configurations Mobile Reports General page
    And   I remove text for the OOS Reason Button Text and save the changes

  @commented_out_in_cypress
  Scenario: Configure KPIs to Actions, disable time based fraud prevention for OOS Reason, configure OOS messages on Reporting Configurations, configure OOS Reason Button text & verify displaying default Edit OOS Reason button on mobile report
    When  I add KPIs if it is not added to the KPIs Linked to Actions table
    And   I navigate to the Mobile Reports OOS Reasons page
    And   I verify configured OOS messages in Reporting Configurations OOS messages page
    And   I navigate to Reporting configurations Mobile Reports General page tab
    And   I uncheck "Enable time based fraud prevention for OOS reason" checkbox if it is checked & save the changes
    And   I uncheck "Collapse OOS Action Groups" checkbox if it is checked & save the changes
    And   I navigate to live mobile report through URL
    And   I click on the Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions
    And   I long press on SKUs
    And   I handle the multiple selected SKUs by clicking on the OOS Reason button
    And   I navigate to Handled tab
    And   I navigate to the product details page by clicking on an SKU for OOS Reason Button Text test
    And   I verify that the default Edit OOS Reason button is displayed on product details page
    And   I navigate back to the Actions page from the product details page
    And   I navigate to Handled tab
    And   I verify that the default Edit OOS Reason button is displayed for sliding
    And   I navigate to live mobile report through URL
    And   I click on the Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions
    And   I navigate to Handled tab
    And   I long press on SKUs
    And   I verify that the default Edit OOS Reason button is displayed for multiple selection
    And   I navigate to live mobile report through URL
    And   I click on the Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions
    And   I navigate to Handled tab
    And   I remove the OOS Reason of the handled SKUs by multiple selecting
    And   I verify the OOS Reason has removed and the SKUs are moved to the pending tab again
    Then  I verify that the SKUs are not in the handled tab after OOS Reason removing
