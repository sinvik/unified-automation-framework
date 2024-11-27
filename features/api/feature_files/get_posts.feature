@api @posts
Feature: API: Validate Posts

  Background:
    Given the JSONPlaceholder API is available

  Scenario: Get all posts
    When I request all posts
    Then the list should not be empty

  Scenario: Get a post by valid ID
    When I request post with ID 1
    Then the list should not be empty
    And the post ID should be 1

  Scenario Outline: Get posts by various valid IDs
    When I request post with ID <post_id>
    Then the response should contain the post data
    And the post ID should be <post_id>

    Examples:
      | post_id |
      | 1       |
      | 2       |
      | 3       |
