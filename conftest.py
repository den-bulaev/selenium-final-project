from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):

    """обработчик считывает 2 параметра(--browser_name и --language)
    в --browser_name по умолчанию стоит chrome"""

    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption("--language", action="store", default="en",
                     help="Choose your language")


@pytest.fixture(scope="function")
def browser(request):

    """фикстура передает выбранный браузер и язык"""

    browser_name = request.config.getoption("browser_name")     # ЗАПРОС ЗНАЧЕНИЯ ПАРАМЕТРА
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        options = Options()  # указываем язык браузера используя класс Options и метод add_experimental_option
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()  # для firefox объявление языка выглядит иначе
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()
