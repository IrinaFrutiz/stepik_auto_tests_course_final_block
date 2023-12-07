import allure
import pytest
from selenium import webdriver
# Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
# FireFox
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.firefox.options import Options as OptionsFirefox
# Edge
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en-gb',
                     help="Choose language: '--language=en-gb' or '--language=ru'")


@pytest.fixture(scope="function", autouse=True)
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language", default="en-gb")

    if browser_name == "chrome":
        options_chrome = Options()
        options_chrome.add_experimental_option(
            'prefs', {'intl.accept_languages': user_language})
        options_chrome.add_argument("--window-size=1920,1080")
        options_chrome.add_argument("--headless")
        options_chrome.add_argument("--no-sandbox")
        options_chrome.add_argument("--disable-dev-shm-usage")
        browser = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options_chrome)

    elif browser_name == "firefox":
        options_firefox = OptionsFirefox()
        options_firefox.set_preference("intl.accept_languages", user_language)
        options_firefox.add_argument("--window-size=1920,1080")
        options_firefox.add_argument("--headless")
        browser = webdriver.Firefox(
            service=FFService(GeckoDriverManager().install()),
            options=options_firefox)

    elif browser_name == "edge":
        options_edge = EdgeOptions()
        options_edge.add_experimental_option(
            'prefs', {'intl.accept_languages': user_language}
        )
        options_edge.add_argument("--window-size=1920,1080")
        options_edge.add_argument("--headless")
        browser = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()),
            options=options_edge)

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    
    yield browser
    attach = browser.get_screenshot_as_png()
    from datetime import datetime
    allure.attach(attach, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)
    browser.quit()
