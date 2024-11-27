@api @users
Feature: API: Validate Users

  Background:
    Given the JSONPlaceholder API is available


  Scenario Outline: Get users by various valid IDs
    When I request user with ID <user_id>
    Then the response should contain the user data
    And the user ID should be <user_id>

    Examples:
      | user_id |
      | 1       |
      | 2       |
      | 3       |

  Scenario: Check response time is within acceptable limits
    When I request user with ID 1
    Then the response time for 1 user should be less than 500 milliseconds
