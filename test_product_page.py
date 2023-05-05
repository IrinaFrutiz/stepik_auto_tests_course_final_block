import pytest
from pages.base_page import BasePage
from pages.basket_page import BasketPage
from pages.locators import ProductPageLocators
from pages.login_page import LoginPage
from pages.product_page import ProductPage
import time


@pytest.mark.parametrize("link", ["https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019",
                                "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
                                    ])
def test_guest_can_add_product_to_basket_new_year(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.should_click_to_button_add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_message_book_added_to_basket()
    page.should_be_equal_sum_on_basket_and_book()

@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
                                  ])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_click_to_button_add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_message_book_added_to_basket()
    page.should_be_equal_sum_on_basket_and_book()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.should_click_to_button_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_no_massage_after_adding_product_to_basket()

def test_guest_cant_see_success_message(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.should_no_massage_after_adding_product_to_basket()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.should_click_to_button_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_desappeared_massage_after_adding_product_to_basket()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_view_basket()
    basket = BasketPage(browser, link)
    basket.check_basket_is_empty()
    basket.check_text_that_basket_is_empty()

@pytest.mark.login
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'https://selenium1py.pythonanywhere.com/ru/accounts/login/'
        email = str(time.time()) + "@fakemail.org"
        self.login = LoginPage(browser, link)
        self.login.open()
        self.login.register_new_user(email)
        self.login = BasePage(browser, link)
        self.login.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        page = ProductPage(browser, link)
        page.open()
        page.should_no_massage_after_adding_product_to_basket()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket_new_year(self, browser):
        link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_page()
        page.should_click_to_button_add_to_basket()
        page.solve_quiz_and_get_code()
        page.check_message_book_added_to_basket()
        page.should_be_equal_sum_on_basket_and_book()


