"""
login_page.py:
    Integrate with web automation and perform login checks
"""
from selenium.webdriver.common.by import By
from tests.web.utils.web_utils import WebHelper


# pylint: disable=too-few-public-methods
class LoginPageLocators:
    """
    Modify locators value or type as per web element
    """
    USERNAME_INPUT = (By.ID, 'user-name')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    ERROR_MESSAGE = (By.CLASS_NAME, 'error-message-container')


class LogInPage(WebHelper):
    """
    Accessed locators and WebHelper to perform testing, methods can be extended as per use case
    """
    _locators = LoginPageLocators()

    def enter_username(self, username):
        """
        Finds element and enter value
        :param username:
        """
        self.enter_text(self._locators.USERNAME_INPUT, username)

    def enter_password(self, password):
        """
        Finds element and enter value
        :param password:
        """

        self.enter_text(self._locators.PASSWORD_INPUT, password)

    def login(self):
        """
        Finds element and click
        """

        self.click_element(self._locators.LOGIN_BUTTON)

    def get_error_message(self):
        """
        Finds element and extract info
        """

        return self.get_text(self._locators.ERROR_MESSAGE)
