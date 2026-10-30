@from_explorer
Feature: Mobile Reports Product Details Page feature

  This contains the Mobile Reports Product Details Page feature

    Background: Navigate to Explorer Visit Viewer Page
      Given I login to Trax successfully through Okta
      When  I navigate to the Explorer application
      And   I can see that the "Explorer - Visits" title

    Scenario: Navigate to Product Details Page and verify the page layout and product properties according to the products and brands app
      When  I search by giving visit ID
      And   I proceed to Product Details page
      Then  I verify that the "Product Details" page title
      And   I verify that the layout of the Product Details page and verify the product properties values
      When  I navigate to the Products and Brands app
      And   I navigate to product page and verify the mobile report product details are equal to the product details in the Product and Brands app
