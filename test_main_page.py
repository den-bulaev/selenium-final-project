from pages.main_page import MainPage
from pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page.open()         # открываем страницу
    page.should_be_login_link()
    page.go_to_login_page()          # выполняем метод страницы - переходим на страницу логина

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
# запускаем тест командой: pytest -v --tb=line --language=en test_main_page.py
# предварительно не забыв перейти в нужную директорию
