@from_explorer
Feature: Mobile Reports Store Report feature

  This contains the Mobile Reports Store Report feature

    Background: Navigate to Reporting Configuration Mobile Reports General page & Verify Mobile Reports page title
      Given I login to Trax successfully through Okta
      When  I navigate to the Reporting configurations Mobile Reports General page
      And   I see that the title is "Mobile Reports"
      And   I check "Store Report" checkbox & save the changes, if it is unchecked
      And   I delete all the KPIs from the store report table
      And   I add the KPIs to the Store Report table

    @commented_out_in_cypress
    Scenario: Check the store report checkbox and verify whether it is checked and validate showing the Store Report menu item and verify the Store Report page
      When I check "Store Report" checkbox if it is unchecked & save the changes
      And  I check that "Store Report" checkbox is checked
      And  I navigate to the Explorer application
      And  I see that the title is "Explorer - Visits"
      And  I navigate to the Visit Viewer page
      Then I verify that showing the Store Report menu item in three dots menu
      And  I verify that the Store Report Page

    @commented_out_in_cypress
    Scenario: Uncheck the checkbox and verify whether it is unchecked and validate not showing the Store Report menu item
      When I uncheck "Store Report" checkbox & save the changes, if it is checked
      And  I check that "Store Report" checkbox is unchecked
      And  I navigate to the Explorer application
      And  I see that the title is "Explorer - Visits"
      And  I navigate to the Visit Viewer page
      Then I verify that not showing the Store Report menu item in three dots menu

    @commented_out_in_cypress
    Scenario: Check product count
      When I navigate to the Explorer application
      And  I see that the title is "Explorer - Visits"
      And  I navigate to the Visit Viewer page
      And  I go to Store Report page
      And  I check the status of the product count
      Then I verify the status product count

    @commented_out_in_cypress
    Scenario: Check the product details page
      When I navigate to the Explorer application
      And  I see that the title is "Explorer - Visits"
      And  I navigate to the Visit Viewer page
      And  I go to Store Report page
      And  I go to product details page and verify the values
      And  I navigate to the Products and Brands app
      Then I proceed to the product page and verify the store report product details are equal to the product details in the Product and Brands app

    @commented_out_in_cypress
    Scenario: Filter By Category
      When I navigate to the Explorer application
      And  I see that the title is "Explorer - Visits"
      And  I navigate to the Visit Viewer page
      And  I go to Store Report page
      And  I filter product by category and get the product count
      Then I verify that the category filtered product count

    @commented_out_in_cypress
    Scenario: Verify back button
      When I navigate to the Explorer application
      And  I see that the title is "Explorer - Visits"
      And  I navigate to the Visit Viewer page
      And  I go to Store Report page
      And  I click on back button and verify the pop up window
      And  I click the Cancel button and verify
      And  I click the Close button and verify

    @commented_out_in_cypress
    Scenario: Generate store report PDF file and verify the product names
      When I navigate to the Explorer application
      And  I see that the title is "Explorer - Visits"
      And  I navigate to the Visit Viewer page
      And  I go to Store Report page
      And  I click on the Generate button option
      And  I click on the Download PDF button option
      Then I verify that the pdf file is in the download folder and verify the header
      And  I verify that the products names in the PDF file

    @commented_out_in_cypress
    Scenario: Check the store report product names filter by OOS Reason functionality in the All and Missing tabs
      When I navigate to the Explorer application
      And  I see that the title is "Explorer - Visits"
      And  I navigate to the Visit Viewer page
      And  I go to Store Report page
      And  I filter the Store Report products by OOS Reason and get the product name
      Then I verify the OOS Reason filtered products names in the All and Missing tabs

    @commented_out_in_cypress
    Scenario: Verify the message when there is no product in the Present tab when filtering by OOS Reason
      When I navigate to the Explorer application
      And  I see that the title is "Explorer - Visits"
      And  I navigate to the Visit Viewer page
      And  I go to Store Report page
      And  I filter products by OOS Reason
      And  I go to the Present tab
      Then I verify the no present product in the present tab and verify message for the selected OOS Reason

    @commented_out_in_cypress
    Scenario Outline: Verify the product barcode according to the product barcode settings
      When  I go the Project Settings page in the P&B app
      And   I click the edit button in the product barcode settings
      And   I select the <storageField> and click save button
      And   I verify the <storageField> is selected in the product barcode settings
      And   I navigate to the Explorer application
      And   I see that the title is "Explorer - Visits"
      And   I navigate to the Visit Viewer page
      And   I go to Store Report page
      And   I get the <barcodeValue> value
      And   I navigate to the Products and Brands app
      Then  I verify <barcodeValue> is equal to the Product and Brands app
          Examples:
              | storageField          | barcodeValue              |
              | "Item Code"           | "itemCode"                |
              | "Product Global Code" | "productGlobalCode"       |
              | "EAN"                 | "ean"                     |

    @commented_out_in_cypress
    Scenario: Check the behavior of hiding a single product by swiping the product
      When I navigate to the Explorer application
      And  I see that the title is "Explorer - Visits"
      And  I navigate to Visit Viewer page
      And  I go to Store Report page
      And  I swipe product to the left side
      And  I click the HIDE button
      And  I verify the hide product is in disable mode
      And  I download pdf
      Then I verify hidden product is not available in product list

    @commented_out_in_cypress
    Scenario: Check the behavior when showing a hidden product by swiping the product
      When I navigate to the Explorer application
      And  I see that the title is "Explorer - Visits"
      And  I navigate to Visit Viewer page
      And  I go to Store Report page
      And  I swipe the product to right side
      And  I click the SHOW button
      Then I verify the hidden product is in enable mode

    @commented_out_in_cypress
    Scenario: Check the behavior of hiding and showing the multiple products by long press and selecting the products
      When I navigate to the Explorer application
      And  I see that the title is "Explorer - Visits"
      And  I navigate to Visit Viewer page to see the Mobile Report
      And  I go to Store Report page
      And  I long press the product name and select products
      And  I check the selected products count
      And  I click on the HIDE button for hide selected three products
      And  I verify the hidden products are in disable mode
      And  I download pdf
      And  I verify hidden products are not available in the product list
      And  I long press the product name and select products
      And  I click on the SHOW button to show the hidden products
      Then I verify the hidden products are in enable mode

    @commented_out_in_cypress
    Scenario Outline: Verify the Store Reports Products grouping behavior according to OOS Reason, Status and Ungrouped
      When I add the <groupBy> value to the Default Store Report Grouping drop-down and save the changes
      And  I navigate to the Explorer application
      And  I see that the title is "Explorer - Visits"
      And  I navigate to the Visit Viewer page
      And  I go to Store Report page
      And  I verify that the <menuOption> product grouping option is selected in the grouping options menu
      Then I verify the Group By headers for the <menuOption>

      Examples:
        | groupBy         | menuOption       |
        | "By OOS Reason" | "OOS Reason"     |
        | "By Status"     | "Status"         |
        | "Ungrouped"     | "Ungrouped"      |
