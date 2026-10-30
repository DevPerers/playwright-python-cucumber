@from_url
Feature: Mobile Reports Product Details Page feature

  This contains the Mobile Reports Product Details Page feature

    Background: Navigate to the mobile report through the URL
      Given I login to Trax successfully through Okta
      When  I proceed to regular mobile report through URL

    @commented_out_in_cypress
    Scenario: Navigate to Product Details Page and verify the page layout and product properties according to the products and brands app
      When  I navigate to Product Details page
      Then  I verify that the page title is "Product Details"
      And   I verify the layout of the Product Details page and verify the product properties values
      When  I navigate to the Products and Brands app
      And   I navigate to the product page and verify the mobile report product details are equal to the product details in the Product and Brands app
