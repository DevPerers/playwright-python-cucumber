@from_url
Feature: Mobile Reports Home Page feature

  This contains the Mobile Reports Home Page feature

    Background: Navigate to Reporting Configuration Mobile Reports General page & Verify Mobile Reports page title
      Given I login to Trax successfully through Okta
      When  I navigate to the Reporting configurations Explorer page
      And   I see "Explorer" as title

    @commented_out_in_cypress
    Scenario: Check the Show Live Report first checkbox and verify whether it is checked
      When  I set the "Show Live Report first" checkbox to true & save the changes
      Then  I verify that the "Show Live Report first" checkbox is checked

    @commented_out_in_cypress
    Scenario: Navigate to mobile report through URL and validate showing the regular report first
      When  I navigate to the old mobile report through URL
      Then  I see the "Visit Summary" text in the report header

    @commented_out_in_cypress
    Scenario: Uncheck the checkbox and verify whether it is unchecked
      When  I set the "Show Live Report first" checkbox to false & save the changes
      Then  I verify that the "Show Live Report first" checkbox is unchecked

    @commented_out_in_cypress
    Scenario: Navigate to the old mobile report through URL and validate showing the regular report first
      When  I navigate to the old mobile report through URL
      Then  I see the "Visit Summary" text in the report header

    @commented_out_in_cypress
    Scenario: Navigate to the mobile report, verify the KPI order on mobile report, navigate to Reporting Configurations KPI page and verify the KPI order values
      When  I navigate to regular mobile report through the URL
      And   I get KPI circle titles
      And   I navigate to the Reporting configuration Mobile Reports KPI page
      And   I get KPI order values in Reporting configuration Mobile Reports KPI page
      Then  I verify KPI order values with the KPI display order in the mobile report

    @commented_out_in_cypress
    Scenario: Navigate to the mobile report and verify the delta values of the KPI circles
      When  I navigate to regular mobile report through the URL for delta values verifying test
      And   I get KPI circle values of the current visit
      And   I get KPI delta values of the current visit
      And   I proceed to the recent visit
      And   I get KPI circle values of the recent previous visit
      Then  I verify the delta values of the KPI circles of the current visit

    @commented_out_in_cypress
    Scenario: Navigate to Reporting Configurations KPIs page, configure KPI color threshold values and colors for Result when Threshold of is Target and verify colors on Mobile Report
      When  I navigate to the Reporting configuration Mobile Reports KPI page
      And   I search by a KPI for color configuration
      And   I enable color thresholds for the KPI
      And   I verify 'Target' is selected as Threshold of radio button
      And   I select 'Result' radio button as Circle Value if it is not selected
      And   I configure KPI color threshold values and colors for a particular KPI
      And   I save changes for the KPI
      And   I navigate to regular mobile report through the URL for KPI colors verifying test
      Then  I verify color of KPI circle and value on the mobile report when Threshold of is Target and Result is selected as Circle Value

    @commented_out_in_cypress
    Scenario: Navigate to Reporting Configurations KPIs page, configure KPI color threshold values and colors for Score when Threshold of is Target and verify colors on Mobile Report
      When  I navigate to the Reporting configuration Mobile Reports KPI page
      And   I search by a KPI for color configuration
      And   I select 'Score' radio button as Circle Value if it is not selected
      And   I save changes for the KPI
      And   I navigate to regular mobile report through the URL for KPI colors verifying test
      Then  I verify color of KPI circle and value on the mobile report when Threshold of is Target and Score is selected as Circle Value

    @commented_out_in_cypress
    Scenario: Navigate to Reporting Configurations KPIs page, configure KPI color threshold values and colors for Result when Threshold of is KPI result and verify colors on Mobile Report
      When  I navigate to the Reporting configuration Mobile Reports KPI page
      And   I search by a KPI for color configuration
      And   I select 'KPI result' as Threshold of radio button
      And   I verify 'KPI result' is selected as Threshold of radio button
      And   I select 'Result' radio button as Circle Value if it is not selected
      And   I save changes for the KPI
      And   I navigate to regular mobile report through the URL for KPI colors verifying test
      Then  I verify color of KPI circle and value on the mobile report when Threshold of is KPI result and Result is selected as Circle Value

    @commented_out_in_cypress
    Scenario: Navigate to Reporting Configurations KPIs page, configure KPI color threshold values and colors for Score when Threshold of is KPI result and verify colors on Mobile Report
      When  I navigate to the Reporting configuration Mobile Reports KPI page
      And   I search by a KPI for color configuration
      And   I select 'Score' radio button as Circle Value if it is not selected
      And   I save changes for the KPI
      And   I navigate to regular mobile report through the URL for KPI colors verifying test
      Then  I verify color of KPI circle and value on the mobile report when Threshold of is KPI result and Score is selected as Circle Value

    @commented_out_in_cypress
    Scenario: Navigate to Reporting Configurations KPIs page, disable color thresholds for the KPI and verify colors on Mobile Report
      When  I navigate to the Reporting configuration Mobile Reports KPI page
      And   I search by a KPI for color configuration
      And   I disable color thresholds for the KPI
      And   I save changes for the KPI
      And   I navigate to regular mobile report through the URL for KPI colors verifying test
      Then  I verify color of KPI circle and value on the mobile report when color thresholds are disabled

    @commented_out_in_cypress
    Scenario: Log out from the X-Suite and verify that the user has no access to Mobile Report
      When  I log out from X-Suite
      And   I navigate to Mobile Report and verify that the user has no access to the Mobile Report
      And   I verify that the Mobile Report is not visible to the user
      Then  I verify that the user is redirected to the login page

    @commented_out_in_cypress
    Scenario: Log in again to the X-Suite and verify that the user has access to Mobile Report
      When  I navigate to Mobile Report and verify that the user has access to the Mobile Report
      Then  I verify that the Mobile Report is visible to the user

    @commented_out_in_cypress
    Scenario: Navigate to Reporting Configurations KPIs page, rename the KPI circle title and verify KPI circle title on Mobile Report
      When  I navigate to the Reporting configuration Mobile Reports KPI page
      And   I search by a KPI for KPI circle title renaming test
      And   I rename the KPI circle title
      And   I save changes for the KPI
      And   I navigate to regular mobile report through the URL for KPI circle title renaming test
      Then  I verify that the renaming has applied to the KPI circle title on the mobile report

    @commented_out_in_cypress
    Scenario: Navigate to Reporting Configurations KPIs page, rename the KPI circle title back to the original name and verify KPI circle title on Mobile Report
      When  I navigate to the Reporting configuration Mobile Reports KPI page
      And   I search by a KPI for KPI circle title renaming test
      And   I rename the KPI circle title back to the original name
      And   I save changes for the KPI
      And   I navigate to regular mobile report through the URL for KPI circle title renaming test
      Then  I verify that the original name has applied to the KPI circle title on the mobile report

    @commented_out_in_cypress
    Scenario: Verify color of the delta value for the positive Delta Coloring Method with positive delta value of the KPI circle
      When  I navigate to the Reporting Configurations K-Engine KPI Attributes page
      And   I retrieve Delta Coloring Method for the KPI when KPI has positive Delta Coloring Method
      And   I navigate to regular mobile report through the URL for Delta Coloring Method verifying test when positive Delta Coloring Method with positive delta value
      And   I get KPI circle value of the first KPI of the current visit
      And   I get KPI delta value of the first KPI of the current visit
      And   I navigate to the recent visit for Delta Coloring Method test when positive Delta Coloring Method with positive delta value
      And   I get KPI circle value of the first KPI of the recent previous visit
      And   I verify the delta value of the first KPI circle of the current visit
      And   I navigate to regular mobile report through the URL for Delta Coloring Method verifying test when positive Delta Coloring Method with positive delta value
      Then  I verify the delta color of the KPI circle of the current visit when KPI has positive Delta Coloring Method

    @commented_out_in_cypress
    Scenario: Verify color of the delta value for the positive Delta Coloring Method with negative delta value of the KPI circle
      When  I navigate to the Reporting Configurations K-Engine KPI Attributes page
      And   I retrieve Delta Coloring Method for the KPI when KPI has positive Delta Coloring Method
      And   I navigate to regular mobile report through the URL for Delta Coloring Method verifying test when positive Delta Coloring Method with negative delta value
      And   I get KPI circle value of the first KPI of the current visit
      And   I get KPI delta value of the first KPI of the current visit
      And   I navigate to the recent visit for Delta Coloring Method test when positive Delta Coloring Method with negative delta value
      And   I get KPI circle value of the first KPI of the recent previous visit
      And   I verify the delta value of the first KPI circle of the current visit
      And   I navigate to regular mobile report through the URL for Delta Coloring Method verifying test when positive Delta Coloring Method with negative delta value
      Then  I verify the delta color of the KPI circle of the current visit when KPI has positive Delta Coloring Method

    @commented_out_in_cypress
    Scenario: Verify color of the delta value for the negative Delta Coloring Method with positive delta value of the KPI circle
      When  I navigate to the Reporting Configurations K-Engine KPI Attributes page
      And   I retrieve Delta Coloring Method for the KPI when KPI has negative Delta Coloring Method
      And   I navigate to regular mobile report through the URL for Delta Coloring Method verifying test when negative Delta Coloring Method with positive delta value
      And   I get KPI circle value of the second KPI of the current visit
      And   I get KPI delta value of the second KPI of the current visit
      And   I navigate to the recent visit for Delta Coloring Method test when negative Delta Coloring Method with positive delta value
      And   I get KPI circle value of the second KPI of the recent previous visit
      And   I verify the delta value of the second KPI circle of the current visit
      And   I navigate to regular mobile report through the URL for Delta Coloring Method verifying test when negative Delta Coloring Method with positive delta value
      Then  I verify the delta color of the KPI circle of the current visit when KPI has negative Delta Coloring Method

    @commented_out_in_cypress
    Scenario: Verify color of the delta value for the negative Delta Coloring Method with negative delta value of the KPI circle
      When  I navigate to the Reporting Configurations K-Engine KPI Attributes page
      And   I retrieve Delta Coloring Method for the KPI when KPI has negative Delta Coloring Method
      And   I navigate to regular mobile report through the URL for Delta Coloring Method verifying test when negative Delta Coloring Method with negative delta value
      And   I get KPI circle value of the second KPI of the current visit
      And   I get KPI delta value of the second KPI of the current visit
      And   I navigate to the recent visit for Delta Coloring Method test when negative Delta Coloring Method with negative delta value
      And   I get KPI circle value of the second KPI of the recent previous visit
      And   I verify the delta value of the second KPI circle of the current visit
      And   I navigate to regular mobile report through the URL for Delta Coloring Method verifying test when negative Delta Coloring Method with negative delta value
      Then  I verify the delta color of the KPI circle of the current visit when KPI has negative Delta Coloring Method
