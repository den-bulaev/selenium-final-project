from pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_product_page()
    page.solve_quiz_and_get_code()

    basket_page = ProductPage(browser, browser.current_url)
    basket_page.expected_results()
