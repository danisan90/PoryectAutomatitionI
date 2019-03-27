from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class SeleccionarAutorizadoresLocators:
    #SELECCIONO A EMICHELENA, PENDIENTE PENSARLO COMO HACER PARA OTRO USUARIO
    SELECCION_ANALISTA = Locator(By.XPATH, '//option[@value="c3a21e4b-e427-4435-ab92-02400bb69b1f"]')
    BUTTON_SELECCIONAR = Locator(By.ID, 'ctl00_CPH1_lnkSeleccionar')
    AUTORIZADOR_SELECCIONADO = Locator(By.XPATH, '//option[@value="c3a21e4b-e427-4435-ab92-02400bb69b1f"]')
    GUARDAR_Y_VOLVER = Locator(By.ID, 'ctl00_CPH1_lnkSiguientePaso')
