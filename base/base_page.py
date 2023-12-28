import math

import allure
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    LOGIN_LINK = ('id', 'login_link')
    LOGOUT_BUTTON = ('id', 'logout_link')
    VIEW_BASKET = ('xpath', '//a[contains(text(), "View basket")]')
    USER_ICON = ('css selector', '.icon-user')

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 20, poll_frequency=0.5)

    @allure.step('open the URL')
    def open(self, url):
        self.browser.get(url)

    @allure.step('check that element is not present on the page')
    def element_is_not_present(self, value):
        try:
            self.wait.until(EC.presence_of_element_located(value))
        except TimeoutException:
            return True

        return False

    @allure.step('check that element disappeared after 15 seconds')
    def is_disappeared(self, value):
        try:
            self.wait.until_not(EC.presence_of_element_located(value))
        except TimeoutException:
            return False

        return True

    @allure.step('the quiz')
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(int(x))))))
        with allure.step('solving the quiz'):
            alert.send_keys(answer)
            alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    @allure.step('go to login page')
    def go_to_login_page(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_LINK)).click()

    @allure.step('check the login link')
    def should_be_login_link(self):
        assert self.wait.until(EC.visibility_of_element_located(self.LOGIN_LINK)),\
            "Login link is not presented"

    @allure.step('check a basket button')
    def go_to_view_basket(self):
        with allure.step('click a basket button'):
            self.wait.until(EC.element_to_be_clickable(self.VIEW_BASKET)).click()

    @allure.step('check the user is authorized')
    def should_be_authorized_user(self):
        assert self.wait.until(EC.element_to_be_clickable(self.USER_ICON)),\
            "User icon is not presented probably unauthorised user"

    @allure.step('user can logout')
    def user_can_logout(self):
        assert self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BUTTON)), \
            "User can't logout"
