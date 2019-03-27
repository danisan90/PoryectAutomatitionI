from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class EnviarAAutorizacionLocators:
    ENVIAR_A_AUTORIZAR = Locator(By.ID, 'ctl00_CPH1_lnkEnviarAutorizar')
