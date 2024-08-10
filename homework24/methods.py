"""This module contains add_contact method, edit and delete contact
 methods. """

import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from homework24.locators.add_contact_page import AddContactPageLocators
from homework24.locators.contact_details_page import ContactDetailsPageLocators
from homework24.locators.contact_list_page import ContactListPageLocators
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
      ((By.XPATH, ContactListPageLocators.CONTACT_TABLE_ROW))).click())
    (wait.until
     (EC.element_to_be_clickable
      ((By.XPATH, ContactDetailsPageLocators.EDIT_CONTACT_BUTTON))).click())
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
                    ((By.XPATH, ContactListPageLocators.CONTACT_TABLE_ROW))))
    contact_name = contact_row.text
    contact_row.click()
    (wait.until
     (EC.element_to_be_clickable
      ((By.XPATH, ContactDetailsPageLocators.DELETE_CONTACT_BUTTON))).click())
    wait.until(EC.alert_is_present()).accept()
    try:
        (wait.until
         (EC.presence_of_element_located
          ((By.XPATH, f"//*[contains(text(), '{contact_name}')]"))))
        return False
    except TimeoutException:
        return True
