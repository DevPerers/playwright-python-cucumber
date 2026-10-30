@from_explorer
Feature: Mobile Reports Home Page feature

  This contains the Mobile Reports Home Page feature

    Background: Navigate to Reporting Configuration Mobile Reports General page & Verify Mobile Reports page title
      Given I login to Trax successfully through Okta
      When  I navigate to the Reporting configurations Explorer page
      And   I can see the title as "Explorer"

    @commented_out_in_cypress
    Scenario: Check the Show Live Report first checkbox and verify whether it is checked    
      When  I set "Show Live Report first" checkbox to true & save the changes
      Then  I verify the "Show Live Report first" checkbox is checked

    @commented_out_in_cypress
    Scenario: Navigate to Explorer Visit Viewer Page and validate showing the live report first
      When  I navigate to the Explorer application
      And   I can see the title as "Explorer - Visits"
      And   I search by live first visit ID
      Then  I verify that visit is completed
      And   I see "Live Summary" text in the report header

    @commented_out_in_cypress
    Scenario: Uncheck the checkbox and verify whether it is unchecked
      When  I set "Show Live Report first" checkbox to false & save the changes
      Then  I verify the "Show Live Report first" checkbox is unchecked

    @commented_out_in_cypress
    Scenario: Navigate to Explorer Visit Viewer Page and validate showing the regular report first
      When  I navigate to the Explorer application
      And   I can see the title as "Explorer - Visits"
      And   I search by live first visit ID
      Then  I see "Visit Summary" text in the report header

    @commented_out_in_cypress
    Scenario: Navigate to Explorer Visit Viewer Page, verify the KPI order on mobile report, navigate to Reporting Configurations KPI page and verify the KPI order values
      When  I navigate to the Explorer application
      And   I can see the title as "Explorer - Visits"
      And   I search by live first visit ID
      And   I get the KPI circle titles
      And   I navigate to the Reporting configuration Mobile Reports KPI page
      And   I get the KPI order values in Reporting configuration Mobile Reports KPI page
      Then  I verify the KPI order values with the KPI display order in the mobile report

    @commented_out_in_cypress
    Scenario: Navigate to Explorer Visit Viewer Page and verify the delta values of the KPI circles
      When  I navigate to the Explorer application
      And   I can see the title as "Explorer - Visits"
      And   I search by visit ID for delta values verifying test
      And   I get the KPI circle values of the current visit
      And   I get the KPI delta values of the current visit
      And   I navigate to the recent visit
      And   I get the KPI circle values of the recent previous visit
      Then  I verify delta values of the KPI circles of the current visit
