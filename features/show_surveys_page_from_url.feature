@from_url
Feature: Mobile Reports Show Surveys feature

  This contains the Mobile Reports Show Surveys feature

    Background: Navigate to Reporting Configurations Mobile Reports General page & Verify Mobile Reports page title
      Given I login to Trax successfully through Okta
      When  I navigate to the Reporting configurations Mobile Reports General page
      Then  I see the "Mobile Reports" title

    @commented_out_in_cypress
    Scenario: Check the checkbox and verify whether it is checked
      When  I check "Show Surveys" checkbox if it is unchecked and save the changes
      Then  I see that "Show Surveys" checkbox is checked

    @commented_out_in_cypress
    Scenario: Navigate to the mobile report through URL and validate showing the Show Surveys menu item and verify the Show Surveys page
      When  I proceed to the live mobile report through URL
      And   I verify showing the "Show Surveys" menu item in three dots menu
      And   I verify the Show Surveys Page

    @commented_out_in_cypress
    Scenario:  Uncheck the checkbox and verify whether it is unchecked
      When  I uncheck "Show Surveys" checkbox if it is checked and save the changes
      Then  I see "Show Surveys" checkbox is unchecked

    @commented_out_in_cypress
    Scenario: Navigate to the mobile report through URL and validate not showing the Show Surveys menu item
      When  I proceed to the live mobile report through URL
      And   I verify not showing the "Show Surveys" menu item in three dots menu
