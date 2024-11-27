import time
import allure
from behave import given, when, then
from tests.api.utils.api_service import APIService
from tests.api.utils.api_utils import APIUtils
from tests.api.end_points.json_place_holder_api import EndPoints
from common.utils.shared_utils import AllureUtils, logging_service

log = logging_service.getLogger(__file__)


@when('I request all posts')
def step_impl(context):
    service = APIService(context.base_url)
    with allure.step('I request all posts'):
        context.data = service.get_request(EndPoints.get_post_endpoint())


@when('I request post with ID {post_id}')
def step_impl(context, post_id):
    service = APIService(context.base_url)
    with allure.step(f'I request post with ID {post_id}'):
        context.data = service.get_request(EndPoints.get_post_endpoint(post_id))


@then('the list should not be empty')
def step_impl(context):

    actual = len(context.data)
    with allure.step('the list should not be empty'):
        try:
            assert actual != 0

        except AssertionError as e:
            log.error(f"Post lists seems to be empty. {e}")
            raise AssertionError(f"Post lists seems to be empty") from e


@then('the response should contain the post data')
def step_impl(context):
    expected = ["id", "title", "body", "userId"]
    actual = context.data
    with allure.step('Response should contain the post data'):
        try:
            assert APIUtils.validate_json_structure(actual, expected)

        except AssertionError as e:
            log.error(f"Expected keys: {expected}, got keys: {actual} {e}")
            raise AssertionError(f"Expected keys: {expected}, got keys: {actual}") from e


@then('the post ID should be {post_id:d}')
def step_impl(context, post_id):
    expected = post_id
    actual = context.data["id"]
    with allure.step(f'Post ID should be {expected}'):
        try:
            assert expected == actual

        except AssertionError as e:
            log.error(f"Expected post ID {expected}, got {actual} {e}")
            raise AssertionError(f"Expected post ID {expected}, got {actual}") from e
