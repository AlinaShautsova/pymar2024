"""This module for adding, updating, and deleting contacts."""

import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from homework24.locators.contact_list_page import ContactListPageLocators
from homework24.locators.add_contact_page import AddContactPageLocators
from homework24.locators.delete_contact import DeleteContactDetails
from homework24.locators.edit_contact_page import EditContactPageLocators


def add_contact(browser, contact_info):
    """Function add a contact."""
    wait = WebDriverWait(browser, 10)
    (wait.until
     (EC.element_to_be_clickable
      ((By.XPATH, ContactListPageLocators.ADD_A_NEW_CONTACT_BUTTON))).click())
    for field, value in contact_info.items():
        element = wait.until(EC.presence_of_element_located((By.XPATH, field)))
        element.send_keys(value)
    (wait.until
     (EC.element_to_be_clickable
      ((By.XPATH, AddContactPageLocators.SUBMIT_BUTTON))).click())


def edit_contact(browser, updated_info):
    """Function edit a contact."""
    wait = WebDriverWait(browser, 10)
    (wait.until
     (EC.element_to_be_clickable
      ((By.XPATH, EditContactPageLocators.CONTACT_TABLE_ROW))).click())
    (wait.until
     (EC.element_to_be_clickable
      ((By.XPATH, EditContactPageLocators.EDIT_CONTACT_BUTTON))).click())
    time.sleep(1)
    for field, value in updated_info.items():
        element = wait.until(EC.element_to_be_clickable((By.XPATH, field)))
        element.clear()
        element.send_keys(value)
    (wait.until
     (EC.element_to_be_clickable
      ((By.XPATH, EditContactPageLocators.SUBMIT_BUTTON))).click())
    time.sleep(5)


def delete_contact(browser):
    """Function delete a contact."""
    wait = WebDriverWait(browser, 10)
    contact_row = (wait.until
                   (EC.presence_of_element_located
                    ((By.XPATH, DeleteContactDetails.CONTACT_TABLE_ROW))))
    contact_name = contact_row.text
    contact_row.click()
    (wait.until
     (EC.element_to_be_clickable
      ((By.XPATH, DeleteContactDetails.DELETE_CONTACT_BUTTON))).click())
    wait.until(EC.alert_is_present()).accept()
    try:
        (wait.until
         (EC.presence_of_element_located
          ((By.XPATH, f"//*[contains(text(), '{contact_name}')]"))))
        return False
    except TimeoutException:
        return True


def test_add_contact(open_browser):
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
        AddContactPageLocators.ADD_STATE_OF_PROVINCE_INPUT: 'NY',
        AddContactPageLocators.ADD_POSTAL_CODE_INPUT: '123409',
        AddContactPageLocators.ADD_COUNTRY_INPUT: 'USA',
    }
    browser = open_browser
    add_contact(browser, contact_info)
    contact_row = (WebDriverWait
                   (browser, 10).until
                   (EC.presence_of_element_located
                    ((By.XPATH, EditContactPageLocators.CONTACT_TABLE_ROW))))
    assert contact_row is not None


def test_edit_contact(open_browser):
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


def test_delete_contact(open_browser):
    """Test case for deleting a contact."""
    browser = open_browser
    assert delete_contact(browser), "Contact was not deleted successfully."
