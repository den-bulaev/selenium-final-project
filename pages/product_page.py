from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def expected_results(self):
        self.product_name_in_basket_is_correct()
        self.basket_total_price_is_correct()

    def go_to_product_page(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON), "button is missing"
        btn = self.browser.find_element(*ProductPageLocators.BUTTON)
        btn.click()

    def product_name_in_basket_is_correct(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "product name is not presented"
        assert self.is_element_present(*ProductPageLocators.ADDING_MESSAGE), "adding message is not presented"
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_MESSAGE).text
        assert name == message, "wrong product name in message"

    def basket_total_price_is_correct(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "no any price here"
        assert self.is_element_present(*ProductPageLocators.TOTAL_PRICE_MESSAGE),\
            "total price message is missing"
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        message = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE_MESSAGE).text
        assert message == price, "wrong price in message"
