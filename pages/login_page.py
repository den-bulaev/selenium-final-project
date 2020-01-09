from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "url is not contained login substring"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "register form is not presented"

    def register_new_user(self, email, password):
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), "email field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD), "password field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_REPEAT_PASSWORD),\
            "repeat password field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), "registration button is not presented"

        mail = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        mail.send_keys(email)

        password_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        password_field.send_keys(password)

        repeat_password = self.browser.find_element(*LoginPageLocators.REGISTER_REPEAT_PASSWORD)
        repeat_password.send_keys(password)

        register_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_btn.click()
