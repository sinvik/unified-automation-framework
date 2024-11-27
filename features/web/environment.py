from behave.runner import Context
from tests.web.utils.browser import WebDriverSetup
from tests.web.pages.home_page import HomePage
from common.utils.shared_utils import AllureUtils, in_memory_log


def before_scenario(context: Context, scenario):
    """
    Setup steps to be executed before each scenario.
    """

    in_memory_log.clear()

    driver_setup = WebDriverSetup()
    context.driver = driver_setup.get_web_driver()
    context.home_page = HomePage(context.driver)
    context.url = ""


def after_scenario(context: Context, scenario):
    """
    Cleanup steps to be executed after each scenario.
    """
    context.driver.close()
    context.driver.quit()

    collected_logs = in_memory_log.get_logs()
    AllureUtils.attach_log_to_allure(collected_logs, "log")

