@web @login
Feature: WEB: Login Feature
  As a user
  I want to login to the website
  So that I can access my account

  Background:
    Given I open the web browser
    And I navigate to the login page

  Scenario Outline: Successful login
    When I enter username: "<username>" and password: "<password>"
    And I click the login button
    Then I should see the app logo on success
    And I log out from site

    Examples:
      | username      | password     |
      | standard_user | secret_sauce |
      | problem_user  | secret_sauce |
      | visual_user   | secret_sauce |
      | error_user    | secret_sauce |

  Scenario Outline: Invalid login
    When I enter username: "<username>" and password: "<password>"
    And I click the login button
    Then I should see the following error message on failure
      | message                                                                   |
      | Epic sadface: Username and password do not match any user in this service |

    Examples:
      | username | password    |
      | Akash    | infy@123    |
      | vikas    | invalid_cre |
      | amit     | infy@123    |
