"""
home_page.py:
    Integrate with web automation
"""
from selenium.webdriver.common.by import By
from tests.web.utils.web_utils import WebHelper


# pylint: disable=too-few-public-methods
class HomePageLocators:
    """
    Modify locators value or type as per web element
    """
    CART_LINK = 'cart.html'
    MENU_ICON = (By.ID, 'react-burger-menu-btn')
    LOGOUT_BTN = (By.ID, 'logout_sidebar_link')
    USER_MENU = (By.CLASS_NAME, 'app_logo')
    SHOPPING_CART_BADGE = (By.CLASS_NAME, 'shopping_cart_badge')
    BACK_TO_HOME = (By.ID, 'back-to-products')

    @staticmethod
    def inventory_item_name(item: str) -> tuple:
        """
        Name of the item
        """
        return By.XPATH, f"//div[@class='inventory_item_name' and text()='{item}']"


class HomePage(WebHelper):
    """
    Accessed locators and WebHelper to perform testing, methods can be extended as per use case
    """
    _locators = HomePageLocators()

    def click_on_product(self, item):
        """
        Finds element and click
        """
        product_locator = self._locators.inventory_item_name(item)
        self.click_element(product_locator)

    def get_cart_display_count(self):
        """
        Obtain the count of product added in cart
        """
        return self.get_text(self._locators.SHOPPING_CART_BADGE)

    def navigate_to_cart_list(self):
        """
        Click on cart icon to proceed for checkout
        """
        self.navigate_url(self._locators.CART_LINK)

    def back_to_home(self):
        """
        Go back to home once you have added item in cart
        """
        self.click_element(self._locators.BACK_TO_HOME)

    def is_user_menu_displayed(self):
        """
        Finds element and extract info
        """

        return self.get_text(self._locators.USER_MENU)

    def log_out(self):
        """
        Log out from the portal
        """
        if self.is_element_visible(self._locators.MENU_ICON):
            self.click_element(self._locators.MENU_ICON)
            self.click_element(self._locators.LOGOUT_BTN)
