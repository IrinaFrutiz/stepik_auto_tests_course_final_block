from pages.base_page import BasePage
from pages.locators import BasePageLocators


class BasketPage(BasePage):
    locators = BasePageLocators
    def check_basket_is_empty(self):
        assert self.is_not_element_present(self.locators.TOTAL), \
        "Basket is not empty"

    def check_text_that_basket_is_empty(self):
        languages = {
            "ar": "سلة التسوق فارغة",
            "ca": "La seva cistella està buida.",
            "cs": "Váš košík je prázdný.",
            "da": "Din indkøbskurv er tom.",
            "de": "Ihr Warenkorb ist leer.",
            "en-gb": "Your basket is empty.",
            "en": "Your basket is empty.",
            "el": "Το καλάθι σας είναι άδειο.",
            "es": "Tu carrito esta vacío.",
            "fi": "Korisi on tyhjä",
            "fr": "Votre panier est vide.",
            "it": "Il tuo carrello è vuoto.",
            "ko": "장바구니가 비었습니다.",
            "nl": "Je winkelmand is leeg",
            "pl": "Twój koszyk jest pusty.",
            "pt": "O carrinho está vazio.",
            "pt-br": "Sua cesta está vazia.",
            "ro": "Cosul tau este gol.",
            "ru": "Ваша корзина пуста",
            "sk": "Váš košík je prázdny",
            "uk": "Ваш кошик пустий.",
            "zh-cn": "Your basket is empty.",
        }
        language = self.browser.execute_script(
            "return window.navigator.userLanguage || window.navigator.language")
        message = self.browser.find_element(*BasePageLocators.EMPTY_LINK)
        assert languages[language] in message.text, \
        f'{message.text} is not contain {languages[language]}'
