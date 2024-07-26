Feature: Remove item
  Scenario: Remove one item from cart
    Given launch chrome browser
    When open Saucedemo homepage
    And enter username "standard_user" and password "secret_sauce"
    And click on login button
    And add item one for removal
    And add item two for removal
    And add item three for removal
    And add item four for removal
    And open cart
    Then remove one item and varify
