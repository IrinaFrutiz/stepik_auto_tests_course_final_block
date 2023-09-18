import allure
import pytest
from pages.locators import BasePageLocators
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.basket_page import BasketPage
# import conftest


@pytest.mark.login_guest
@allure.feature("LoginFromMainPage")
class TestLoginFromMainPage:
    @allure.title("Check go to login page")
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    @allure.title("Check see login link")
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


@allure.title("Check guest_should_be_login_page")
def test_guest_should_be_login_page(browser):
    link = f'https://selenium1py.pythonanywhere.com/accounts/login/'
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()


@allure.title("Check guest_cant_see_product_in_basket_opened_from_main_page")
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = LoginPage(browser, link)
    page.open()
    page.go_to_view_basket()
    basket = BasketPage(browser, link)
    basket.check_basket_is_empty()
    basket.check_text_that_basket_is_empty()
