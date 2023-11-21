from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_LINK_INVALID = (By.ID, "login_link_inc")
    VIEW_BASKET = (By.XPATH, '//a[contains(text(), "View basket")]')
    TOTAL = (By.CSS_SELECTOR, "#basket_formset > div")
    EMPTY_LINK = (By.ID, 'content_inner')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators:
    LOG_IN_FORM = (By.ID, "login_form")
    LOG_IN_EMAIL = (By.ID, "id_login-username")
    LOG_IN_PASSWORD = (By.ID, "id_login-password")
    LOG_IN_BUTTON = (By.NAME, "login_submit")

    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.NAME, 'registration_submit')

    LOGIN_BUTTON_TOP = (By.ID, 'login_link')
    LOGOUT_BUTTON = (By.ID, 'logout_link')


class ProductPageLocators:
    PRODUCT_ADD_TO_BASKET = (By.XPATH, '//button[@value="Add to basket"]')
    PRODUCT_BOOK_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    PRODUCT_BASKET_PRICE = (By.CSS_SELECTOR, 'div.alertinner > p > strong')
    PRODUCT_NAME_FROM_BOOK = (By.CSS_SELECTOR, 'ul.breadcrumb > li.active')
    PRODUCT_NAME = (By.TAG_NAME, 'h1')
    PRODUCT_ADDED_TO_BASKET = (By.XPATH, '(//div[@class="alertinner "])[1]')
