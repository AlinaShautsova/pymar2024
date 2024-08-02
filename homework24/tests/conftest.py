"""Module with necessary fixtures."""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from homework24.constants import URL, EMAIL, PASSWORD
from homework24.locators.login_page import LoginPageLocators


@pytest.fixture()
def open_browser():
    """Fixture opens a browser and navigates to a specified URL."""
    browser = webdriver.Chrome()
    browser.get(URL)
    yield browser
    browser.quit()


@pytest.fixture(autouse=True)
def login(open_browser):
    """The browser fixture to open the login page."""

    browser = open_browser
    wait = WebDriverWait(browser, 10)

    email_field = wait.until(EC.presence_of_element_located(
        (By.XPATH, LoginPageLocators.LOGIN_EMAIL_INPUT)))
    email_field.send_keys(EMAIL)

    password_field = browser.find_element(
        By.XPATH, LoginPageLocators.LOGIN_PASSWORD_INPUT)
    password_field.send_keys(PASSWORD)

    button_submit = browser.find_element(
        By.XPATH, LoginPageLocators.LOGIN_SUBMIT_BUTTON)
    button_submit.click()

    wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[contains(text(), "Contact List")]')))
