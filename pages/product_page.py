from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def expected_results(self):
        self.product_name_in_basket_is_correct()
        self.basket_total_price_is_correct()

    def add_to_basket(self):
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

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDING_MESSAGE),\
            "success message is presented, but should not to be"

    def element_should_be_fade(self):
        assert self.is_disappeared(*ProductPageLocators.ADDING_MESSAGE),\
            "element is not fade"
