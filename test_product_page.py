from pages.product_page import ProductPage
import pytest

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"


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
