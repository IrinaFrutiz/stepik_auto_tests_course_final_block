import allure
import pytest
from faker import Faker
from pages.base_page import BasePage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
import time


@allure.title("Check guest_can_add_product_to_basket_new_year")
@pytest.mark.parametrize("link", [
    "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019",
    "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"])
def test_guest_can_add_product_to_basket_new_year(browser, link):
    page = ProductPage(browser, link)
    page.open()
    time.sleep(10)
    page.should_be_product_page()
    page.should_click_to_button_add_to_basket()
    page.solve_quiz_and_get_code()
    page.check_message_book_added_to_basket()
    page.should_be_equal_sum_on_basket_and_book()


@allure.title("Check guest_can_add_product_to_basket")
@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
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


@allure.title("Check guest_cant_see_success_message_after_adding_product_to_basket")
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.should_click_to_button_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_no_message_after_adding_product_to_basket()


@allure.title("Check guest_cant_see_success_message")
def test_guest_cant_see_success_message(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.should_no_message_after_adding_product_to_basket()


@allure.title("Check message_disappeared_after_adding_product_to_basket")
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.should_click_to_button_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_disappeared_massage_after_adding_product_to_basket()


@allure.title("Check guest_should_see_login_link_on_product_page")
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@allure.title("Check guest_can_go_to_login_page_from_product_page")
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@allure.title("Check guest_cant_see_product_in_basket_opened_from_product_page")
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_view_basket()
    basket = BasketPage(browser, link)
    basket.check_basket_is_empty()
    basket.check_text_that_basket_is_empty()


@allure.title('Faild test')
@allure.severity('trivial')
def test_fail_test():
    assert 2 == 1, \
        f"Failed test 2 != 1"


@allure.feature("Check UserAddToBasketFromProductPage")
@pytest.mark.login
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        fake = Faker()
        link = 'https://selenium1py.pythonanywhere.com/accounts/login/'
        email = fake.email()
        self.login = LoginPage(browser, link)
        self.login.open()
        self.login.register_new_user(email)
        self.login = BasePage(browser, link)
        self.login.should_be_authorized_user()

    @allure.title("Check user can't see success message")
    def test_user_cant_see_success_message(self, browser):
        link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        page = ProductPage(browser, link)
        page.open()
        page.should_no_message_after_adding_product_to_basket()

    @allure.title("Check user can add a product to the basket")
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_page()
        page.should_click_to_button_add_to_basket()
        page.solve_quiz_and_get_code()
        page.check_message_book_added_to_basket()
        page.should_be_equal_sum_on_basket_and_book()
