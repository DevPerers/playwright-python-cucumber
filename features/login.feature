Feature: Verify the login page and its functionality
  
  Background: user navigates to the login page
    Given the user navigates to the login page
    
  Scenario: Verify the login page is accessible
    Then the login page should be visible

  Scenario: Verify the login page UI
    Then the login page UI elements are visible

  Scenario: User sees an error message on login page
    When clicks the login button
    Then the user should see the error message as "Please provide a user name"

  Scenario: User logs in with incorrect credentials
    When the user enters username "aut_auth1@traxretail.com" and password "a1"
    And clicks the login button
    Then the user should see the error message as "Invalid credentials."

  Scenario: User logs in with correct credentials
    When the user enters username "aut_auth@traxretail.com" and password "a"
    And clicks the login button
    Then user should see OKTA login page
    When the user enters OKTAusername "aut_auth@traxretail.com" and password "Cypress@Automation25"
    And clicks the OKTA login button
    Then the homepage application header should be visible as "Homepage "
