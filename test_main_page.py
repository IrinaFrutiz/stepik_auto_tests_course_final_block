from pages.login_page import LoginPage
from pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_should_be_login_page(browser, language):
    link = f'https://selenium1py.pythonanywhere.com/{language}/accounts/login/'
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()



