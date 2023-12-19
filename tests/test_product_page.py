import allure
import pytest
from base.base_test import BaseTest


class TestGuest(BaseTest):
    @allure.title("Check guest_can_add_product_to_basket_new_year")
    @pytest.mark.parametrize("link", [
        "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019",
        "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"])
    def test_guest_can_add_product_to_basket_new_year(self, link):
        self.product_page.open(link)
        self.product_page.should_be_product_page()
        self.product_page.should_click_to_button_add_to_basket()
        self.product_page.solve_quiz_and_get_code()
        self.product_page.check_message_book_added_to_basket()
        self.product_page.should_be_equal_sum_on_basket_and_book()

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
    def test_guest_can_add_product_to_basket(self, link):
        self.product_page.open(link)
        self.product_page.should_click_to_button_add_to_basket()
        self.product_page.solve_quiz_and_get_code()
        self.product_page.check_message_book_added_to_basket()
        self.product_page.should_be_equal_sum_on_basket_and_book()

    @allure.title("Check guest_cant_see_success_message_after_adding_product_to_basket")
    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
        link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        self.product_page.open(link)
        self.product_page.should_click_to_button_add_to_basket()
        self.product_page.solve_quiz_and_get_code()
        self.product_page.should_no_message_after_adding_product_to_basket()

    @allure.title("Check guest_cant_see_success_message")
    def test_guest_cant_see_success_message(self):
        link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        self.product_page.open(link)
        self.product_page.should_no_message_after_adding_product_to_basket()

    @allure.title("Check message_disappeared_after_adding_product_to_basket")
    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self):
        link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        self.product_page.open(link)
        self.product_page.should_click_to_button_add_to_basket()
        self.product_page.solve_quiz_and_get_code()
        self.product_page.should_disappeared_massage_after_adding_product_to_basket()

    @allure.title("Check guest_should_see_login_link_on_product_page")
    def test_guest_should_see_login_link_on_product_page(self):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
        self.product_page.open(link)
        self.product_page.should_be_login_link()

    @allure.title("Check guest_can_go_to_login_page_from_product_page")
    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self):
        link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        self.product_page.open(link)
        self.product_page.go_to_login_page()

    @allure.title("Check guest_cant_see_product_in_basket_opened_from_product_page")
    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self):
        link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        self.product_page.open(link)
        self.product_page.go_to_view_basket()
        self.basket_page.check_basket_is_empty()
        self.basket_page.check_text_that_basket_is_empty()

    @allure.title('Failed test')
    @allure.severity('trivial')
    def test_fail_test(self):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-age-of-the-pussyfoot_89/'
        self.product_page.open(link)
        self.product_page.should_check_book_name()
        self.product_page.should_click_to_button_add_to_basket()
        self.product_page.should_click_to_button_add_to_basket()
        self.product_page.should_be_equal_sum_on_basket_and_book()


@allure.feature("Check UserAddToBasketFromProductPage")
@pytest.mark.login
class TestUserAddToBasketFromProductPage(BaseTest):
    @pytest.fixture(scope="function")
    def setup_test(self):
        link = 'https://selenium1py.pythonanywhere.com/accounts/login/'
        self.base_page.open(link)
        self.login_page.register_new_user(self.data.email)
        self.base_page.should_be_authorized_user()

    @allure.title("Check user can't see success message")
    def test_user_cant_see_success_message(self):
        link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        self.base_page.open(link)
        self.product_page.should_no_message_after_adding_product_to_basket()

    @allure.title("Check user can add a product to the basket")
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self):
        link = 'https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        self.product_page.open(link)
        self.product_page.should_be_product_page()
        self.product_page.should_click_to_button_add_to_basket()
        self.product_page.solve_quiz_and_get_code()
        self.product_page.check_message_book_added_to_basket()
        self.product_page.should_be_equal_sum_on_basket_and_book()
