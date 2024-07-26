Feature: Checkout Journey
  Scenario: Checkout process
    Given launch chrome browser
    When open Saucedemo homepage
    And enter username "standard_user" and password "secret_sauce"
    And click on login button
    And order one
    And order two
    And order three
    And order four
    And open cartbox
    And remove one item and varify
    And click on checkout button
    And enter firstname "Rohit" and lastname "kumar" and zipcode "12345"
    And click on continue button
    And varify the total ammount
    And click on finish button
    Then varify the final page
