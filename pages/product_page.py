import allure
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):

    PRODUCT_ADD_TO_BASKET = ('xpath', '//button[@value="Add to basket"]')
    PRODUCT_BOOK_PRICE = ('css selector', 'p.price_color')
    PRODUCT_BASKET_PRICE = ('css selector', 'div.alertinner > p > strong')
    PRODUCT_NAME_FROM_BOOK = ('css selector', 'ul.breadcrumb > li.active')
    PRODUCT_NAME = ('tag name', 'h1')
    PRODUCT_ADDED_TO_BASKET = ('xpath', '(//div[@class="alertinner "])[1]')

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
        book_name = self.browser.find_element(*self.PRODUCT_NAME)
        book_name_top = self.browser.find_element(*self.PRODUCT_NAME_FROM_BOOK)
        assert book_name.text == book_name_top.text, \
            f"{book_name.text} not {book_name_top.text}"

    @allure.step('add a book to a basket')
    def should_click_to_button_add_to_basket(self):
        button = self.wait.until(EC.element_to_be_clickable(self.PRODUCT_ADD_TO_BASKET))
        button.click()
        assert button, \
            "Can't find button and click Add to basket"

    @allure.step('check sum on the basket and the book')
    def should_be_equal_sum_on_basket_and_book(self):
        sum_basket = self.browser.find_element(*self.PRODUCT_BASKET_PRICE).text
        sum_book = self.browser.find_element(*self.PRODUCT_BOOK_PRICE).text
        assert sum_book == sum_basket,\
            f'{sum_book} is not equal to {sum_basket}'

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
        messages = self.wait.until(EC.visibility_of_element_located(self.PRODUCT_ADDED_TO_BASKET))
        book_name = self.browser.find_element(*self.PRODUCT_NAME)
        expected_message = f"{book_name.text}{languages[language]}"
        assert expected_message in messages.text, \
            f'{messages.text} is not {expected_message}'

    @allure.step('check no message that the book added to the basket')
    def should_not_be_success_message(self):
        assert self.element_is_not_present(self.PRODUCT_ADDED_TO_BASKET), \
            "Success message is presented, but should not be"

    @allure.step("there is no message on the page, because the user don't add the product to the basket")
    def should_no_message_after_adding_product_to_basket(self):
        assert self.element_is_not_present(self.PRODUCT_ADDED_TO_BASKET), \
            "Can't be success message after adding product to the basket"

    @allure.step('check the message(the book added) is disappeared')
    def should_disappeared_massage_after_adding_product_to_basket(self):
        assert self.wait.until(EC.invisibility_of_element_located(self.PRODUCT_ADDED_TO_BASKET)),\
            "The success message don't disappear"
