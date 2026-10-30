@from_explorer
Feature: Mobile Reports View Images Page feature

  This contains the Mobile Reports View Images Page feature

    Background: Navigate to Explorer Visit Viewer Page
      Given I login to Trax successfully through Okta
      When  I navigate to the Reporting configurations Explorer page
      And   I get the value of "Show Live Report first" checkbox in Reporting Configurations
      And   I navigate to the Explorer application
      And   I see the title "Explorer - Visits"
      And   I search by visit ID
      And   I navigate to regular report for View Images Page test

    @commented_out_in_cypress
    Scenario: Navigate to View Images Page and verify the Images page and the Products Tagging page inside the Image page
      When  I navigate to the View Images page
      Then  I verify "Images" page title
      And   I verify that the layout of View Images Page Scene Cards
      And   I navigate to Product Tagging page
      Then  I verify "Product Tagging" page title
      And   I verify that the layout of the Product Tagging page
