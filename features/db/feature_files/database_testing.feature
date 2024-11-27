@db
Feature: DB: Compare Actual vs Expected

  Scenario: Validate Employees and Departments
    Given a connection to the database
    When I fetch all employees
    Then the result should contain the following employees
      | EMPLOYEE_NAME  | DEPARTMENT_NAME |
      | John Doe       | HR              |
      | Jane Smith     | IT              |
      | Alice Johnson  | Finance         |

  Scenario: Validate Projects
    Given a connection to the database
    When I fetch all projects
    Then the result should contain the following projects
      | PROJECT_NAME | START_DATE | END_DATE   |
      | Project A    | 2024-01-01 | 2024-06-30 |
      | Project B    | 2024-02-01 | 2024-07-31 |
