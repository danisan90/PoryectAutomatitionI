from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class CompletarInformacionBasicaLocators:
    ITEMS = Locator(By.ID, 'ctl00_CPH1_lnkItems')
    UNIDAD_SOLICITANTE_INPUT = Locator(By.ID, 'ctl00_CPH1_txtUnidadSolicitante')
    ACEPTA_ANTICIPO_FINANCIERO_RADIO = Locator(By.ID, 'ctl00_CPH1_rdbAnticipo_0')
    CORTO_PLAZO = Locator(By.ID, 'ctl00_CPH1_rdbAnticipoPlazo_0')
    ANEXO_SCO_INPUT = Locator(By.ID, 'ctl00_CPH1_AnexosBastrap_uplFile')
    ANEXO_SCO_BTN = Locator(By.ID, 'ctl00_CPH1_AnexosBastrap_lnkIngresarAnexo')
    GUARDAR_VOLVER_BTN = Locator(By.ID, 'ctl00_CPH1_lnkGuardarVolver')
    PORCENTAJE_AF = Locator(By.ID, 'ctl00_CPH1_txtPorcentajeAnticipo')
