@from_explorer
Feature: Mobile Reports Show Surveys feature

  This contains the Mobile Reports Show Surveys feature

    Background: Navigate to Reporting Configurations Mobile Reports General page & Verify Mobile Reports page title
      Given I login to Trax successfully through Okta
      When  I navigate to the Reporting configurations Mobile Reports General page
      Then  I verify the title as "Mobile Reports"

    @commented_out_in_cypress
    Scenario: Check the checkbox and verify whether it is checked
      When  I check the "Show Surveys" checkbox if it is unchecked and save the changes
      Then  I see that the "Show Surveys" checkbox is checked

    @commented_out_in_cypress
    Scenario: Navigate to Explorer Visit Viewer Page and validate showing the Show Surveys menu item and verify the Show Surveys page
      When  I navigate to the Explorer application
      Then  I verify the title as "Explorer - Visits"
      When  I search by visit ID for surveys test
      Then  I verify that the visit is completed
      And   I verify showing "Show Surveys" menu item in three dots menu
      And   I verify Show Surveys Page

    @commented_out_in_cypress
    Scenario:  Uncheck the checkbox and verify whether it is unchecked
      When  I uncheck the "Show Surveys" checkbox if it is checked and save the changes
      Then  I see that the "Show Surveys" checkbox is unchecked

    @commented_out_in_cypress
    Scenario: Navigate to Explorer Visit Viewer Page and validate not showing the Show Surveys menu item
      When  I navigate to the Explorer application
      Then  I verify the title as "Explorer - Visits"
      When  I search by visit ID for surveys test
      Then  I verify that the visit is completed
      And   I verify not showing "Show Surveys" menu item in three dots menu
