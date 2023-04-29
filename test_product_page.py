import time
from telnetlib import EC

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.locators import ProductPageLocators
from pages.product_page import ProductPage


links = [
    "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
]

@pytest.mark.parametrize("product", links)
def test_guest_can_add_product_to_basket(browser, product: str) -> None:
    link = product
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.should_click_to_button_add_to_basket()
    page.solve_quiz_and_get_code


@pytest.mark.parametrize("product", links)
def test_guest_check_data(browser, product: str) -> None:
    link = product
    page = ProductPage(browser, link)
    page.open()
    page.should_check_book_name()

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
    page.should_be_equel_sum_on_basket_and_book
    # time.sleep(50)



