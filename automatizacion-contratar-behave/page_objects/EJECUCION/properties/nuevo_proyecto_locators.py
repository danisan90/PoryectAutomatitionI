from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class NuevoProyectoLocators:
    NUEVO_PROYECTO = Locator(By.ID, 'ctl00_CPH1_lnkAgregarNuevoPE')
