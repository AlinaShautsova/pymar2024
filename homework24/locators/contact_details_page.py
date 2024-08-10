"""This module contains locators for Contact Details page."""


class ContactDetailsPageLocators:
    """The class contains locators for contact details page."""
    # spans
    FIRST_NAME_SPAN = '//span[@id="firstName"]'
    LAST_NAME_SPAN = '//span[@id="lastName"]'
    BIRTHDATE_SPAN = '//span[@id="birthdate"]'
    EMAIL_SPAN = '//span[@id="email"]'
    PHONE_SPAN = '//span[@id="phone"]'
    STREET1_SPAN = '//span[@id="street1"]'
    STREET2_SPAN = '//span[@id="street2"]'
    CITY_SPAN = '//span[@id="city"]'
    STATE_PROVINCE_SPAN = '//span[@id="stateProvince"]'
    POSTAL_CODE_SPAN = '//span[@id="postalCode"]'
    COUNTRY_SPAN = '//span[@id="country"]'

    # buttons
    EDIT_CONTACT_BUTTON = '//button[@id="edit-contact"]'
    DELETE_CONTACT_BUTTON = '//button[@id="delete"]'
    RETURN_TO_CONTACT_LIST_BUTTON = '//button[@id="return"]'
    LOGOUT_BUTTON = '//button[@id="logout"]'
