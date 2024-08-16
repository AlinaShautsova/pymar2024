"""All methods for Base page"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Class base page."""

    def __init__(self, driver):
        """Initialisation."""
        self.driver = driver

    def open(self, url):
        """Open page by url."""
        self.driver.get(url)

    def find_element(self, selector):
        """Find element by selector."""
        return self.driver.find_element(By.XPATH, selector)

    def find_elements(self, selector):
        """Find elements by selector."""
        return self.driver.find_elements(By.XPATH, selector)

    def wait_until_element_value(self, selector, value):
        """Wait until element value present."""
        (WebDriverWait(self.driver, 10).until
         (EC.text_to_be_present_in_element_value((By.XPATH, selector),
                                                 value)))
