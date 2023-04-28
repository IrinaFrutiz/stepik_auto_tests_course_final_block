import math

from selenium.common import NoAlertPresentException

from pages.base_page import BasePage
from pages.locators import ProductPageLocators
from pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket(browser, language):
    link = f'http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    batton = browser.find_element(*ProductPageLocators.PRODUCT_ADD_TO_BASKET)
    batton.click()
    # alert = BasePage(browser)
    # alert.solve_quiz_and_get_code()
    alert = browser.switch_to.alert
    x = alert.text.split(" ")[2]
    answer = str(math.log(abs((12 * math.sin(int(x))))))
    alert.send_keys(answer)
    alert.accept()
    try:
        alert = browser.switch_to.alert
        alert_text = alert.text
        print(f"Your code: {alert_text}")
        alert.accept()
    except NoAlertPresentException:
        print("No second alert presented")



