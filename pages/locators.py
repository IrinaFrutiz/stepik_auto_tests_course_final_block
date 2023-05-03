from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators:
    LOG_IN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOG_IN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOG_IN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOG_IN_BUTTON = (By.NAME, "login_submit")

    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators:
    PRODUCT_ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_BASKET_PRICE = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/text()')
    PRODUCT_NAME_FROM_BOOK = (By.CSS_SELECTOR, '#default > div.container-fluid.page > div > ul > li.active')
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_ADDED_TO_BASKET = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div')
