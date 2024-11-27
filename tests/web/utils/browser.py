"""
browser.py:
    To interact with web-elements we need middle person, example: chromedriver for Chrome browser.
    This module automatically identifies version of browser
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from common.utils.file_and_folder_service import FileFolderService
from common.utils.shared_utils import logging_service

log = logging_service.getLogger(__file__)


# pylint: disable=too-few-public-methods
class WebDriverSetup:
    """
    WebDriverSetup:
        Initialize WebDriverSetup() and perform browser configuration
    """
    def __init__(self):
        self.config = FileFolderService().load_config()["WEB"]
        self.browser = self.config["browser"]
        self.headless = self.config["headless"]

        log.info(f"Configured browser: {self.browser}")
        log.info(f"Configured headless: {self.headless}")

    def get_web_driver(self):
        """
        This method decides which browser to choose
        """
        if self.browser == 'chrome':
            return self._get_chrome_driver()
        if self.browser == 'firefox':
            return self._get_firefox_driver()
        log.error(f"Unsupported browser: {self.browser}")
        raise ValueError(f"Unsupported browser: {self.browser}")

    def _get_chrome_driver(self):
        """
        This method returns browser to get_web_driver() method
        """
        chrome_options = ChromeOptions()
        if self.headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--start-maximized")
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                options=chrome_options)

    def _get_firefox_driver(self):
        """
        This method returns browser to get_web_driver() method
        """
        firefox_options = FirefoxOptions()
        if self.headless:
            firefox_options.add_argument("--headless")
        firefox_options.add_argument("--start-maximized")
        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),
                                 options=firefox_options)
