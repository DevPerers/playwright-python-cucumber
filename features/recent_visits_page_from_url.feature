@from_url
Feature: Mobile Reports Recent Visits Page feature

  This contains the Mobile Reports Recent Visits Page feature

    Background: Log into trax and navigate to mobile report through the URL
      Given I login to Trax successfully through Okta
      When  I proceed to the regular mobile report through URL

    @commented_out_in_cypress
    Scenario: Verify the Recent Visits menu item, navigate to the Recent Visits page and verify the page
      Then  I verify showing the Recent Visits menu item in three dots menu
      When  I navigate to Recent Visits page
      Then  I verify the Recent Visits page layout
      When  I filter the the Recent Visits page by single user filtering
      Then  I verify the Recent Visits page single user filtering and clearing the filter
      When  I filter the the Recent Visits page by multiple user filtering
      Then  I verify the Recent Visits page multiple user filtering and clearing the filter
      And   I verify the navigation to recent visits
