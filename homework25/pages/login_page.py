"""All methods for Login page."""

from homework25.pages.base_page import BasePage
from homework24.locators.login_page import LoginPageLocators


class LoginPage(BasePage):
    """Class Login Page."""

    def enter_email(self, email):
        """ Enter email."""
        email_input = self.find_element(LoginPageLocators.LOGIN_EMAIL_INPUT)
        email_input.send_keys(email)

    def enter_password(self, password):
        """Enter password."""
        password_input = (self.find_element
                          (LoginPageLocators.LOGIN_PASSWORD_INPUT))
        password_input.send_keys(password)

    def click_submit_button(self):
        """Click on submit button."""
        submit_button = (self.find_element
                         (LoginPageLocators.LOGIN_SUBMIT_BUTTON))
        submit_button.click()

    def login(self, email, password):
        """Login page is completed."""
        self.enter_email(email)
        self.enter_password(password)
        self.click_submit_button()
