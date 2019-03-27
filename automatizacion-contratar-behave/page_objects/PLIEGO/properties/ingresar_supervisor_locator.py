from selenium.webdriver.common.by import By
from page_objects.base_page import Locator


class IngresarSupervisorLocators:
    SELECCIONO_SUPERVISOR = Locator(By.ID, 'ctl00_CPH1_supervisorUC_lsbUsuarios')
    AGREGAR_SUPERVISOR = Locator(By.ID, 'ctl00_CPH1_supervisorUC_btnAgregar')
    @staticmethod
    def chequear_supervisor(supervisor):
        return Locator(By.ID, '//select[@id="ctl00_CPH1_supervisorUC_lsbUsuariosSeleccionados"]//option[contains(text(), '')]'.format(supervisor))
