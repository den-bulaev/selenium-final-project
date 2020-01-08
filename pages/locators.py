from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group a")


class BasketPageLocators:
    BASKET_TITLE = (By.CLASS_NAME, "basket-title")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ADDING_MESSAGE = (By.CSS_SELECTOR, "#messages>:nth-child(1)>.alertinner")
    PRODUCT_NAME_MESSAGE = (By.CSS_SELECTOR, "#messages>:nth-child(1)>.alertinner>strong")
    TOTAL_PRICE_MESSAGE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
