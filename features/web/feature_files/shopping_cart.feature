@web @shoppingcart
Feature: WEB: Shopping Cart Feature
  As a shopper
  I want to add items to my cart, verify cart contents, and checkout
  So that I can purchase items from the Sauce Labs store

  Background:
    Given I open the web browser
    And I navigate to the login page
    When I enter username: "standard_user" and password: "secret_sauce"
    And I click the login button
    Then I should see the app logo on success

  Scenario: Add item and checkout
    When I add the following items to the cart
      | item                    |
      | Sauce Labs Backpack     |
      | Sauce Labs Bolt T-Shirt |
    Then the cart should display the item count as "2"
    When I click on the cart icon to navigate to added products
    Then I should see the following items in the cart
      | item                    |
      | Sauce Labs Backpack     |
      | Sauce Labs Bolt T-Shirt |
    When I proceed to checkout
    And I enter the following details
      | First Name | Last Name | Postal Code |
      | Vikaskumar | Singh     | 441108      |
    And I click on continue
    Then I should see the checkout information
    And I log out from site
