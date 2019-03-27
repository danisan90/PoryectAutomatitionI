from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class BuscarSolicitudContratacionLocators():
    INPUT_NUMERO = Locator(By.ID, 'ctl00_CPH1_txtNumSolicitudGasto')
    NUMERO = Locator(By.ID, 'ctl00_CPH1_EncabezadoSG_lblNumero')
    BUSCAR_BUTTON = Locator(By.ID, 'ctl00_CPH1_btnVer')
    AGARRAR_SOLICITUD = Locator(By.XPATH, '//img[@title="Editar Solicitud de contratación"]')
    AUTORIZAR_RECHAZAR_SOLICITUD = Locator(By.XPATH, '//img[@title="Autorizar o Rechazar Solicitud de Contratación"]')
    AUTORIZAR_SCO = Locator(By.ID, 'ctl00_CPH1_lnkAutorizar')
    RECHAZAR_SCO = Locator(By.ID, 'ctl00_CPH1_lnkRechazar')
    ESTADO_SG_LBL = Locator(By.XPATH, '//tr[@id="ctl00_CPH1_gridResultado_DXDataRow0"]//td[5]')
