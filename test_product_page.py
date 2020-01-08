from pages.product_page import ProductPage
from pages.basket_page import BasketPage
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.mark.parametrize('promo', ["0", "1", "2", "3", "4", "5", "6",
                                   pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo):
    page = ProductPage(browser, "http://selenium1py.pythonanywhere.com"
                                "/catalogue/coders-at-work_207/?promo=offer{}".format(promo))
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()

    basket_page = ProductPage(browser, browser.current_url)
    basket_page.expected_results()


@pytest.mark.xfail
@pytest.mark.smoke
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.smoke
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link, timeout=0)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
@pytest.mark.smoke
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.element_should_be_fade()


@pytest.mark.from_product_to_login
def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.from_product_to_login
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.basket
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    page2 = BasketPage(browser, browser.current_url)
    page2.basket_should_be_empty()
    page2.must_be_text_that_the_basket_is_empty()
