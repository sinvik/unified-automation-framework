"""
check_out_page.py:
    Integrate with web automation
"""
from selenium.webdriver.common.by import By
from tests.web.utils.web_utils import WebHelper


# pylint: disable=too-few-public-methods
class CheckoutPageLocators:
    """
    Modify locators value or type as per web element
    """

    CHECKOUT_BUTTON = (By.CLASS_NAME, 'checkout_button')
    CONTINUE_BUTTON = (By.XPATH, '//*[@id="continue"]')
    FIRST_NAME_INPUT = (By.ID, 'first-name')
    LAST_NAME_INPUT = (By.ID, 'last-name')
    POSTAL_CODE_INPUT = (By.ID, 'postal-code')
    SUMMARY_INFO = (By.CLASS_NAME, 'summary_info_label')

    @staticmethod
    def add_to_cart_button(item: str) -> tuple:
        """
        Click on Add to cart button
        """
        return (By.XPATH,
                f"//div[text()='{item}']/ancestor::div[@class='inventory_item']//button")

    @staticmethod
    def cart_item_name(item: str) -> tuple:
        """
        Product name that are added for checkout
        """
        return (By.XPATH,
                f"//div[@class='cart_list']//div[@class='inventory_item_name' and text()='{item}']")


class CheckoutPage(WebHelper):
    """
    Accessed locators and WebHelper to perform testing, methods can be extended as per use case
    """
    _locators = CheckoutPageLocators()

    def add_to_cart(self, item):
        """
        Finds element and click
        """
        add_to_cart_locator = self._locators.add_to_cart_button(item)
        self.click_element(add_to_cart_locator)

    def verify_product(self, item):
        """
        Verify Product name which is listed in cart
        :param item: Product name
        """
        cart_item_locator = self._locators.cart_item_name(item)
        return self.is_element_visible(cart_item_locator)

    def proceed_checkout(self):
        """
        Go to checkout page
        """
        self.click_element(self._locators.CHECKOUT_BUTTON)

    def fill_your_information(self, first_name, last_name, postal_code):
        """
        Fill up required information on check page
        :param first_name:
        :param last_name:
        :param postal_code:
        """
        self.enter_text(self._locators.FIRST_NAME_INPUT, first_name)
        self.enter_text(self._locators.LAST_NAME_INPUT, last_name)
        self.enter_text(self._locators.POSTAL_CODE_INPUT, postal_code)

    def click_on_continue(self):
        """
        Click on continue button
        """
        self.is_clickable(self._locators.CONTINUE_BUTTON)
        self.click_element(self._locators.CONTINUE_BUTTON)

    def is_checkout_information_displayed(self):
        """
        Verify if Payment summary information page is displayed
        """
        return self.is_element_visible(self._locators.SUMMARY_INFO)
