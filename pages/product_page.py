from pages.base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_promo_in_url()
        self.should_be_button_add_to_basket()
        # self.should_click_to_button_add_to_basket()

    def should_be_promo_in_url(self):
        url = self.browser.current_url
        assert "?promo=newYear" in url,\
        f"{url} don't contain ?promo=newYear"

    def should_be_button_add_to_basket(self):
        batton = self.is_element_present(*ProductPageLocators.PRODUCT_ADD_TO_BASKET)
        assert batton,\
        f"Can't find button Add to basket"

    def should_click_to_button_add_to_basket(self):
        batton = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_TO_BASKET)
        batton.click()
        assert batton.click(), \
            f"Can't find button and click Add to basket"

    def should_be_equel_sum_on_basket_and_book(self):
        sum_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_BASKET_PRICE)
        sum_book = self.browser.find_element(*ProductPageLocators.PRODUCT_BOOK_PRICE)
        assert sum_book.text == sum_basket.text,\
        f'{sum_book.text} is not equal to {sum_basket.text}'


    def should_check_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        book_name_ = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_FROM_BOOK)
        assert book_name_.text == book_name.text, \
        f'{book_name_.text} is not equal to {book_name.text}'
