Feature: Login
  Scenario: User logs in successfully
    Given launch chrome browser
    When open Saucedemo homepage
    And enter username "standard_user" and password "secret_sauce"
    And click on login button
    Then user should be successful login
