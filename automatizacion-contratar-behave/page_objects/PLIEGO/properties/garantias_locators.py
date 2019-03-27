from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class GarantiasLocators:
    PORCENTAJE_GARANTIA = Locator(By.ID, 'ctl00_CPH1_txtGarantiaPropuesta')
    GUARDAR_Y_VOLVER = Locator(By.ID, 'ctl00_CPH1_lnkGuardarYVolver')
