"""All methods for Edit contact page"""
from homework25.pages.base_page import BasePage
from homework24.locators.edit_contact_page import EditContactPageLocators


class EditContactPage(BasePage):
    """Class Edit Contact page."""

    def __init__(self, driver):
        """Initialisation."""
        super().__init__(driver)

    def clean_edit_field(self, locator, value):
        """Clean and edit fields."""
        first_name_input = self.find_element(locator)
        first_name_input.clear()
        self.wait_until_element_value(locator, "")
        first_name_input.send_keys(value)
        self.wait_until_element_value(locator, value)

    def edit_first_name(self, first_name):
        """Edit first name."""
        self.clean_edit_field(EditContactPageLocators.ADD_FIRSTNAME_INPUT,
                              first_name)

    def edit_last_name(self, last_name):
        """Edit last name."""
        self.clean_edit_field(EditContactPageLocators.ADD_LASTNAME_INPUT,
                              last_name)

    def edit_date_of_birth(self, birth_date):
        """Edit date of birth."""
        self.clean_edit_field(EditContactPageLocators.ADD_DATE_OF_BIRTH_INPUT,
                              birth_date)

    def edit_email(self, email):
        """Edit email."""
        self.clean_edit_field(EditContactPageLocators.ADD_EMAIL_INPUT, email)

    def edit_phone(self, phone):
        """Edit phone."""
        self.clean_edit_field(EditContactPageLocators.ADD_PHONE_INPUT, phone)

    def edit_street_address1(self, address1):
        """Edit street address 1."""
        self.clean_edit_field(
            EditContactPageLocators.ADD_STREET_ADDRESS1_INPUT, address1)

    def edit_street_address2(self, address2):
        """Edit street address 2."""
        self.clean_edit_field(
            EditContactPageLocators.ADD_STREET_ADDRESS2_INPUT, address2)

    def edit_city(self, city):
        """Edit city."""
        self.clean_edit_field(EditContactPageLocators.ADD_CITY_INPUT, city)

    def edit_state_or_province(self, state_or_province):
        """Edit state or province."""
        self.clean_edit_field(
            EditContactPageLocators.ADD_STATE_OR_PROVINCE_INPUT,
            state_or_province)

    def edit_postal_code(self, postal_code):
        """Edit postal code."""
        self.clean_edit_field(EditContactPageLocators.ADD_POSTAL_CODE_INPUT,
                              postal_code)

    def edit_country(self, country):
        """Edit country."""
        self.clean_edit_field(EditContactPageLocators.ADD_COUNTRY_INPUT,
                              country)

    def click_submit_button(self):
        """Click submit button"""
        submit_button = self.find_element(EditContactPageLocators.
                                          SUBMIT_BUTTON)
        submit_button.click()

    def edit_contact(self, first_name, last_name, birth_date, email, phone,
                     street_address1, street_address2, city, state_or_province,
                     postal_code, country):
        """Edit contact."""
        self.edit_first_name(first_name)
        self.edit_last_name(last_name)
        self.edit_date_of_birth(birth_date)
        self.edit_email(email)
        self.edit_phone(phone)
        self.edit_street_address1(street_address1)
        self.edit_street_address2(street_address2)
        self.edit_city(city)
        self.edit_state_or_province(state_or_province)
        self.edit_postal_code(postal_code)
        self.edit_country(country)
        self.click_submit_button()
