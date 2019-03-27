from page_objects.MENU.properties.menu_ciudadano_locators import LoginPageLocators
from page_objects.base_page import BasePage


class LoginPageObject(BasePage):
    def login(self, user, password):
        modal = self.find_element(LoginPageLocators.MODAL).click()
        user = self.find_element(LoginPageLocators.USER).send_keys(user)
        password = self.find_element(LoginPageLocators.PASSWORD).send_keys(password)
        submit = self.find_element(LoginPageLocators.SUBMIT).click()
        return self.url
