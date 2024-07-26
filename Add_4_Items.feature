Feature: Add 4 Items to cart
  Scenario: User adds 4 items to cart
    Given launch chrome browser
    When open Saucedemo homepage
    And enter username "standard_user" and password "secret_sauce"
    And click on login button
    And add item one to cart
    And add item two
    And add item three
    And add item four
    Then click on cart to verify
