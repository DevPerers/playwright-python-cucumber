@from_explorer
Feature: Mobile Reports Recent Visits Page feature

  This contains the Mobile Reports Recent Visits Page feature

    Background: Navigate to Explorer app and navigate to Explorer Visit Viewer Page
      Given I login to Trax successfully through Okta
      When  I navigate to the Explorer application
      And   I see that the "Explorer - Visits" title

    @commented_out_in_cypress
    Scenario: Verify the Recent Visits menu item, navigate to the Recent Visits page and verify the page
      When  I search by giving a visit ID
      Then  I verify that showing the Recent Visits menu item in three dots menu
      When  I proceed to Recent Visits page
      Then  I verify that the Recent Visits page layout
      When  I filter that the the Recent Visits page by single user filtering
      Then  I verify that the Recent Visits page single user filtering and clearing the filter
      When  I filter the Recent Visits page by multiple user filtering
      Then  I verify that the Recent Visits page multiple user filtering and clearing the filter
      And   I verify that the navigation to recent visits
