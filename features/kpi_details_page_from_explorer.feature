@from_explorer
Feature: Mobile Reports KPI Details Page feature

  This contains the Mobile Reports KPI Details Page feature

    Background: Navigate to Reporting Configurations Mobile Reports General page, verify Mobile Reports page title & check whether the Show Live Report first checkbox is checked
      Given I login to Trax successfully through Okta
      When  I navigate to the Reporting configurations Explorer page
      And   I see the title as "Explorer" in Reporting configurations
      And   I set "Show Live Report first" checkbox in Reporting Configurations to true & save the changes
      Then  I verify "Show Live Report first" checkbox is checked in Reporting Configurations

    @commented_out_in_cypress
    Scenario: Configure reference images for the KPI and verify showing KPI reference images in mobile report KPI details Page
      When  I navigate to the Reporting configuration Mobile Reports KPI page
      And   I add reference images to the KPI
      And   I navigate to the Explorer application
      When  I can see the title as "Explorer - Visits"
      And   I search by live first visit ID for KPI reference image test
      And   I navigate to KPI details page
      And   I verify showing KPI reference image button in KPI details page
      And   I verify KPI reference images page

    @commented_out_in_cypress
    Scenario: Delete all KPI reference images for the KPI and verify not showing KPI reference image icon in mobile report KPI details Page
      When  I navigate to the Reporting configuration Mobile Reports KPI page
      And   I remove all the reference images for the KPI
      And   I navigate to the Explorer application
      When  I can see the title as "Explorer - Visits"
      And   I search by live first visit ID for KPI reference image test
      And   I navigate to KPI details page
      And   I verify not showing KPI reference image button in KPI details page

    @commented_out_in_cypress
    Scenario: Navigate to KPI details page of the Mobile Report and verify sorting of the KPI entities
      When  I navigate to the Explorer application
      And   I can see the title as "Explorer - Visits"
      And   I search by live first visit ID for KPI entities sorting test
      And   I navigate to the regular report
      And   I navigate to KPI details page for the KPI entities sorting test
      And   I capture KPI entity names and entity headers in the KPI details page
      Then  I verify KPI entities sorting menu options as per the KPI entity names and headers in the KPI details page
      And   I sort KPI entities in ascending order
      And   I verify sorting of KPI entities in ascending order
      And   I sort KPI entities in descending order
      And   I verify sorting of KPI entities in descending order
