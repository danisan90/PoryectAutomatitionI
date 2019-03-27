from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class IndicesDelPliegoLocators:
    NUMERO_PC = Locator(By.ID, 'ctl00_CPH1_usrCabeceraPliego_lblNumPliego')
    INFO_BASICA_PC = Locator(By.ID, 'ctl00_CPH1_seccionIndice1_hlDatos')
    SCO = Locator(By.ID, 'ctl00_CPH1_seccionIndice2_hlDatos')
    PLIEGO_BASES_CONDICIONES = Locator(By.ID, 'ctl00_CPH1_seccionIndice5_hlDatos')
    REQUISITOS_MINIMOS_DE_PARTICIPACION = Locator(By.ID, 'ctl00_CPH1_seccionIndice6_hlDatos')
    INDICE_GARANTIAS = Locator(By.ID, 'ctl00_CPH1_seccionIndice9_hlDatos')
    MONTOS_Y_PLAZOS_CONTRATACION = Locator(By.ID, 'ctl00_CPH1_seccionIndice10_hlDatos')
    SEPERVISOR = Locator(By.ID, 'ctl00_CPH1_SeccionIngresoSupervisor_hlDatos')

