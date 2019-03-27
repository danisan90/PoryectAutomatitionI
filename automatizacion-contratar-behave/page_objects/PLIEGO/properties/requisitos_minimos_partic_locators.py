from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class RequisitosMinimosParticipacionLocator:
    REQUISITOS_ECONOMICOS_Y_FINANCIEROS = Locator(By.ID, 'ctl00_CPH1_rRequisitos_ctl01_UCRequisitosMinimosParticipacion_RE_1_1_txtDescripcion')
    REQUISITO_TECNICOS = Locator(By.ID, 'ctl00_CPH1_rRequisitos_ctl01_UCRequisitosMinimosParticipacion_RT_1_2_txtDescripcion')
    REQUISITOS_ADMINISTRATIVOS = Locator(By.ID, 'ctl00_CPH1_rRequisitos_ctl01_UCRequisitosMinimosParticipacion_RA_1_3_txtDescripcion')
    GUARDAR_Y_VOLVER = Locator(By.ID, 'ctl00_CPH1_lnkGuardarVolver')
