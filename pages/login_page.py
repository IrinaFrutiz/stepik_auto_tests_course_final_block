import allure
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):

    LOG_IN_FORM = ('id', 'login_form')
    LOG_IN_EMAIL = ('id', 'id_login-username')
    LOG_IN_PASSWORD = ('id', 'id_login-password')
    LOG_IN_BUTTON = ('name', 'login_submit')

    REGISTER_FORM = ('id', 'register_form')
    REGISTER_EMAIL = ('id', 'id_registration-email')
    REGISTER_PASSWORD = ('id', 'id_registration-password1')
    REGISTER_CONFIRM_PASSWORD = ('id', 'id_registration-password2')
    REGISTER_BUTTON = ('name', 'registration_submit')

    @allure.step('check a login page')
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    @allure.step('check login url on a page')
    def should_be_login_url(self):
        assert self.wait.until(EC.url_contains("/accounts/login/")),\
            f'Browser URL do not contain /accounts/login/'

    @allure.step('check a login form')
    def should_be_login_form(self):
        assert self.wait.until(EC.visibility_of_element_located(self.LOG_IN_FORM)), \
            "Login form is not presented"

    @allure.step('check a register form')
    def should_be_register_form(self):
        assert self.wait.until(EC.visibility_of_element_located(self.REGISTER_FORM)), \
            "Register form is not presented"

    @allure.step('register a new user')
    def register_new_user(self, email, password='Password123Q'):
        with allure.step("filling fields"):
            self.wait.until(EC.visibility_of_element_located(self.REGISTER_EMAIL)).send_keys(email)
            self.browser.find_element(*self.REGISTER_PASSWORD).send_keys(password)
            self.browser.find_element(*self.REGISTER_CONFIRM_PASSWORD).send_keys(password)
        with allure.step('click register button'):
            self.browser.find_element(*self.REGISTER_BUTTON).click()
