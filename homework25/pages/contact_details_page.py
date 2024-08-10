"""All methods for Contact details page."""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from homework24.locators.contact_details_page import ContactDetailsPageLocators
from homework25.pages.base_page import BasePage
from homework25.test_data.contact_details_test_data import URL


class ContactDetailsPage(BasePage):
    """Class Contact details page."""
    def __init__(self, driver):
        """Initialisation."""
        super().__init__(driver)
        self.url = URL

    def click_edit_button(self):
        """Click edit button."""
        edit_contact_button = \
            (self.find_element(ContactDetailsPageLocators.EDIT_CONTACT_BUTTON))
        edit_contact_button.click()

    def click_delete_button(self):
        """Click delete button."""
        delete_button = (self.find_element
                         (ContactDetailsPageLocators.DELETE_CONTACT_BUTTON))
        delete_button.click()

    def return_to_contact_list_button(self):
        """Click on return to contact list button."""
        return_button = (self.find_element
                         (ContactDetailsPageLocators.
                          RETURN_TO_CONTACT_LIST_BUTTON))
        return_button.click()

    def delete_contact(self):
        """Function delete a contact."""
        self.click_delete_button()

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.alert_is_present()).accept()
