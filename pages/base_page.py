import math
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.locators import BasePageLocators


class BasePage:
    locators = BasePageLocators

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, value):
        try:
            self.browser.find_element(value)
        except NoSuchElementException:
            return False
        return True

    def element_is_visible(self, value, timeout=10):
        return wait(self.browser, timeout).until(EC.visibility_of_element_located(value))

    def is_not_element_present(self, locator, timeout=4):
        try:
            wait(self.browser, timeout).until(EC.presence_of_element_located((locator)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, value, timeout=4):
        try:
            wait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located(value))
        except TimeoutException:
            return False

        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(int(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
        print("Test go_to_login_page Passed")

    def should_be_login_link(self):
        assert self.browser.find_element(*BasePageLocators.LOGIN_LINK),\
            "Login link is not presented"

    def go_to_view_basket(self):
        button = self.browser.find_element(*BasePageLocators.VIEW_BASKET)
        button.click()

    def should_be_authorized_user(self):
        assert self.element_is_visible(self.locators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"
