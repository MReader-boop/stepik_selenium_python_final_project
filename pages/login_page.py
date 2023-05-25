from .base_page import BasePage
from .locators import LoginPagelocators as Locators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url()
        assert '/accounts/login/' in current_url, 'Not login page url!'

    def should_be_login_form(self):
        assert self.is_element_present(*Locators.LOGIN_FORM), 'No login form!'

    def should_be_register_form(self):
        assert self.is_element_present(*Locators.REGISTRATION_FORM), 'No registration form!'