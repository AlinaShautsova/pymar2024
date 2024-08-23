"""This module for adding, updating, and deleting contacts."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from homework24.locators.add_contact_page import AddContactPageLocators
from homework24.locators.contact_list_page import ContactListPageLocators
from homework24.locators.edit_contact_page import EditContactPageLocators
from homework24.methods import add_contact, edit_contact, delete_contact


def test_add_contact(open_browser, login):
    """Test case for adding a new contact."""
    contact_info = {
        AddContactPageLocators.ADD_FIRSTNAME_INPUT: 'Kate',
        AddContactPageLocators.ADD_LAST_NAME_INPUT: 'Mirror',
        AddContactPageLocators.ADD_DATE_OF_BIRTH_INPUT: '1988-05-09',
        AddContactPageLocators.ADD_EMAIL_INPUT: 'zxcvb@gmail.com',
        AddContactPageLocators.ADD_PHONE_INPUT: '2342635332',
        AddContactPageLocators.ADD_STREET_ADDRESS1_INPUT: 'First st 6',
        AddContactPageLocators.ADD_STREET_ADDRESS2_INPUT: 'Second 1',
        AddContactPageLocators.ADD_CITY_INPUT: 'New York',
        AddContactPageLocators.ADD_STATE_OR_PROVINCE_INPUT: 'NY',
        AddContactPageLocators.ADD_POSTAL_CODE_INPUT: '123409',
        AddContactPageLocators.ADD_COUNTRY_INPUT: 'USA',
    }
    browser = open_browser
    add_contact(browser, contact_info)
    contact_row = (WebDriverWait
                   (browser, 10).until
                   (EC.presence_of_element_located
                    ((By.XPATH, ContactListPageLocators.CONTACT_TABLE_ROW
                      + '[1]'))))
    assert contact_row is not None


def test_edit_contact(open_browser, login):
    """Test case for editing an existing contact."""
    updated_info = {
        EditContactPageLocators.ADD_LASTNAME_INPUT: 'Petrova',
        EditContactPageLocators.ADD_EMAIL_INPUT: '789asdf@gmail.com',
        EditContactPageLocators.ADD_PHONE_INPUT: '83543463847',
        EditContactPageLocators.ADD_COUNTRY_INPUT: 'Netherlands',
    }
    expected_details = {
        '//span[@id="lastName"]': 'Petrova',
        '//span[@id="email"]': '789asdf@gmail.com',
        '//span[@id="phone"]': '83543463847',
        '//span[@id="country"]': 'Netherlands',
    }
    browser = open_browser
    edit_contact(browser, updated_info)
    for key, value in expected_details.items():
        assert browser.find_element(By.XPATH, key).text == value


def test_delete_contact(open_browser, login):
    """Test case for deleting a contact."""
    browser = open_browser
    assert delete_contact(browser), "Contact was not deleted successfully."
