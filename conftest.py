import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en-gb',
                     help="Choose language: '--language=en-gb' or '--language=ru'")

@pytest.fixture(scope="function")
def browser(request):
        browser_name = request.config.getoption("browser_name")
        user_language = request.config.getoption("language", default="en-gb")
        chrome_options = Options()
        # chrome_options.add_argument("--prefs=intl.accept_languages=en-gb")
        chrome_options.add_experimental_option(
            'prefs', {'intl.accept_languages': user_language})
        # chrome_options.add_argument(f"--language={user_language}")

        options_firefox = OptionsFirefox()
        options_firefox.set_preference("intl.accept_languages", user_language)
        browser = None
        if browser_name == "chrome":
            print("\nstart chrome browser for test..")
            browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

        elif browser_name == "firefox":
            print("\nstart firefox browser for test..")
            browser = webdriver.Firefox(options=options_firefox)
        else:
            raise pytest.UsageError("--browser_name should be chrome or firefox")
        # if you need open browser on all window
        # browser.maximize_window()
        yield browser
        print(f"\nquit {browser_name}..")
        browser.quit()

# supported_languages = {
#     'ar',
#     'ca',
#     'cs',
#     'da',
#     'de',
#     'en-gb',
#     'el',
#     'es',
#     'fi',
#     'fr',
#     'it',
#     'ko',
#     'nl',
#     'pl',
#     'pt',
#     'pt-br',
#     'ro',
#     'ru',
#     'sk',
#     'uk',
#     'zh-hans'
# }
# @pytest.fixture(scope="function")
# def language(request):
#     language = request.config.getoption("language")
#     if language in supported_languages:
#         return language
#     else:
#         raise pytest.UsageError("Choose the right language!")