import allure
from base.base_page import BasePage


class BasketPage(BasePage):

    TOTAL = ('css selector', '#basket_formset > div')
    EMPTY_LINK = ('id', 'content_inner')

    @allure.step('check the basket is empty')
    def check_basket_is_empty(self):
        assert self.element_is_not_present(self.TOTAL), \
            "Basket is not empty"

    @allure.step('check the text that the basket is empty')
    def check_text_that_basket_is_empty(self):
        languages = {
            "ar": "سلة التسوق فارغة",
            "ca": "La seva cistella està buida.",
            "cs": "Váš košík je prázdný.",
            "da": "Din indkøbskurv er tom.",
            "de": "Ihr Warenkorb ist leer.",
            "en-gb": "Your basket is empty.",
            "en-US": "Your basket is empty.",
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
        message = self.browser.find_element(*self.EMPTY_LINK)
        assert languages[language] in message.text, \
            f'{message.text} is not contain {languages[language]}'
