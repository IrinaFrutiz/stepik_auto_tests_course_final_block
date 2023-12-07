import pytest

from pages.login_page import LoginPage
from base.base_page import BasePage
from pages.basket_page import BasketPage
from pages.product_page import ProductPage
from pages.main_page import MainPage

class BaseTest:
    login_page: LoginPage
    base_page: BasePage
    basket_page: BasketPage
    product_page: ProductPage
    main_page: MainPage


    @pytest.fixture(autouse=True)
    def setup(self, request, browser):
        request.cls.browser = browser
        request.cls.login_page = LoginPage(browser)
        request.cls.base_page = BasePage(browser)
        request.cls.basket_page = BasketPage(browser)
        request.cls.product_page = ProductPage(browser)
        request.cls.main_page = MainPage(browser)
