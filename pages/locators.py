from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


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
