import allure
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    locators = LoginPageLocators

    @allure.step('check a login page')
    def should_be_login_page(self):
        self.should_be_login_button_top()
        self.can_click_login_button_top()
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    @allure.step('shoud be login button at the top of the page')
    def should_be_login_button_top(self):
        self.element_is_visible(self.locators.LOGIN_BUTTON_TOP)

    @allure.step('can ckick on login at the top of the page')
    def can_click_login_button_top(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON_TOP).click()
    @allure.step('check login url on a page')
    def should_be_login_url(self):
        url = self.browser.current_url
        assert "/accounts/login/" in url,\
            f'{url} do not contain /accounts/login/'

    @allure.step('check a login form')
    def should_be_login_form(self):
        assert self.element_is_visible(self.locators.LOG_IN_FORM), \
            "Login form is not presented"

    @allure.step('check a register form')
    def should_be_register_form(self):
        assert self.element_is_visible(self.locators.REGISTER_FORM), \
            "Register form is not presented"

    @allure.step('register a new user')
    def register_new_user(self, email, password='Password123Q'):
        with allure.step("filling fields"):
            self.element_is_visible(self.locators.REGISTER_EMAIL).send_keys(email)
            self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
            self.browser.find_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD).send_keys(password)
        with allure.step('click register button'):
            self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

    @allure.step('user can click logout button')
    def user_can_logout(self):
        self.element_is_visible(self.locators.LOGOUT_BUTTON)
        self.browser.find_element(*LoginPageLocators.LOGOUT_BUTTON).click()
