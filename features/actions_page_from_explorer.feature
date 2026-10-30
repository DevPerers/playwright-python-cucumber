@from_explorer
Feature: Mobile Reports Actions Page Feature

  This contains the Mobile Reports Actions Page feature

  Background: Login to Trax and navigate to Reporting Configuration Mobile Reports General page & remove all KPIs linked to actions
    Given I login to Trax successfully through Okta
    When  I navigate to the Reporting configurations Mobile Reports General page
    And   I see the title as "Mobile Reports"
    And   I remove all the KPIs form the KPIs Linked to Actions table

  @commented_out_in_cypress
  Scenario: Configure KPIs to actions & verify showing actions in mobile report according to Collapse OOS Action Groups checkbox
    When  I add KPIs if it is not added to the KPIs Linked to Actions table
    And   I navigate to the Reporting configurations Explorer page
    And   I get the value of "Show Live Report first" checkbox
    And   I navigate to the Reporting configurations Mobile Reports General page
    And   I check the "Collapse OOS Action Groups" checkbox if it is unchecked & save the changes
    And   I navigate to the Explorer application
    And   I see the title as "Explorer - Visits"
    And   I search by the visit ID
    And   I navigate to live report
    And   I click on the Actions button when actions are collapsed and see the collapsed actions
    And   I navigate to the Reporting configurations Mobile Reports General page
    And   I uncheck the "Collapse OOS Action Groups" checkbox if it is checked & save the changes
    And   I navigate to the Explorer application
    And   I see the title as "Explorer - Visits"
    And   I search by the visit ID
    And   I navigate to live report
    And   I click on Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions

  @commented_out_in_cypress
  Scenario: Configure KPIs to actions & navigate to Explorer Visit Viewer Page & navigate to Actions page & verify the actions count on the report when there are actions
    When  I add KPIs if it is not added to the KPIs Linked to Actions table
    And   I uncheck the "Collapse OOS Action Groups" checkbox if it is checked & save the changes
    And   I navigate to the Reporting configurations Explorer page
    And   I get the value of "Show Live Report first" checkbox
    And   I navigate to the Explorer application
    And   I search by the visit ID
    And   I navigate to live report
    And   I click on Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions
    And   I verify the actions count on pending tab count badge
    And   I click on Back Arrow in the Actions page
    And   I verify the actions count on Actions button
    And   I refresh the page
    And   I navigate to live report
    And   I click on Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions
    And   I navigate to the Handled tab
    Then  I verify the actions count on handled tab count badge

  @commented_out_in_cypress
  Scenario: Navigate to Explorer Visit Viewer Page & navigate to Actions page and verify Actions count on the report when there are no actions in the report
    When  I navigate to the Explorer application
    And   I see the title as "Explorer - Visits"
    And   I search by the visit ID
    And   I click on Actions button when there are no actions on the Report
    And   I verify the actions count on pending tab count badge
    And   I click on Back Arrow in the Actions page
    And   I verify the actions count on Actions button
    And   I refresh the page
    And   I click on Actions button when there are no actions on the Report
    And   I verify the actions count on handled tab count badge

  @commented_out_in_cypress
  Scenario: Configure KPIs to Actions, disable fraud prevention for OOS Reason, configure OOS & Override messages on Reporting Configurations & verify not showing the Override messages for OOS Reason on mobile report
    When  I add KPIs if it is not added to the KPIs Linked to Actions table
    And   I navigate to Mobile Reports OOS Reasons page
    And   I configure the OOS messages for User Override
    And   I navigate to the Reporting configurations Mobile Reports General tab
    And   I uncheck the "Enable time based fraud prevention for OOS reason" checkbox if it is checked & save the changes
    And   I uncheck the "Collapse OOS Action Groups" checkbox if it is checked & save the changes
    And   I navigate to the Reporting configurations Explorer page
    And   I get the value of "Show Live Report first" checkbox
    And   I navigate to the Explorer application
    And   I see the title as "Explorer - Visits"
    And   I search by the visit ID
    And   I navigate to live report
    And   I click on Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions
    And   I slide an SKU and click on OOS Reason button
    Then  I verify the Override messages is not shwon for the OOS Reason

  @commented_out_in_cypress
  Scenario: Configure KPIs to actions & navigate to Explorer Visit Viewer Page & navigate to Category KPI page & verify the actions count on the actions page when there are actions
    When  I add KPIs if it is not added to the KPIs Linked to Actions table
    And   I uncheck the "Collapse OOS Action Groups" checkbox if it is checked & save the changes
    And   I navigate to the Reporting configurations Explorer page
    And   I get the value of "Show Live Report first" checkbox
    And   I navigate to the Explorer application
    And   I see the title as "Explorer - Visits"
    And   I search by the visit ID
    And   I navigate to regular report
    And   I navigate to the category KPI page
    And   I click on Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions
    And   I verify the actions count on pending tab count badge
    And   I click on Back Arrow in the Actions page
    And   I verify the actions count on Actions button
    And   I refresh the page
    And   I navigate to live report
    And   I click on Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions
    And   I navigate to the Handled tab
    Then  I verify the actions count on handled tab count badge

  @commented_out_in_cypress
  Scenario: Navigate to Explorer Visit Viewer Page & navigate to Category KPI page & verify Actions count on the report when there are no actions in the report
    When  I navigate to the Explorer application
    And   I see the title as "Explorer - Visits"
    And   I search by the visit ID
    And   I click on Actions button when there are no actions on the Report
    And   I verify the actions count on pending tab count badge
    And   I click on Back Arrow in the Actions page
    And   I verify the actions count on Actions button
    And   I refresh the page
    And   I click on Actions button when there are no actions on the Report
    And   I navigate to the Handled tab
    Then  I verify the actions count on handled tab count badge

  @commented_out_in_cypress
  Scenario: Configure single KPI per live and per regular to actions, configure Ungrouped as default actions page layout & verify the actions are ungrouped in actions page of Explorer report
    When  I add the single KPIs per live and per regular if they are not added to the KPIs Linked to Actions table
    And   I configure the "Ungrouped" option for default actions page layout
    And   I uncheck the "Collapse OOS Action Groups" checkbox if it is checked & save the changes
    And   I navigate to the Reporting configurations Explorer page
    And   I get the value of "Show Live Report first" checkbox
    And   I navigate to the Explorer application
    And   I see the title as "Explorer - Visits"
    And   I search by the visit ID
    And   I navigate to live report
    And   I click on Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions
    Then  I verify showing all the actions grouping options in actions page
    And   I verify that the "No Grouping" actions grouping option has selected in grouping options menu
    And   I verify that SKUs have ungrouped

  @commented_out_in_cypress
  Scenario: Configure single KPI per live and per regular to actions, configure By Category as default actions page layout & verify showing the actions By Category in the actions page of Explorer report
    When  I add the single KPIs per live and per regular if they are not added to the KPIs Linked to Actions table
    And   I configure the "By Category" option for default actions page layout
    And   I uncheck the "Collapse OOS Action Groups" checkbox if it is checked & save the changes
    And   I navigate to the Reporting configurations Explorer page
    And   I get the value of "Show Live Report first" checkbox
    And   I navigate to the Explorer application
    And   I see the title as "Explorer - Visits"
    And   I search by the visit ID
    And   I navigate to live report
    And   I click on Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions
    Then  I verify showing all the actions grouping options in actions page
    And   I verify that the "By Category" actions grouping option has selected in grouping options menu
    And   I verify that SKUs have grouped By Category in the actions page

  @commented_out_in_cypress
  Scenario: Configure single KPI per live and per regular to actions, configure By KPI as default actions page layout & verify showing the actions By KPI in the actions page of Explorer report
    When  I add the single KPIs per live and per regular if they are not added to the KPIs Linked to Actions table
    And   I configure the "By KPI" option for default actions page layout
    And   I uncheck the "Collapse OOS Action Groups" checkbox if it is checked & save the changes
    And   I navigate to the Reporting configurations Explorer page
    And   I get the value of "Show Live Report first" checkbox
    And   I navigate to the Explorer application
    And   I see the title as "Explorer - Visits"
    And   I search by the visit ID
    And   I navigate to live report
    And   I click on Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions
    Then  I verify showing all the actions grouping options in actions page
    And   I verify that the "By KPI" actions grouping option has selected in grouping options menu
    And   I verify that SKUs have grouped By KPI in the actions page

  @commented_out_in_cypress
  Scenario: Configure single KPI per live and per regular to actions, configure By Brand as default actions page layout & verify showing the actions By Brand in the actions page of Explorer report
    When  I add the single KPIs per live and per regular if they are not added to the KPIs Linked to Actions table
    And   I configure the "By Brand" option for default actions page layout
    And   I uncheck the "Collapse OOS Action Groups" checkbox if it is checked & save the changes
    And   I navigate to the Reporting configurations Explorer page
    And   I get the value of "Show Live Report first" checkbox
    And   I navigate to the Explorer application
    And   I see the title as "Explorer - Visits"
    And   I search by the visit ID
    And   I navigate to live report
    And   I click on Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions
    Then  I verify showing all the actions grouping options in actions page
    And   I verify that the "By Brand" actions grouping option has selected in grouping options menu
    And   I verify that the SKUs have grouped By Brand in actions page

  @commented_out_in_cypress
  Scenario: Configure multiple KPIs per live and per regular to actions & navigate to Explorer Visit Viewer Page & navigate to Actions page & verify showing the actions By KPI in the report
    When  I add KPIs if it is not added to the KPIs Linked to Actions table
    And   I verify the configuration of By KPI as default actions page layout dropdown value in Reporting Configurations
    And   I uncheck the "Collapse OOS Action Groups" checkbox if it is checked & save the changes
    And   I navigate to the Reporting configurations Explorer page
    And   I get the value of "Show Live Report first" checkbox
    And   I navigate to the Explorer application
    And   I see the title as "Explorer - Visits"
    And   I search by the visit ID
    And   I navigate to live report
    And   I click on Actions button when there are actions and the actions are not collapsed on the Report and see the expanded OOS actions
    Then  I verify showing only the By KPI actions grouping options in actions page
