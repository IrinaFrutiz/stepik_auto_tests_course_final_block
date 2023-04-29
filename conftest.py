import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en-gb',
                     help="Choose language: '--language=en' or '--language=ru'")

@pytest.fixture(scope="function")
def browser(request):
        browser_name = request.config.getoption("browser_name")
        user_language = request.config.getoption("language")
        options = Options()
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': user_language})

        options_firefox = OptionsFirefox()
        options_firefox.set_preference("intl.accept_languages", user_language)
        browser = None
        if browser_name == "chrome":
            print("\nstart chrome browser for test..")
            browser = webdriver.Chrome(options=options)
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

