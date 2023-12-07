import allure
import pytest
from faker import Faker

from base.base_test import BasketPage, LoginPage, MainPage, BasePage


@pytest.mark.login_guest
@allure.feature("LoginFromMainPage")
class TestLoginFromMainPage:
    @allure.title("Check go to login page by guest")
    @allure.severity(severity_level="CRITICAL")
    def test_guest_can_go_to_login_page(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    @allure.title("Check see login link")
    def test_guest_should_see_login_link(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    @allure.title("Check guest can see login page")
    @allure.severity(severity_level="CRITICAL")
    def test_guest_should_be_login_page(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_page()

    @allure.title("Check guest_cant_see_product_in_basket_opened_from_main_page")
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = 'http://selenium1py.pythonanywhere.com'
        page = LoginPage(browser, link)
        page.open()
        page.go_to_view_basket()
        basket = BasketPage(browser, link)
        basket.check_basket_is_empty()
        basket.check_text_that_basket_is_empty()


@allure.feature("Check User")
@pytest.mark.login
class TestsByUser:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        fake = Faker()
        email = fake.name() + fake.email()
        link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        self.login = LoginPage(browser, link)
        self.login.open()
        self.login.register_new_user(email)
        self.login = BasePage(browser, link)
        self.login.should_be_authorized_user()

    @allure.title('User can login, logout and after check login page')
    @allure.severity(severity_level="CRITICAL")
    def test_user_can_logout(self, browser):
        link = 'http://selenium1py.pythonanywhere.com'
        page = BasePage(browser, link)
        page.user_can_logout()
