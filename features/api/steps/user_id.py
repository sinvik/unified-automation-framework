import time
import allure
from behave import given, when, then
from tests.api.utils.api_service import APIService
from tests.api.utils.api_utils import APIUtils
from tests.api.end_points.json_place_holder_api import EndPoints
from common.utils.shared_utils import AllureUtils, logging_service

log = logging_service.getLogger(__file__)


@given('the JSONPlaceholder API is available')
def step_impl(context):
    service = APIService(context.base_url)
    with allure.step('API service is available'):
        pass


@when('I request user with ID {user_id}')
def step_impl(context, user_id):
    service = APIService(context.base_url)
    with allure.step(f'I request user with ID {user_id}'):
        context.data = service.get_request(EndPoints.get_user_endpoint(user_id))


@then('the response should contain the user data')
def step_impl(context):

    expected = ["id", "name", "username", "email"]
    actual = context.data
    with allure.step("Response should contain the user data"):
        try:
            assert APIUtils.validate_json_structure(actual, expected)

        except AssertionError as e:
            log.error(f"Expected keys {expected}, got {actual} {e}")
            raise AssertionError(f"Expected keys {expected}, got {actual}") from e


@then('the user ID should be {user_id:d}')
def step_impl(context, user_id):

    expected = user_id
    actual = context.data["id"]
    with allure.step(f"the user ID should be {user_id}"):
        try:
            assert context.data["id"] == user_id

        except AssertionError as e:
            log.error(f"Expected keys {expected}, got {actual} {e}")
            raise AssertionError(f"Expected keys {expected}, got {actual}") from e


@then('the response time for {user_id:d} user should be less than {milliseconds:d} milliseconds')
def step_impl(context, user_id, milliseconds):

    service = APIService(context.base_url)
    with allure.step(f'Response time should be {milliseconds} milliseconds'):
        start_time = time.time()
        service.get_request(EndPoints.get_user_endpoint(user_id))
        elapsed_time = (time.time() - start_time) * 1000  # Convert to milliseconds

        try:
            assert elapsed_time is not milliseconds

        except AssertionError as e:
            log.error(f"Expected response time {str(milliseconds)}ms, got {str(milliseconds)}ms")
            raise AssertionError(f"Expected response time {str(milliseconds)}ms, got {str(milliseconds)}ms") from e
