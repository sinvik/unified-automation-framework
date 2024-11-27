import allure
from behave import given, when, then
from common.utils.shared_utils import AllureUtils, logging_service

log = logging_service.getLogger(__file__)


@given('a connection to the database')
def step_impl(context):
    context.db.establish_connection()


@when('I fetch all employees')
def step_impl(context):
    query = """
    SELECT E.EMPLOYEE_NAME, D.DEPARTMENT_NAME
    FROM EMPLOYEES E
    JOIN DEPARTMENTS D ON E.DEPARTMENT_ID = D.DEPARTMENT_ID
    """
    with allure.step("I fetch all employees"):
        context.employees = context.db.fetch_all(query)
        actual_employees = [{'EMPLOYEE_NAME': row[0], 'DEPARTMENT_NAME': row[1]} for row in context.employees]
        AllureUtils.attach_log_to_allure(actual_employees, "actual_employees")


@then('the result should contain the following employees')
def step_impl(context):
    expected_employees = [row.as_dict() for row in context.table]

    with allure.step(f"the result should contain the following employees"):
        AllureUtils.attach_log_to_allure(expected_employees, "expected_employees")
        actual_employees = [{'EMPLOYEE_NAME': row[0], 'DEPARTMENT_NAME': row[1]} for row in context.employees]

        try:
            assert expected_employees == actual_employees

        except AssertionError as e:
            log.error(f"Expected {expected_employees}, but got {actual_employees}")
            raise AssertionError(f"Expected {expected_employees}, but got {actual_employees}")


@when('I fetch all projects')
def step_impl(context):
    query = "SELECT PROJECT_NAME, START_DATE, END_DATE FROM PROJECTS"
    with allure.step('I fetch all projects'):
        context.projects = context.db.fetch_all(query)
        actual_projects = [row[0] for row in context.projects]
        AllureUtils.attach_log_to_allure(actual_projects, "actual_projects")


@then('the result should contain the following projects')
def step_impl(context):

    actual_projects = [row[0] for row in context.projects]
    expected_projects = [row['PROJECT_NAME'] for row in context.table]
    with allure.step("the result should contain the following projects"):
        AllureUtils.attach_log_to_allure(expected_projects, "expected_projects")
        try:
            assert expected_projects == actual_projects

        except AssertionError as e:
            log.error(f"Expected {expected_projects}, but got {actual_projects}")
            raise AssertionError(f"Expected {expected_projects}, but got {actual_projects}")
