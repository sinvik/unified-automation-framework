import allure
from behave import given, when, then
from tests.web.pages.login_page import LogInPage
from common.utils.shared_utils import AllureUtils, logging_service

log = logging_service.getLogger(__file__)


@given('I open the web browser')
def step_impl(context):
    context.login_page = LogInPage(context.driver)


@given('I navigate to the login page')
def step_impl(context):
    context.login_page.navigate_url(context.url)


@when('I enter username: "{username}" and password: "{password}"')
def step_impl(context, username, password):
    with allure.step(f"I entered username {username}"):
        context.login_page.enter_username(username)

    with allure.step(f"I entered password {username}"):
        context.login_page.enter_password(password)


@when('I click the login button')
def step_impl(context):
    context.login_page.login()


@then('I should see the app logo on success')
def step_impl(context):
    with allure.step('I should see the app logo on success'):
        try:
            assert context.home_page.is_user_menu_displayed()

        except AssertionError as e:
            log.error("User menu is not displayed")
            raise AssertionError("Log In Failed")


@then('I log out from site')
def step_impl(context):
    context.home_page.log_out()


@then('I should see the following error message on failure')
def step_impl(context):
    message = context.table[0]['message']
    with allure.step('I should see the following error message on failure'):
        try:
            assert context.login_page.get_error_message() == message

        except AssertionError as e:
            log.error(f"Couldn't find message: {message}")
            raise AssertionError(f"Expected message not found")
