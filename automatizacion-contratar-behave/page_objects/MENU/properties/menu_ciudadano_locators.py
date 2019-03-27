from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class LoginPageLocators:
    MODAL = Locator(By.XPATH, '//strong[contains(.,"Ingresar")]')
    USER = Locator(By.XPATH, '//input[contains(@id,"Username")]')
    PASSWORD = Locator(By.XPATH, '//input[contains(@id,"txtPassword")]')
    SUBMIT = Locator(By.XPATH, '//input[contains(@id,"Ingresar")]')

