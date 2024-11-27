"""
web_utils.py:
    Userful methods to perform selenium related operations
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from common.utils.file_and_folder_service import FileFolderService
from common.utils.shared_utils import logging_service

log = logging_service.getLogger(__file__)


class WebHelper:
    """
    Initialize WebHelper() class and make use of all methods
    """
    def __init__(self, driver):
        """
        Initializes the BasePage with a WebDriver instance and base URL.
        """
        super().__init__()

        os_operations = FileFolderService()

        self.config = os_operations.load_config()["WEB"]
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.base_url = self.config["base_url"]
        self.timeout = 10  # Default timeout for waiting

    def navigate_url(self, url_path: str):
        """
        Opens a web page by combining the base URL with a specified path.

        Args:
            url_path (str): The URL path to open.
        """
        url = f"{self.base_url}/{url_path}"
        log.info(f"URL: {url}")

        try:
            self.driver.get(url)
        except WebDriverException as e:
            log.error(f"Occurred error while opening url: {url}")
            raise WebDriverException("Occurred error while opening url") from e

    def find_element(self, locator):
        """Find a single web element."""
        try:
            element = self.driver.find_element(*locator)
            return element
        except NoSuchElementException as e:
            log.error(f"Element not found: {locator}")
            raise NoSuchElementException(f"Element not found: {locator}") from e

    def find_elements(self, locator):
        """Find multiple web elements."""
        try:
            elements = self.driver.find_elements(*locator)
            return elements
        except NoSuchElementException as e:
            log.error(f"Element not found: {locator}")
            raise NoSuchElementException(f"Element not found: {locator}") from e

    def click_element(self, locator):
        """Click on a web element."""
        element = self.find_element(locator)
        if element:
            element.click()

    def enter_text(self, locator, text):
        """Enter text into a web element."""
        element = self.find_element(locator)
        if element:
            element.clear()
            element.send_keys(text)

    def get_text(self, locator):
        """Get text from a web element."""
        element = self.find_element(locator)
        return element.text if element else ""

    def is_element_visible(self, locator):
        """Check if a web element is visible."""
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException as e:
            log.error(f"Element is not visible: {locator}")
            raise TimeoutException(f"Element is not visible: {locator}") from e

    def wait_for_element(self, locator):
        """Wait for a web element to be present."""
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException as e:
            log.error(f"Element is not visible yet: {locator}")
            raise TimeoutException(f"Element is not visible yet: {locator}") from e

    def is_clickable(self, locator):
        """Check if a web element is clickable."""
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return True
        except TimeoutException as e:
            log.error(f"Element is not clickable: {locator}")
            raise TimeoutException(f"Element is not clickable: {locator}") from e
