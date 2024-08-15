"""All methods for Contact list page."""

from homework25.pages.base_page import BasePage
from homework24.locators.contact_list_page import ContactListPageLocators


class ContactListPage(BasePage):
    """Class contact list page."""

    def click_add_a_new_contact(self):
        """Click on add a new contact button."""
        new_contact_btn = (self.find_element
                           (ContactListPageLocators.ADD_A_NEW_CONTACT_BUTTON))
        new_contact_btn.click()

    def click_row(self, number_of_row):
        """Click on first row to view the Contact Details."""
        row = self.find_element(ContactListPageLocators.CONTACT_TABLE_ROW +
                                f"[{number_of_row}]")
        row.click()
