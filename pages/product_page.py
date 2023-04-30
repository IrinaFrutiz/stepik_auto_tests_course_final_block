from pages.base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    locators = ProductPageLocators()
    def should_be_product_page(self):
        self.should_be_promo_in_url()
        self.should_be_button_add_to_basket()
        self.should_check_book_name()

    def should_be_promo_in_url(self):
        url = self.browser.current_url
        assert "?promo=newYear" in url,\
        f"{url} don't contain ?promo=newYear"

    def should_be_button_add_to_basket(self):
        batton = self.is_element_present(self.locators.PRODUCT_ADD_TO_BASKET)
        assert batton,\
        f"Can't find button Add to basket"

    def should_click_to_button_add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_TO_BASKET)
        button.click()
        assert button, \
            f"Can't find button and click Add to basket"

    def should_be_equel_sum_on_basket_and_book(self):
        sum_basket = self.browser.element_is_visible(self.locators.PRODUCT_BASKET_PRICE)
        sum_book = self.browser.find_element(*ProductPageLocators.PRODUCT_BOOK_PRICE)
        assert sum_book.text == sum_basket.text,\
        f'{sum_book.text} is not equal to {sum_basket.text}'


    def should_check_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        book_name_top = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_FROM_BOOK)
        assert book_name.text == book_name_top.text, \
        f"{book_name.text} not {book_name_top.text}"


    def check_message_book_added_to_basket(self):
        messages = self.element_is_visible(self.locators.PRODUCT_ADDED_TO_BASKET)
        book_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        expected_message = f"{book_name.text} has been added to your basket."
        assert (messages.text) == expected_message, \
        f'{messages.text} is not {expected_message}'


