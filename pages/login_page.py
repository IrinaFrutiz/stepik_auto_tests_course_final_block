from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    locators = LoginPageLocators
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert  "/accounts/login/" in url,\
        f'{url} do not contain /accounts/login/'

    def should_be_login_form(self):
        assert self.element_is_visible(self.locators.LOG_IN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.element_is_visible(self.locators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password='Password123Q'):
        add_email = self.element_is_visible(self.locators.REGISTER_EMAIL)
        add_pass = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        add_pass_conf = self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD)
        add_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        add_email.send_keys(email)
        add_pass.send_keys(password)
        add_pass_conf.send_keys(password)
        add_button.click()