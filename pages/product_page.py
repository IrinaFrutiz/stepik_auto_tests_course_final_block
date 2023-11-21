import allure

from pages.base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    locators = ProductPageLocators()

    @allure.step('check a product page')
    def should_be_product_page(self):
        self.should_be_promo_in_url()
        self.should_check_book_name()
        self.should_not_be_success_message()

    @allure.step('check promo in an url')
    def should_be_promo_in_url(self):
        url = self.browser.current_url
        assert "?promo=newYear" in url,\
            f"{url} don't contain ?promo=newYear"

    @allure.step('check book names matching')
    def should_check_book_name(self):
        BOOK_NAME = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        BOOK_NAME_TOP = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_FROM_BOOK)
        assert BOOK_NAME.text == BOOK_NAME_TOP.text, \
            f"{BOOK_NAME.text} not {BOOK_NAME_TOP.text}"

    @allure.step('add a book to a basket')
    def should_click_to_button_add_to_basket(self):
        BUTTON = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_TO_BASKET)
        BUTTON.click()
        assert BUTTON, \
            f"Can't find button and click Add to basket"

    @allure.step('check sum on the basket and the book')
    def should_be_equal_sum_on_basket_and_book(self):
        SUM_BASKET = self.browser.find_element(*ProductPageLocators.PRODUCT_BASKET_PRICE).text
        SUM_BOOK = self.browser.find_element(*ProductPageLocators.PRODUCT_BOOK_PRICE).text
        assert SUM_BOOK == SUM_BASKET,\
            f'{SUM_BOOK} is not equal to {SUM_BASKET}'

    @allure.step('check a message that the book added to the basket')
    def check_message_book_added_to_basket(self):
        languages = {
            "ar": " has been added to your basket.",
            "ca": " s'ha afegit a la seva cistella.",
            "cs": " byla přidána do vašeho košíku.",
            "da": " er lagt i din indkøbskurv.",
            "de": " wurde Ihrem Warenkorb hinzugefügt.",
            "en-gb": " has been added to your basket.",
            "en-US": " has been added to your basket.",
            "en": " has been added to your basket.",
            "el": " has been added to your basket.",
            "es": " ha sido añadido al carrito.",
            "fi": " lisätty koriisi.",
            "fr": " a été ajouté à votre panier.",
            "it": " byl přidán do vašeho košíku.",
            "ko": "이(가) 장바구니에 추가되었습니다.",
            "nl": " is toegevoegd aan je winkelmand.",
            "pl": " został dodany do koszyka.",
            "pt": " foi adicionado ao seu carrinho.",
            "pt-br": " foi adicionado à sua cesta.",
            "ro": " a fost adaugat in cos.",
            "ru": " был добавлен в вашу корзину.",
            "sk": " bol pridaný do košíka.",
            "uk": " було додано до Вашого кошику.",
            "zh-cn": " has been added to your basket.",
        }
        language = self.browser.execute_script(
            "return window.navigator.userLanguage || window.navigator.language")
        MESSAGES = self.element_is_visible(self.locators.PRODUCT_ADDED_TO_BASKET)
        BOOK_NAME = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        EXPECTED_MESSAGE = f"{BOOK_NAME.text}{languages[language]}"
        assert EXPECTED_MESSAGE in MESSAGES.text, \
            f'{MESSAGES.text} is not {EXPECTED_MESSAGE}'

    @allure.step('check no message that the book added to the basket')
    def should_not_be_success_message(self):
        assert self.is_not_element_present(self.locators.PRODUCT_ADDED_TO_BASKET), \
            "Success message is presented, but should not be"

    @allure.step("there is no message on the page, because the user don't add the product to the basket")
    def should_no_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(self.locators.PRODUCT_ADDED_TO_BASKET), \
            f"Can't be success message after adding product to the basket"

    @allure.step('check the message(the book added) is disappeared')
    def should_disappeared_massage_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET), \
            f"The success message don't disappear"
