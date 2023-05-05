from pages.base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    locators = ProductPageLocators()
    def should_be_product_page(self):
        self.should_be_promo_in_url()
        self.should_check_book_name()
        self.should_not_be_success_message()

    def should_be_promo_in_url(self):
        url = self.browser.current_url
        assert "?promo=newYear" in url,\
        f"{url} don't contain ?promo=newYear"

    def should_check_book_name(self):
        book_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        book_name_top = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_FROM_BOOK)
        assert book_name.text == book_name_top.text, \
        f"{book_name.text} not {book_name_top.text}"

    def should_click_to_button_add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_TO_BASKET)
        button.click()
        assert button, \
            f"Can't find button and click Add to basket"

    def should_be_equal_sum_on_basket_and_book(self):
        sum_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_BASKET_PRICE)
        sum_book = self.browser.find_element(*ProductPageLocators.PRODUCT_BOOK_PRICE)
        assert sum_book.text == sum_basket.text,\
        f'{sum_book.text} is not equal to {sum_basket.text}'

    def check_message_book_added_to_basket(self):
        languages = {
            "ar": " has been added to your basket.",
            "ca": " s'ha afegit a la seva cistella.",
            "cs": " byla přidána do vašeho košíku.",
            "da": " er lagt i din indkøbskurv.",
            "de": " wurde Ihrem Warenkorb hinzugefügt.",
            "en-gb": " has been added to your basket.",
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
        messages = self.element_is_visible(self.locators.PRODUCT_ADDED_TO_BASKET)
        book_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        expected_message = f"{book_name.text}{languages[language]}"
        assert expected_message in (messages.text), \
        f'{messages.text} is not {expected_message}'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(self.locators.PRODUCT_ADDED_TO_BASKET), \
            "Success message is presented, but should not be"

    def should_no_massage_after_adding_product_to_basket(self):
        assert self.is_not_element_present(self.locators.PRODUCT_ADDED_TO_BASKET), \
            f"Can't be success message after adding product to the basket"

    def should_desappeared_massage_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET), \
        f"The success message don't desappear"


