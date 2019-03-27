from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class EnviarAAutorizadorLocators:
    MENSAJE_EXITO = Locator(By.ID, 'ctl00_CPH1_lblMensaje')
