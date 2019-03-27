from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class CompletarSolicitudContratacionLocators:
    NUMERO = Locator(By.ID, 'ctl00_CPH1_EncabezadoSG_lblNumero')
    NOMBRE = Locator(By.XPATH, '//span[contains(@id,"EncabezadoSG_lblNombre")]')
    #NUMERO = Locator(By.XPATH, '//span[contains(@id,"Numero")]')
    ESTADO = Locator(By.XPATH, '//span[contains(@id,"EncabezadoSG_lblEstado")]')
    INFO_BASICA = Locator(By.ID, 'ctl00_CPH1_lnkInformacionBasica')
    ITEMS = Locator(By.ID, 'ctl00_CPH1_lnkItems')
    DATOS_OBRA = Locator(By.ID, 'ctl00_CPH1_lnkDatosObra')
    VNR = Locator(By.ID, 'ctl00_CPH1_lnkTabla1')
    ENVIAR_ANALISTA = Locator(By.ID, 'ctl00_CPH1_lnkSiguientePaso')
    INFO_PRESUPUESTARIA = Locator(By.ID, 'ctl00_CPH1_lnkImputacion')
    LISTA_AUTORIZADORES = Locator(By.ID, 'ctl00_CPH1_lnkAutorizadores')
    SIGUIENTE_PASO = Locator(By.ID, 'ctl00_CPH1_lnkSiguientePasoAutorizar')
