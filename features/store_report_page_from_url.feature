@from_url
Feature: Mobile Reports Store Report feature

  This contains the Mobile Reports Store Report feature

    Background: Navigate to Reporting Configuration Mobile Reports General page & Verify Mobile Reports page title
      Given I login to Trax successfully through Okta
      When I navigate to the Reporting configurations Mobile Reports General page
      And  I can see the title "Mobile Reports"
      And  I check "Store Report" checkbox if it is unchecked & save the changes
      And  I delete all KPIs from the store report table
      And  I add KPIs to the Store Report table

    @commented_out_in_cypress
    Scenario: Check the store report checkbox and verify whether it is checked and validate showing the Store Report menu item and verify the Store Report page
      When I check "Store Report" checkbox if it is unchecked & save the changes
      Then I verify "Store Report" checkbox is checked
      When I navigate to the live mobile report through URL
      Then I verify showing the Store Report menu item in three dots menu
      And  I verify the Store Report Page

    @commented_out_in_cypress
    Scenario: Uncheck the checkbox and verify whether it is unchecked and validate not showing the Store Report menu item
      When I uncheck "Store Report" checkbox if it is checked & save the changes
      And  I verify "Store Report" checkbox is unchecked
      And  I navigate to the live mobile report through URL
      Then I verify not showing the Store Report menu item in three dots menu

    @commented_out_in_cypress
    Scenario: Check product count
      When I navigate to the live mobile report through URL
      And  I go to the Store Report page
      And  I check the status product count
      Then I verify status product count

    @commented_out_in_cypress
    Scenario: Check the product details page
      When I navigate to the live mobile report through URL
      And  I go to the Store Report page
      Then I go to the product details page and verify the values
      When I navigate to the Products and Brands app
      Then I navigate to the product page and verify the store report product details are equal to the product details in the Product and Brands app

    @commented_out_in_cypress
    Scenario: Filter By Category
      When I navigate to the live mobile report through URL
      And  I go to the Store Report page
      And  I filter the product by category and get the product count
      Then I verify the category filtered product count

    @commented_out_in_cypress
    Scenario: Verify back button
      When I navigate to the live mobile report through URL
      And  I go to the Store Report page
      Then I click on the back button and verify the pop up window
      And  I click Cancel button and verify
      And  I click Close button and verify

    @commented_out_in_cypress
    Scenario: Generate store report PDF file and verify the product names
      When I navigate to the live mobile report through URL
      And  I go to the Store Report page
      And  I click on the Generate button
      And  I click on the Download PDF button
      Then I verify the pdf file is in the download folder and verify the header
      And  I verify the products names in the PDF file

    @commented_out_in_cypress
    Scenario Outline: Verify the product barcode according to the product barcode settings
        When  I go the Project Settings page in the P&B app
        And   I click edit button in the product barcode settings
        And   I select <storageField> and click save button
        And   I verify <storageField> is selected in the product barcode settings
        And   I navigate to the live mobile report through URL
        And   I go to the Store Report page
        And   I get <barcodeValue> value
        And   I navigate to the Products and Brands app
        Then  I verify the <barcodeValue> is equal to the Product and Brands app
            Examples:
                | storageField          | barcodeValue              |
                | "Item Code"           | "itemCode"                |
                | "Product Global Code" | "productGlobalCode"       |
                | "EAN"                 | "ean"                     |

    @commented_out_in_cypress
    Scenario: Check the store report product names filter by OOS Reason functionality in the All and Missing tabs
      When I navigate to the live mobile report through URL
      And  I go to the Store Report page
      And  I filter the products by OOS Reason and get the product name
      Then I verify the OOS Reason filtered product name

    @commented_out_in_cypress
    Scenario: Check the behavior of hiding a single product by swiping the product
      When I go to the live mobile report through URL
      And  I go to the Store Report page
      And  I swipe the product to the left side
      And  I click on the HIDE button
      And  I verify hide product is in disable mode
      And  I download the pdf
      Then I verify hidden product is not available in the product list

    @commented_out_in_cypress
    Scenario: Check the behavior when showing a hidden product by swiping the product
      When I go to the live mobile report through URL
      And  I go to the Store Report page
      And  I swipe the product to the right side
      And  I click on the SHOW button
      Then I verify hidden product is in enable mode

    @commented_out_in_cypress
    Scenario: Verify the message when there is no product in the Present tab when filtering by OOS Reason
      When I navigate to the live mobile report through URL
      And  I go to the Store Report page
      And  I filter the products by OOS Reason
      And  I go to Present tab
      Then I verify no present product in the present tab and verify message for the selected OOS Reason

    @commented_out_in_cypress
    Scenario: Check the behavior of hiding and showing the multiple products by long press
      When I go to the live mobile report through URL to check the hide and show functionality by long press
      And  I go to the Store Report page
      And  I long press the product name and select multiple products
      And  I verify the selected products count
      And  I click on the HIDE button for hide the multiple products
      And  I verify the hide products are in disable mode
      And  I download the pdf
      And  I verify the hidden products are not available in the product list
      And  I long press the product name and select multiple products
      And  I click on the SHOW button to show multiple products
      Then I verify hidden products are in enable mode

    @commented_out_in_cypress
    Scenario Outline: Verify the Store Reports Products grouping behavior according to OOS Reason, Status and Ungrouped
      When I add a <groupBy> value to the Default Store Report Grouping drop-down and save the changes
      And  I navigate to the live mobile report through URL
      And  I go to the Store Report page
      And  I verify that <menuOption> product grouping option is selected in the grouping options menu
      Then I verify the Group By headers for <menuOption>
        Examples:
        | groupBy         | menuOption       |
        | "By OOS Reason" | "OOS Reason"     |
        | "By Status"     | "Status"         |
        | "Ungrouped"     | "Ungrouped"      |
