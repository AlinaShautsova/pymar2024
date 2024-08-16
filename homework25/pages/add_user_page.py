"""All methods for Add user page."""

from homework25.pages.base_page import BasePage
from homework24.locators.add_user_page import AddUserPageLocators


class AddUserPage(BasePage):
    """Class Add user."""

    def enter_first_name(self, first_name):
        """Enter first name."""
        first_name_input = (self.find_element
                            (AddUserPageLocators.ADD_FIRSTNAME_INPUT))
        first_name_input.send_keys(first_name)

    def enter_last_name(self, last_name):
        """Enter last name."""
        last_name_input = (self.find_element
                           (AddUserPageLocators.ADD_LASTNAME_INPUT))
        last_name_input.send_keys(last_name)

    def enter_email(self, email):
        """Enter email."""
        email_input = self.find_element(AddUserPageLocators.ADD_EMAIL_INPUT)
        email_input.send_keys(email)

    def enter_password(self, password):
        """Enter password."""
        password_input = (self.find_element
                          (AddUserPageLocators.ADD_PASSWORD_INPUT))
        password_input.send_keys(password)

    def click_submit_button(self):
        """Click on submit button."""
        submit_button = self.find_element(AddUserPageLocators.SUBMIT_BUTTON)
        submit_button.click()

    def add_user(self, first_name, last_name, email, password):
        """Adding a user is completed."""
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email)
        self.enter_password(password)
        self.click_submit_button()
