from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):

    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TITLE), "basket isn't empty"

    def must_be_text_that_the_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "message not found"
        message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert message.strip() == "Your basket is empty. Continue shopping", "wrong message"
