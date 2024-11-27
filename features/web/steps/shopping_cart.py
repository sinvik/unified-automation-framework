import time
import allure
from behave import given, when, then
from tests.web.pages.home_page import HomePage
from tests.web.pages.check_out_page import CheckoutPage
from common.utils.shared_utils import AllureUtils, logging_service
from common.utils.exceptions import SomeErrorOuccured

log = logging_service.getLogger(__file__)


@when('I add the following items to the cart')
def step_impl(context):
    context.checkout_page = CheckoutPage(context.driver)

    for row in context.table:
        item = row['item']

        try:
            log.info(f"Adding item: {item}")

            # context.home_page.click_on_product(item)
            context.checkout_page.add_to_cart(item)
            # context.home_page.back_to_home()
        except SomeErrorOuccured as e:
            log.error(f"Unrecognized error, check previous steps: {e}")
            raise SomeErrorOuccured("Unrecognized error")


@then('the cart should display the item count as "{item_count}"')
def step_impl(context, item_count):
    with allure.step(f"the cart should display the item count as {item_count}"):
        try:
            assert str(context.home_page.get_cart_display_count()) == str(item_count)

        except AssertionError as e:
            log.error(f"Expected '{item_count}' in cart, but not found.")
            raise AssertionError(f"Expected '{item_count}' in cart, but not found.")


@when('I click on the cart icon to navigate to added products')
def step_impl(context):
    context.home_page.navigate_to_cart_list()


@then('I should see the following items in the cart')
def step_impl(context):
    with allure.step("I should see the following items in the cart"):
        actual_items = []
        expected_items = []

        for row in context.table:
            item = row['item']
            expected_items.append(item)
            if context.checkout_page.verify_product(item):
                log.info(f"Found item: {item}")
                actual_items.append(item)

        AllureUtils.attach_log_to_allure(expected_items, "expected_items")
        AllureUtils.attach_log_to_allure(actual_items, "actual_items")

        try:

            assert len(actual_items) == len(expected_items)

        except AssertionError as e:
            log.error(f"Some items are missing: {e}")
            raise AssertionError(f"Some items are missing") from e


@when('I proceed to checkout')
def step_impl(context):
    context.checkout_page.proceed_checkout()


@when('I enter the following details')
def step_impl(context):
    for row in context.table:
        first_name = row['First Name']
        last_name = row['Last Name']
        postal_code = row['Postal Code']
        context.checkout_page.fill_your_information(first_name, last_name, postal_code)
        break


@when('I click on continue')
def step_impl(context):
    context.checkout_page.click_on_continue()


@then('I should see the checkout information')
def step_impl(context):

    try:
        log.info("I should see the checkout information")
        context.checkout_page.is_checkout_information_displayed()

    except AssertionError as e:

        log.error("Expected Checkout information page")
        raise AssertionError("Expected Checkout information page")
