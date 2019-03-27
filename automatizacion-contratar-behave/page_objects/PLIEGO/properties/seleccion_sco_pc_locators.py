from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class SeleccionSCOLocators:
    NUMERO_SCO = Locator(By.ID, 'ctl00_CPH1_txtNumSolGasto')
    BUTTON_AGREGAR = Locator(By.ID, 'ctl00_CPH1_btnVerNroProcesoCompra')
    NUMERO_SCO_INGRESADO = Locator(By.ID, 'ctl00_CPH1_gvSolGastoSel_cell0_0_lblNumerolnk')
    GUARDAR_Y_VOLVER = Locator(By.ID, 'ctl00_CPH1_lnkGuardarYVolver')
