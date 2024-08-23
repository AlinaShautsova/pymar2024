"""All methods for Add contact page."""

from homework25.pages.base_page import BasePage
from homework24.locators.add_contact_page import AddContactPageLocators


class AddContactPage(BasePage):
    """Class Add contact."""

    def enter_first_name(self, first_name):
        """Enter first name."""
        first_name_input = (self.find_element
                            (AddContactPageLocators.ADD_FIRSTNAME_INPUT))
        first_name_input.send_keys(first_name)

    def enter_last_name(self, last_name):
        """Enter last name."""
        last_name_input = (self.find_element
                           (AddContactPageLocators.ADD_LAST_NAME_INPUT))
        last_name_input.send_keys(last_name)

    def enter_date_of_birth(self, birth_date):
        """Enter date of birth."""
        date_of_birth_input = self.find_element(
            AddContactPageLocators.ADD_DATE_OF_BIRTH_INPUT)
        date_of_birth_input.send_keys(birth_date)

    def enter_email(self, email):
        """Enter email."""
        email_input = self.find_element(AddContactPageLocators.ADD_EMAIL_INPUT)
        email_input.send_keys(email)

    def enter_phone(self, phone):
        """Enter phone."""
        phone_input = self.find_element(AddContactPageLocators.ADD_PHONE_INPUT)
        phone_input.send_keys(phone)

    def enter_street_address1(self, address1):
        """Enter street address 1."""
        street_address1_input = (
            self.find_element
            (AddContactPageLocators.ADD_STREET_ADDRESS1_INPUT))
        street_address1_input.send_keys(address1)

    def enter_street_address2(self, address2):
        """Enter street address 2."""
        street_address2_input = (
            self.find_element
            (AddContactPageLocators.ADD_STREET_ADDRESS2_INPUT))
        street_address2_input.send_keys(address2)

    def enter_city(self, city):
        """Enter city."""
        city_input = self.find_element(AddContactPageLocators.ADD_CITY_INPUT)
        city_input.send_keys(city)

    def enter_state(self, state):
        """Enter state or province."""
        state_input = (
            self.find_element
            (AddContactPageLocators.ADD_STATE_OR_PROVINCE_INPUT))
        state_input.send_keys(state)

    def enter_postal_code(self, postal_code):
        """Enter postal code."""
        postal_code_input = (self.find_element
                             (AddContactPageLocators.ADD_POSTAL_CODE_INPUT))
        postal_code_input.send_keys(postal_code)

    def enter_country(self, country):
        """Enter country."""
        country_input = (self.find_element
                         (AddContactPageLocators.ADD_COUNTRY_INPUT))
        country_input.send_keys(country)

    def click_submit_button(self):
        """Click on submit button."""
        submit_button = (self.find_element
                         (AddContactPageLocators.SUBMIT_BUTTON))
        submit_button.click()

    def add_contact(self, first_name, last_name, birth_date, email, phone,
                    address1, address2, city, state, postal_code, country):
        """Adding a contact is completed."""
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_date_of_birth(birth_date)
        self.enter_email(email)
        self.enter_phone(phone)
        self.enter_street_address1(address1)
        self.enter_street_address2(address2)
        self.enter_city(city)
        self.enter_state(state)
        self.enter_postal_code(postal_code)
        self.enter_country(country)
        self.click_submit_button()
