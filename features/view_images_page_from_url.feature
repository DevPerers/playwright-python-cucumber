@from_url
Feature: Mobile Reports View Images Page feature

  This contains the Mobile Reports View Images Page feature

    Background: Navigate to Explorer Visit Viewer Page
      Given I login to Trax successfully through Okta
      When  I navigate to the regular mobile report through URL

    @commented_out_in_cypress
    Scenario: Navigate to View Images Page and verify the Images page and the Products Tagging page inside the Image page
      When  I navigate to View Images page
      Then  I verify the "Images" page title
      And   I verify the layout of View Images Page Scene Cards
      And   I navigate to the Product Tagging page
      Then  I verify the "Product Tagging" page title
      And   I verify the layout of the Product Tagging page
