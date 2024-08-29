import allure
import pytest
from base.base_test import BaseTest


@pytest.mark.login_guest
@allure.feature("Check Login Page by Guest")
class TestLoginFromMainPage(BaseTest):
    @allure.title("Check go to login page by guest")
    @allure.severity("Critical")
    def test_guest_can_go_to_login_page(self):
        link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        self.base_page.open(link)
        self.base_page.go_to_login_page()
        self.login_page.should_be_login_page()

    @allure.title("Check see login link")
    def test_guest_should_see_login_link(self):
        link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        self.base_page.open(link)
        self.login_page.should_be_login_link()

    @allure.title("Check guest can see login page")
    @allure.severity("Critical")
    def test_guest_should_be_login_page(self):
        link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        self.login_page.open(link)
        self.login_page.should_be_login_page()

    @allure.title("Check guest_cant_see_product_in_basket_opened_from_main_page")
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = 'http://selenium1py.pythonanywhere.com'
        self.login_page.open(link)
        self.login_page.go_to_view_basket()
        self.basket_page.check_basket_is_empty()
        self.basket_page.check_text_that_basket_is_empty()


@allure.feature("Check User")
@pytest.mark.login
class TestsUser(BaseTest):
    @pytest.fixture(scope="function")
    def user_login(self):
        link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        self.base_page.open(link)
        self.login_page.register_new_user(self.data.generate_email())
        self.base_page.should_be_authorized_user()

    @allure.title('User can login, logout and after check login page')
    @allure.severity("Critical")
    def test_user_can_logout(self, user_login):
        link = 'http://selenium1py.pythonanywhere.com'
        self.base_page.open(link)
        self.base_page.user_can_logout()
