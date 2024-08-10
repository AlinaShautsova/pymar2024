"""This module for adding, updating, and deleting contacts."""
import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from homework24.locators.contact_details_page import ContactDetailsPageLocators
from homework24.locators.contact_list_page import ContactListPageLocators
from homework25.pages.add_contact_page import AddContactPage
from homework25.pages.contact_details_page import ContactDetailsPage
from homework25.pages.contact_list_page import ContactListPage
from homework25.pages.edit_contact_page import EditContactPage
from homework25.test_data.add_contact_test_data import *
from homework25.test_data.edit_contact_test_data import *


def test_add_contact(open_browser, login):
    """Test case for adding a new contact."""
    contact_list_page = ContactListPage(open_browser)
    contact_list_page.click_add_a_new_contact()

    add_contact_page = AddContactPage(open_browser)
    add_contact_page.add_contact(FIRST_NAME, LAST_NAME, BIRTH_DATE, EMAIL,
                                 PHONE, ADDRESS_STREET1, ADDRESS_STREET2, CITY,
                                 STATE_OR_PROVINCE, POST_CODE, COUNTRY)
    contact_row = (WebDriverWait
                   (open_browser, 10).until
                   (EC.presence_of_element_located
                    ((By.XPATH, ContactListPageLocators.CONTACT_TABLE_ROW
                      + '[1]'))))
    assert contact_row is not None


def test_edit_contact(open_browser, login):
    """Test case for editing an existing contact."""
    contact_list_page = ContactListPage(open_browser)
    contact_list_page.click_row(1)

    contact_details_page = ContactDetailsPage(open_browser)
    contact_details_page.click_edit_button()

    edit_contact_page = EditContactPage(open_browser)
    edit_contact_page.edit_contact(EDIT_FIRST_NAME, EDIT_LAST_NAME,
                                   EDIT_BIRTH_DATE, EDIT_EMAIL, EDIT_PHONE,
                                   EDIT_ADDRESS_STREET1, EDIT_ADDRESS_STREET2,
                                   EDIT_CITY, EDIT_STATE_OR_PROVINCE,
                                   EDIT_POST_CODE,  EDIT_COUNTRY)

    time.sleep(3)

    expected_details = {
        ContactDetailsPageLocators.FIRST_NAME_SPAN: EDIT_FIRST_NAME,
        ContactDetailsPageLocators.LAST_NAME_SPAN: EDIT_LAST_NAME,
        ContactDetailsPageLocators.BIRTHDATE_SPAN: EDIT_BIRTH_DATE,
        ContactDetailsPageLocators.EMAIL_SPAN: EDIT_EMAIL,
        ContactDetailsPageLocators.PHONE_SPAN: EDIT_PHONE,
        ContactDetailsPageLocators.STREET1_SPAN: EDIT_ADDRESS_STREET1,
        ContactDetailsPageLocators.STREET2_SPAN: EDIT_ADDRESS_STREET2,
        ContactDetailsPageLocators.CITY_SPAN: EDIT_CITY,
        ContactDetailsPageLocators.STATE_PROVINCE_SPAN: EDIT_STATE_OR_PROVINCE,
        ContactDetailsPageLocators.POSTAL_CODE_SPAN: EDIT_POST_CODE,
        ContactDetailsPageLocators.COUNTRY_SPAN: EDIT_COUNTRY
    }
    for key, value in expected_details.items():
        assert open_browser.find_element(By.XPATH, key).text == value


def test_delete_contact(open_browser, login):
    """Test case for deleting a contact."""
    contact_list_page = ContactListPage(open_browser)
    contact_list_page.click_row(1)

    contact_details_page = ContactDetailsPage(open_browser)
    contact_details_page.delete_contact()

    wait = WebDriverWait(open_browser, 10)
    try:
        (wait.until
         (EC.presence_of_element_located
          ((By.XPATH, f"//*[contains(text(), '{EDIT_FIRST_NAME} + "
                      f"{EDIT_LAST_NAME}')]"))))
        assert False, (f"Contact: {EDIT_FIRST_NAME} + {EDIT_LAST_NAME} was "
                       f"not deleted successfully.")
    except TimeoutException:
        assert True
