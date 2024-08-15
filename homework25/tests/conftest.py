"""Module with necessary fixtures."""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from homework24.locators.contact_list_page import ContactListPageLocators
from homework25.pages.login_page import LoginPage
from homework25.test_data.login_page_test_data import URL, EMAIL, PASSWORD


@pytest.fixture()
def open_browser():
    """Fixture opens a browser and navigates to a specified URL."""
    browser = webdriver.Chrome()
    browser.get(URL)
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


@pytest.fixture()
def login(open_browser):
    """The browser fixture to open the login page."""

    browser = open_browser
    wait = WebDriverWait(browser, 10)

    login_page = LoginPage(browser)
    login_page.login(EMAIL, PASSWORD)

    wait.until(EC.presence_of_element_located(
        (By.XPATH, ContactListPageLocators.HEADER)))
